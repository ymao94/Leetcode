class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.dict = {}
        self.rkey = []

    def get(self, key: int) -> int:
        if key in self.dict:
            self.rkey.remove(key)
            self.rkey.append(key)
            return self.dict[key]
        else:
            return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.dict:
            self.dict[key] = value
            self.rkey.remove(key)
            self.rkey.append(key)
        else:
            if len(self.dict) == self.capacity:
                self.dict.pop(self.rkey[0])
                self.rkey.remove(self.rkey[0])
            self.dict[key] = value
            self.rkey.append(key)


"""
use a list to store the order of operated keys
"""
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
