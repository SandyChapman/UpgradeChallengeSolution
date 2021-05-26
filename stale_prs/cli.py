#!/usr/bin/env python3

from json import encoder
from stale_prs.dataclass_encoder import DataclassEncoder
from stale_prs.models.githubprinfo import GitHubPullRequestInfo
from stale_prs.githubclient import GitHubEndpoint
import keyring
from getpass import getpass
import logging
import json

logging.basicConfig(level=logging.INFO)

def get_github_token() -> str:
    pw = keyring.get_password('system', 'github_key')
    if pw is None:
        pw = getpass(prompt='Please paste a GitHub API token. This will be stored in your system keychain: ')
        keyring.set_password('system', 'github_key', pw)
    return pw

def request_prs(client, repo, label_filters, age_filter) -> list[GitHubPullRequestInfo]:
    client.update_context(**repo.__dict__)
    result = client.get(GitHubEndpoint.pulls)
    if not result.ok:
        raise Exception(f'Invalid response from API. {result.status_code}')
    return [GitHubPullRequestInfo(pr['user']['login'], pr['url']) for pr in result.json() if age_filter(pr) and all(f(pr) for f in label_filters)]

def print_prs(prs: list[GitHubPullRequestInfo]) -> None:
    for pr in prs:
        logging.info(pr)

def write_prs_to_file(prs: list[GitHubPullRequestInfo], filename: str) -> None:
    with open(filename, 'w') as f:
        json.dump(prs, f, cls=DataclassEncoder, indent=2)
