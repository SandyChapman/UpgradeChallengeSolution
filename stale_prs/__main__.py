#!/usr/bin/env python3

import logging
from stale_prs.githubclient import GitHubClient
from stale_prs.models.githubcredentials import GitHubCredentials
from stale_prs.cli import get_github_token, print_prs, request_prs, write_prs_to_file
from stale_prs.parsing import parse_arguments
from stale_prs.filters import create_age_filter, create_label_filter

pat = get_github_token()
args = parse_arguments()
credentials = GitHubCredentials('SandyChapman', pat)
client = GitHubClient(credentials)

label_filters = [create_label_filter(label) for label in args.labels]
age_filter = create_age_filter(args.age)

prs = []
for repo in args.repos:
    try:
        prs += request_prs(client, repo, label_filters, age_filter)
    except:
        logging.exception(f'Error retrieving PRs from repo {repo}')

if args.output:
    write_prs_to_file(prs, args.output)
else:
    print_prs(prs)
