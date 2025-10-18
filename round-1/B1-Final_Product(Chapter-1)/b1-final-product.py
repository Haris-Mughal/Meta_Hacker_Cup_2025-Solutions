from math import isqrt

def best_divisor_leq_A(B: int, A: int) -> int:
    """Return the largest divisor of B that is <= A."""
    if A >= B:
        return B
    if B % A == 0:
        return A

    best = 1
    r = isqrt(B)
    for i in range(1, r + 1):
        if B % i == 0:
            if i <= A and i > best:
                best = i
            j = B // i
            if j <= A and j > best:
                best = j
            if best == A:
                break
    return best


def solve():
    with open("input.txt", "r", encoding="utf-8") as fin:
        T = int(fin.readline().strip())
        results = []

        for case_idx in range(1, T + 1):
            N, A, B = map(int, fin.readline().split())

            coolness = 1
            phase1 = []

            # --- Phase 1: grow step-by-step but never exceed A ---
            for _ in range(N):
                if coolness * 3 <= A:
                    phase1.append(3)
                    coolness *= 3
                elif coolness * 2 <= A:
                    phase1.append(2)
                    coolness *= 2
                else:
                    phase1.append(1)

            # --- Phase 2: reach B exactly ---
            remaining = B // coolness
            phase2 = [remaining] + [1] * (N - 1)

            seq = phase1 + phase2
            results.append(f"Case #{case_idx}: " + " ".join(map(str, seq)))

    print("\n".join(results))


if __name__ == "__main__":
    solve()
