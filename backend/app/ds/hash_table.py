"""Custom hash table (chaining or open addressing) with rehashing. CNIC, case number, username, tracking ID lookups. O(1) average."""


class HashTable:
    def __init__(self):
        # TODO: implement
        pass

    def put(self, *args, **kwargs):
        raise NotImplementedError

    def get(self, *args, **kwargs):
        raise NotImplementedError

    def remove(self, *args, **kwargs):
        raise NotImplementedError

    def contains(self, *args, **kwargs):
        raise NotImplementedError

    def _resize(self, *args, **kwargs):
        raise NotImplementedError

    def _hash(self, *args, **kwargs):
        raise NotImplementedError
