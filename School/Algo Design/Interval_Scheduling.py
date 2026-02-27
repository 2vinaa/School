from typing import List
import itertools
import random
import matplotlib.pyplot as plt
import time
import numpy as np


class Job:
    def __init__(self, start, finish):
        self.start  = start
        self.finish = finish
  
def interval_scheduling(job):
    
    job = sorted(job, key = lambda j: j.finish)
    
    index = list(range(len(job)))

    max_set = set()
    prev_event_time = 0
    for i in range(len(index)):
        if job[i].start >= prev_event_time:
            max_set.add(i)
            prev_event_time = job[i].finish 
    return max_set

def is_non_overlapping(subset):
        subset = sorted(subset, key=lambda j: j.start)
        for i in range(len(subset) - 1):
            if subset[i].finish > subset[i + 1].start:
                return False
        return True


def brute_force(job):
    max_subset = []
    n = len(job)
    for r in range(1, n + 1):
        for subset in itertools.combinations(job, r):
            if is_non_overlapping(subset) and len(subset) > len(max_subset):
                max_subset = list(subset)
    indices = {job.index(j) for j in max_subset}
    return indices

def job_creator(n):
    jobs = []
    for i in range(n):
        start = random.randint(1, 50)
        finish = start + random.randint(1,50)
        jobs.append(Job(start, finish))
    return jobs


def time_function(func, jobs):
    start = time.time()
    func(jobs)
    end = time.time()
    return (end - start) * 1000  # milliseconds

input_sizes = [50, 100, 200, 300, 500, 1000]
interval_times = []
brute_times = []

for n in input_sizes:
    jobs = job_creator(n)
    interval_times.append(time_function(interval_scheduling, jobs))
    brute_times.append(time_function(brute_force, jobs))

for n, itime, btime in zip(input_sizes, interval_times, brute_times):
    print(f"Input size: {n}, Interval Scheduling time: {itime:.4f} ms, Brute Force time: {btime:.4f} ms")



# Plotting the results
plt.figure(figsize=(10, 6))
plt.plot(input_sizes, interval_times, marker='o', label='Interval Scheduling (sorted)')
plt.plot(input_sizes, brute_times, marker='s', label='Brute Force (no sort)')
plt.xlabel('Number of jobs (n)')
plt.ylabel('Time (milliseconds)')
plt.title('Computational Time Comparison of Interval Scheduling Algorithms')
plt.legend()
plt.grid(True)
plt.show()


#automae the creation of Jobs/intervals
job = [Job(1, 2), Job(3, 5), Job(6, 19), Job(2, 100)]



 
result = interval_scheduling(job)
result2 = brute_force(job)

print('Maximum number of tasks can be executed are', result)
print('Maximum number of tasks can be executed are', result2)
