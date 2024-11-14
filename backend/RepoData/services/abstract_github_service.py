from abc import ABC, abstractmethod
import requests

# Abstract class for different github API calls, extend this to implement calls to different Github APIs
class AbstractGithubService(ABC):

    @abstractmethod
    def call_github_api(self, endpoint, page, etag=None):
        pass
