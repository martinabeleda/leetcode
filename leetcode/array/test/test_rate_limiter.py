import time

from leetcode.array.rate_limiter import RateLimiter


def test_rate_limiter():
    rate_limiter = RateLimiter(n_seconds=1.0, max_requests=2)
    assert rate_limiter.rate_limit(1) is True
    assert rate_limiter.rate_limit(1) is True
    assert rate_limiter.rate_limit(1) is False
    assert rate_limiter.rate_limit(2) is True
    assert rate_limiter.rate_limit(2) is True
    assert rate_limiter.rate_limit(2) is False
    print("Test passed!")


def test_rate_limiter_next_interval():
    rate_limiter = RateLimiter(n_seconds=1.0, max_requests=2)
    assert rate_limiter.rate_limit(1) is True
    assert rate_limiter.rate_limit(1) is True
    assert rate_limiter.rate_limit(1) is False
    time.sleep(2)
    assert rate_limiter.rate_limit(1) is True
    assert rate_limiter.rate_limit(1) is True
    assert rate_limiter.rate_limit(1) is False
