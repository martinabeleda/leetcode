import time


class RateLimiter:
    def __init__(self, n_seconds, max_requests):
        """
        Limits the number of requests a user can make to at most max_requests
        in any n_seconds long interval.
        """
        self.n_seconds = n_seconds
        self.max_requests = max_requests
        # Dictionary used to keep track of each user's requests.
        self.request_history = {}

    def rate_limit(self, user_id):
        """
        Records a request made by the user, and returns True if the request
        does not exceed the rate limit, or False if the request does.
        """
        if user_id not in self.request_history:
            self.request_history[user_id] = []

        # Record the current request.
        now = time.time()
        self.request_history[user_id].append(now)

        self.request_history[user_id] = [
            t for t in self.request_history[user_id] if t >= now - self.n_seconds
        ]

        # Check whether the request exceeds the rate limit.
        if len(self.request_history[user_id]) > self.max_requests:
            return False

        return True
