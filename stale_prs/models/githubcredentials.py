from dataclasses import dataclass

@dataclass
class GitHubCredentials():
    username: str
    personal_access_token: str
