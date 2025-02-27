# DFA Minimization Assignment

## Student Information
- **Student’s Full Name:** Hever André Alfonso Jiménez and Moises Vergara Garces
- **Student’s Class Number:** C2561-SI2002-7308

## Environment Details
- **Operating System:** (Example: macOS Catalina 10.15.7 / Windows 10 / Linux distribution)
- **Processor:** 2.4 GHz Intel Core i5 (quad-core)
- **Programming Language:** Python 3.13.0
- **Tools Used:** Standard Python libraries (no external dependencies)

## How to Run the Implementation

1. **Clone or Download the Repository:**
   - Use Git to clone the repository or download the ZIP file and extract it.

2. **Navigate to the Project Directory:**
   - Open a terminal/command prompt and navigate to the directory containing the source code.

3. **Run the Program:**
   - Execute the program using Python by running the following command:
     ```bash
     python dfa.py < input.txt
     ```
   - Here, `input.txt` should contain the test cases formatted according to the assignment specifications:
     - The first line contains the number of cases.
     - For each case:
       - A line with the number of states.
       - A line with the alphabet (symbols separated by spaces).
       - A line with the final states (numbers separated by spaces).
       - A line for each state containing the transition values (one row per state).

## Explanation of the Algorithm

The implemented algorithm is based on the table-filling (marking) method for DFA minimization as described in Kozen's *Automata and Computability* (1997, Lecture 14). The steps involved are:

1. **Input Parsing:**
   - The DFA is read from input, including the number of states, the alphabet, the final states, and the transition table.

2. **Initialization:**
   - A 2D boolean table `marked` is initialized to record whether pairs of states are distinguishable.
   - Pairs where one state is a final state and the other is not are immediately marked as distinguishable.

3. **Iterative Marking Process:**
   - The algorithm repeatedly scans through all pairs of states.
   - For each pair, it checks if there exists any input symbol for which the corresponding transitions lead to a pair that has already been marked as distinguishable.
   - If such an input is found, the pair is marked as distinguishable.
   - This process continues until no further changes are made.

4. **Collecting Equivalent States:**
   - After the marking process stabilizes, pairs that remain unmarked are considered equivalent.
   - These pairs are output in lexicographical order as the result.

This algorithm ensures that all equivalent states are identified, allowing the DFA to be minimized by collapsing these states.

## Additional Notes
- Make sure that the input DFA has no inaccessible states, as per the assignment requirements.
- The program uses standard input/output operations; ensure the input is correctly piped or redirected when executing the script.