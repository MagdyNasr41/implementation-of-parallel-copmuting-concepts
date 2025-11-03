import random

class CacheLevel:
    def __init__(self, name, size, latency, data, next_level=None):
        self.name = name
        self.size = size
        self.latency = latency
        self.data = data  
        self.next_level = next_level
        self.read_hits = 0
        self.write_hits = 0
        self.misses = 0
    
    # Hard coded if condition (Bad Code)
    def read(self, address):
        """Access a memory address; return total latency"""
        # Check if address exists in L1
        if address in self.data:
            self.read_hits += 1 # if found increase the read_hits and return the latency of that layer
            return self.latency  

        self.misses += 1 # if not found in L1 add a miss

        # Check if address exists in L2
        if address in self.next_level.data:
            self.next_level.read_hits += 1
            return self.next_level.latency
        else:
            self.next_level.misses += 1

            # Check if address exists in L3
            if address in self.next_level.next_level.data:
                self.next_level.next_level.read_hits += 1
                return self.next_level.next_level.latency
            else:
                self.next_level.next_level.misses += 1

                # Check if address exists in RAM
                if address in self.next_level.next_level.next_level.data:
                    self.next_level.next_level.next_level.read_hits += 1
                    return self.next_level.next_level.next_level.latency
                else:
                    self.next_level.next_level.next_level.misses += 1
                    self.write(address)
                    return self.next_level.next_level.next_level.latency
    
    # Recursion! (Intelligent Code)
    def read(self, address):
        if address in self.data:
            self.read_hits += 1
            return self.latency

        self.misses += 1
        if self.next_level:
            next_latency = self.next_level.read(address)
            # self.write(address)  # bring into current cache
            return self.latency + next_latency
        else:
            # No next level (RAM)
            self.write(address)
            return self.latency


    def write(self, address, flag=False):

        # when i call write not from read but to actually write data, then i should add a hit or miss so flag will be true.
        if flag:
            if address in self.data:
                self.write_hits += 1
                return 0 
            self.misses += 1

        if len(self.data) >= self.size:
            evicted = self.data.pop(0)
            print(f"{self.name}: Evicted {evicted}")

        # Add new address
        self.data.append(address)
        print(f"{self.name}: Wrote {address}")

        # Propagate write to lower level (if any)
        if self.next_level:
            self.next_level.write(address)

    def stats(self):
        total = self.read_hits + self.write_hits + self.misses
        hit_rate = (self.read_hits + self.write_hits) / total if total > 0 else 0
        return f"{self.name}: Hits={self.read_hits+self.write_hits}, Misses={self.misses}, HitRate={hit_rate:.2f}"


class Prefetcher:
    def __init__(self, prefetch_distance=1):
        self.last_address = None
        self.prefetch_distance = prefetch_distance

    def detect_and_prefetch(self, current_addr, cache):
        """Simple stride-1 prefetcher"""
        if self.last_address is not None and current_addr == self.last_address + 1:
            next_addr = current_addr + self.prefetch_distance
            cache.insert(next_addr)  # prefetch into L2 or L1
        self.last_address = current_addr


# ------------------------------
# Global shared data
# ------------------------------
L1_data  = [0,1,2,3,4,5,6,7]  
L2_data  = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]  
L3_data  = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31] 
RAM_data = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33] 


# ------------------------------
# Build hierarchy
# ------------------------------
RAM = CacheLevel("RAM", size=99999, latency=50, data=RAM_data)
L3 = CacheLevel("L3", size=32, latency=12, next_level=RAM, data=L3_data)
L2 = CacheLevel("L2", size=16, latency=4, next_level=L3, data=L2_data)
L1 = CacheLevel("L1", size=8, latency=1, next_level=L2, data=L1_data)
# CPU starts checking the existance of a data from L1 layer.

prefetcher = Prefetcher(prefetch_distance=1)

# ------------------------------
# Simulate access patterns
# ------------------------------
addresses = list(range(0, 35))  # (from 0 to 34) total 35 address
# You can also try random: addresses = [random.randint(0, 50) for _ in range(40)]

total_latency = 0

print("(L1  initially contains 0 to 7):")
print("(L2  initially contains 0 to 15):")
print("(L3  initially contains 0 to 32):")
print("(RAM initially contains 0 to 33):")

for address in addresses:
    latency = L1.read(address)
    total_latency += latency

# ------------------------------
# Results
# ------------------------------
print("=== Simulation Results ===")
print(L1.stats())
print(L2.stats())
print(L3.stats())
print(RAM.stats())
print(f"Average access latency: {total_latency / len(addresses):.2f} cycles")
