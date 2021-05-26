from dataclasses import dataclass

@dataclass
class GitHubPullRequestInfo():
    owner: str
    url: str

    def __repr__(self) -> str:
        return f'Owner: {self.owner} - URL: {self.url}'
