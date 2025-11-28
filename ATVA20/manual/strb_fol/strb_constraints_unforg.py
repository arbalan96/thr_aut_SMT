from time import *
start = time()
import sys
from z3 import *
s = Solver()

#Declaring parameter variables

N = Int('N')
T = Int('T')
F = Int('F')
s.add(N >= 0)
s.add(T >= 0)
s.add(F >= 0)

#Adding the resilience condition

s.add(N > 3 * T)
s.add(T >= F)
s.add(T >= 1)

####################################################################################

#Creating constraints for a run between the 0th and 1th configurations

################Step 1#################


#Creating many copies of location variables

loc0_0 = Int('loc0_0')
loc0_1 = Int('loc0_1')
loc0_2 = Int('loc0_2')
loc0_3 = Int('loc0_3')
loc0_4 = Int('loc0_4')
loc0_5 = Int('loc0_5')
loc0_6 = Int('loc0_6')
loc0_7 = Int('loc0_7')
s.add(loc0_0 >= 0)
s.add(loc0_1 >= 0)
s.add(loc0_2 >= 0)
s.add(loc0_3 >= 0)
s.add(loc0_4 >= 0)
s.add(loc0_5 >= 0)
s.add(loc0_6 >= 0)
s.add(loc0_7 >= 0)

loc1_0 = Int('loc1_0')
loc1_1 = Int('loc1_1')
loc1_2 = Int('loc1_2')
loc1_3 = Int('loc1_3')
loc1_4 = Int('loc1_4')
loc1_5 = Int('loc1_5')
loc1_6 = Int('loc1_6')
loc1_7 = Int('loc1_7')
s.add(loc1_0 >= 0)
s.add(loc1_1 >= 0)
s.add(loc1_2 >= 0)
s.add(loc1_3 >= 0)
s.add(loc1_4 >= 0)
s.add(loc1_5 >= 0)
s.add(loc1_6 >= 0)
s.add(loc1_7 >= 0)

locSE_0 = Int('locSE_0')
locSE_1 = Int('locSE_1')
locSE_2 = Int('locSE_2')
locSE_3 = Int('locSE_3')
locSE_4 = Int('locSE_4')
locSE_5 = Int('locSE_5')
locSE_6 = Int('locSE_6')
locSE_7 = Int('locSE_7')
s.add(locSE_0 >= 0)
s.add(locSE_1 >= 0)
s.add(locSE_2 >= 0)
s.add(locSE_3 >= 0)
s.add(locSE_4 >= 0)
s.add(locSE_5 >= 0)
s.add(locSE_6 >= 0)
s.add(locSE_7 >= 0)

locAC_0 = Int('locAC_0')
locAC_1 = Int('locAC_1')
locAC_2 = Int('locAC_2')
locAC_3 = Int('locAC_3')
locAC_4 = Int('locAC_4')
locAC_5 = Int('locAC_5')
locAC_6 = Int('locAC_6')
locAC_7 = Int('locAC_7')
s.add(locAC_0 >= 0)
s.add(locAC_1 >= 0)
s.add(locAC_2 >= 0)
s.add(locAC_3 >= 0)
s.add(locAC_4 >= 0)
s.add(locAC_5 >= 0)
s.add(locAC_6 >= 0)
s.add(locAC_7 >= 0)


#Adding the constraint for the number of processes

s.add(loc0_0 + loc1_0 + locSE_0 + locAC_0 == N - F)
s.add(loc0_1 + loc1_1 + locSE_1 + locAC_1 == N - F)
s.add(loc0_2 + loc1_2 + locSE_2 + locAC_2 == N - F)
s.add(loc0_3 + loc1_3 + locSE_3 + locAC_3 == N - F)
s.add(loc0_4 + loc1_4 + locSE_4 + locAC_4 == N - F)
s.add(loc0_5 + loc1_5 + locSE_5 + locAC_5 == N - F)
s.add(loc0_6 + loc1_6 + locSE_6 + locAC_6 == N - F)
s.add(loc0_7 + loc1_7 + locSE_7 + locAC_7 == N - F)

