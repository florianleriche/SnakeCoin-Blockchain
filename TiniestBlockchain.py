# --------------------------------------------------------------
#  Project :    Tiniest Blockchain
#  Author  :    Floks
#  Description :
#      A simple blockchain implementation in Python 3.
#      This program creates a blockchain with a Genesis block
#      and adds successive blocks by generating a unique hash.
# --------------------------------------------------------------

import hashlib as hasher
import datetime as date

# Definition of a block
class Block:
    def __init__(self, index, timestamp, data, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.hash_block()

    def hash_block(self):
        sha = hasher.sha256()
        sha.update(f"{self.index}{self.timestamp}{self.data}{self.previous_hash}".encode('utf-8'))
        return sha.hexdigest()

    def __repr__(self):
        return f"Block(index={self.index}, hash={self.hash})"

# Generation of the Genesis block
def create_genesis_block():
    return Block(0, date.datetime.now(), "Genesis Block", "0")

# Generation of the subsequent blocks
def next_block(last_block):
    this_index = last_block.index + 1
    this_timestamp = date.datetime.now()
    this_data = f"Hey! I'm block {this_index}"
    this_hash = last_block.hash
    return Block(this_index, this_timestamp, this_data, this_hash)

# Create the blockchain with the Genesis block
blockchain = [create_genesis_block()]
previous_block = blockchain[0]

# Number of blocks to add
num_of_blocks_to_add = 20

# Adding blocks to the blockchain
for _ in range(num_of_blocks_to_add):
    block_to_add = next_block(previous_block)
    blockchain.append(block_to_add)
    previous_block = block_to_add

    # Display the added block's information
    print(f"Block #{block_to_add.index} has been added to the blockchain!")
    print(f"Hash: {block_to_add.hash}\n")
