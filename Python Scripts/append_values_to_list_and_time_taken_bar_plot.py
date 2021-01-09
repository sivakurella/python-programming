import time
import matplotlib.pyplot as plt

times = {}
iterations = 1000
numbers = list(range(20))

for _ in range(iterations):
    # initialize the list
    l = []

    for i in numbers:
        start_time = time.time()
        l.append(i)
        delta = time.time() - start_time
        
        if i not in times:
            times[i] = []
        
        times[i].append(delta)
        

# create avg_times list
avg_times = []
for _ in numbers:
    avg_times.append(sum(times[_]))

# lets plot the avg_times
plt.bar(numbers, avg_times)
    

    