#Creating many copies of shared variables

nsnt_0 = Int('nsnt_0')
nsnt_1 = Int('nsnt_1')
nsnt_2 = Int('nsnt_2')
nsnt_3 = Int('nsnt_3')
nsnt_4 = Int('nsnt_4')
nsnt_5 = Int('nsnt_5')
nsnt_6 = Int('nsnt_6')
nsnt_7 = Int('nsnt_7')
s.add(nsnt_0 >= 0)
s.add(nsnt_1 >= 0)
s.add(nsnt_2 >= 0)
s.add(nsnt_3 >= 0)
s.add(nsnt_4 >= 0)
s.add(nsnt_5 >= 0)
s.add(nsnt_6 >= 0)
s.add(nsnt_7 >= 0)


#Ensuring that the alternating indices have the same context

s.add((nsnt_0 >= T + 1 - F ) == (nsnt_1 >= T + 1 - F ))
s.add((nsnt_0 >= N - T - F ) == (nsnt_1 >= N - T - F ))
s.add((nsnt_2 >= T + 1 - F ) == (nsnt_3 >= T + 1 - F ))
s.add((nsnt_2 >= N - T - F ) == (nsnt_3 >= N - T - F ))
s.add((nsnt_4 >= T + 1 - F ) == (nsnt_5 >= T + 1 - F ))
s.add((nsnt_4 >= N - T - F ) == (nsnt_5 >= N - T - F ))
s.add((nsnt_6 >= T + 1 - F ) == (nsnt_7 >= T + 1 - F ))
s.add((nsnt_6 >= N - T - F ) == (nsnt_7 >= N - T - F ))

#Creating many copies of variables for rules

x0_0 = Int('x0_0')
x0_1 = Int('x0_1')
x0_2 = Int('x0_2')
x0_3 = Int('x0_3')
x0_4 = Int('x0_4')
x0_5 = Int('x0_5')
x0_6 = Int('x0_6')
s.add(x0_0 >= 0)
s.add(x0_1 >= 0)
s.add(x0_2 >= 0)
s.add(x0_3 >= 0)
s.add(x0_4 >= 0)
s.add(x0_5 >= 0)
s.add(x0_6 >= 0)

x1_0 = Int('x1_0')
x1_1 = Int('x1_1')
x1_2 = Int('x1_2')
x1_3 = Int('x1_3')
x1_4 = Int('x1_4')
x1_5 = Int('x1_5')
x1_6 = Int('x1_6')
s.add(x1_0 >= 0)
s.add(x1_1 >= 0)
s.add(x1_2 >= 0)
s.add(x1_3 >= 0)
s.add(x1_4 >= 0)
s.add(x1_5 >= 0)
s.add(x1_6 >= 0)

x2_0 = Int('x2_0')
x2_1 = Int('x2_1')
x2_2 = Int('x2_2')
x2_3 = Int('x2_3')
x2_4 = Int('x2_4')
x2_5 = Int('x2_5')
x2_6 = Int('x2_6')
s.add(x2_0 >= 0)
s.add(x2_1 >= 0)
s.add(x2_2 >= 0)
s.add(x2_3 >= 0)
s.add(x2_4 >= 0)
s.add(x2_5 >= 0)
s.add(x2_6 >= 0)

x3_0 = Int('x3_0')
x3_1 = Int('x3_1')
x3_2 = Int('x3_2')
x3_3 = Int('x3_3')
x3_4 = Int('x3_4')
x3_5 = Int('x3_5')
x3_6 = Int('x3_6')
s.add(x3_0 >= 0)
s.add(x3_1 >= 0)
s.add(x3_2 >= 0)
s.add(x3_3 >= 0)
s.add(x3_4 >= 0)
s.add(x3_5 >= 0)
s.add(x3_6 >= 0)

