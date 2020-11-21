class HashMap:
    def __init__(self, initial_size=10):
        self.bucket_array = [None for _ in range(initial_size)]
        self.p = 37 # a prime number
        self.num_entries = 0

    def put(self, key, value):
        pass

    def get(self, key):
        pass

    def get_bucket_index(self, key):
        return self.get_hash_code(key)

    def get_hash_code(self, key):
        key = str(key)

        current_coefficient = 1
        hash_code = 0

        for character in key:
            hash_code += ord(character) * current_coefficient
            current_coefficient *= self.p

        return hash_code

    def size(self):
        return self.num_entries

hash_map = HashMap()
bucket_index = hash_map.get_bucket_index("abcd")
print(bucket_index)


