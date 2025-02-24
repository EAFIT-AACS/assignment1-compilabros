def main():
    import sys
    input = sys.stdin.read().split('\n')
    ptr = 0
    c = int(input[ptr].strip())
    ptr += 1
    for _ in range(c):
        # Read number of states
        n = int(input[ptr].strip())
        ptr += 1
        # Read alphabet
        alphabet = input[ptr].split()
        ptr += 1
        # Read final states
        final_states = list(map(int, input[ptr].split()))
        final_set = set(final_states)
        ptr += 1
        # Read transitions
        transitions = []
        for _ in range(n):
            trans = list(map(int, input[ptr].split()))
            transitions.append(trans)
            ptr += 1
        # Initialize marked matrix
        marked = [[False for _ in range(n)] for __ in range(n)]
        # Step 2: Mark pairs where one is final and the other is not
        for p in range(n):
            for q in range(p+1, n):
                if (p in final_set) != (q in final_set):
                    marked[p][q] = True
        # Step 3: Iterate until no changes
        changed = True
        while changed:
            changed = False
            for p in range(n):
                for q in range(p+1, n):
                    if not marked[p][q]:
                        for a_idx in range(len(alphabet)):
                            s = transitions[p][a_idx]
                            t = transitions[q][a_idx]
                            if s != t:
                                s_, t_ = (s, t) if s < t else (t, s)
                                if marked[s_][t_]:
                                    marked[p][q] = True
                                    changed = True
                                    break  # Break out of the symbol loop
                        if marked[p][q]:
                            continue  
                        
        # Collect equivalent pairs
        equivalent = []
        for p in range(n):
            for q in range(p+1, n):
                if not marked[p][q]:
                    equivalent.append((p, q))
        # Prepare output
        output_parts = []
        for p, q in equivalent:
            output_parts.append(str(p))
            output_parts.append(str(q))
        print(' '.join(output_parts))
        
if __name__ == "__main__":
    main()