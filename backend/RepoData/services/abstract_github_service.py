from abc import ABC, abstractmethod
import requests

class AbstractGithubService(ABC):

    @abstractmethod
    def call_github_api(self, endpoint, page, etag=None):
        pass
