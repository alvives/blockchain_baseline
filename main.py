import hashlib

class NeuralCoinBlock:
    def __init__(self, previous_block_hash, transaction_list):
        self.previous_block_hash = previous_block_hash
        self.transaction_list = transaction_list

        # Create block data string for hashing
        self.block_data = previous_block_hash + "-" + "-".join(transaction_list)
        self.block_hash = hashlib.sha256(self.block_data.encode()).hexdigest()

    def print_data(self):
        print("🧩  Block Hash:", self.block_hash)
        print("🔗  Previous Hash:", self.previous_block_hash)
        print("💰  Transactions:")
        for tx in self.transaction_list:
            print("   •", tx)
        print("-" * 60)


# Example transactions
t1 = "Mapfre sends 2 ALC to Mutua"
t2 = "AXA sends 4 ALC to The Occident"
t3 = "Ocaso sends 10 ALC to Santa Lucia"
t4 = "Helvetia sends 4 ALC to Caixa"
t5 = "AXA sends 4 ALC to The Santa Lucia"
t6 = "ING sends 5 ALC to Mutua"

# Create blocks
first_block = NeuralCoinBlock("First String", [t1, t2])
first_block.print_data()

second_block = NeuralCoinBlock(first_block.block_hash, [t3, t4])
second_block.print_data()

third_block = NeuralCoinBlock(second_block.block_hash, [t5, t6])
third_block.print_data()
