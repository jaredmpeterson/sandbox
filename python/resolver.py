import socket
import pprint


class Resolver:
    def __init__(self):
        self._cache = {}

    def __call__(self, host: str):
        if host not in self._cache:
            self._cache[host] = socket.gethostbyname(host)
        return self._cache[host]

    def clear(self):
        self._cache.clear()

    def has_host(self, host: str):
        return host in self._cache

    @property
    def view(self):
        pprint.pprint(self._cache)
