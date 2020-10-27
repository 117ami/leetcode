#!/usr/local/bin/python3.7
import json
import re
import requests
from bs4 import BeautifulSoup
from pprint import pprint
import arrow
import random
import time
import sys
import os
import logging
from termcolor import colored

FORMAT = '[%(asctime)-15s] %(message)s'
logging.basicConfig(format=FORMAT, level=logging.INFO)


class LeetCode():
    def __init__(self,
                 header_file='data/xiuheader.dat'):
        self.s = requests.Session()
        # cookies = self._get_config(cookie_file)
        # self.s.cookies.update(cookies)
        headers = self._get_config(header_file)
        self.s.headers.update(headers)
        self.title = ''

    def _update_question_id(self):
        res = requests.Session().get(
            'https://leetcode.com/api/problems/all')
        # print(res, res.text)
        json.dump(res.json(), open('data/question_ids.json', 'w'), indent=2)

    def _get_config(self, head_file):
        '''Load config (head/cookie) from file
        '''
        with open(head_file, 'r') as f:
            return dict(
                map(lambda l: l.rstrip().split("\t")[:2], f.readlines()))

    def init_code_env(self, title='two-sum'):
        self.title = title
        j = {
            'operationName': "getQuestionDetail",
            'query':
            "query getQuestionDetail($titleSlug: String!) {\n isCurrentUserAuthenticated\n userStatus {\n isPremium\n __typename\n }\n question(titleSlug: $titleSlug) {\n questionId\n questionFrontendId\n questionTitle\n translatedTitle\n questionTitleSlug\n content\n translatedContent\n difficulty\n stats\n allowDiscuss\n contributors {\n username\n profileUrl\n __typename\n }\n similarQuestions\n mysqlSchemas\n randomQuestionUrl\n sessionId\n categoryTitle\n submitUrl\n interpretUrl\n codeDefinition\n sampleTestCase\n enableTestMode\n metaData\n langToValidPlayground\n enableRunCode\n enableSubmit\n judgerAvailable\n infoVerified\n envInfo\n urlManager\n article\n questionDetailUrl\n libraryUrl\n topicTags {\n name\n slug\n translatedName\n __typename\n }\n __typename\n }\n subscribeUrl\n loginUrl\n}\n",
            'variables': {
                'titleSlug': title
            }
        }
        r = self.s.post('https://leetcode.com/graphql/', json=j)
        with open('pro.json', 'w') as f:
            f.write(r.text)

        self.parse_res()

    def parse_res(self):
        j = json.load(open('pro.json', 'r'))
        details = j['data']['question']
        difficulty = details['difficulty']
        id = details['questionFrontendId']
        title = details['questionTitleSlug']
        content = details['content']
        env = details['codeDefinition']
        # print(id, title, content, env)
        env = json.loads(env)
        for nj in env:
            if nj['value'] == 'cpp':
                fname = f"{id}.{title}.cpp"
                os.system(f"cat conf.d/head.cpp > {fname}")
                with open(f"{id}.{title}.cpp", 'a') as f:
                    f.write(nj['defaultCode'] + '\n')
                os.system(f"cat conf.d/tail.cpp >> {fname}")
            elif nj['value'] == 'python3':
                fname = f"{id}.{title}.py"
                os.system(f"cat conf.d/head.py > {fname}")
                with open(fname, 'a') as f:
                    f.write(f'# https://leetcode.com/problems/{self.title}/description/\n')
                    f.write(f'# {difficulty}\n')
                    f.write(nj['defaultCode'] + '\n')
            elif nj['value'] == 'mysql':
                creat_sql_codes = ';\n'.join(details['mysqlSchemas'] + [''])
                tables = re.findall(r'Not Exists (.*?) \(', creat_sql_codes)
                drop_tables_codes = 'drop tables ' + ', '.join(tables) + '; \n'
                open('c.sh', 'w').write(drop_tables_codes + creat_sql_codes)
                print(creat_sql_codes)
                fname = f"{id}.{title}.sql"
                os.system(f'touch {fname}')
                # os.system(f'echo {creat_sql_codes} > c.sh')


if __name__ == "__main__":
    url = sys.argv[1] + '/description'
    title = re.findall(r'problems/(.*?)(/description)', url)[0][0].strip('/')
    print(title)
    LeetCode().init_code_env(title)