x4_0 = Int('x4_0')
x4_1 = Int('x4_1')
x4_2 = Int('x4_2')
x4_3 = Int('x4_3')
x4_4 = Int('x4_4')
x4_5 = Int('x4_5')
x4_6 = Int('x4_6')
s.add(x4_0 >= 0)
s.add(x4_1 >= 0)
s.add(x4_2 >= 0)
s.add(x4_3 >= 0)
s.add(x4_4 >= 0)
s.add(x4_5 >= 0)
s.add(x4_6 >= 0)

x5_0 = Int('x5_0')
x5_1 = Int('x5_1')
x5_2 = Int('x5_2')
x5_3 = Int('x5_3')
x5_4 = Int('x5_4')
x5_5 = Int('x5_5')
x5_6 = Int('x5_6')
s.add(x5_0 >= 0)
s.add(x5_1 >= 0)
s.add(x5_2 >= 0)
s.add(x5_3 >= 0)
s.add(x5_4 >= 0)
s.add(x5_5 >= 0)
s.add(x5_6 >= 0)

x6_0 = Int('x6_0')
x6_1 = Int('x6_1')
x6_2 = Int('x6_2')
x6_3 = Int('x6_3')
x6_4 = Int('x6_4')
x6_5 = Int('x6_5')
x6_6 = Int('x6_6')
s.add(x6_0 >= 0)
s.add(x6_1 >= 0)
s.add(x6_2 >= 0)
s.add(x6_3 >= 0)
s.add(x6_4 >= 0)
s.add(x6_5 >= 0)
s.add(x6_6 >= 0)

x7_0 = Int('x7_0')
x7_1 = Int('x7_1')
x7_2 = Int('x7_2')
x7_3 = Int('x7_3')
x7_4 = Int('x7_4')
x7_5 = Int('x7_5')
x7_6 = Int('x7_6')
s.add(x7_0 >= 0)
s.add(x7_1 >= 0)
s.add(x7_2 >= 0)
s.add(x7_3 >= 0)
s.add(x7_4 >= 0)
s.add(x7_5 >= 0)
s.add(x7_6 >= 0)


#Ensuring that at most one rule is fired between alternating configurations

s.add(Or((x0_1 == 0), (x0_1 == 1)))
s.add(Or((x1_1 == 0), (x1_1 == 1)))
s.add(Or((x2_1 == 0), (x2_1 == 1)))
s.add(Or((x3_1 == 0), (x3_1 == 1)))
s.add(Or((x4_1 == 0), (x4_1 == 1)))
s.add(Or((x5_1 == 0), (x5_1 == 1)))
s.add(Or((x6_1 == 0), (x6_1 == 1)))
s.add(Or((x7_1 == 0), (x7_1 == 1)))
s.add(x0_1 + x1_1 + x2_1 + x3_1 + x4_1 + x5_1 + x6_1 + x7_1 <= 1)

s.add(Or((x0_3 == 0), (x0_3 == 1)))
s.add(Or((x1_3 == 0), (x1_3 == 1)))
s.add(Or((x2_3 == 0), (x2_3 == 1)))
s.add(Or((x3_3 == 0), (x3_3 == 1)))
s.add(Or((x4_3 == 0), (x4_3 == 1)))
s.add(Or((x5_3 == 0), (x5_3 == 1)))
s.add(Or((x6_3 == 0), (x6_3 == 1)))
s.add(Or((x7_3 == 0), (x7_3 == 1)))
s.add(x0_3 + x1_3 + x2_3 + x3_3 + x4_3 + x5_3 + x6_3 + x7_3 <= 1)

