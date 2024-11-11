class RateLimitExceeded(Exception):
    """Exception raised when GitHub API rate limit is exceeded."""
    pass


class UnauthorizedAccess(Exception):
    """Exception raised when unauthorized access to GitHub API occurs."""
    pass
