# 🍳 Chef Alfredo and the Perfect Temperature

Chef Alfredo is catering his friend Benji's wedding and has **N dishes** (numbered from `1` to `N`) that must all be served at their **exact target temperatures**.

- Each dish `i` currently has a temperature of `Aᵢ` degrees.  
- Each dish `i` must reach a **target temperature** of `Bᵢ` degrees.

---

## 🧠 Problem Statement

While Alfredo owns a fancy thermometer, he prefers to trust his **chef instincts** rather than measure constantly.  
His strategy is simple — he repeatedly performs the following operation:

> Pick two dishes `i` and `j` of **different temperatures**, and **warm up the colder dish** so that it **matches** the temperature of the hotter one.

Your task is to help Alfredo determine a sequence of at most `N` such operations to make all dishes reach their **target temperatures**, or determine that it’s **impossible**.

---

## ⚙️ Operation Rule

- You can only **increase** a dish’s temperature — never decrease it.
- Each operation selects two indices `(i, j)`:
  - If `A[i] < A[j]`, then `A[i]` becomes `A[j]`.

---

## 🧩 Constraints

```
1 ≤ T ≤ 95
1 ≤ N ≤ 500,000
1 ≤ Aᵢ ≤ N
1 ≤ Bᵢ ≤ N
```

---

## 📥 Input Format

- The first line contains an integer `T`, the number of test cases.  
- For each test case:
  - The first line contains a single integer `N`.
  - The second line contains `N` space-separated integers — `A₁, A₂, …, Aₙ` (current temperatures).
  - The third line contains `N` space-separated integers — `B₁, B₂, …, Bₙ` (target temperatures).

---

## 📤 Output Format

For the `i`-th test case:

- If it’s possible to reach all target temperatures:
`Case #i: K`
followed by `K` lines, each containing two integers `i j`, representing the dishes chosen for each operation.
- If it’s impossible, output:
`Case #i: -1` 


where `0 ≤ K ≤ N`.

---

## 💡 Example Explanation

**Test Case 2:**

Initial: `[1, 1, 2]`  
Target: `[2, 2, 2]`

Operations:
1. Warm dish 1 using dish 3 → `[2, 1, 2]`
2. Warm dish 2 using dish 3 → `[2, 2, 2]` ✅

---

## 🧾 Sample Input
```
6
5
1 2 3 4 5
1 2 3 4 5
3
1 1 2
2 2 2
4
1 2 3 4
3 4 4 4
4
1 2 3 4
1 2 3 3
3
1 3 3
2 2 2
2
1 2
2 1
```

---

## ✅ Sample Output

```
Case #1: 0
Case #2: 2
3 1
3 2
Case #3: 3
3 1
4 2
4 3
Case #4: -1
Case #5: -1
Case #6: -1
```

---

## 🧮 Logic Summary

- You can **only heat up**, never cool down.  
  ⇒ If `Bᵢ < Aᵢ` for any dish → ❌ impossible.  
- Every **target temperature** must already exist in the current list `A`.  
  ⇒ Otherwise, there’s no “source” dish to copy from.  
- The algorithm processes target temperatures **in ascending order** — ensuring valid sources always exist.

---

## ⚡ Complexity

- **Time Complexity:** `O(N log N)`  
- **Space Complexity:** `O(N)`

---

## 🧰 Files

| File | Description |
|------|--------------|
| `warmup.py` | Main solution script |
| `input.txt` | Contains test cases |
| `output.txt` *(optional)* | Can be used to save program output |

---

## 👨‍🍳 Example Run

```bash
python warmup.py
```

**Input:** read automatically from input.txt
**Output:** printed in console or redirected to output.txt


