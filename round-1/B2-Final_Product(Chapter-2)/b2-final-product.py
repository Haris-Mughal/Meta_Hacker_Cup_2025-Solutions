from math import isqrt

MOD = 10**9 + 7

def prime_factors(n: int):
    fac = {}
    while n % 2 == 0:
        fac[2] = fac.get(2, 0) + 1
        n //= 2
    d = 3
    lim = isqrt(n)
    while d <= lim and n > 1:
        while n % d == 0:
            fac[d] = fac.get(d, 0) + 1
            n //= d
            lim = isqrt(n)
        d += 2
    if n > 1:
        fac[n] = fac.get(n, 0) + 1
    return fac

def precompute_stars_table(N: int, e: int):
    arr = [1] * (e + 1)
    for x in range(1, e + 1):
        arr[x] = (arr[x-1] * ((N - 1 + x) % MOD)) % MOD
        arr[x] = (arr[x] * pow(x, MOD - 2, MOD)) % MOD
    return arr

def solve_case(N: int, A: int, B: int) -> int:
    if B == 1:
        return 1 if A >= 1 else 0

    pf = prime_factors(B)
    primes = list(pf.keys())
    exps = [pf[p] for p in primes]

    ways_first = []
    ways_second = []
    for e in exps:
        t = precompute_stars_table(N, e) 
        ways_first.append(t)        
        ways_second.append(t[::-1])

    total = 0

    def dfs(idx: int, prod: int, wf: int, ws: int):
        nonlocal total
        if idx == len(primes):
            total = (total + (wf * ws) % MOD) % MOD
            return
        p, e = primes[idx], exps[idx]
        cur_pow = 1
        for x in range(e + 1):
            if prod * cur_pow > A:
                break
            dfs(idx + 1,
                prod * cur_pow,
                (wf * ways_first[idx][x]) % MOD,
                (ws * ways_second[idx][x]) % MOD)
            # next power
            if x != e:
                cur_pow *= p
                if cur_pow > A and prod >= 1:
                    pass

    dfs(0, 1, 1, 1)
    return total

def main():
    with open('input.txt', 'r', encoding='utf-8') as f:
        it = iter(f.read().strip().split())
    T = int(next(it))
    out = []
    for case in range(1, T + 1):
        N = int(next(it)); A = int(next(it)); B = int(next(it))
        ans = solve_case(N, A, B)
        out.append(f"Case #{case}: {ans}")
    print('\n'.join(out) + '\n')

if __name__ == "__main__":
    main()
