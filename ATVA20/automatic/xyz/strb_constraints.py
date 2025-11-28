from z3 import *
s = Solver()

################Step 1#################


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

#Creating many copies of location variables

loc00 = Int('loc00')
loc01 = Int('loc01')
loc02 = Int('loc02')
loc03 = Int('loc03')
loc04 = Int('loc04')
loc05 = Int('loc05')
loc06 = Int('loc06')
loc07 = Int('loc07')
s.add(loc00 >= 0)
s.add(loc01 >= 0)
s.add(loc02 >= 0)
s.add(loc03 >= 0)
s.add(loc04 >= 0)
s.add(loc05 >= 0)
s.add(loc06 >= 0)
s.add(loc07 >= 0)

loc10 = Int('loc10')
loc11 = Int('loc11')
loc12 = Int('loc12')
loc13 = Int('loc13')
loc14 = Int('loc14')
loc15 = Int('loc15')
loc16 = Int('loc16')
loc17 = Int('loc17')
s.add(loc10 >= 0)
s.add(loc11 >= 0)
s.add(loc12 >= 0)
s.add(loc13 >= 0)
s.add(loc14 >= 0)
s.add(loc15 >= 0)
s.add(loc16 >= 0)
s.add(loc17 >= 0)

locSE0 = Int('locSE0')
locSE1 = Int('locSE1')
locSE2 = Int('locSE2')
locSE3 = Int('locSE3')
locSE4 = Int('locSE4')
locSE5 = Int('locSE5')
locSE6 = Int('locSE6')
locSE7 = Int('locSE7')
s.add(locSE0 >= 0)
s.add(locSE1 >= 0)
s.add(locSE2 >= 0)
s.add(locSE3 >= 0)
s.add(locSE4 >= 0)
s.add(locSE5 >= 0)
s.add(locSE6 >= 0)
s.add(locSE7 >= 0)

locAC0 = Int('locAC0')
locAC1 = Int('locAC1')
locAC2 = Int('locAC2')
locAC3 = Int('locAC3')
locAC4 = Int('locAC4')
locAC5 = Int('locAC5')
locAC6 = Int('locAC6')
locAC7 = Int('locAC7')
s.add(locAC0 >= 0)
s.add(locAC1 >= 0)
s.add(locAC2 >= 0)
s.add(locAC3 >= 0)
s.add(locAC4 >= 0)
s.add(locAC5 >= 0)
s.add(locAC6 >= 0)
s.add(locAC7 >= 0)


#Adding the constraint for the number of processes

s.add(loc00 + loc10 + locSE0 + locAC0 == N - F)
s.add(loc01 + loc11 + locSE1 + locAC1 == N - F)
s.add(loc02 + loc12 + locSE2 + locAC2 == N - F)
s.add(loc03 + loc13 + locSE3 + locAC3 == N - F)
s.add(loc04 + loc14 + locSE4 + locAC4 == N - F)
s.add(loc05 + loc15 + locSE5 + locAC5 == N - F)
s.add(loc06 + loc16 + locSE6 + locAC6 == N - F)
s.add(loc07 + loc17 + locSE7 + locAC7 == N - F)

#Creating many copies of shared variables

nsnt0 = Int('nsnt0')
nsnt1 = Int('nsnt1')
nsnt2 = Int('nsnt2')
nsnt3 = Int('nsnt3')
nsnt4 = Int('nsnt4')
nsnt5 = Int('nsnt5')
nsnt6 = Int('nsnt6')
nsnt7 = Int('nsnt7')
s.add(nsnt0 >= 0)
s.add(nsnt1 >= 0)
s.add(nsnt2 >= 0)
s.add(nsnt3 >= 0)
s.add(nsnt4 >= 0)
s.add(nsnt5 >= 0)
s.add(nsnt6 >= 0)
s.add(nsnt7 >= 0)


#Ensuring that the odd to even indices have the same context

s.add((nsnt0 >= T + 1 - F ) == (nsnt1 >= T + 1 - F ))
s.add((nsnt0 >= N - T - F ) == (nsnt1 >= N - T - F ))
s.add((nsnt2 >= T + 1 - F ) == (nsnt3 >= T + 1 - F ))
s.add((nsnt2 >= N - T - F ) == (nsnt3 >= N - T - F ))
s.add((nsnt4 >= T + 1 - F ) == (nsnt5 >= T + 1 - F ))
s.add((nsnt4 >= N - T - F ) == (nsnt5 >= N - T - F ))
s.add((nsnt6 >= T + 1 - F ) == (nsnt7 >= T + 1 - F ))
s.add((nsnt6 >= N - T - F ) == (nsnt7 >= N - T - F ))

