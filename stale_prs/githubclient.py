

from enum import Enum
from urllib.parse import urljoin
from stale_prs.models.githubcredentials import GitHubCredentials
import requests

class GitHubEndpoint(Enum):
    pulls = 'repos/{owner}/{name}/pulls'

class GitHubClient(requests.Session):

    def __init__(self, credentials: GitHubCredentials):
        super().__init__()
        self.auth = (credentials.username, credentials.personal_access_token)
        self._base_url = 'https://api.github.com/'
        self._context = {}

    def get(self, endpoint: GitHubEndpoint):
        path = endpoint.value.format(**self._context)
        url = urljoin(self._base_url, path)
        return super().get(url)

    def update_context(self, **context):
        self._context.update(context)