s.add(Or((x0_5 == 0), (x0_5 == 1)))
s.add(Or((x1_5 == 0), (x1_5 == 1)))
s.add(Or((x2_5 == 0), (x2_5 == 1)))
s.add(Or((x3_5 == 0), (x3_5 == 1)))
s.add(Or((x4_5 == 0), (x4_5 == 1)))
s.add(Or((x5_5 == 0), (x5_5 == 1)))
s.add(Or((x6_5 == 0), (x6_5 == 1)))
s.add(Or((x7_5 == 0), (x7_5 == 1)))
s.add(x0_5 + x1_5 + x2_5 + x3_5 + x4_5 + x5_5 + x6_5 + x7_5 <= 1)


###################Step 2####################


#Flow equations for the locations

s.add( - x1_0 - x3_0 - x5_0 + x5_0 ==  loc0_1 - loc0_0)
s.add( - x0_0 - x2_0 ==  loc1_1 - loc1_0)
s.add( + x0_0 + x3_0 - x4_0 - x6_0 + x6_0 ==  locSE_1 - locSE_0)
s.add( + x1_0 + x2_0 + x4_0 - x7_0 + x7_0 ==  locAC_1 - locAC_0)
s.add( - x1_1 - x3_1 - x5_1 + x5_1 ==  loc0_2 - loc0_1)
s.add( - x0_1 - x2_1 ==  loc1_2 - loc1_1)
s.add( + x0_1 + x3_1 - x4_1 - x6_1 + x6_1 ==  locSE_2 - locSE_1)
s.add( + x1_1 + x2_1 + x4_1 - x7_1 + x7_1 ==  locAC_2 - locAC_1)
s.add( - x1_2 - x3_2 - x5_2 + x5_2 ==  loc0_3 - loc0_2)
s.add( - x0_2 - x2_2 ==  loc1_3 - loc1_2)
s.add( + x0_2 + x3_2 - x4_2 - x6_2 + x6_2 ==  locSE_3 - locSE_2)
s.add( + x1_2 + x2_2 + x4_2 - x7_2 + x7_2 ==  locAC_3 - locAC_2)
s.add( - x1_3 - x3_3 - x5_3 + x5_3 ==  loc0_4 - loc0_3)
s.add( - x0_3 - x2_3 ==  loc1_4 - loc1_3)
s.add( + x0_3 + x3_3 - x4_3 - x6_3 + x6_3 ==  locSE_4 - locSE_3)
s.add( + x1_3 + x2_3 + x4_3 - x7_3 + x7_3 ==  locAC_4 - locAC_3)
s.add( - x1_4 - x3_4 - x5_4 + x5_4 ==  loc0_5 - loc0_4)
s.add( - x0_4 - x2_4 ==  loc1_5 - loc1_4)
s.add( + x0_4 + x3_4 - x4_4 - x6_4 + x6_4 ==  locSE_5 - locSE_4)
s.add( + x1_4 + x2_4 + x4_4 - x7_4 + x7_4 ==  locAC_5 - locAC_4)
s.add( - x1_5 - x3_5 - x5_5 + x5_5 ==  loc0_6 - loc0_5)
s.add( - x0_5 - x2_5 ==  loc1_6 - loc1_5)
s.add( + x0_5 + x3_5 - x4_5 - x6_5 + x6_5 ==  locSE_6 - locSE_5)
s.add( + x1_5 + x2_5 + x4_5 - x7_5 + x7_5 ==  locAC_6 - locAC_5)
s.add( - x1_6 - x3_6 - x5_6 + x5_6 ==  loc0_7 - loc0_6)
s.add( - x0_6 - x2_6 ==  loc1_7 - loc1_6)
s.add( + x0_6 + x3_6 - x4_6 - x6_6 + x6_6 ==  locSE_7 - locSE_6)
s.add( + x1_6 + x2_6 + x4_6 - x7_6 + x7_6 ==  locAC_7 - locAC_6)

##################Step 3########################


#Flow equations for the shared variables

