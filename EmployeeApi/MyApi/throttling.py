from rest_framework.throttling import UserRateThrottle


class DKThrottle(UserRateThrottle):
    scope = 'DK'
