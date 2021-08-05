# Belajar Python [Dasar] - 03 - Cara Kerja Program dan bytecode
import time
start_time = time.time()

print("Hello, World!!!")

a = 10
for i in range(1, 1000):
    a = i

print(a,"\n")
print(time.time() - start_time, " detik")