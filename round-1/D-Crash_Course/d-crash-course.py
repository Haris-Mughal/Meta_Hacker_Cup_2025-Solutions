def solve_game(s):
    memo = {}
    
    def can_win(state, is_alice_turn):
        if not state:
            return False
        
        key = (is_alice_turn, state)
        if key in memo:
            return memo[key]
        
        if is_alice_turn:
            has_move = False
            for i in range(len(state)):
                if state[i] == 'A':
                    has_move = True
                    remaining = state[i+1:]
                    
                    if not can_win(remaining, False):
                        memo[key] = True
                        return True
            
            memo[key] = False
            return False
        
        else:
            has_move = False
            for i in range(len(state)):
                if state[i] == 'B':
                    has_move = True
                    remaining = state[:i]
                    
                    if not can_win(remaining, True):
                        memo[key] = True
                        return True
            
            memo[key] = False
            return False
    
    if can_win(s, True):
        return "Alice"
    else:
        return "Bob"


with open('input.txt', 'r') as infile:
    lines = infile.readlines()

results = []
t = int(lines[0].strip())
line_idx = 1

for case_num in range(1, t + 1):
    n = int(lines[line_idx].strip())
    s = lines[line_idx + 1].strip()
    line_idx += 2
    
    result = solve_game(s)
    results.append(f"Case #{case_num}: {result}")

with open('d-crash-course-output.txt', 'w') as outfile:
    for result in results:
        outfile.write(result + '\n')