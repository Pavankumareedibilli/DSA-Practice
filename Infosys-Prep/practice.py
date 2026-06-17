import copy
import time

a = list(range(10_000))

start = time.time()
copy.copy(a)
print("shallow:", time.time() - start)

start = time.time()
copy.deepcopy(a)
print("deep:", time.time() - start)