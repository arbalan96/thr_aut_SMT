# Verification of threshold automata using SMT solvers
Code for the paper "Complexity of Verification and Synthesis of Threshold Automata"

This is the Python code for the paper "Complexity of Verification and Synthesis of Threshold Automata".
For it to work, Z3 needs to be installed.

## Benchmarks

There are two set of benchmarks: automatic and manual. The manual folder consits of hand-coded threshold automata, the automatic contains the other benchmarks.

Both those folders contain an 'executor.py' file, which if run, will ask for the benchmark that you want to test (and also the case that you want to test).
For each specification for that benchmark, it creates a python file with Z3 constraints and then runs it. For each specification, it outputs whether it is satisfied or not.
Finally, it returns the total time taken for that benchmark.

The file 'executor_all.py' simply executed all of the benchmarks on all of the specifications.

