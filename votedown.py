import json
import re
import requests
from bs4 import BeautifulSoup
from pprint import pprint
import arrow
import random
import time
import base64
import sys, os
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
        delimiter = "\t" if "xiu" in header_file else ": "
        headers = self._get_config(header_file, delimiter)
        self.s.headers.update(headers)

    def _get_config(self, head_file: str, delimiter="\t")->Dict:
        '''Load config (head/cookie) from file
        '''
        with open(head_file, 'r') as f:
            return dict(map(lambda l: l.rstrip().split(delimiter)[:2], f.readlines()))

    def _query_post_id(self, topic_url: str)->str:
        topic_id = re.findall(r'discuss/(\d+?)/', topic_url)[0]
        json_dict: Dict = {
            "operationName": "DiscussTopic",
            "query": "query DiscussTopic($topicId: Int!) {\n topic(id: $topicId) {\n id\n viewCount\n topLevelCommentCount\n subscribed\n title\n pinned\n tags\n hideFromTrending\n post {\n ...DiscussPost\n __typename\n }\n __typename\n }\n}\n\nfragment DiscussPost on PostNode {\n id\n voteCount\n voteStatus\n content\n updationDate\n creationDate\n status\n isHidden\n coinRewards {\n ...CoinReward\n __typename\n }\n author {\n isDiscussAdmin\n isDiscussStaff\n username\n profile {\n userAvatar\n reputation\n userSlug\n __typename\n }\n isActive\n __typename\n }\n authorIsModerator\n isOwnPost\n __typename\n}\n\nfragment CoinReward on ScoreNode {\n id\n score\n description\n date\n __typename\n}\n",
            "variables": {"topicId": topic_id}
        }
        ret = self.s.post(UrlEnum.GRAPHSQL, json=json_dict, verify=False)
        # print(ret, ret.text)
        return ret.json()['data']['topic']['post']['id']

    def _downvote_topic(self, post_id: str):
        json_dict: Dict = {
            "operationName": "votePost",
            "variables": {
                "postId": post_id,
                "voteStatus": -1
                },
            "query": "mutation votePost($postId: Int!, $voteStatus: Int!) {\n votePost(postId: $postId, value: $voteStatus) {\n ok\n error\n value\n post {\n id\n voteStatus\n __typename\n }\n __typename\n }\n}\n"
        }
        ret = self.s.post(UrlEnum.GRAPHSQL, json=json_dict)
        print(ret, ret.text)
        return ret.json()
    
    def entry(self, post_url: str):
        post_id = self._query_post_id(post_url)
        self._downvote_topic(post_id)


if __name__ == "__main__":
    topic_url = sys.argv[1]
    # LeetCode().entry(topic_url)
    # LeetCode('data/adawa.dat').entry(topic_url)
    # LeetCode('data/qiusa.dat').entry(topic_url)
    # LeetCode('data/hera.dat').entry(topic_url)
    # LeetCode('data/lilei.dat').entry(topic_url)
    # LeetCode('data/maya.dat').entry(topic_url)
    # LeetCode('data/lila.dat').entry(topic_url)
    LeetCode('data/elenaheader.dat').entry(topic_url)


