from abc import ABC, abstractmethod
import requests

class GitHubServiceInterface(ABC):

    @abstractmethod
    def call_github_api(self, endpoint, page, etag=None):
        pass
