#!/usr/bin/python
from .pub_sub.server import PubSub


class DistributedCache:
    @staticmethod
    def new_client():
        """Creates a new PubSub instance in order to listen, process and return messages between cache instances

        Returns:
            PubSub instance
        """
        return PubSub()
