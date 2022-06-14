import requests
import json
import config
import time
import os
from datetime import datetime

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

CACHE_PATH = './cache.json'

class LeetcodeDataSourcer:
    def __init__(self) -> None:
        self.default_endpoint = 'https://leetcode.com/'
        self.submission_endpoint = 'https://leetcode.com/api/submissions/'
        self.problem_endpoint = 'https://leetcode.com/api/problems/all/'
        
        # request information
        self.user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_2) AppleWebKit/537.36 \
        (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36'
        self.headers = {'User-Agent': self.user_agent, 'Connection': 'keep-alive', 'Content-Type': 'application/json'}
        
        # read from config
        self.cookies = {
            'LEETCODE_SESSION': config.LEET_SESH,
            'csrftoken': config.CSRF
        }
        
    def access_cache(self, key, data=None, read=True):
        if not os.path.exists(CACHE_PATH) or os.path.getsize(CACHE_PATH) == 0:
            with open(CACHE_PATH,'w') as f:
                json.dump({}, f)
        
        if read:
            with open(CACHE_PATH, 'r') as f:
                cache_data = json.load(f)
            
            try:
                print('Retrieved cache[%s]' % key)
                return cache_data[key]
            except:
                print('Could not retrieve cache[%s]' % key)
                print('Making API request instead')
            
            return None
        
        with open(CACHE_PATH, 'r') as f:
            cache_data = json.load(f)
        # if cache is empty
        if not cache_data:
            cache_data = {key: {}}

        with open(CACHE_PATH, 'w') as f:
            cache_entry = {}
            if key in cache_data.keys():
                cache_entry = cache_data[key]
            
            cache_entry['data'] = data
            cache_entry['timestamp'] = datetime.now().timestamp()
            
            cache_data[key] = cache_entry
            
            print('Succesfully cached cache[%s]' % key)
            
            json.dump(cache_data, f, indent=4)
                
    def get_api_json(self, endpoint):
        session = requests.Session()
        resp = session.get(endpoint, cookies=self.cookies)
        # remove unicode decorator
        return json.loads(resp.content.decode('utf-8').replace(u'\xa0', u' '))

    def get_solved_problems(self):
        diff_map = {1: 'easy', 2: 'medium', 3: 'hard'}
        # filter problems by solved
        cached = self.access_cache('problems', read=True)
        all_problems = []
        
        if cached:
            all_problems = cached['data']
        else:
            all_problems = self.get_api_json(self.problem_endpoint)['stat_status_pairs']
            self.access_cache('problems', all_problems, read=False)
            
        solved_problems = list(filter(lambda obj: obj['status'] == 'ac', all_problems))
        # add problem url to problem objects
        for i in range(len(solved_problems)):
            solved_problems[i]['url'] = self.default_endpoint + 'problems/' \
                + solved_problems[i]['stat']['question__title_slug']
            # fix convoluted difficulty assignment
            solved_problems[i]['difficulty'] = diff_map[solved_problems[i]['difficulty']['level']]
        
        # create categories
        return { 
                cat: list(filter(lambda obj: obj['difficulty'] == cat, solved_problems))
                for cat in ['easy', 'medium', 'hard'] 
            }
    
    def get_submissions(self):
        cached = self.access_cache('submissions', read=True)
        submission_data_raw = []
        
        if cached:
            submission_data_raw = cached['data']
        else:
            offset = 0
            limit = 20
            
            pagination_query = lambda offset, limit: '?offset=%d&limit=%d' % (offset, limit)
            
            submission_data_raw = []
            current_sub_query = self.get_api_json(
                self.submission_endpoint + pagination_query(offset, limit)
            )['submissions_dump']
            
            while len(current_sub_query) > 0:
                submission_data_raw += current_sub_query
                # prevent a bad request from too many repeated endpoint requests
                time.sleep(2)
                
                offset += limit
                current_sub_query = self.get_api_json(
                    self.submission_endpoint + pagination_query(offset, limit)
                )['submissions_dump']
            
            self.access_cache('submissions', submission_data_raw, read=False)
            
        # filter out wrong submission
        submission_accepted = list(filter(lambda obj: obj['status_display'] == 'Accepted', submission_data_raw))
        # make set of title slugs
        title_slugs = set()
        for submission in submission_accepted:
            title_slugs.add(submission['title_slug'])
        # obtain best submission for each
        latest_submissions = []
        for title in title_slugs:
            all_submissions = list(filter(lambda x: x['title_slug'] == title, submission_accepted))
            all_submissions.sort(key=lambda sub: sub['timestamp'])
            latest_submissions.append({
                'title': title,
                'data': all_submissions[0]
            })
        
        return latest_submissions
    
    def get_solved_problem(self, title_slug, difficulty):
        all_solved = self.get_solved_problems()[difficulty]
        return list(filter(
            lambda solved: solved['stat']['question__title_slug'] == title_slug, all_solved)
        )[0]
    
    def get_submission(self, title_slug):
        submissions = self.get_submissions()
        return list(filter(lambda x: x['title'] == title_slug, submissions))[0]
    
    def download_submission(self):
        pass
    
    def update_cool_stats():
        pass
    
class SpreadsheetUpdater:
    pass

if __name__ == '__main__':
    lc = LeetcodeDataSourcer()
    lc.get_submissions()