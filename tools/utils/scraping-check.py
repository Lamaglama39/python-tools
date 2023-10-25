#!/usr/bin/env python3

import requests
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-u", "--url", type=str, help="check target url",
                    default='https://requests.readthedocs.io')
args = parser.parse_args()


def check_url(url):
    target_url = url + '/robots.txt'
    try:
        response = requests.get(target_url)
        if response.status_code == 200:
            print(
                f'Target URL: {target_url}\n'
                f'Status Code: {response.status_code}\n')
            if any(keyword in response.text for keyword in ['User-agent', 'Allow', 'Disallow', 'Sitemap']):
                print("Relevant lines found in robots.txt:")
                for line in response.text.splitlines():
                    if any(keyword in line for keyword in ['User-agent', 'Allow', 'Disallow', 'Sitemap']):
                        print(line)
        else:
            print(
                f'Target URL: {target_url}\n'
                f'Status Code: {response.status_code}\n')
            print('No robots.txt file found')
    except requests.RequestException as e:
        print(f'Requests Error:\n{e}')


if __name__ == '__main__':
    check_url(args.url)
