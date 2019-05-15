import subprocess
import sys
import time

if __name__ == "__main__":
    start = time.time()

    print("n,time")

    for i in range(2000):
        res = subprocess.run(["./pyne", str(i)], stdout=subprocess.PIPE)
        print(f'{i},{res.stdout.decode("utf8")}')

    elapsed_time = time.time() - start
    # print(elapsed_time)
