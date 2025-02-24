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