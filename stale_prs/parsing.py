from .models.githubrepo import GitHubRepo
import argparse
import dateparser

def age_type(arg):
    age = dateparser.parse(arg, settings={'RETURN_AS_TIMEZONE_AWARE': True})
    if age is None:
        raise Exception(f"Invalid date/time format for argument -a {arg}")
    return age

def repo_type(arg: str):
    owner, name = arg.split('/')
    return GitHubRepo(owner=owner, name=name)

def parse_arguments() -> argparse.Namespace:
    parser = argparse.ArgumentParser('python -m stale_prs', description='The Upgrade test CLI tool by Sandy Chapman.')
    parser.add_argument(
        '-a', '--age', 
        type=age_type, 
        required=False,
        default='now',
        help="Minimum age in plain text format. E.g. '1 month', '3 days', '1 hour 30 minutes'"
    )
    parser.add_argument(
        '-l', 
        '--labels', 
        type=str, 
        default=[], 
        required=False, 
        nargs='*',
        help="One or more label names that are applied to the PR. E.g. 'bug', 'documentation'"
    )
    parser.add_argument(
        '-r', '--repos', 
        type=repo_type, 
        default=[], 
        required=True, 
        nargs='+',
        help="One or more GitHub repositories to lookup in 'Owner/Repo' format. E.g. 'SandyChapman/SomeExcellentRepo'"
    )
    parser.add_argument(
        '-o', '--output', 
        type=str, 
        default=None, 
        required=False, 
        help="Specify an output filename for output in json. If not specified, output is printed to standard out."
    )
    args = parser.parse_args()
    return args
