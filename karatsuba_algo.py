# Karatsuba algorithm implementation
# Note that Karatsuba only faster with manual calculation, with computer calculation
# The computation is more complex, so it is slower

import random
import time

def karatsuba(x, y):
    if x < 10 or y < 10:
        return x*y

    n = max(len(str(x)), len(str(y)))
    half = n//2
    a = x//(10**half)
    b = x%(10**half)
    
    c = y//(10**half)
    d = y%(10**half)

    ac = karatsuba(a, c)
    bd = karatsuba(b, d)
    ad_plus_bc = karatsuba(a+b, c+d)- ac - bd

    return ac*(10**(half*2)) + ad_plus_bc*(10**half) + bd

if __name__ == "__main__":
    a = 146
    b = 374289
    start_time = time.time()
    cumulative_k_time = 0
    cumulative_orig_time = 0
    for i in range(1000):
        x = random.randint(1, 10000)
        y = random.randint(1, 10000)

        k_start_time = time.time()
        karatsuba(x, y)
        cumulative_k_time += time.time() - k_start_time
        
        orig_start_time = time.time()
        x*y
        cumulative_orig_time += time.time() - orig_start_time

    print(f"Total time for Karatsuba: {cumulative_k_time}, Total time for Orig computation: {cumulative_orig_time}")     
    # Total time for Karatsuba: 0.01633453369140625, Total time for Orig computation: 0.0
