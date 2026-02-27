import time
from LinkedList import LinkedList


class Block:
    def __init__(self, index, data, previous_hash):
        self.index = index
        self.timestamp = time.time()
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        # TODO: Implement!
        pass

    def __str__(self):
        return f"Block {self.index} [data={self.data}, hash={self.hash}, prev={self.previous_hash}]"


class Blockchain:
    def __init__(self):
        self.chain = LinkedList()
        genesis = Block(0, "Genesis Block", 0)
        self.chain.append(genesis)


    def add_block(self, data):
        x = self.chain.head
        prev_node = None
        while x:
            if x.next is None:
                prev_node = x
            x = x.next
        index = prev_node.hash
        newblock_ = Block(self.chain.size, data, index)
        self.chain.append(newblock_)

    def is_valid(self):
         
        pass

    def __str__(self):
        return str(self.chain)


if __name__ == "__main__":
    print("=== Blockchain Test ===")
    blockchain = Blockchain()

    # Add blocks
    blockchain.add_block("Alice -> Bob: 50 CHF")
    blockchain.add_block("Bob -> Charlie: 20 CHF")
    blockchain.add_block("Charlie -> Alice: 10 CHF")
    blockchain.add_block("Alice -> Dave: 5 CHF")
    blockchain.add_block("Dave -> Eve: 2 CHF")

    # Print blockchain
    print(blockchain)

    # Validate blockchain
    assert blockchain.is_valid() is True
    print("Blockchain is valid")

    # Tamper with blockchain
    block_to_tamper = blockchain.chain[2]
    block_to_tamper.data = "Bob -> Charlie: 999 CHF"
    block_to_tamper.hash = block_to_tamper.calculate_hash()

    # Check validation again
    assert blockchain.is_valid() is False
    print("Blockchain tampering detected correctly!")