###################Step 1 1/2###################


#Creating many copies of variables for rules

x00 = Int('x00')
x01 = Int('x01')
x02 = Int('x02')
x03 = Int('x03')
x04 = Int('x04')
x05 = Int('x05')
x06 = Int('x06')
s.add(x00 >= 0)
s.add(x01 >= 0)
s.add(x02 >= 0)
s.add(x03 >= 0)
s.add(x04 >= 0)
s.add(x05 >= 0)
s.add(x06 >= 0)

x10 = Int('x10')
x11 = Int('x11')
x12 = Int('x12')
x13 = Int('x13')
x14 = Int('x14')
x15 = Int('x15')
x16 = Int('x16')
s.add(x10 >= 0)
s.add(x11 >= 0)
s.add(x12 >= 0)
s.add(x13 >= 0)
s.add(x14 >= 0)
s.add(x15 >= 0)
s.add(x16 >= 0)

x20 = Int('x20')
x21 = Int('x21')
x22 = Int('x22')
x23 = Int('x23')
x24 = Int('x24')
x25 = Int('x25')
x26 = Int('x26')
s.add(x20 >= 0)
s.add(x21 >= 0)
s.add(x22 >= 0)
s.add(x23 >= 0)
s.add(x24 >= 0)
s.add(x25 >= 0)
s.add(x26 >= 0)

x30 = Int('x30')
x31 = Int('x31')
x32 = Int('x32')
x33 = Int('x33')
x34 = Int('x34')
x35 = Int('x35')
x36 = Int('x36')
s.add(x30 >= 0)
s.add(x31 >= 0)
s.add(x32 >= 0)
s.add(x33 >= 0)
s.add(x34 >= 0)
s.add(x35 >= 0)
s.add(x36 >= 0)

x40 = Int('x40')
x41 = Int('x41')
x42 = Int('x42')
x43 = Int('x43')
x44 = Int('x44')
x45 = Int('x45')
x46 = Int('x46')
s.add(x40 >= 0)
s.add(x41 >= 0)
s.add(x42 >= 0)
s.add(x43 >= 0)
s.add(x44 >= 0)
s.add(x45 >= 0)
s.add(x46 >= 0)


#Ensuring that at most one rule is fired from an odd to an even configuration

s.add(Or((x11 == 0), (x11 == 1)))
s.add(Or((x21 == 0), (x21 == 1)))
s.add(Or((x31 == 0), (x31 == 1)))
s.add(Or((x41 == 0), (x41 == 1)))
s.add(x01 + x11 + x21 + x31 + x41 <= 1)

s.add(Or((x13 == 0), (x13 == 1)))
s.add(Or((x23 == 0), (x23 == 1)))
s.add(Or((x33 == 0), (x33 == 1)))
s.add(Or((x43 == 0), (x43 == 1)))
s.add(x03 + x13 + x23 + x33 + x43 <= 1)

s.add(Or((x15 == 0), (x15 == 1)))
s.add(Or((x25 == 0), (x25 == 1)))
s.add(Or((x35 == 0), (x35 == 1)))
s.add(Or((x45 == 0), (x45 == 1)))
s.add(x05 + x15 + x25 + x35 + x45 <= 1)


###################Step 2####################


#Flow equations for the locations

s.add( - x10 - x30 ==  loc01 - loc00)
s.add( - x00 - x20 ==  loc11 - loc10)
s.add( + x00 + x30 - x40 ==  locSE1 - locSE0)
s.add( + x10 + x20 + x40 ==  locAC1 - locAC0)
s.add( - x11 - x31 ==  loc02 - loc01)
s.add( - x01 - x21 ==  loc12 - loc11)
s.add( + x01 + x31 - x41 ==  locSE2 - locSE1)
s.add( + x11 + x21 + x41 ==  locAC2 - locAC1)
s.add( - x12 - x32 ==  loc03 - loc02)
s.add( - x02 - x22 ==  loc13 - loc12)
s.add( + x02 + x32 - x42 ==  locSE3 - locSE2)
s.add( + x12 + x22 + x42 ==  locAC3 - locAC2)
s.add( - x13 - x33 ==  loc04 - loc03)
s.add( - x03 - x23 ==  loc14 - loc13)
s.add( + x03 + x33 - x43 ==  locSE4 - locSE3)
s.add( + x13 + x23 + x43 ==  locAC4 - locAC3)
s.add( - x14 - x34 ==  loc05 - loc04)
s.add( - x04 - x24 ==  loc15 - loc14)
s.add( + x04 + x34 - x44 ==  locSE5 - locSE4)
s.add( + x14 + x24 + x44 ==  locAC5 - locAC4)
s.add( - x15 - x35 ==  loc06 - loc05)
s.add( - x05 - x25 ==  loc16 - loc15)
s.add( + x05 + x35 - x45 ==  locSE6 - locSE5)
s.add( + x15 + x25 + x45 ==  locAC6 - locAC5)
s.add( - x16 - x36 ==  loc07 - loc06)
s.add( - x06 - x26 ==  loc17 - loc16)
s.add( + x06 + x36 - x46 ==  locSE7 - locSE6)
s.add( + x16 + x26 + x46 ==  locAC7 - locAC6)

