import itertools
import random
import time
import matplotlib.pyplot as plt

class Job:
    def __init__(self, start, finish, weight):
        self.start  = start
        self.finish = finish
        self.weight = weight
    def __repr__(self):
        return f"Job({self.start}, {self.finish}, {self.weight})"

def is_non_overlapping(subset):
    subset = sorted(subset, key=lambda j: j.start)
    for i in range(len(subset) - 1):
        if subset[i].finish > subset[i + 1].start:
            return False
    return True

def binary_search(jobs, i):
    lo = 0
    hi = i - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if jobs[mid].finish <= jobs[i].start:
            if mid + 1 < len(jobs) and jobs[mid + 1].finish <= jobs[i].start:
                lo = mid + 1
            else:
                return mid
        else:
            hi = mid - 1
    return -1

def dynamic_programming(jobs): #O(nlogn)
    # Sort jobs by finish time
    jobs_sorted = sorted(jobs, key=lambda j: j.finish)
    n = len(jobs_sorted)

    # P[i] = index of last non-conflicting job before job i
    P = [binary_search(jobs_sorted, i) for i in range(n)]

    # DP table
    dp = [0] * (n + 1)

    # Fill DP table
    for i in range(1, n + 1):
        include = jobs_sorted[i - 1].weight
        if P[i - 1] != -1:
            include += dp[P[i - 1] + 1]
        exclude = dp[i - 1]
        dp[i] = max(include, exclude)

    # Reconstruct solution
    chosen = []
    i = n
    while i > 0:
        if jobs_sorted[i - 1].weight + (dp[P[i - 1] + 1] if P[i - 1] != -1 else 0) >= dp[i - 1]:
            chosen.append(jobs_sorted[i - 1])
            i = P[i - 1] + 1
        else:
            i -= 1

    chosen.reverse()

    # Convert chosen jobs to original indices
    indices = {jobs.index(j) for j in chosen}

    return chosen, indices, dp[-1]




def brute_force(jobs): #O(n2^n)
    best_subset = []
    best_weight = 0
    n = len(jobs)

    for r in range(1, n + 1):
        for subset in itertools.combinations(jobs, r):
            if is_non_overlapping(subset):
                w = sum(j.weight for j in subset)
                if w > best_weight:
                    best_weight = w
                    best_subset = subset

    # Return indices of chosen jobs + total weight
    indices = {jobs.index(j) for j in best_subset}
    return list(best_subset),indices, best_weight

def job_creator(n):
    jobs = []
    for _ in range(n):
        start = random.randint(1, n//2)
        finish = start + random.randint(1, n//2)
        weight = random.randint(1,20)
        jobs.append(Job(start, finish,weight))
    return jobs

sizes = [10, 15, 20, 25]
dynamic_time = []
brute_times = []

for n in sizes:
    jobs = job_creator(n)

    start = time.time()
    subset, order, weight = dynamic_programming(jobs)
    end = time.time()
    dynamic_time.append((end - start))

    start = time.time()
    subset, order, weight = brute_force(jobs)
    end = time.time()
    brute_times.append((end - start))

plt.plot(sizes, dynamic_time, marker='o', label='Dynamic Programming')
plt.plot(sizes, brute_times, marker='o', label='Brute Force')
plt.xlabel('Number of Jobs')
plt.ylabel('Time (seconds)')
plt.title('Time vs Problem Size')
plt.legend()
plt.grid(True)
plt.show()