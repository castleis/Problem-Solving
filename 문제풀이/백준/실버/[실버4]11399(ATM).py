import sys
input = sys.stdin.readline

def solve(times):
    whole_time = 0
    times.sort()
    T = 0
    for t in times:
        T += t
        whole_time += T
    return whole_time

def main():
    N = int(input())
    times = list(map(int,input().split()))
    print(solve(times))

if __name__ == "__main__":
    main()
