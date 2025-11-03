# Implementation of Parallel Computing Concepts

**Keywords:** Parallel Computing, Computer Architecture, Cache Hierarchy, Memory Latency, CPU Simulation, Prefetching, Multi-level Cache, Performance Analysis

---

## Overview

This repository, **Implementation of Parallel Computing Concepts**, is a growing collection of Python-based implementations and experiments that explore how modern computer systems manage computation, memory, and concurrency.

Each script focuses on a specific concept from **parallel computing**, **computer architecture**, or **systems design**, demonstrating both theory and practice through code.

---

## Project: Cache Hierarchy Simulation

### Project Name: `cache_hierarchy_sim.py`

This simulation models a **multi-level cache hierarchy (L1 → L2 → L3 → RAM)** and measures data access latency, hit/miss rates, and cache propagation behavior.

It helps visualize how data moves across levels in a real CPU architecture and how caching strategies impact performance.

### Features
- Hierarchical cache simulation (L1, L2, L3, RAM)
- Recursive read and write propagation
- Intelligent replacement policy (eviction when full)
- Basic **prefetcher** to anticipate memory access patterns
- Latency and hit/miss rate reporting
- Simple access pattern simulator for deterministic or random sequences

### Layer Details
| Level | Name | Size | Latency (cycles) | Description |
|-------|------|------|------------------|--------------|
| L1 | Level 1 Cache | 8 | 1 | Fastest access; closest to CPU |
| L2 | Level 2 Cache | 16 | 4 | Intermediate speed and size |
| L3 | Level 3 Cache | 32 | 12 | Shared cache between cores |
| RAM | Main Memory | 99999 | 50 | Slowest but largest memory level |

---

## How to Run

### Prerequisites
- Python 3.8 or later
- No external dependencies (pure Python)

### Steps
1. Clone this repository:
   ```bash
   git clone https://github.com/<your-username>/implementation-of-parallel-computing-concepts.git
   cd implementation-of-parallel-computing-concepts
