class MyHashMap:

    def __init__(self):
        self.dict = [[]] * 2069
        self.len = 0

    def put(self, key: int, value: int) -> None:
        real_key = key % 2069
        if self.get(key) != -1:
            self.remove(key)
        self.dict[real_key].append([key, value])

    def get(self, key: int) -> int:
        real_key = key % 2069
        result = [i for i in self.dict[real_key] if i[0] == key]
        if len(result) == 0:
            return -1
        return result[0][1]

    def remove(self, key: int) -> None:
        real_key = key % 2069
        self.dict[real_key] = [i for i in self.dict[real_key] if i[0] != key]


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
