#!/usr/bin/env python
from datetime import datetime, timedelta
import requests


def get_trending_repositories(top_size):
    url = 'https://api.github.com/search/repositories'
    time_week_ago = (datetime.now() - timedelta(days=7)).strftime('%Y-%m-%d')
    payload = {'q': 'created:>'+time_week_ago, 'sort': 'stars'}
    return requests.get(url, params=payload).json()['items'][:top_size]


def get_open_issues_amount(repo_owner, repo_name):
    url = 'https://api.github.com/repos/{}/{}/issues'.format(repo_owner,
                                                             repo_name)
    return requests.get(url).json()


if __name__ == '__main__':
    top_size = 20
    print('There are top {} repos in https://github.com:'.format(top_size))
    for repo in get_trending_repositories(top_size):
        oi = get_open_issues_amount(repo['owner']['login'],
                                              repo['name'])
        print(repo['html_url'], 'open_issues:', oi)
