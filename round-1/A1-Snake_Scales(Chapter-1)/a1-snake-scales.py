def solve():
    with open("input.txt", "r") as my_input_file:
        data = my_input_file.read().strip().split()
    
    t = int(data[0])
    index = 1
    results = []
    
    for case_number in range(1, t + 1):
        n = int(data[index]); index += 1
        A = list(map(int, data[index:index + n]))
        index += n
        
        if n == 1:
            ans = 0
        else:
            ans = max(abs(A[i] - A[i + 1]) for i in range(n - 1))
        
        results.append(f"Case #{case_number}: {ans}")
    
    print("\n".join(results))


if __name__ == "__main__":
    solve()
