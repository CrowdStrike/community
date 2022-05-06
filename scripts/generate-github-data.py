#!/usr/bin/python3

from github import Github, GithubException
from urllib.parse import urlparse
import json
import yaml
import argparse


parser = argparse.ArgumentParser()
parser.add_argument("-o", "--output", required=True,
                    help="output GitHub repos in json")
parser.add_argument("--type", default="yaml", type=str, choices=['yaml', 'json'],
                    help="output format of GitHub repos")
parser.add_argument("-t", "--token",
                    help="GitHub token for API access")

args = parser.parse_args()

outfile = args.output
r_list = []

if args.token:
    g = Github(args.token)
else:
    g = Github()

for repo in g.get_organization(login="CrowdStrike").get_repos():
    if not repo.fork and not repo.private and not repo.archived:
        repo_dict = {"name": repo.name,
                     "html_url": repo.html_url,
                     "forks_count": repo.forks_count,
                     "stargazers_count": repo.stargazers_count,
                     "description": repo.description,
                     "homepage": repo.homepage,
                     "language": repo.language,
                     "tags": repo.topics,
                     "created": repo.created_at.strftime("%B %d, %Y"),
                     "updated": repo.updated_at.strftime("%B %d, %Y"),
                     }

        # Ensure there are None doesn't exist as a value
        for k, v in repo_dict.items():
            if v is None:
                repo_dict[k] = ""

        # Append the repo information into a list of dictionaries
        r_list.append(repo_dict)

# sort by name key
r_list = sorted(r_list, key=lambda i: i['name'])

with open(outfile, 'w', encoding='utf-8') as f:
    if args.type == 'json':
        json.dump({"list": r_list}, f, indent=2)
    else:
        yaml.dump({"list": r_list}, f, indent=2, sort_keys=False)
