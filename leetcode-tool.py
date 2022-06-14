import requests
import json
import config
import os
import time

from pprint import pprint

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
        
    def get_api_json(self, endpoint):
        """Get a JSON object from a GET request to API endpoint
        Uses Leetcode's private user cookies to authenticate the request.
        Returns:
            dict: JSON response as dictionary
        """        
        session = requests.Session()
        resp = session.get(endpoint, cookies=self.cookies)
        # remove unicode decorator
        return json.loads(resp.content.decode('utf-8').replace(u'\xa0', u' '))

    def get_solved_problems(self):
        """Return solved problems by user, sorted into difficulty categories

        Returns:
            dict: Difficulty based categories of user-solved problems
        """        
        diff_map = {1: 'easy', 2: 'medium', 3: 'hard'}
        # filter problems by solved
        all_problems = self.get_api_json(self.problem_endpoint)['stat_status_pairs']
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
        """Get latest accepted code submissions in decorated JSON format
        """
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
        
        print(title_slugs, len(title_slugs))
    
    def download_submission(self):
        pass
    
    def update_cool_stats():
        pass
    
class SpreadsheetUpdater:
    pass

if __name__ == '__main__':
    lc = LeetcodeDataSourcer()
    lc.get_submissions()