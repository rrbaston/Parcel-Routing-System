class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]

    def _hash_function(self,key):
        return key % self.size
    
    def insert(self, package):
        index = self._hash_function(package.package_id)
        # Check for existing package ID and update
        for item in self.table[index]:
            if item.package_id == package.package_id:
                self.table[index].remove(item)
                break
        # Insert new item
        self.table[index].append(package)

    def delete(self, package):
        index = self._hash_function(package.package_id)
        for item in self.table[index]:
            if item.package_id == package.package_id:
                self.table[index].remove(item)
    
    def display(self):
        for i, bucket in enumerate(self.table):
            if bucket:
                print(f"Bucket {i}:")
                for package in bucket:
                    print(f"  {package}")
            else:
                print(f"Bucket {i}: Empty")
    
    def lookup(self, package_id):
        index = self._hash_function(package_id)
        for package in self.table[index]:
            if package.package_id == package_id:
                return package
            return None #Return None if package not found