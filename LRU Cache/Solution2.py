from collections import OrderedDict
class LRUCache:

    def __init__(self, capacity: int):
        self.dict = OrderedDict()
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key in self.dict:
            self.dict.move_to_end(key)
            return self.dict[key]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.dict:
            self.dict.move_to_end(key)
            self.dict[key] = value
        else:
            if len(self.dict) == self.capacity:
                self.dict.popitem(last = False)
                # least recent
            self.dict[key] = value
             
        


# Your LRUCache object will be instantiated and called as such:
obj = LRUCache(2)
obj.put(1,1)
obj.put(2,2)
obj.get(1)
print(obj.dict)
print(obj.dict.popitem())
print(obj.dict)
# param_1 = obj.get(key)
# obj.put(key,value)
