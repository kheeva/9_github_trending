#!/usr/bin/env python
import requests


def get_trending_repositories(top_size):
    url = 'https://api.github.com/search/repositories?q=created&sort=stars'
    return requests.get(url).json()['items'][:top_size]


if __name__ == '__main__':
    top_size = 20
    print('There are top {} repos in https://github.com:'.format(top_size))
    for repo in get_trending_repositories(top_size):
        print(repo['html_url'], 'open_issues:', repo['open_issues_count'])
