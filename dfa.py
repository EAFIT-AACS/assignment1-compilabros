def read_input():
    """
    Reads input from stdin and processes it into test cases.
    Each test case consists of:
    - Number of states (n)
    - Alphabet symbols
    - Final states set
    - Transition table
    """
    import sys
    input_data = sys.stdin.read().split('\n')
    ptr = 0
    c = int(input_data[ptr].strip())
    ptr += 1
    test_cases = []
    
    for _ in range(c):
        n = int(input_data[ptr].strip())
        ptr += 1
        alphabet = input_data[ptr].split()
        ptr += 1
        final_states = list(map(int, input_data[ptr].split()))
        final_set = set(final_states)
        ptr += 1
        transitions = []
        for _ in range(n):
            trans = list(map(int, input_data[ptr].split()))
            transitions.append(trans[1:1 + len(alphabet)])
            ptr += 1
        test_cases.append((n, alphabet, final_set, transitions))
    
    return test_cases

def initialize_marked(n, final_set):
    """
    Initializes the marking table for state pairs.
    Marks pairs (p, q) where one state is final and the other is not.
    """
    marked = [[False] * n for _ in range(n)]
    for p in range(n):
        for q in range(p + 1, n):
            if (p in final_set) != (q in final_set):
                marked[p][q] = True
    return marked

def mark_distinguishable(n, alphabet, transitions, marked):
    """
    Iteratively marks state pairs as distinguishable based on transitions.
    Uses a propagation approach until no more changes occur.
    """
    changed = True
    while changed:
        changed = False
        for p in range(n):
            for q in range(p + 1, n):
                if not marked[p][q]:
                    for a_idx in range(len(alphabet)):
                        s, t = transitions[p][a_idx], transitions[q][a_idx]
                        s_, t_ = (s, t) if s < t else (t, s)
                        if s_ < t_ and marked[s_][t_]:
                            marked[p][q] = True
                            changed = True
                            break

def collect_equivalent_pairs(n, marked):
    """
    Collects and returns equivalent state pairs from the marking table.
    Equivalent states are those that remain unmarked.
    """
    equivalent = []
    for p in range(n):
        for q in range(p + 1, n):
            if not marked[p][q]:
                equivalent.append((p, q))
    return equivalent

def main():
    """
    Main function to process input and apply DFA minimization.
    Prints equivalent state pairs for each test case.
    """
    test_cases = read_input()
    for n, alphabet, final_set, transitions in test_cases:
        marked = initialize_marked(n, final_set)
        mark_distinguishable(n, alphabet, transitions, marked)
        equivalent = collect_equivalent_pairs(n, marked)
        output = ' '.join([f"({p}, {q})" for p, q in equivalent])
        print(output)

if __name__ == "__main__":
    main() 