def solve_case(arr):
    n = len(arr)
    if all(x == 0 for x in arr):
        return 0
    
    total = 0
    for i in range(n):
        for j in range(i, n):
            total += (arr[j] - arr[i]) ** 2
    
    return total

def main():
    with open("input.txt", "r") as f:
        t = int(f.readline().strip())
        results = []
        for case in range(1, t + 1):
            n = int(f.readline().strip())
            arr = list(map(int, f.readline().split()))
            ans = solve_case(arr)
            results.append(f"Case #{case}: {ans}")
    
    with open("c-narrowing-down-output.txt", "w") as f:
        f.write("\n".join(results) + "\n")

if __name__ == "__main__":
    main()
