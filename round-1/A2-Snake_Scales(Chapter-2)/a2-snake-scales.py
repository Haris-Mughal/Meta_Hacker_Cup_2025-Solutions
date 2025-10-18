def can_visit_all(A, h):
    n = len(A)
    visited = [False] * n

    starts = [i for i in range(n) if A[i] <= h]


    if not starts:
        return False

    stackk = starts[:]


    while stackk:
        i = stackk.pop()

        if visited[i]:
            continue

        visited[i] = True

        if i - 1 >= 0 and not visited[i - 1] and abs(A[i - 1] - A[i]) <= h:
            stackk.append(i - 1)

        if i + 1 < n and not visited[i + 1] and abs(A[i + 1] - A[i]) <= h:
            stackk.append(i + 1)

    return all(visited)


def solve():
    with open("input.txt", "r") as f:
        daata = f.read().strip().split()

    t = int(daata[0])
    idx = 1


    results = []

    for case_num in range(1, t + 1):
        n = int(daata[idx]); idx += 1

        A = list(map(int, daata[idx:idx + n])); idx += n

        lower, higher = 0, max(A)


        while lower < higher:
            midd = (lower + higher) // 2

            if can_visit_all(A, midd):
                higher = midd
            else:

                lower = midd + 1

        results.append(f"Case #{case_num}: {lower}")

    print("\n".join(results))


if __name__ == "__main__":
    solve()