s.add(0 + x0_0 * 1 + x1_0 * 1 + x2_0 * 1 + x3_0 * 1 == nsnt_1 - nsnt_0)
s.add(0 + x0_1 * 1 + x1_1 * 1 + x2_1 * 1 + x3_1 * 1 == nsnt_2 - nsnt_1)
s.add(0 + x0_2 * 1 + x1_2 * 1 + x2_2 * 1 + x3_2 * 1 == nsnt_3 - nsnt_2)
s.add(0 + x0_3 * 1 + x1_3 * 1 + x2_3 * 1 + x3_3 * 1 == nsnt_4 - nsnt_3)
s.add(0 + x0_4 * 1 + x1_4 * 1 + x2_4 * 1 + x3_4 * 1 == nsnt_5 - nsnt_4)
s.add(0 + x0_5 * 1 + x1_5 * 1 + x2_5 * 1 + x3_5 * 1 == nsnt_6 - nsnt_5)
s.add(0 + x0_6 * 1 + x1_6 * 1 + x2_6 * 1 + x3_6 * 1 == nsnt_7 - nsnt_6)

####################Step 4########################


#Rule is fired implies rule is enabled

s.add(Implies( (x0_0 > 0), ((True) ) ))
s.add(Implies( (x0_1 > 0), ((True) ) ))
s.add(Implies( (x0_2 > 0), ((True) ) ))
s.add(Implies( (x0_3 > 0), ((True) ) ))
s.add(Implies( (x0_4 > 0), ((True) ) ))
s.add(Implies( (x0_5 > 0), ((True) ) ))
s.add(Implies( (x0_6 > 0), ((True) ) ))
s.add(Implies( (x1_0 > 0), ((nsnt_0 >= N - T - F) ) ))
s.add(Implies( (x1_1 > 0), ((nsnt_1 >= N - T - F) ) ))
s.add(Implies( (x1_2 > 0), ((nsnt_2 >= N - T - F) ) ))
s.add(Implies( (x1_3 > 0), ((nsnt_3 >= N - T - F) ) ))
s.add(Implies( (x1_4 > 0), ((nsnt_4 >= N - T - F) ) ))
s.add(Implies( (x1_5 > 0), ((nsnt_5 >= N - T - F) ) ))
s.add(Implies( (x1_6 > 0), ((nsnt_6 >= N - T - F) ) ))
s.add(Implies( (x2_0 > 0), ((nsnt_0 >= N - T - F) ) ))
s.add(Implies( (x2_1 > 0), ((nsnt_1 >= N - T - F) ) ))
s.add(Implies( (x2_2 > 0), ((nsnt_2 >= N - T - F) ) ))
s.add(Implies( (x2_3 > 0), ((nsnt_3 >= N - T - F) ) ))
s.add(Implies( (x2_4 > 0), ((nsnt_4 >= N - T - F) ) ))
s.add(Implies( (x2_5 > 0), ((nsnt_5 >= N - T - F) ) ))
s.add(Implies( (x2_6 > 0), ((nsnt_6 >= N - T - F) ) ))
s.add(Implies( (x3_0 > 0), ((nsnt_0 >= T + 1 - F) ) ))
s.add(Implies( (x3_1 > 0), ((nsnt_1 >= T + 1 - F) ) ))
s.add(Implies( (x3_2 > 0), ((nsnt_2 >= T + 1 - F) ) ))
s.add(Implies( (x3_3 > 0), ((nsnt_3 >= T + 1 - F) ) ))
s.add(Implies( (x3_4 > 0), ((nsnt_4 >= T + 1 - F) ) ))
s.add(Implies( (x3_5 > 0), ((nsnt_5 >= T + 1 - F) ) ))
s.add(Implies( (x3_6 > 0), ((nsnt_6 >= T + 1 - F) ) ))
s.add(Implies( (x4_0 > 0), ((nsnt_0 >= N - T - F) ) ))
s.add(Implies( (x4_1 > 0), ((nsnt_1 >= N - T - F) ) ))
s.add(Implies( (x4_2 > 0), ((nsnt_2 >= N - T - F) ) ))
s.add(Implies( (x4_3 > 0), ((nsnt_3 >= N - T - F) ) ))
s.add(Implies( (x4_4 > 0), ((nsnt_4 >= N - T - F) ) ))
s.add(Implies( (x4_5 > 0), ((nsnt_5 >= N - T - F) ) ))
s.add(Implies( (x4_6 > 0), ((nsnt_6 >= N - T - F) ) ))
s.add(Implies( (x5_0 > 0), ((True) ) ))
s.add(Implies( (x5_1 > 0), ((True) ) ))
s.add(Implies( (x5_2 > 0), ((True) ) ))
s.add(Implies( (x5_3 > 0), ((True) ) ))
s.add(Implies( (x5_4 > 0), ((True) ) ))
s.add(Implies( (x5_5 > 0), ((True) ) ))
s.add(Implies( (x5_6 > 0), ((True) ) ))
s.add(Implies( (x6_0 > 0), ((True) ) ))
s.add(Implies( (x6_1 > 0), ((True) ) ))
s.add(Implies( (x6_2 > 0), ((True) ) ))
s.add(Implies( (x6_3 > 0), ((True) ) ))
s.add(Implies( (x6_4 > 0), ((True) ) ))
s.add(Implies( (x6_5 > 0), ((True) ) ))
s.add(Implies( (x6_6 > 0), ((True) ) ))
s.add(Implies( (x7_0 > 0), ((True) ) ))
s.add(Implies( (x7_1 > 0), ((True) ) ))
s.add(Implies( (x7_2 > 0), ((True) ) ))
s.add(Implies( (x7_3 > 0), ((True) ) ))
s.add(Implies( (x7_4 > 0), ((True) ) ))
s.add(Implies( (x7_5 > 0), ((True) ) ))
s.add(Implies( (x7_6 > 0), ((True) ) ))

