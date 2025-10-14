import sys
from collections import defaultdict, deque

sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

def warmup():
    t_line = input().strip()
    if not t_line:
        return
    t = int(t_line)
    for case in range(1, t+1):
        n = int(input())
        A = list(map(int, input().split()))
        B = list(map(int, input().split()))

        if any(B[i] < A[i] for i in range(n)):
            print(f"Case #{case}: -1")
            continue

        count_A = defaultdict(int)
        for x in A:
            count_A[x] += 1
        distinct_B = set(B)
        impossible = False
        for v in distinct_B:
            if count_A[v] == 0:
                impossible = True
                break
        if impossible:
            print(f"Case #{case}: -1")
            continue

        group_B = defaultdict(list)
        for i, v in enumerate(B):
            group_B[v].append(i)

        cur_indices = defaultdict(deque)
        for i, x in enumerate(A):
            cur_indices[x].append(i)

        operations = []

        for v in sorted(group_B.keys()):
            if not cur_indices[v]:
                impossible = True
                break
            source = cur_indices[v][0]
            for idx in group_B[v]:
                if A[idx] == v:
                    continue
                operations.append((source + 1, idx + 1))
                A[idx] = v
                cur_indices[v].append(idx)

        if impossible:
            print(f"Case #{case}: -1")
        else:
            print(f"Case #{case}: {len(operations)}")
            for x, y in operations:
                print(x, y)


if __name__ == "__main__":
    warmup()
