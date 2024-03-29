import numpy, sys, time, random

if (len(sys.argv) != 2):
    print("usage: python %s N" % sys.argv[0])
    quit()

n = int(sys.argv[1])

d = list(range(n))
e = list(range(n))

for i in range(n):
    d[i] = random.randrange(n)  
    e[i] = i  

begin = time.time()

sum = 0
for i in range(n):
    sum += e[d[i]] #0.430
    #sum += e[i] #0.181

end = time.time()
print("time: %.6f sec" % (end - begin))

# Print C for debugging. Comment out the print before measuring the execution time.
#total = 0
#for i in range(n):
    #for j in range(n):
        # print c[i, j]
        #total += c[i, j]
# Print out the sum of all values in C.
# This should be 450 for N=3, 3680 for N=4, and 18250 for N=5.
#print("sum: %.6f" % total)