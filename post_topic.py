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

from typing import Dict, Sequence, List

FORMAT = '[%(asctime)-15s] %(message)s'
logging.basicConfig(format=FORMAT, level=logging.INFO)

# Leetcode related urls
class UrlEnum:
    GRAPHSQL: str = "https://leetcode.com/graphql"
    HOMEPAGE_117: str = "https://leetcode.com/l117"


class LeetCode():
    def __init__(self,
                 header_file='data/xiuheader.dat'):
        self.s = requests.Session()
        delimiter = ": " if "elena" in header_file else "\t"
        headers = self._get_config(header_file, delimiter)
        self.s.headers.update(headers)

    def _get_config(self, head_file: str, delimiter="\t")->Dict:
        '''Load config (head/cookie) from file
        '''
        with open(head_file, 'r') as f:
            return dict(map(lambda l: l.rstrip().split(delimiter)[:2], f.readlines()))

    def _query_question_id(self)->str:
        json_dict: Dict = {
            "operationName": "getQuestionDetail",
            "variables": {
                "titleSlug": '.'.join(self.topic_file.split('/')[-1].split('.')[1:-1])
            },
            "query": "query getQuestionDetail($titleSlug: String!) {\n isCurrentUserAuthenticated\n userStatus {\n isPremium\n __typename\n }\n question(titleSlug: $titleSlug) {\n questionId\n questionFrontendId\n questionTitle\n translatedTitle\n questionTitleSlug\n content\n translatedContent\n difficulty\n stats\n allowDiscuss\n contributors {\n username\n profileUrl\n __typename\n }\n similarQuestions\n mysqlSchemas\n randomQuestionUrl\n sessionId\n categoryTitle\n submitUrl\n interpretUrl\n codeDefinition\n sampleTestCase\n enableTestMode\n metaData\n langToValidPlayground\n enableRunCode\n enableSubmit\n judgerAvailable\n infoVerified\n envInfo\n urlManager\n article\n questionDetailUrl\n libraryUrl\n topicTags {\n name\n slug\n translatedName\n __typename\n }\n __typename\n }\n subscribeUrl\n loginUrl\n}\n"
        }
        ret = self.s.post(UrlEnum.GRAPHSQL, json=json_dict, verify=False)
        return ret.json()['data']['question']['questionId']

    def _post_topic(self, question_id: str, title: str, content: str):
        json_dict: Dict = {
            "operationName": "postTopic",
            "variables": {
                "tags": [],
                "title": title,
                "questionId": question_id,
                "content": content 
                },
            "query": "mutation postTopic($title: String!, $content: String!, $questionId: Int!, $tags: [String!]) {\n createTopicForQuestion(title: $title, content: $content, questionId: $questionId, tags: $tags) {\n error\n topic {\n id\n __typename\n }\n __typename\n }\n}\n"
        }
        ret = self.s.post(UrlEnum.GRAPHSQL, json=json_dict)
        print(ret, ret.text)
        return ret.json()

    def _get_topic_title(self) -> str:
        # Get topic title from markdown file
        with open(self.topic_file, 'r') as f:
            return next(filter(lambda l: l.startswith('title:'), \
                f.readlines())).replace('title:', '').strip()

    def _get_topic_content(self) -> str:
        # Get topic content from markdown file
        with open(self.topic_file, 'r') as f:
            return ''.join(filter(lambda l: not l.startswith('title:'), \
                f.readlines()))
    
    def _main(self, topic_file: str):
        self.topic_file = topic_file
        self._post_topic(
            self._query_question_id(), 
            self._get_topic_title(), 
            self._get_topic_content())


if __name__ == "__main__":
    LeetCode('data/leetcode_header.dat')._main(sys.argv[1])
    # print(LeetCode()._get_topic_title(sys.argv[1]))
    # print(LeetCode()._get_topic_content(sys.argv[1]))
    

