# Verification of threshold automata using SMT solvers
Code for the paper "Complexity of Verification and Synthesis of Threshold Automata"

This is the Python code for the papers "Complexity of Verification and Synthesis of Threshold Automata" (ATVA20)
and "Parameterized Complexity of Safety of Threshold Automata" (FST&TCS20).
For both of them to work, Z3 needs to be installed.

## ATVA 20 Benchmarks

There are two sets of benchmarks: automatic and manual. The manual folder consits of hand-coded threshold automata, the automatic contains the other benchmarks.

Both those folders contain an 'executor.py' file, which if run, will ask for the benchmark that you want to test (and also the case that you want to test).
For each specification for that benchmark, it creates a python file with Z3 constraints and then runs it. For each specification, it outputs whether it is satisfied or not.
Finally, it returns the total time taken for that benchmark.

The file 'executor_all.py' simply executes all of the benchmarks on all of the specifications.

## FST&TCS 20 Benchmarks

Once again there are two sets of benchmarks, but both of them are now in a single folder.

The 'executor.py' file, if run, will ask for the benchmark that you want to test (and also the case that you want to test).
For each (safety) specification for that benchmark, it creates a python file with Z3 constraints and then runs it. For each specification, it outputs whether it is satisfied or not.
Finally, it returns the total time taken for that benchmark.

The file 'executor_all.py' simply executes all of the benchmarks on all of the specifications.
