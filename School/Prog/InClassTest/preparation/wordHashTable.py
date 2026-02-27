from hashTableADT import HashTableAdt
class WordHashTable:
    def __init__(self,size):
        self.hashTable = HashTableAdt(size)

    def insert(self, word):
        self.hashTable.insert(word)

    def get_frequency(self,word):
        counter = 0
        for element in self.hashTable.array:
            if element == word:
                counter += 1
        return counter

table = WordHashTable(size=10)
table.insert("data")
table.insert("science")
#table.insert("data")
print(table.get_frequency("data")) # 2print(table.get_frequency("science")) # 1

