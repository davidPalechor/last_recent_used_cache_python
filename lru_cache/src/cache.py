#!/usr/bin/python
class _Node:
    def __init__(self, key: str, data):
        self.key = key
        self.data = data
        self.previous = None
        self.next = None


class LRUCache:
    def __init__(self, max_capacity: int = 50000, expiration: int = 7200):
        self._hash_table = {}
        self._max_capacity = max_capacity
        self._expiration = expiration
        self._head = _Node('-1', -1)
        self._tail = _Node('-1', -1)

        self._head.next = self._tail
        self._tail.previous = self._head

        self._total_items = 0

    @staticmethod
    def _remove_from_cache(node: _Node):
        """Removes a node from cache

        Args:
            node: Existing node in cache
        """
        aux_prev = node.previous
        aux_next = node.next

        aux_prev.next = aux_next
        aux_next.prev = aux_prev

    def _remove_lru(self):
        """Removes cache Least Recently Used
        """
        tail = self._pop()

        del self._hash_table[tail.key]

    def _pop(self):
        """Pops an item from the cache

        Returns:
            Node
        """
        tail = self._tail.previous
        self._remove_from_cache(tail)

        return tail

    def _add_to_front(self, node: _Node):
        """Push a new item into the cache

        Args:
            node: Item to be pushed
        """
        node.previous = self._head
        node.next = self._head.next

        self._head.next.previous = node
        self._head.next = node

    def _move_to_front(self, node: _Node):
        """Moves an existing right next to the cache head item

        Args:
            node: Item to be moved
        """
        self._remove_from_cache(node)
        self._add_to_front(node)

    def get(self, key: str):
        """Gets data from the wanted key item

        Args:
            key: Item key to be obtained

        Returns:
            data
        """
        node = self._hash_table.get(key)

        if not node:
            return None

        self._move_to_front(node)
        return node.data

    def put_in_cache(self, key: str, value):
        """Inserts an item into the cache

        Args:
            key: Item key to be stored and will be consulted
            value: Item value associated to its key
        """
        node = self._hash_table.get(key)

        if not node:
            new_entry = _Node(key, value)
            self._hash_table[key] = new_entry
            self._add_to_front(new_entry)

            self._total_items += 1
            if self._total_items > self._max_capacity:
                self._remove_lru()
        else:
            node.data = value
            self._move_to_front(node)

    def _empty_cache(self):
        """Empty the cache by pointing head to tail and vice versa
        """
        self._head.next = self._tail
        self._tail.previous = self._head
        self._hash_table = {}

    def traverse_cache(self):
        node = self._head
        while node:
            yield node.data
            node = node.next