######################Step 5#####################


#Constraints that the 0th configuration has to satisfy

s.add(loc1_0 == 0 )

#######################Step 5 1/2################


#Ensure that the constraints on the initial configuration are satisfied

s.add((loc0_0 + loc1_0) == N - F)
s.add(locSE_0 == 0)
s.add(locAC_0 == 0)
s.add(nsnt_0 == 0)

#####################Step 6########################


#Constraints that the path between the 0th and 1th configuration has to satisfy

s.add(True )
s.add(True )
s.add(True )
s.add(True )
s.add(True )
s.add(True )
s.add(True )
s.add(True )

#####################Step 7#########################


#In the inital part, we do not allow all the edges in a cycle to be fired as this is clearly wasteful, assuming the automaton is canonical


#Further, if an edge is a self-loop, we do not fire that as well

s.add(x5_0 == 0)
s.add(x5_1 == 0)
s.add(x5_2 == 0)
s.add(x5_3 == 0)
s.add(x5_4 == 0)
s.add(x5_5 == 0)
s.add(x5_6 == 0)
s.add(x6_0 == 0)
s.add(x6_1 == 0)
s.add(x6_2 == 0)
s.add(x6_3 == 0)
s.add(x6_4 == 0)
s.add(x6_5 == 0)
s.add(x6_6 == 0)
s.add(x7_0 == 0)
s.add(x7_1 == 0)
s.add(x7_2 == 0)
s.add(x7_3 == 0)
s.add(x7_4 == 0)
s.add(x7_5 == 0)
s.add(x7_6 == 0)

##########Closing path###########

s.add(locAC_7 != 0 )

if s.check() == sat:

	print("Specification not satisfied")

	raise StopIteration("stop here")

s.reset()

#Declaring parameter variables

N = Int('N')
T = Int('T')
F = Int('F')
s.add(N >= 0)
s.add(T >= 0)
s.add(F >= 0)

#Adding the resilience condition

s.add(N > 3 * T)
s.add(T >= F)
s.add(T >= 1)

print("Specification satisfied")