import json
import re
import requests
from bs4 import BeautifulSoup
from pprint import pprint
import arrow
import random
import time
import base64
import sys
import os
import logging
from termcolor import colored
import subprocess

FORMAT = '[%(asctime)-15s] %(message)s'
logging.basicConfig(format=FORMAT, level=logging.INFO)


class LeetCode():
    def __init__(self, header_file='data/xiuheader.dat'):
        self.s = requests.Session()
        headers = self._get_config(header_file)
        self.s.headers.update(headers)

    def _update_question_id(self):
        res = requests.Session().get('https://leetcode.com/api/problems/all')
        # print(res, res.text)
        json.dump(res.json(), open('data/question_ids.json', 'w'), indent=2)

    def _get_config(self, head_file):
        '''Load config (head/cookie) from file
        '''
        with open(head_file, 'r') as f:
            return dict(
                map(lambda l: l.rstrip().split("\t")[:2], f.readlines()))

    def _read_code_file(self, fname='test.py'):
        # Read codes from file, and ignore all debug lines,
        # e.g., those with print commands .
        with open(fname) as f:
            return ''.join(
                filter(
                    lambda line: re.findall("(say|print)\(.*\)", line) == [],
                    f.readlines()))

    def _get_question_id(self, code_file, early_stop=False):
        '''Frontend question id can be different from real question id.
        '''
        js = json.load(open('data/question_ids.json', 'r'))
        frontend_id = code_file.split('/')[-1].split('.')[0]
        for s in js['stat_status_pairs']:
            if s['stat']['frontend_question_id'] == int(frontend_id):
                return s['stat']['question_id']

        if early_stop:
            logging.warning(
                "No backend id found from API. Please check your file name.")
        else:
            logging.warning(
                "Found no backend id for current question. Update from API...")
            # self._update_question_id()
            return self._get_id_from_sql(code_file)

    def _get_id_from_sql(self, code_file):
        '''Get Question ID from graphql 
        '''
        title = '.'.join(code_file.split('.')[1:-1])
        data = {
            "operationName":
            "getQuestionDetail",
            "variables": {
                "titleSlug": title
            },
            "query":
            "query getQuestionDetail($titleSlug: String!) {\n  isCurrentUserAuthenticated\n  question(titleSlug: $titleSlug) {\n    questionId\n    questionFrontendId\n    questionTitle\n    translatedTitle\n    questionTitleSlug\n    content\n    translatedContent\n    difficulty\n    stats\n    allowDiscuss\n    contributors {\n      username\n      profileUrl\n      __typename\n    }\n    similarQuestions\n    mysqlSchemas\n    randomQuestionUrl\n    sessionId\n    categoryTitle\n    submitUrl\n    interpretUrl\n    codeDefinition\n    sampleTestCase\n    enableTestMode\n    metaData\n    enableRunCode\n    enableSubmit\n    judgerAvailable\n    infoVerified\n    envInfo\n    urlManager\n    article\n    questionDetailUrl\n    libraryUrl\n    adminUrl\n    companyTags {\n      name\n      slug\n      translatedName\n      __typename\n    }\n    companyTagStats\n    topicTags {\n      name\n      slug\n      translatedName\n      __typename\n    }\n    __typename\n  }\n  interviewed {\n    interviewedUrl\n    companies {\n      id\n      name\n      slug\n      __typename\n    }\n    timeOptions {\n      id\n      name\n      __typename\n    }\n    stageOptions {\n      id\n      name\n      __typename\n    }\n    __typename\n  }\n  subscribeUrl\n  isPremium\n  loginUrl\n}\n"
        }
        url = 'https://leetcode.com/graphql'
        res = requests.Session().post(url, json=data, verify=False)
        return res.json()['data']['question']['questionId']

    def submit_answer(self, code_file, title_slug, item_id):
        code = self._read_code_file(code_file)
        bid = str(self._get_question_id(code_file))  # backend id
        # Set submitted language. Either python3, cpp or rust.
        langs = {'py': 'python3', 'cpp': 'cpp', 'rs': 'rust'}
        code_language = langs[code_file.split('.')[-1]]

        idata = {
            "question_id": bid,
            "data_input": "",
            "lang": code_language,
            "typed_code": code,
            "test_mode": False,
            "judge_type": "large",
            "item_id": item_id
        }
        logging.info('Submitting file %s ', code_file)
        logging.info('Backend id %s ', str(bid))
        res = self.s.post(
            f'https://leetcode.com/explore/{title_slug}/submit/',
            json=idata,
            verify=False)
        msg = str(res) + res.text
        logging.info(msg)
        logging.info('Submission result copied to clipboard.')
        os.system(
            f"echo https://leetcode.com/submissions/detail/{res.json()['submission_id']}/ | pbcopy"
        )
        # self._get_result(res.json()['submission_id'])

    def get_itemid(self, id):
        j = {'operationName': "GetItem",
            'query':
            "query GetItem($itemId: String!) {\n item(id: $itemId) {\n id\n title\n type\n paidOnly\n lang\n isEligibleForCompletion\n question {\n questionId\n title\n titleSlug\n __typename\n }\n article {\n id\n title\n __typename\n }\n video {\n id\n __typename\n }\n htmlArticle {\n id\n __typename\n }\n webPage {\n id\n __typename\n }\n __typename\n }\n isCurrentUserAuthenticated\n}\n",
            'variables': {
                "itemId": str(id)
            }
        }
        r = self.s.post('https://leetcode.com/graphql/', json=j)
        q = r.json()['data']['item']['question']
        # print(q)
        return (q['questionId'], q['titleSlug'])

    def do_daily_challenge(self):
        j = {
            'operationName': "GetChaptersWithItems",
            'query':
            "query GetChaptersWithItems($cardSlug: String!) {\n chapters(cardSlug: $cardSlug) {\n ...ExtendedChapterDetail\n descriptionText\n __typename\n }\n}\n\nfragment ExtendedChapterDetail on ChapterNode {\n id\n title\n slug\n items {\n id\n title\n type\n info\n paidOnly\n chapterId\n isEligibleForCompletion\n prerequisites {\n id\n chapterId\n __typename\n }\n __typename\n }\n __typename\n}\n",
            'variables': {
                "cardSlug": "september-leetcoding-challenge"
            }
        }
        r = self.s.post('https://leetcode.com/graphql/', json=j)
        cs = r.json()['data']['chapters']
        items = []
        for c in cs:
            for nj in c['items']:
                # Some problems for VIP only
                if nj['paidOnly'] == False:
                    items.append((nj['chapterId'], nj['id'], nj['title']))

        # print(items, len(items))
        for chapter_id, item_id, title in items[::-1][:2]:
            qid, title_slug = self.get_itemid(item_id)
            js = json.load(open('data/question_ids.json', 'r'))
            front_id = 1
            for s in js['stat_status_pairs']:
                if s['stat']['question_id'] == int(qid):
                    front_id = s['stat']['frontend_question_id']
                    break
            # print(qid, title_slug)
            try:
                python_file = f"{front_id}.{title_slug}.py"
                cpp_file = f"{front_id}.{title_slug}.cpp"
                local_file = f'python_solutions/{python_file}'
                print(python_file, local_file)
                self.submit_answer(local_file, title_slug, item_id)
                
                local_file = f'python_solutions/{cpp_file}'
                if os.path.exists(local_file):
                    time.sleep(10)
                    self.submit_answer(local_file, title_slug, item_id)
                time.sleep(10)
            except:
                pass 


if __name__ == "__main__":
    cur_month = arrow.now().format('MM') 
    LeetCode().do_daily_challenge()
    LeetCode('data/leetcode_header.dat').do_daily_challenge()