##################Step 3########################


#Flow equations for the shared variables

s.add(0 + x00 * 1 + x10 * 1 + x20 * 1 + x30 * 1 == nsnt1 - nsnt0)
s.add(0 + x01 * 1 + x11 * 1 + x21 * 1 + x31 * 1 == nsnt2 - nsnt1)
s.add(0 + x02 * 1 + x12 * 1 + x22 * 1 + x32 * 1 == nsnt3 - nsnt2)
s.add(0 + x03 * 1 + x13 * 1 + x23 * 1 + x33 * 1 == nsnt4 - nsnt3)
s.add(0 + x04 * 1 + x14 * 1 + x24 * 1 + x34 * 1 == nsnt5 - nsnt4)
s.add(0 + x05 * 1 + x15 * 1 + x25 * 1 + x35 * 1 == nsnt6 - nsnt5)
s.add(0 + x06 * 1 + x16 * 1 + x26 * 1 + x36 * 1 == nsnt7 - nsnt6)

####################Step 4########################


#Rule is fired implies rule is enabled

s.add(Implies( (x10 > 0), (nsnt0 >= N - T - F ) ))
s.add(Implies( (x11 > 0), (nsnt1 >= N - T - F ) ))
s.add(Implies( (x12 > 0), (nsnt2 >= N - T - F ) ))
s.add(Implies( (x13 > 0), (nsnt3 >= N - T - F ) ))
s.add(Implies( (x14 > 0), (nsnt4 >= N - T - F ) ))
s.add(Implies( (x15 > 0), (nsnt5 >= N - T - F ) ))
s.add(Implies( (x16 > 0), (nsnt6 >= N - T - F ) ))
s.add(Implies( (x20 > 0), (nsnt0 >= N - T - F ) ))
s.add(Implies( (x21 > 0), (nsnt1 >= N - T - F ) ))
s.add(Implies( (x22 > 0), (nsnt2 >= N - T - F ) ))
s.add(Implies( (x23 > 0), (nsnt3 >= N - T - F ) ))
s.add(Implies( (x24 > 0), (nsnt4 >= N - T - F ) ))
s.add(Implies( (x25 > 0), (nsnt5 >= N - T - F ) ))
s.add(Implies( (x26 > 0), (nsnt6 >= N - T - F ) ))
s.add(Implies( (x30 > 0), (nsnt0 >= T + 1 - F ) ))
s.add(Implies( (x31 > 0), (nsnt1 >= T + 1 - F ) ))
s.add(Implies( (x32 > 0), (nsnt2 >= T + 1 - F ) ))
s.add(Implies( (x33 > 0), (nsnt3 >= T + 1 - F ) ))
s.add(Implies( (x34 > 0), (nsnt4 >= T + 1 - F ) ))
s.add(Implies( (x35 > 0), (nsnt5 >= T + 1 - F ) ))
s.add(Implies( (x36 > 0), (nsnt6 >= T + 1 - F ) ))
s.add(Implies( (x40 > 0), (nsnt0 >= N - T - F ) ))
s.add(Implies( (x41 > 0), (nsnt1 >= N - T - F ) ))
s.add(Implies( (x42 > 0), (nsnt2 >= N - T - F ) ))
s.add(Implies( (x43 > 0), (nsnt3 >= N - T - F ) ))
s.add(Implies( (x44 > 0), (nsnt4 >= N - T - F ) ))
s.add(Implies( (x45 > 0), (nsnt5 >= N - T - F ) ))
s.add(Implies( (x46 > 0), (nsnt6 >= N - T - F ) ))

####################Step 5#################


#Constraints for initial configuration

s.add(loc00 >= 0 )
s.add(loc10 >= 0 )
s.add(locSE0 == 0 )
s.add(locAC0 == 0 )
s.add(nsnt0 == 0 )

#################Step 6####################


#Specification, as of now hand written

s.add(loc10 == 0)
s.add(Or(locAC0 > 0, locAC0 > 0, locAC1 > 0, locAC2 > 0, locAC3 > 0, locAC4 > 0, locAC5 > 0, locAC6 > 0, locAC7 > 0))

print(s.check())
