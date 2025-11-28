from z3 import *
s = Solver()

#Declaring parameter variables

N = Real('N')
s.add(N >= 0)
T = Real('T')
s.add(T >= 0)
F = Real('F')
s.add(F >= 0)

#Adding the resilience condition

s.add(N > 2 * T)
s.add(T >= F)
s.add(T >= 0)
s.add(F >= 0)

####################################################################################

#Creating constraints for a run between the x0th and y0th configurations

################Step 1#################


#Creating many copies of location variables

loc0_x0 = Real('loc0_x0')
loc0_y0 = Real('loc0_y0')
s.add(loc0_x0 >= 0)
s.add(loc0_y0 >= 0)
loc1_x0 = Real('loc1_x0')
loc1_y0 = Real('loc1_y0')
s.add(loc1_x0 >= 0)
s.add(loc1_y0 >= 0)
locP0_x0 = Real('locP0_x0')
locP0_y0 = Real('locP0_y0')
s.add(locP0_x0 >= 0)
s.add(locP0_y0 >= 0)
locP1_x0 = Real('locP1_x0')
locP1_y0 = Real('locP1_y0')
s.add(locP1_x0 >= 0)
s.add(locP1_y0 >= 0)
locAC0_x0 = Real('locAC0_x0')
locAC0_y0 = Real('locAC0_y0')
s.add(locAC0_x0 >= 0)
s.add(locAC0_y0 >= 0)
locAC1_x0 = Real('locAC1_x0')
locAC1_y0 = Real('locAC1_y0')
s.add(locAC1_x0 >= 0)
s.add(locAC1_y0 >= 0)
locCR_x0 = Real('locCR_x0')
locCR_y0 = Real('locCR_y0')
s.add(locCR_x0 >= 0)
s.add(locCR_y0 >= 0)






#Creating many copies of shared variables

nsnt00_x0 = Real('nsnt00_x0')
nsnt00_y0 = Real('nsnt00_y0')
s.add(nsnt00_x0 >= 0)
s.add(nsnt00_y0 >= 0)
nsnt01_x0 = Real('nsnt01_x0')
nsnt01_y0 = Real('nsnt01_y0')
s.add(nsnt01_x0 >= 0)
s.add(nsnt01_y0 >= 0)
nsnt10_x0 = Real('nsnt10_x0')
nsnt10_y0 = Real('nsnt10_y0')
s.add(nsnt10_x0 >= 0)
s.add(nsnt10_y0 >= 0)
nsnt11_x0 = Real('nsnt11_x0')
nsnt11_y0 = Real('nsnt11_y0')
s.add(nsnt11_x0 >= 0)
s.add(nsnt11_y0 >= 0)
nsnt00plus01_x0 = Real('nsnt00plus01_x0')
nsnt00plus01_y0 = Real('nsnt00plus01_y0')
s.add(nsnt00plus01_x0 >= 0)
s.add(nsnt00plus01_y0 >= 0)
nfaulty_x0 = Real('nfaulty_x0')
nfaulty_y0 = Real('nfaulty_y0')
s.add(nfaulty_x0 >= 0)
s.add(nfaulty_y0 >= 0)






#Creating many copies of variables for rules

rule0_x0 = Real('rule0_x0')
s.add(rule0_x0 >= 0)
rule1_x0 = Real('rule1_x0')
s.add(rule1_x0 >= 0)
rule2_x0 = Real('rule2_x0')
s.add(rule2_x0 >= 0)
rule3_x0 = Real('rule3_x0')
s.add(rule3_x0 >= 0)
rule4_x0 = Real('rule4_x0')
s.add(rule4_x0 >= 0)
rule5_x0 = Real('rule5_x0')
s.add(rule5_x0 >= 0)
rule6_x0 = Real('rule6_x0')
s.add(rule6_x0 >= 0)
rule7_x0 = Real('rule7_x0')
s.add(rule7_x0 >= 0)
rule8_x0 = Real('rule8_x0')
s.add(rule8_x0 >= 0)
rule9_x0 = Real('rule9_x0')
s.add(rule9_x0 >= 0)
rule10_x0 = Real('rule10_x0')
s.add(rule10_x0 >= 0)
rule11_x0 = Real('rule11_x0')
s.add(rule11_x0 >= 0)
rule12_x0 = Real('rule12_x0')
s.add(rule12_x0 >= 0)
rule13_x0 = Real('rule13_x0')
s.add(rule13_x0 >= 0)






###################Step 2####################


#Flow equations for the locations

s.add(0 - rule0_x0 ==  loc0_y0 - loc0_x0)
s.add(0 - rule1_x0 ==  loc1_y0 - loc1_x0)
s.add(0 + rule0_x0 + rule1_x0 - rule2_x0 - rule3_x0 - rule6_x0 - rule10_x0 + rule10_x0 ==  locP0_y0 - locP0_x0)
s.add(0 + rule2_x0 + rule3_x0 - rule4_x0 - rule5_x0 - rule7_x0 - rule11_x0 + rule11_x0 ==  locP1_y0 - locP1_x0)
s.add(0 + rule4_x0 - rule8_x0 - rule12_x0 + rule12_x0 ==  locAC0_y0 - locAC0_x0)
s.add(0 + rule5_x0 - rule9_x0 - rule13_x0 + rule13_x0 ==  locAC1_y0 - locAC1_x0)
s.add(0 + rule6_x0 + rule7_x0 + rule8_x0 + rule9_x0 ==  locCR_y0 - locCR_x0)






##################Step 3########################


#Flow equations for the shared variables

s.add(0 + rule0_x0 == nsnt00_y0 - nsnt00_x0)
s.add(0 + rule1_x0 == nsnt01_y0 - nsnt01_x0)
s.add(0 + rule2_x0 == nsnt10_y0 - nsnt10_x0)
s.add(0 + rule3_x0 == nsnt11_y0 - nsnt11_x0)
s.add(0 + rule0_x0 + rule1_x0 == nsnt00plus01_y0 - nsnt00plus01_x0)
s.add(0 + rule6_x0 + rule7_x0 + rule8_x0 + rule9_x0 == nfaulty_y0 - nfaulty_x0)






####################Step 4########################


#Rule is fired implies rule is enabled

s.add(Implies( (rule0_x0 > 0), And(True, ) ))
s.add(Implies( (rule1_x0 > 0), And(True, ) ))
s.add(Implies( (rule2_x0 > 0), And(nsnt00plus01_x0>=N-T, 2*nsnt00_x0>=N-T+1, ) ))
s.add(Implies( (rule3_x0 > 0), And(nsnt00plus01_x0>=N-T, 2*nsnt01_x0>=N-T+1, ) ))
s.add(Implies( (rule4_x0 > 0), And(2*nsnt10_x0>=N+1, ) ))
s.add(Implies( (rule5_x0 > 0), And(2*nsnt11_x0>=N+1, ) ))
s.add(Implies( (rule6_x0 > 0), And(nfaulty_x0<F, ) ))
s.add(Implies( (rule7_x0 > 0), And(nfaulty_x0<F, ) ))
s.add(Implies( (rule8_x0 > 0), And(nfaulty_x0<F, ) ))
s.add(Implies( (rule9_x0 > 0), And(nfaulty_x0<F, ) ))
s.add(Implies( (rule10_x0 > 0), And(True, ) ))
s.add(Implies( (rule11_x0 > 0), And(True, ) ))
s.add(Implies( (rule12_x0 > 0), And(True, ) ))
s.add(Implies( (rule13_x0 > 0), And(True, ) ))

##################Step 5#########################


#Ensuring that configurations x0 and y0 have the same context

s.add((2*nsnt11_x0>=N+1) == (2*nsnt11_y0>=N+1))
s.add((2*nsnt01_x0>=N-T+1) == (2*nsnt01_y0>=N-T+1))
s.add((2*nsnt10_x0>=N+1) == (2*nsnt10_y0>=N+1))
s.add((True) == (True))
s.add((nsnt00plus01_x0>=N-T) == (nsnt00plus01_y0>=N-T))
s.add((nfaulty_x0<F) == (nfaulty_y0<F))
s.add((2*nsnt00_x0>=N-T+1) == (2*nsnt00_y0>=N-T+1))

#############Additional step for the initial configuration#####################


#############Ensure that the first configuration only contains initial locations###########

s.add((loc0_x0 + loc1_x0) == N)
s.add(locP0_x0 == 0)
s.add(locP1_x0 == 0)
s.add(locAC0_x0 == 0)
s.add(locAC1_x0 == 0)
s.add(locCR_x0 == 0)
s.add(nsnt00_x0 == 0)
s.add(nsnt01_x0 == 0)
s.add(nsnt10_x0 == 0)
s.add(nsnt11_x0 == 0)
s.add(nsnt00plus01_x0 == 0)
s.add(nfaulty_x0 == 0)






###########Ensure that the first configuration satisfies the initial condition#############

s.add(And(loc0_x0 == 0, loc0_x0 == 0))






####################################################################################

#Creating constraints for a run between the x1th and y1th configurations

################Step 1#################


#Creating many copies of location variables

loc0_x1 = Real('loc0_x1')
loc0_y1 = Real('loc0_y1')
s.add(loc0_x1 >= 0)
s.add(loc0_y1 >= 0)
loc1_x1 = Real('loc1_x1')
loc1_y1 = Real('loc1_y1')
s.add(loc1_x1 >= 0)
s.add(loc1_y1 >= 0)
locP0_x1 = Real('locP0_x1')
locP0_y1 = Real('locP0_y1')
s.add(locP0_x1 >= 0)
s.add(locP0_y1 >= 0)
locP1_x1 = Real('locP1_x1')
locP1_y1 = Real('locP1_y1')
s.add(locP1_x1 >= 0)
s.add(locP1_y1 >= 0)
locAC0_x1 = Real('locAC0_x1')
locAC0_y1 = Real('locAC0_y1')
s.add(locAC0_x1 >= 0)
s.add(locAC0_y1 >= 0)
locAC1_x1 = Real('locAC1_x1')
locAC1_y1 = Real('locAC1_y1')
s.add(locAC1_x1 >= 0)
s.add(locAC1_y1 >= 0)
locCR_x1 = Real('locCR_x1')
locCR_y1 = Real('locCR_y1')
s.add(locCR_x1 >= 0)
s.add(locCR_y1 >= 0)






#Creating many copies of shared variables

nsnt00_x1 = Real('nsnt00_x1')
nsnt00_y1 = Real('nsnt00_y1')
s.add(nsnt00_x1 >= 0)
s.add(nsnt00_y1 >= 0)
nsnt01_x1 = Real('nsnt01_x1')
nsnt01_y1 = Real('nsnt01_y1')
s.add(nsnt01_x1 >= 0)
s.add(nsnt01_y1 >= 0)
nsnt10_x1 = Real('nsnt10_x1')
nsnt10_y1 = Real('nsnt10_y1')
s.add(nsnt10_x1 >= 0)
s.add(nsnt10_y1 >= 0)
nsnt11_x1 = Real('nsnt11_x1')
nsnt11_y1 = Real('nsnt11_y1')
s.add(nsnt11_x1 >= 0)
s.add(nsnt11_y1 >= 0)
nsnt00plus01_x1 = Real('nsnt00plus01_x1')
nsnt00plus01_y1 = Real('nsnt00plus01_y1')
s.add(nsnt00plus01_x1 >= 0)
s.add(nsnt00plus01_y1 >= 0)
nfaulty_x1 = Real('nfaulty_x1')
nfaulty_y1 = Real('nfaulty_y1')
s.add(nfaulty_x1 >= 0)
s.add(nfaulty_y1 >= 0)






#Creating many copies of variables for rules

rule0_x1 = Real('rule0_x1')
s.add(rule0_x1 >= 0)
rule1_x1 = Real('rule1_x1')
s.add(rule1_x1 >= 0)
rule2_x1 = Real('rule2_x1')
s.add(rule2_x1 >= 0)
rule3_x1 = Real('rule3_x1')
s.add(rule3_x1 >= 0)
rule4_x1 = Real('rule4_x1')
s.add(rule4_x1 >= 0)
rule5_x1 = Real('rule5_x1')
s.add(rule5_x1 >= 0)
rule6_x1 = Real('rule6_x1')
s.add(rule6_x1 >= 0)
rule7_x1 = Real('rule7_x1')
s.add(rule7_x1 >= 0)
rule8_x1 = Real('rule8_x1')
s.add(rule8_x1 >= 0)
rule9_x1 = Real('rule9_x1')
s.add(rule9_x1 >= 0)
rule10_x1 = Real('rule10_x1')
s.add(rule10_x1 >= 0)
rule11_x1 = Real('rule11_x1')
s.add(rule11_x1 >= 0)
rule12_x1 = Real('rule12_x1')
s.add(rule12_x1 >= 0)
rule13_x1 = Real('rule13_x1')
s.add(rule13_x1 >= 0)






###################Step 2####################


#Flow equations for the locations

s.add(0 - rule0_x1 ==  loc0_y1 - loc0_x1)
s.add(0 - rule1_x1 ==  loc1_y1 - loc1_x1)
s.add(0 + rule0_x1 + rule1_x1 - rule2_x1 - rule3_x1 - rule6_x1 - rule10_x1 + rule10_x1 ==  locP0_y1 - locP0_x1)
s.add(0 + rule2_x1 + rule3_x1 - rule4_x1 - rule5_x1 - rule7_x1 - rule11_x1 + rule11_x1 ==  locP1_y1 - locP1_x1)
s.add(0 + rule4_x1 - rule8_x1 - rule12_x1 + rule12_x1 ==  locAC0_y1 - locAC0_x1)
s.add(0 + rule5_x1 - rule9_x1 - rule13_x1 + rule13_x1 ==  locAC1_y1 - locAC1_x1)
s.add(0 + rule6_x1 + rule7_x1 + rule8_x1 + rule9_x1 ==  locCR_y1 - locCR_x1)






##################Step 3########################


#Flow equations for the shared variables

s.add(0 + rule0_x1 == nsnt00_y1 - nsnt00_x1)
s.add(0 + rule1_x1 == nsnt01_y1 - nsnt01_x1)
s.add(0 + rule2_x1 == nsnt10_y1 - nsnt10_x1)
s.add(0 + rule3_x1 == nsnt11_y1 - nsnt11_x1)
s.add(0 + rule0_x1 + rule1_x1 == nsnt00plus01_y1 - nsnt00plus01_x1)
s.add(0 + rule6_x1 + rule7_x1 + rule8_x1 + rule9_x1 == nfaulty_y1 - nfaulty_x1)






####################Step 4########################


#Rule is fired implies rule is enabled

s.add(Implies( (rule0_x1 > 0), And(True, ) ))
s.add(Implies( (rule1_x1 > 0), And(True, ) ))
s.add(Implies( (rule2_x1 > 0), And(nsnt00plus01_x1>=N-T, 2*nsnt00_x1>=N-T+1, ) ))
s.add(Implies( (rule3_x1 > 0), And(nsnt00plus01_x1>=N-T, 2*nsnt01_x1>=N-T+1, ) ))
s.add(Implies( (rule4_x1 > 0), And(2*nsnt10_x1>=N+1, ) ))
s.add(Implies( (rule5_x1 > 0), And(2*nsnt11_x1>=N+1, ) ))
s.add(Implies( (rule6_x1 > 0), And(nfaulty_x1<F, ) ))
s.add(Implies( (rule7_x1 > 0), And(nfaulty_x1<F, ) ))
s.add(Implies( (rule8_x1 > 0), And(nfaulty_x1<F, ) ))
s.add(Implies( (rule9_x1 > 0), And(nfaulty_x1<F, ) ))
s.add(Implies( (rule10_x1 > 0), And(True, ) ))
s.add(Implies( (rule11_x1 > 0), And(True, ) ))
s.add(Implies( (rule12_x1 > 0), And(True, ) ))
s.add(Implies( (rule13_x1 > 0), And(True, ) ))

##################Step 5#########################


#Ensuring that configurations x1 and y1 have the same context

s.add((2*nsnt11_x1>=N+1) == (2*nsnt11_y1>=N+1))
s.add((2*nsnt01_x1>=N-T+1) == (2*nsnt01_y1>=N-T+1))
s.add((2*nsnt10_x1>=N+1) == (2*nsnt10_y1>=N+1))
s.add((True) == (True))
s.add((nsnt00plus01_x1>=N-T) == (nsnt00plus01_y1>=N-T))
s.add((nfaulty_x1<F) == (nfaulty_y1<F))
s.add((2*nsnt00_x1>=N-T+1) == (2*nsnt00_y1>=N-T+1))

####################################################################################

#Creating constraints for a run between the x2th and y2th configurations

################Step 1#################


#Creating many copies of location variables

loc0_x2 = Real('loc0_x2')
loc0_y2 = Real('loc0_y2')
s.add(loc0_x2 >= 0)
s.add(loc0_y2 >= 0)
loc1_x2 = Real('loc1_x2')
loc1_y2 = Real('loc1_y2')
s.add(loc1_x2 >= 0)
s.add(loc1_y2 >= 0)
locP0_x2 = Real('locP0_x2')
locP0_y2 = Real('locP0_y2')
s.add(locP0_x2 >= 0)
s.add(locP0_y2 >= 0)
locP1_x2 = Real('locP1_x2')
locP1_y2 = Real('locP1_y2')
s.add(locP1_x2 >= 0)
s.add(locP1_y2 >= 0)
locAC0_x2 = Real('locAC0_x2')
locAC0_y2 = Real('locAC0_y2')
s.add(locAC0_x2 >= 0)
s.add(locAC0_y2 >= 0)
locAC1_x2 = Real('locAC1_x2')
locAC1_y2 = Real('locAC1_y2')
s.add(locAC1_x2 >= 0)
s.add(locAC1_y2 >= 0)
locCR_x2 = Real('locCR_x2')
locCR_y2 = Real('locCR_y2')
s.add(locCR_x2 >= 0)
s.add(locCR_y2 >= 0)






#Creating many copies of shared variables

nsnt00_x2 = Real('nsnt00_x2')
nsnt00_y2 = Real('nsnt00_y2')
s.add(nsnt00_x2 >= 0)
s.add(nsnt00_y2 >= 0)
nsnt01_x2 = Real('nsnt01_x2')
nsnt01_y2 = Real('nsnt01_y2')
s.add(nsnt01_x2 >= 0)
s.add(nsnt01_y2 >= 0)
nsnt10_x2 = Real('nsnt10_x2')
nsnt10_y2 = Real('nsnt10_y2')
s.add(nsnt10_x2 >= 0)
s.add(nsnt10_y2 >= 0)
nsnt11_x2 = Real('nsnt11_x2')
nsnt11_y2 = Real('nsnt11_y2')
s.add(nsnt11_x2 >= 0)
s.add(nsnt11_y2 >= 0)
nsnt00plus01_x2 = Real('nsnt00plus01_x2')
nsnt00plus01_y2 = Real('nsnt00plus01_y2')
s.add(nsnt00plus01_x2 >= 0)
s.add(nsnt00plus01_y2 >= 0)
nfaulty_x2 = Real('nfaulty_x2')
nfaulty_y2 = Real('nfaulty_y2')
s.add(nfaulty_x2 >= 0)
s.add(nfaulty_y2 >= 0)






#Creating many copies of variables for rules

rule0_x2 = Real('rule0_x2')
s.add(rule0_x2 >= 0)
rule1_x2 = Real('rule1_x2')
s.add(rule1_x2 >= 0)
rule2_x2 = Real('rule2_x2')
s.add(rule2_x2 >= 0)
rule3_x2 = Real('rule3_x2')
s.add(rule3_x2 >= 0)
rule4_x2 = Real('rule4_x2')
s.add(rule4_x2 >= 0)
rule5_x2 = Real('rule5_x2')
s.add(rule5_x2 >= 0)
rule6_x2 = Real('rule6_x2')
s.add(rule6_x2 >= 0)
rule7_x2 = Real('rule7_x2')
s.add(rule7_x2 >= 0)
rule8_x2 = Real('rule8_x2')
s.add(rule8_x2 >= 0)
rule9_x2 = Real('rule9_x2')
s.add(rule9_x2 >= 0)
rule10_x2 = Real('rule10_x2')
s.add(rule10_x2 >= 0)
rule11_x2 = Real('rule11_x2')
s.add(rule11_x2 >= 0)
rule12_x2 = Real('rule12_x2')
s.add(rule12_x2 >= 0)
rule13_x2 = Real('rule13_x2')
s.add(rule13_x2 >= 0)






###################Step 2####################


#Flow equations for the locations

s.add(0 - rule0_x2 ==  loc0_y2 - loc0_x2)
s.add(0 - rule1_x2 ==  loc1_y2 - loc1_x2)
s.add(0 + rule0_x2 + rule1_x2 - rule2_x2 - rule3_x2 - rule6_x2 - rule10_x2 + rule10_x2 ==  locP0_y2 - locP0_x2)
s.add(0 + rule2_x2 + rule3_x2 - rule4_x2 - rule5_x2 - rule7_x2 - rule11_x2 + rule11_x2 ==  locP1_y2 - locP1_x2)
s.add(0 + rule4_x2 - rule8_x2 - rule12_x2 + rule12_x2 ==  locAC0_y2 - locAC0_x2)
s.add(0 + rule5_x2 - rule9_x2 - rule13_x2 + rule13_x2 ==  locAC1_y2 - locAC1_x2)
s.add(0 + rule6_x2 + rule7_x2 + rule8_x2 + rule9_x2 ==  locCR_y2 - locCR_x2)






##################Step 3########################


#Flow equations for the shared variables

s.add(0 + rule0_x2 == nsnt00_y2 - nsnt00_x2)
s.add(0 + rule1_x2 == nsnt01_y2 - nsnt01_x2)
s.add(0 + rule2_x2 == nsnt10_y2 - nsnt10_x2)
s.add(0 + rule3_x2 == nsnt11_y2 - nsnt11_x2)
s.add(0 + rule0_x2 + rule1_x2 == nsnt00plus01_y2 - nsnt00plus01_x2)
s.add(0 + rule6_x2 + rule7_x2 + rule8_x2 + rule9_x2 == nfaulty_y2 - nfaulty_x2)






####################Step 4########################


#Rule is fired implies rule is enabled

s.add(Implies( (rule0_x2 > 0), And(True, ) ))
s.add(Implies( (rule1_x2 > 0), And(True, ) ))
s.add(Implies( (rule2_x2 > 0), And(nsnt00plus01_x2>=N-T, 2*nsnt00_x2>=N-T+1, ) ))
s.add(Implies( (rule3_x2 > 0), And(nsnt00plus01_x2>=N-T, 2*nsnt01_x2>=N-T+1, ) ))
s.add(Implies( (rule4_x2 > 0), And(2*nsnt10_x2>=N+1, ) ))
s.add(Implies( (rule5_x2 > 0), And(2*nsnt11_x2>=N+1, ) ))
s.add(Implies( (rule6_x2 > 0), And(nfaulty_x2<F, ) ))
s.add(Implies( (rule7_x2 > 0), And(nfaulty_x2<F, ) ))
s.add(Implies( (rule8_x2 > 0), And(nfaulty_x2<F, ) ))
s.add(Implies( (rule9_x2 > 0), And(nfaulty_x2<F, ) ))
s.add(Implies( (rule10_x2 > 0), And(True, ) ))
s.add(Implies( (rule11_x2 > 0), And(True, ) ))
s.add(Implies( (rule12_x2 > 0), And(True, ) ))
s.add(Implies( (rule13_x2 > 0), And(True, ) ))

##################Step 5#########################


#Ensuring that configurations x2 and y2 have the same context

s.add((2*nsnt11_x2>=N+1) == (2*nsnt11_y2>=N+1))
s.add((2*nsnt01_x2>=N-T+1) == (2*nsnt01_y2>=N-T+1))
s.add((2*nsnt10_x2>=N+1) == (2*nsnt10_y2>=N+1))
s.add((True) == (True))
s.add((nsnt00plus01_x2>=N-T) == (nsnt00plus01_y2>=N-T))
s.add((nfaulty_x2<F) == (nfaulty_y2<F))
s.add((2*nsnt00_x2>=N-T+1) == (2*nsnt00_y2>=N-T+1))

####################################################################################

#Creating constraints for a run between the x3th and y3th configurations

################Step 1#################


#Creating many copies of location variables

loc0_x3 = Real('loc0_x3')
loc0_y3 = Real('loc0_y3')
s.add(loc0_x3 >= 0)
s.add(loc0_y3 >= 0)
loc1_x3 = Real('loc1_x3')
loc1_y3 = Real('loc1_y3')
s.add(loc1_x3 >= 0)
s.add(loc1_y3 >= 0)
locP0_x3 = Real('locP0_x3')
locP0_y3 = Real('locP0_y3')
s.add(locP0_x3 >= 0)
s.add(locP0_y3 >= 0)
locP1_x3 = Real('locP1_x3')
locP1_y3 = Real('locP1_y3')
s.add(locP1_x3 >= 0)
s.add(locP1_y3 >= 0)
locAC0_x3 = Real('locAC0_x3')
locAC0_y3 = Real('locAC0_y3')
s.add(locAC0_x3 >= 0)
s.add(locAC0_y3 >= 0)
locAC1_x3 = Real('locAC1_x3')
locAC1_y3 = Real('locAC1_y3')
s.add(locAC1_x3 >= 0)
s.add(locAC1_y3 >= 0)
locCR_x3 = Real('locCR_x3')
locCR_y3 = Real('locCR_y3')
s.add(locCR_x3 >= 0)
s.add(locCR_y3 >= 0)






#Creating many copies of shared variables

nsnt00_x3 = Real('nsnt00_x3')
nsnt00_y3 = Real('nsnt00_y3')
s.add(nsnt00_x3 >= 0)
s.add(nsnt00_y3 >= 0)
nsnt01_x3 = Real('nsnt01_x3')
nsnt01_y3 = Real('nsnt01_y3')
s.add(nsnt01_x3 >= 0)
s.add(nsnt01_y3 >= 0)
nsnt10_x3 = Real('nsnt10_x3')
nsnt10_y3 = Real('nsnt10_y3')
s.add(nsnt10_x3 >= 0)
s.add(nsnt10_y3 >= 0)
nsnt11_x3 = Real('nsnt11_x3')
nsnt11_y3 = Real('nsnt11_y3')
s.add(nsnt11_x3 >= 0)
s.add(nsnt11_y3 >= 0)
nsnt00plus01_x3 = Real('nsnt00plus01_x3')
nsnt00plus01_y3 = Real('nsnt00plus01_y3')
s.add(nsnt00plus01_x3 >= 0)
s.add(nsnt00plus01_y3 >= 0)
nfaulty_x3 = Real('nfaulty_x3')
nfaulty_y3 = Real('nfaulty_y3')
s.add(nfaulty_x3 >= 0)
s.add(nfaulty_y3 >= 0)






#Creating many copies of variables for rules

rule0_x3 = Real('rule0_x3')
s.add(rule0_x3 >= 0)
rule1_x3 = Real('rule1_x3')
s.add(rule1_x3 >= 0)
rule2_x3 = Real('rule2_x3')
s.add(rule2_x3 >= 0)
rule3_x3 = Real('rule3_x3')
s.add(rule3_x3 >= 0)
rule4_x3 = Real('rule4_x3')
s.add(rule4_x3 >= 0)
rule5_x3 = Real('rule5_x3')
s.add(rule5_x3 >= 0)
rule6_x3 = Real('rule6_x3')
s.add(rule6_x3 >= 0)
rule7_x3 = Real('rule7_x3')
s.add(rule7_x3 >= 0)
rule8_x3 = Real('rule8_x3')
s.add(rule8_x3 >= 0)
rule9_x3 = Real('rule9_x3')
s.add(rule9_x3 >= 0)
rule10_x3 = Real('rule10_x3')
s.add(rule10_x3 >= 0)
rule11_x3 = Real('rule11_x3')
s.add(rule11_x3 >= 0)
rule12_x3 = Real('rule12_x3')
s.add(rule12_x3 >= 0)
rule13_x3 = Real('rule13_x3')
s.add(rule13_x3 >= 0)






###################Step 2####################


#Flow equations for the locations

s.add(0 - rule0_x3 ==  loc0_y3 - loc0_x3)
s.add(0 - rule1_x3 ==  loc1_y3 - loc1_x3)
s.add(0 + rule0_x3 + rule1_x3 - rule2_x3 - rule3_x3 - rule6_x3 - rule10_x3 + rule10_x3 ==  locP0_y3 - locP0_x3)
s.add(0 + rule2_x3 + rule3_x3 - rule4_x3 - rule5_x3 - rule7_x3 - rule11_x3 + rule11_x3 ==  locP1_y3 - locP1_x3)
s.add(0 + rule4_x3 - rule8_x3 - rule12_x3 + rule12_x3 ==  locAC0_y3 - locAC0_x3)
s.add(0 + rule5_x3 - rule9_x3 - rule13_x3 + rule13_x3 ==  locAC1_y3 - locAC1_x3)
s.add(0 + rule6_x3 + rule7_x3 + rule8_x3 + rule9_x3 ==  locCR_y3 - locCR_x3)






##################Step 3########################


#Flow equations for the shared variables

s.add(0 + rule0_x3 == nsnt00_y3 - nsnt00_x3)
s.add(0 + rule1_x3 == nsnt01_y3 - nsnt01_x3)
s.add(0 + rule2_x3 == nsnt10_y3 - nsnt10_x3)
s.add(0 + rule3_x3 == nsnt11_y3 - nsnt11_x3)
s.add(0 + rule0_x3 + rule1_x3 == nsnt00plus01_y3 - nsnt00plus01_x3)
s.add(0 + rule6_x3 + rule7_x3 + rule8_x3 + rule9_x3 == nfaulty_y3 - nfaulty_x3)






####################Step 4########################


#Rule is fired implies rule is enabled

s.add(Implies( (rule0_x3 > 0), And(True, ) ))
s.add(Implies( (rule1_x3 > 0), And(True, ) ))
s.add(Implies( (rule2_x3 > 0), And(nsnt00plus01_x3>=N-T, 2*nsnt00_x3>=N-T+1, ) ))
s.add(Implies( (rule3_x3 > 0), And(nsnt00plus01_x3>=N-T, 2*nsnt01_x3>=N-T+1, ) ))
s.add(Implies( (rule4_x3 > 0), And(2*nsnt10_x3>=N+1, ) ))
s.add(Implies( (rule5_x3 > 0), And(2*nsnt11_x3>=N+1, ) ))
s.add(Implies( (rule6_x3 > 0), And(nfaulty_x3<F, ) ))
s.add(Implies( (rule7_x3 > 0), And(nfaulty_x3<F, ) ))
s.add(Implies( (rule8_x3 > 0), And(nfaulty_x3<F, ) ))
s.add(Implies( (rule9_x3 > 0), And(nfaulty_x3<F, ) ))
s.add(Implies( (rule10_x3 > 0), And(True, ) ))
s.add(Implies( (rule11_x3 > 0), And(True, ) ))
s.add(Implies( (rule12_x3 > 0), And(True, ) ))
s.add(Implies( (rule13_x3 > 0), And(True, ) ))

##################Step 5#########################


#Ensuring that configurations x3 and y3 have the same context

s.add((2*nsnt11_x3>=N+1) == (2*nsnt11_y3>=N+1))
s.add((2*nsnt01_x3>=N-T+1) == (2*nsnt01_y3>=N-T+1))
s.add((2*nsnt10_x3>=N+1) == (2*nsnt10_y3>=N+1))
s.add((True) == (True))
s.add((nsnt00plus01_x3>=N-T) == (nsnt00plus01_y3>=N-T))
s.add((nfaulty_x3<F) == (nfaulty_y3<F))
s.add((2*nsnt00_x3>=N-T+1) == (2*nsnt00_y3>=N-T+1))

####################################################################################

#Creating constraints for a run between the x4th and y4th configurations

################Step 1#################


#Creating many copies of location variables

loc0_x4 = Real('loc0_x4')
loc0_y4 = Real('loc0_y4')
s.add(loc0_x4 >= 0)
s.add(loc0_y4 >= 0)
loc1_x4 = Real('loc1_x4')
loc1_y4 = Real('loc1_y4')
s.add(loc1_x4 >= 0)
s.add(loc1_y4 >= 0)
locP0_x4 = Real('locP0_x4')
locP0_y4 = Real('locP0_y4')
s.add(locP0_x4 >= 0)
s.add(locP0_y4 >= 0)
locP1_x4 = Real('locP1_x4')
locP1_y4 = Real('locP1_y4')
s.add(locP1_x4 >= 0)
s.add(locP1_y4 >= 0)
locAC0_x4 = Real('locAC0_x4')
locAC0_y4 = Real('locAC0_y4')
s.add(locAC0_x4 >= 0)
s.add(locAC0_y4 >= 0)
locAC1_x4 = Real('locAC1_x4')
locAC1_y4 = Real('locAC1_y4')
s.add(locAC1_x4 >= 0)
s.add(locAC1_y4 >= 0)
locCR_x4 = Real('locCR_x4')
locCR_y4 = Real('locCR_y4')
s.add(locCR_x4 >= 0)
s.add(locCR_y4 >= 0)






#Creating many copies of shared variables

nsnt00_x4 = Real('nsnt00_x4')
nsnt00_y4 = Real('nsnt00_y4')
s.add(nsnt00_x4 >= 0)
s.add(nsnt00_y4 >= 0)
nsnt01_x4 = Real('nsnt01_x4')
nsnt01_y4 = Real('nsnt01_y4')
s.add(nsnt01_x4 >= 0)
s.add(nsnt01_y4 >= 0)
nsnt10_x4 = Real('nsnt10_x4')
nsnt10_y4 = Real('nsnt10_y4')
s.add(nsnt10_x4 >= 0)
s.add(nsnt10_y4 >= 0)
nsnt11_x4 = Real('nsnt11_x4')
nsnt11_y4 = Real('nsnt11_y4')
s.add(nsnt11_x4 >= 0)
s.add(nsnt11_y4 >= 0)
nsnt00plus01_x4 = Real('nsnt00plus01_x4')
nsnt00plus01_y4 = Real('nsnt00plus01_y4')
s.add(nsnt00plus01_x4 >= 0)
s.add(nsnt00plus01_y4 >= 0)
nfaulty_x4 = Real('nfaulty_x4')
nfaulty_y4 = Real('nfaulty_y4')
s.add(nfaulty_x4 >= 0)
s.add(nfaulty_y4 >= 0)






#Creating many copies of variables for rules

rule0_x4 = Real('rule0_x4')
s.add(rule0_x4 >= 0)
rule1_x4 = Real('rule1_x4')
s.add(rule1_x4 >= 0)
rule2_x4 = Real('rule2_x4')
s.add(rule2_x4 >= 0)
rule3_x4 = Real('rule3_x4')
s.add(rule3_x4 >= 0)
rule4_x4 = Real('rule4_x4')
s.add(rule4_x4 >= 0)
rule5_x4 = Real('rule5_x4')
s.add(rule5_x4 >= 0)
rule6_x4 = Real('rule6_x4')
s.add(rule6_x4 >= 0)
rule7_x4 = Real('rule7_x4')
s.add(rule7_x4 >= 0)
rule8_x4 = Real('rule8_x4')
s.add(rule8_x4 >= 0)
rule9_x4 = Real('rule9_x4')
s.add(rule9_x4 >= 0)
rule10_x4 = Real('rule10_x4')
s.add(rule10_x4 >= 0)
rule11_x4 = Real('rule11_x4')
s.add(rule11_x4 >= 0)
rule12_x4 = Real('rule12_x4')
s.add(rule12_x4 >= 0)
rule13_x4 = Real('rule13_x4')
s.add(rule13_x4 >= 0)






###################Step 2####################


#Flow equations for the locations

s.add(0 - rule0_x4 ==  loc0_y4 - loc0_x4)
s.add(0 - rule1_x4 ==  loc1_y4 - loc1_x4)
s.add(0 + rule0_x4 + rule1_x4 - rule2_x4 - rule3_x4 - rule6_x4 - rule10_x4 + rule10_x4 ==  locP0_y4 - locP0_x4)
s.add(0 + rule2_x4 + rule3_x4 - rule4_x4 - rule5_x4 - rule7_x4 - rule11_x4 + rule11_x4 ==  locP1_y4 - locP1_x4)
s.add(0 + rule4_x4 - rule8_x4 - rule12_x4 + rule12_x4 ==  locAC0_y4 - locAC0_x4)
s.add(0 + rule5_x4 - rule9_x4 - rule13_x4 + rule13_x4 ==  locAC1_y4 - locAC1_x4)
s.add(0 + rule6_x4 + rule7_x4 + rule8_x4 + rule9_x4 ==  locCR_y4 - locCR_x4)






##################Step 3########################


#Flow equations for the shared variables

s.add(0 + rule0_x4 == nsnt00_y4 - nsnt00_x4)
s.add(0 + rule1_x4 == nsnt01_y4 - nsnt01_x4)
s.add(0 + rule2_x4 == nsnt10_y4 - nsnt10_x4)
s.add(0 + rule3_x4 == nsnt11_y4 - nsnt11_x4)
s.add(0 + rule0_x4 + rule1_x4 == nsnt00plus01_y4 - nsnt00plus01_x4)
s.add(0 + rule6_x4 + rule7_x4 + rule8_x4 + rule9_x4 == nfaulty_y4 - nfaulty_x4)






####################Step 4########################


#Rule is fired implies rule is enabled

s.add(Implies( (rule0_x4 > 0), And(True, ) ))
s.add(Implies( (rule1_x4 > 0), And(True, ) ))
s.add(Implies( (rule2_x4 > 0), And(nsnt00plus01_x4>=N-T, 2*nsnt00_x4>=N-T+1, ) ))
s.add(Implies( (rule3_x4 > 0), And(nsnt00plus01_x4>=N-T, 2*nsnt01_x4>=N-T+1, ) ))
s.add(Implies( (rule4_x4 > 0), And(2*nsnt10_x4>=N+1, ) ))
s.add(Implies( (rule5_x4 > 0), And(2*nsnt11_x4>=N+1, ) ))
s.add(Implies( (rule6_x4 > 0), And(nfaulty_x4<F, ) ))
s.add(Implies( (rule7_x4 > 0), And(nfaulty_x4<F, ) ))
s.add(Implies( (rule8_x4 > 0), And(nfaulty_x4<F, ) ))
s.add(Implies( (rule9_x4 > 0), And(nfaulty_x4<F, ) ))
s.add(Implies( (rule10_x4 > 0), And(True, ) ))
s.add(Implies( (rule11_x4 > 0), And(True, ) ))
s.add(Implies( (rule12_x4 > 0), And(True, ) ))
s.add(Implies( (rule13_x4 > 0), And(True, ) ))

##################Step 5#########################


#Ensuring that configurations x4 and y4 have the same context

s.add((2*nsnt11_x4>=N+1) == (2*nsnt11_y4>=N+1))
s.add((2*nsnt01_x4>=N-T+1) == (2*nsnt01_y4>=N-T+1))
s.add((2*nsnt10_x4>=N+1) == (2*nsnt10_y4>=N+1))
s.add((True) == (True))
s.add((nsnt00plus01_x4>=N-T) == (nsnt00plus01_y4>=N-T))
s.add((nfaulty_x4<F) == (nfaulty_y4<F))
s.add((2*nsnt00_x4>=N-T+1) == (2*nsnt00_y4>=N-T+1))

####################################################################################

#Creating constraints for a run between the x5th and y5th configurations

################Step 1#################


#Creating many copies of location variables

loc0_x5 = Real('loc0_x5')
loc0_y5 = Real('loc0_y5')
s.add(loc0_x5 >= 0)
s.add(loc0_y5 >= 0)
loc1_x5 = Real('loc1_x5')
loc1_y5 = Real('loc1_y5')
s.add(loc1_x5 >= 0)
s.add(loc1_y5 >= 0)
locP0_x5 = Real('locP0_x5')
locP0_y5 = Real('locP0_y5')
s.add(locP0_x5 >= 0)
s.add(locP0_y5 >= 0)
locP1_x5 = Real('locP1_x5')
locP1_y5 = Real('locP1_y5')
s.add(locP1_x5 >= 0)
s.add(locP1_y5 >= 0)
locAC0_x5 = Real('locAC0_x5')
locAC0_y5 = Real('locAC0_y5')
s.add(locAC0_x5 >= 0)
s.add(locAC0_y5 >= 0)
locAC1_x5 = Real('locAC1_x5')
locAC1_y5 = Real('locAC1_y5')
s.add(locAC1_x5 >= 0)
s.add(locAC1_y5 >= 0)
locCR_x5 = Real('locCR_x5')
locCR_y5 = Real('locCR_y5')
s.add(locCR_x5 >= 0)
s.add(locCR_y5 >= 0)






#Creating many copies of shared variables

nsnt00_x5 = Real('nsnt00_x5')
nsnt00_y5 = Real('nsnt00_y5')
s.add(nsnt00_x5 >= 0)
s.add(nsnt00_y5 >= 0)
nsnt01_x5 = Real('nsnt01_x5')
nsnt01_y5 = Real('nsnt01_y5')
s.add(nsnt01_x5 >= 0)
s.add(nsnt01_y5 >= 0)
nsnt10_x5 = Real('nsnt10_x5')
nsnt10_y5 = Real('nsnt10_y5')
s.add(nsnt10_x5 >= 0)
s.add(nsnt10_y5 >= 0)
nsnt11_x5 = Real('nsnt11_x5')
nsnt11_y5 = Real('nsnt11_y5')
s.add(nsnt11_x5 >= 0)
s.add(nsnt11_y5 >= 0)
nsnt00plus01_x5 = Real('nsnt00plus01_x5')
nsnt00plus01_y5 = Real('nsnt00plus01_y5')
s.add(nsnt00plus01_x5 >= 0)
s.add(nsnt00plus01_y5 >= 0)
nfaulty_x5 = Real('nfaulty_x5')
nfaulty_y5 = Real('nfaulty_y5')
s.add(nfaulty_x5 >= 0)
s.add(nfaulty_y5 >= 0)






#Creating many copies of variables for rules

rule0_x5 = Real('rule0_x5')
s.add(rule0_x5 >= 0)
rule1_x5 = Real('rule1_x5')
s.add(rule1_x5 >= 0)
rule2_x5 = Real('rule2_x5')
s.add(rule2_x5 >= 0)
rule3_x5 = Real('rule3_x5')
s.add(rule3_x5 >= 0)
rule4_x5 = Real('rule4_x5')
s.add(rule4_x5 >= 0)
rule5_x5 = Real('rule5_x5')
s.add(rule5_x5 >= 0)
rule6_x5 = Real('rule6_x5')
s.add(rule6_x5 >= 0)
rule7_x5 = Real('rule7_x5')
s.add(rule7_x5 >= 0)
rule8_x5 = Real('rule8_x5')
s.add(rule8_x5 >= 0)
rule9_x5 = Real('rule9_x5')
s.add(rule9_x5 >= 0)
rule10_x5 = Real('rule10_x5')
s.add(rule10_x5 >= 0)
rule11_x5 = Real('rule11_x5')
s.add(rule11_x5 >= 0)
rule12_x5 = Real('rule12_x5')
s.add(rule12_x5 >= 0)
rule13_x5 = Real('rule13_x5')
s.add(rule13_x5 >= 0)






###################Step 2####################


#Flow equations for the locations

s.add(0 - rule0_x5 ==  loc0_y5 - loc0_x5)
s.add(0 - rule1_x5 ==  loc1_y5 - loc1_x5)
s.add(0 + rule0_x5 + rule1_x5 - rule2_x5 - rule3_x5 - rule6_x5 - rule10_x5 + rule10_x5 ==  locP0_y5 - locP0_x5)
s.add(0 + rule2_x5 + rule3_x5 - rule4_x5 - rule5_x5 - rule7_x5 - rule11_x5 + rule11_x5 ==  locP1_y5 - locP1_x5)
s.add(0 + rule4_x5 - rule8_x5 - rule12_x5 + rule12_x5 ==  locAC0_y5 - locAC0_x5)
s.add(0 + rule5_x5 - rule9_x5 - rule13_x5 + rule13_x5 ==  locAC1_y5 - locAC1_x5)
s.add(0 + rule6_x5 + rule7_x5 + rule8_x5 + rule9_x5 ==  locCR_y5 - locCR_x5)






##################Step 3########################


#Flow equations for the shared variables

s.add(0 + rule0_x5 == nsnt00_y5 - nsnt00_x5)
s.add(0 + rule1_x5 == nsnt01_y5 - nsnt01_x5)
s.add(0 + rule2_x5 == nsnt10_y5 - nsnt10_x5)
s.add(0 + rule3_x5 == nsnt11_y5 - nsnt11_x5)
s.add(0 + rule0_x5 + rule1_x5 == nsnt00plus01_y5 - nsnt00plus01_x5)
s.add(0 + rule6_x5 + rule7_x5 + rule8_x5 + rule9_x5 == nfaulty_y5 - nfaulty_x5)






####################Step 4########################


#Rule is fired implies rule is enabled

s.add(Implies( (rule0_x5 > 0), And(True, ) ))
s.add(Implies( (rule1_x5 > 0), And(True, ) ))
s.add(Implies( (rule2_x5 > 0), And(nsnt00plus01_x5>=N-T, 2*nsnt00_x5>=N-T+1, ) ))
s.add(Implies( (rule3_x5 > 0), And(nsnt00plus01_x5>=N-T, 2*nsnt01_x5>=N-T+1, ) ))
s.add(Implies( (rule4_x5 > 0), And(2*nsnt10_x5>=N+1, ) ))
s.add(Implies( (rule5_x5 > 0), And(2*nsnt11_x5>=N+1, ) ))
s.add(Implies( (rule6_x5 > 0), And(nfaulty_x5<F, ) ))
s.add(Implies( (rule7_x5 > 0), And(nfaulty_x5<F, ) ))
s.add(Implies( (rule8_x5 > 0), And(nfaulty_x5<F, ) ))
s.add(Implies( (rule9_x5 > 0), And(nfaulty_x5<F, ) ))
s.add(Implies( (rule10_x5 > 0), And(True, ) ))
s.add(Implies( (rule11_x5 > 0), And(True, ) ))
s.add(Implies( (rule12_x5 > 0), And(True, ) ))
s.add(Implies( (rule13_x5 > 0), And(True, ) ))

##################Step 5#########################


#Ensuring that configurations x5 and y5 have the same context

s.add((2*nsnt11_x5>=N+1) == (2*nsnt11_y5>=N+1))
s.add((2*nsnt01_x5>=N-T+1) == (2*nsnt01_y5>=N-T+1))
s.add((2*nsnt10_x5>=N+1) == (2*nsnt10_y5>=N+1))
s.add((True) == (True))
s.add((nsnt00plus01_x5>=N-T) == (nsnt00plus01_y5>=N-T))
s.add((nfaulty_x5<F) == (nfaulty_y5<F))
s.add((2*nsnt00_x5>=N-T+1) == (2*nsnt00_y5>=N-T+1))

####################################################################################

#Creating constraints for a run between the x6th and y6th configurations

################Step 1#################


#Creating many copies of location variables

loc0_x6 = Real('loc0_x6')
loc0_y6 = Real('loc0_y6')
s.add(loc0_x6 >= 0)
s.add(loc0_y6 >= 0)
loc1_x6 = Real('loc1_x6')
loc1_y6 = Real('loc1_y6')
s.add(loc1_x6 >= 0)
s.add(loc1_y6 >= 0)
locP0_x6 = Real('locP0_x6')
locP0_y6 = Real('locP0_y6')
s.add(locP0_x6 >= 0)
s.add(locP0_y6 >= 0)
locP1_x6 = Real('locP1_x6')
locP1_y6 = Real('locP1_y6')
s.add(locP1_x6 >= 0)
s.add(locP1_y6 >= 0)
locAC0_x6 = Real('locAC0_x6')
locAC0_y6 = Real('locAC0_y6')
s.add(locAC0_x6 >= 0)
s.add(locAC0_y6 >= 0)
locAC1_x6 = Real('locAC1_x6')
locAC1_y6 = Real('locAC1_y6')
s.add(locAC1_x6 >= 0)
s.add(locAC1_y6 >= 0)
locCR_x6 = Real('locCR_x6')
locCR_y6 = Real('locCR_y6')
s.add(locCR_x6 >= 0)
s.add(locCR_y6 >= 0)






#Creating many copies of shared variables

nsnt00_x6 = Real('nsnt00_x6')
nsnt00_y6 = Real('nsnt00_y6')
s.add(nsnt00_x6 >= 0)
s.add(nsnt00_y6 >= 0)
nsnt01_x6 = Real('nsnt01_x6')
nsnt01_y6 = Real('nsnt01_y6')
s.add(nsnt01_x6 >= 0)
s.add(nsnt01_y6 >= 0)
nsnt10_x6 = Real('nsnt10_x6')
nsnt10_y6 = Real('nsnt10_y6')
s.add(nsnt10_x6 >= 0)
s.add(nsnt10_y6 >= 0)
nsnt11_x6 = Real('nsnt11_x6')
nsnt11_y6 = Real('nsnt11_y6')
s.add(nsnt11_x6 >= 0)
s.add(nsnt11_y6 >= 0)
nsnt00plus01_x6 = Real('nsnt00plus01_x6')
nsnt00plus01_y6 = Real('nsnt00plus01_y6')
s.add(nsnt00plus01_x6 >= 0)
s.add(nsnt00plus01_y6 >= 0)
nfaulty_x6 = Real('nfaulty_x6')
nfaulty_y6 = Real('nfaulty_y6')
s.add(nfaulty_x6 >= 0)
s.add(nfaulty_y6 >= 0)






#Creating many copies of variables for rules

rule0_x6 = Real('rule0_x6')
s.add(rule0_x6 >= 0)
rule1_x6 = Real('rule1_x6')
s.add(rule1_x6 >= 0)
rule2_x6 = Real('rule2_x6')
s.add(rule2_x6 >= 0)
rule3_x6 = Real('rule3_x6')
s.add(rule3_x6 >= 0)
rule4_x6 = Real('rule4_x6')
s.add(rule4_x6 >= 0)
rule5_x6 = Real('rule5_x6')
s.add(rule5_x6 >= 0)
rule6_x6 = Real('rule6_x6')
s.add(rule6_x6 >= 0)
rule7_x6 = Real('rule7_x6')
s.add(rule7_x6 >= 0)
rule8_x6 = Real('rule8_x6')
s.add(rule8_x6 >= 0)
rule9_x6 = Real('rule9_x6')
s.add(rule9_x6 >= 0)
rule10_x6 = Real('rule10_x6')
s.add(rule10_x6 >= 0)
rule11_x6 = Real('rule11_x6')
s.add(rule11_x6 >= 0)
rule12_x6 = Real('rule12_x6')
s.add(rule12_x6 >= 0)
rule13_x6 = Real('rule13_x6')
s.add(rule13_x6 >= 0)






###################Step 2####################


#Flow equations for the locations

s.add(0 - rule0_x6 ==  loc0_y6 - loc0_x6)
s.add(0 - rule1_x6 ==  loc1_y6 - loc1_x6)
s.add(0 + rule0_x6 + rule1_x6 - rule2_x6 - rule3_x6 - rule6_x6 - rule10_x6 + rule10_x6 ==  locP0_y6 - locP0_x6)
s.add(0 + rule2_x6 + rule3_x6 - rule4_x6 - rule5_x6 - rule7_x6 - rule11_x6 + rule11_x6 ==  locP1_y6 - locP1_x6)
s.add(0 + rule4_x6 - rule8_x6 - rule12_x6 + rule12_x6 ==  locAC0_y6 - locAC0_x6)
s.add(0 + rule5_x6 - rule9_x6 - rule13_x6 + rule13_x6 ==  locAC1_y6 - locAC1_x6)
s.add(0 + rule6_x6 + rule7_x6 + rule8_x6 + rule9_x6 ==  locCR_y6 - locCR_x6)






##################Step 3########################


#Flow equations for the shared variables

s.add(0 + rule0_x6 == nsnt00_y6 - nsnt00_x6)
s.add(0 + rule1_x6 == nsnt01_y6 - nsnt01_x6)
s.add(0 + rule2_x6 == nsnt10_y6 - nsnt10_x6)
s.add(0 + rule3_x6 == nsnt11_y6 - nsnt11_x6)
s.add(0 + rule0_x6 + rule1_x6 == nsnt00plus01_y6 - nsnt00plus01_x6)
s.add(0 + rule6_x6 + rule7_x6 + rule8_x6 + rule9_x6 == nfaulty_y6 - nfaulty_x6)






####################Step 4########################


#Rule is fired implies rule is enabled

s.add(Implies( (rule0_x6 > 0), And(True, ) ))
s.add(Implies( (rule1_x6 > 0), And(True, ) ))
s.add(Implies( (rule2_x6 > 0), And(nsnt00plus01_x6>=N-T, 2*nsnt00_x6>=N-T+1, ) ))
s.add(Implies( (rule3_x6 > 0), And(nsnt00plus01_x6>=N-T, 2*nsnt01_x6>=N-T+1, ) ))
s.add(Implies( (rule4_x6 > 0), And(2*nsnt10_x6>=N+1, ) ))
s.add(Implies( (rule5_x6 > 0), And(2*nsnt11_x6>=N+1, ) ))
s.add(Implies( (rule6_x6 > 0), And(nfaulty_x6<F, ) ))
s.add(Implies( (rule7_x6 > 0), And(nfaulty_x6<F, ) ))
s.add(Implies( (rule8_x6 > 0), And(nfaulty_x6<F, ) ))
s.add(Implies( (rule9_x6 > 0), And(nfaulty_x6<F, ) ))
s.add(Implies( (rule10_x6 > 0), And(True, ) ))
s.add(Implies( (rule11_x6 > 0), And(True, ) ))
s.add(Implies( (rule12_x6 > 0), And(True, ) ))
s.add(Implies( (rule13_x6 > 0), And(True, ) ))

##################Step 5#########################


#Ensuring that configurations x6 and y6 have the same context

s.add((2*nsnt11_x6>=N+1) == (2*nsnt11_y6>=N+1))
s.add((2*nsnt01_x6>=N-T+1) == (2*nsnt01_y6>=N-T+1))
s.add((2*nsnt10_x6>=N+1) == (2*nsnt10_y6>=N+1))
s.add((True) == (True))
s.add((nsnt00plus01_x6>=N-T) == (nsnt00plus01_y6>=N-T))
s.add((nfaulty_x6<F) == (nfaulty_y6<F))
s.add((2*nsnt00_x6>=N-T+1) == (2*nsnt00_y6>=N-T+1))

####################################################################################

#Creating constraints for a run between the x7th and y7th configurations

################Step 1#################


#Creating many copies of location variables

loc0_x7 = Real('loc0_x7')
loc0_y7 = Real('loc0_y7')
s.add(loc0_x7 >= 0)
s.add(loc0_y7 >= 0)
loc1_x7 = Real('loc1_x7')
loc1_y7 = Real('loc1_y7')
s.add(loc1_x7 >= 0)
s.add(loc1_y7 >= 0)
locP0_x7 = Real('locP0_x7')
locP0_y7 = Real('locP0_y7')
s.add(locP0_x7 >= 0)
s.add(locP0_y7 >= 0)
locP1_x7 = Real('locP1_x7')
locP1_y7 = Real('locP1_y7')
s.add(locP1_x7 >= 0)
s.add(locP1_y7 >= 0)
locAC0_x7 = Real('locAC0_x7')
locAC0_y7 = Real('locAC0_y7')
s.add(locAC0_x7 >= 0)
s.add(locAC0_y7 >= 0)
locAC1_x7 = Real('locAC1_x7')
locAC1_y7 = Real('locAC1_y7')
s.add(locAC1_x7 >= 0)
s.add(locAC1_y7 >= 0)
locCR_x7 = Real('locCR_x7')
locCR_y7 = Real('locCR_y7')
s.add(locCR_x7 >= 0)
s.add(locCR_y7 >= 0)






#Creating many copies of shared variables

nsnt00_x7 = Real('nsnt00_x7')
nsnt00_y7 = Real('nsnt00_y7')
s.add(nsnt00_x7 >= 0)
s.add(nsnt00_y7 >= 0)
nsnt01_x7 = Real('nsnt01_x7')
nsnt01_y7 = Real('nsnt01_y7')
s.add(nsnt01_x7 >= 0)
s.add(nsnt01_y7 >= 0)
nsnt10_x7 = Real('nsnt10_x7')
nsnt10_y7 = Real('nsnt10_y7')
s.add(nsnt10_x7 >= 0)
s.add(nsnt10_y7 >= 0)
nsnt11_x7 = Real('nsnt11_x7')
nsnt11_y7 = Real('nsnt11_y7')
s.add(nsnt11_x7 >= 0)
s.add(nsnt11_y7 >= 0)
nsnt00plus01_x7 = Real('nsnt00plus01_x7')
nsnt00plus01_y7 = Real('nsnt00plus01_y7')
s.add(nsnt00plus01_x7 >= 0)
s.add(nsnt00plus01_y7 >= 0)
nfaulty_x7 = Real('nfaulty_x7')
nfaulty_y7 = Real('nfaulty_y7')
s.add(nfaulty_x7 >= 0)
s.add(nfaulty_y7 >= 0)






#Creating many copies of variables for rules

rule0_x7 = Real('rule0_x7')
s.add(rule0_x7 >= 0)
rule1_x7 = Real('rule1_x7')
s.add(rule1_x7 >= 0)
rule2_x7 = Real('rule2_x7')
s.add(rule2_x7 >= 0)
rule3_x7 = Real('rule3_x7')
s.add(rule3_x7 >= 0)
rule4_x7 = Real('rule4_x7')
s.add(rule4_x7 >= 0)
rule5_x7 = Real('rule5_x7')
s.add(rule5_x7 >= 0)
rule6_x7 = Real('rule6_x7')
s.add(rule6_x7 >= 0)
rule7_x7 = Real('rule7_x7')
s.add(rule7_x7 >= 0)
rule8_x7 = Real('rule8_x7')
s.add(rule8_x7 >= 0)
rule9_x7 = Real('rule9_x7')
s.add(rule9_x7 >= 0)
rule10_x7 = Real('rule10_x7')
s.add(rule10_x7 >= 0)
rule11_x7 = Real('rule11_x7')
s.add(rule11_x7 >= 0)
rule12_x7 = Real('rule12_x7')
s.add(rule12_x7 >= 0)
rule13_x7 = Real('rule13_x7')
s.add(rule13_x7 >= 0)






###################Step 2####################


#Flow equations for the locations

s.add(0 - rule0_x7 ==  loc0_y7 - loc0_x7)
s.add(0 - rule1_x7 ==  loc1_y7 - loc1_x7)
s.add(0 + rule0_x7 + rule1_x7 - rule2_x7 - rule3_x7 - rule6_x7 - rule10_x7 + rule10_x7 ==  locP0_y7 - locP0_x7)
s.add(0 + rule2_x7 + rule3_x7 - rule4_x7 - rule5_x7 - rule7_x7 - rule11_x7 + rule11_x7 ==  locP1_y7 - locP1_x7)
s.add(0 + rule4_x7 - rule8_x7 - rule12_x7 + rule12_x7 ==  locAC0_y7 - locAC0_x7)
s.add(0 + rule5_x7 - rule9_x7 - rule13_x7 + rule13_x7 ==  locAC1_y7 - locAC1_x7)
s.add(0 + rule6_x7 + rule7_x7 + rule8_x7 + rule9_x7 ==  locCR_y7 - locCR_x7)






##################Step 3########################


#Flow equations for the shared variables

s.add(0 + rule0_x7 == nsnt00_y7 - nsnt00_x7)
s.add(0 + rule1_x7 == nsnt01_y7 - nsnt01_x7)
s.add(0 + rule2_x7 == nsnt10_y7 - nsnt10_x7)
s.add(0 + rule3_x7 == nsnt11_y7 - nsnt11_x7)
s.add(0 + rule0_x7 + rule1_x7 == nsnt00plus01_y7 - nsnt00plus01_x7)
s.add(0 + rule6_x7 + rule7_x7 + rule8_x7 + rule9_x7 == nfaulty_y7 - nfaulty_x7)






####################Step 4########################


#Rule is fired implies rule is enabled

s.add(Implies( (rule0_x7 > 0), And(True, ) ))
s.add(Implies( (rule1_x7 > 0), And(True, ) ))
s.add(Implies( (rule2_x7 > 0), And(nsnt00plus01_x7>=N-T, 2*nsnt00_x7>=N-T+1, ) ))
s.add(Implies( (rule3_x7 > 0), And(nsnt00plus01_x7>=N-T, 2*nsnt01_x7>=N-T+1, ) ))
s.add(Implies( (rule4_x7 > 0), And(2*nsnt10_x7>=N+1, ) ))
s.add(Implies( (rule5_x7 > 0), And(2*nsnt11_x7>=N+1, ) ))
s.add(Implies( (rule6_x7 > 0), And(nfaulty_x7<F, ) ))
s.add(Implies( (rule7_x7 > 0), And(nfaulty_x7<F, ) ))
s.add(Implies( (rule8_x7 > 0), And(nfaulty_x7<F, ) ))
s.add(Implies( (rule9_x7 > 0), And(nfaulty_x7<F, ) ))
s.add(Implies( (rule10_x7 > 0), And(True, ) ))
s.add(Implies( (rule11_x7 > 0), And(True, ) ))
s.add(Implies( (rule12_x7 > 0), And(True, ) ))
s.add(Implies( (rule13_x7 > 0), And(True, ) ))

##################Step 5#########################


#Ensuring that configurations x7 and y7 have the same context

s.add((2*nsnt11_x7>=N+1) == (2*nsnt11_y7>=N+1))
s.add((2*nsnt01_x7>=N-T+1) == (2*nsnt01_y7>=N-T+1))
s.add((2*nsnt10_x7>=N+1) == (2*nsnt10_y7>=N+1))
s.add((True) == (True))
s.add((nsnt00plus01_x7>=N-T) == (nsnt00plus01_y7>=N-T))
s.add((nfaulty_x7<F) == (nfaulty_y7<F))
s.add((2*nsnt00_x7>=N-T+1) == (2*nsnt00_y7>=N-T+1))

####################################################################################

#Creating constraints for a run between the y0th and x1th configurations

################Step 1#################


#Creating many copies of variables for rules

rule0_y0 = Real('rule0_y0')
s.add(rule0_y0 >= 0)
rule1_y0 = Real('rule1_y0')
s.add(rule1_y0 >= 0)
rule2_y0 = Real('rule2_y0')
s.add(rule2_y0 >= 0)
rule3_y0 = Real('rule3_y0')
s.add(rule3_y0 >= 0)
rule4_y0 = Real('rule4_y0')
s.add(rule4_y0 >= 0)
rule5_y0 = Real('rule5_y0')
s.add(rule5_y0 >= 0)
rule6_y0 = Real('rule6_y0')
s.add(rule6_y0 >= 0)
rule7_y0 = Real('rule7_y0')
s.add(rule7_y0 >= 0)
rule8_y0 = Real('rule8_y0')
s.add(rule8_y0 >= 0)
rule9_y0 = Real('rule9_y0')
s.add(rule9_y0 >= 0)
rule10_y0 = Real('rule10_y0')
s.add(rule10_y0 >= 0)
rule11_y0 = Real('rule11_y0')
s.add(rule11_y0 >= 0)
rule12_y0 = Real('rule12_y0')
s.add(rule12_y0 >= 0)
rule13_y0 = Real('rule13_y0')
s.add(rule13_y0 >= 0)






###################Step 2####################


#Flow equations for the locations

s.add(0 - rule0_y0 ==  loc0_x1 - loc0_y0)
s.add(0 - rule1_y0 ==  loc1_x1 - loc1_y0)
s.add(0 + rule0_y0 + rule1_y0 - rule2_y0 - rule3_y0 - rule6_y0 - rule10_y0 + rule10_y0 ==  locP0_x1 - locP0_y0)
s.add(0 + rule2_y0 + rule3_y0 - rule4_y0 - rule5_y0 - rule7_y0 - rule11_y0 + rule11_y0 ==  locP1_x1 - locP1_y0)
s.add(0 + rule4_y0 - rule8_y0 - rule12_y0 + rule12_y0 ==  locAC0_x1 - locAC0_y0)
s.add(0 + rule5_y0 - rule9_y0 - rule13_y0 + rule13_y0 ==  locAC1_x1 - locAC1_y0)
s.add(0 + rule6_y0 + rule7_y0 + rule8_y0 + rule9_y0 ==  locCR_x1 - locCR_y0)






##################Step 3########################


#Flow equations for the shared variables

s.add(0 + rule0_y0 == nsnt00_x1 - nsnt00_y0)
s.add(0 + rule1_y0 == nsnt01_x1 - nsnt01_y0)
s.add(0 + rule2_y0 == nsnt10_x1 - nsnt10_y0)
s.add(0 + rule3_y0 == nsnt11_x1 - nsnt11_y0)
s.add(0 + rule0_y0 + rule1_y0 == nsnt00plus01_x1 - nsnt00plus01_y0)
s.add(0 + rule6_y0 + rule7_y0 + rule8_y0 + rule9_y0 == nfaulty_x1 - nfaulty_y0)






####################Step 4########################


#Rule is fired implies rule is enabled

s.add(Implies( (rule0_y0 > 0), And(True, ) ))
s.add(Implies( (rule1_y0 > 0), And(True, ) ))
s.add(Implies( (rule2_y0 > 0), And(nsnt00plus01_y0>=N-T, 2*nsnt00_y0>=N-T+1, ) ))
s.add(Implies( (rule3_y0 > 0), And(nsnt00plus01_y0>=N-T, 2*nsnt01_y0>=N-T+1, ) ))
s.add(Implies( (rule4_y0 > 0), And(2*nsnt10_y0>=N+1, ) ))
s.add(Implies( (rule5_y0 > 0), And(2*nsnt11_y0>=N+1, ) ))
s.add(Implies( (rule6_y0 > 0), And(nfaulty_y0<F, ) ))
s.add(Implies( (rule7_y0 > 0), And(nfaulty_y0<F, ) ))
s.add(Implies( (rule8_y0 > 0), And(nfaulty_y0<F, ) ))
s.add(Implies( (rule9_y0 > 0), And(nfaulty_y0<F, ) ))
s.add(Implies( (rule10_y0 > 0), And(True, ) ))
s.add(Implies( (rule11_y0 > 0), And(True, ) ))
s.add(Implies( (rule12_y0 > 0), And(True, ) ))
s.add(Implies( (rule13_y0 > 0), And(True, ) ))

##################Step 5########################


#Ensuring that at most one rule is fired alternating configurations y0 and x0, if a fall condition is present

s.add((nfaulty_x1<F) == (nfaulty_y0<F))
s.add(Implies(And((nfaulty_x1<F), Not(nfaulty_y0<F)), Or((rule0_y0 == 0), (rule0_y0 == 1))))
s.add(Implies(And((nfaulty_x1<F), Not(nfaulty_y0<F)), Or((rule1_y0 == 0), (rule1_y0 == 1))))
s.add(Implies(And((nfaulty_x1<F), Not(nfaulty_y0<F)), Or((rule2_y0 == 0), (rule2_y0 == 1))))
s.add(Implies(And((nfaulty_x1<F), Not(nfaulty_y0<F)), Or((rule3_y0 == 0), (rule3_y0 == 1))))
s.add(Implies(And((nfaulty_x1<F), Not(nfaulty_y0<F)), Or((rule4_y0 == 0), (rule4_y0 == 1))))
s.add(Implies(And((nfaulty_x1<F), Not(nfaulty_y0<F)), Or((rule5_y0 == 0), (rule5_y0 == 1))))
s.add(Implies(And((nfaulty_x1<F), Not(nfaulty_y0<F)), Or((rule6_y0 == 0), (rule6_y0 == 1))))
s.add(Implies(And((nfaulty_x1<F), Not(nfaulty_y0<F)), Or((rule7_y0 == 0), (rule7_y0 == 1))))
s.add(Implies(And((nfaulty_x1<F), Not(nfaulty_y0<F)), Or((rule8_y0 == 0), (rule8_y0 == 1))))
s.add(Implies(And((nfaulty_x1<F), Not(nfaulty_y0<F)), Or((rule9_y0 == 0), (rule9_y0 == 1))))
s.add(Implies(And((nfaulty_x1<F), Not(nfaulty_y0<F)), Or((rule10_y0 == 0), (rule10_y0 == 1))))
s.add(Implies(And((nfaulty_x1<F), Not(nfaulty_y0<F)), Or((rule11_y0 == 0), (rule11_y0 == 1))))
s.add(Implies(And((nfaulty_x1<F), Not(nfaulty_y0<F)), Or((rule12_y0 == 0), (rule12_y0 == 1))))
s.add(Implies(And((nfaulty_x1<F), Not(nfaulty_y0<F)), Or((rule13_y0 == 0), (rule13_y0 == 1))))
s.add(Implies(And((nfaulty_x1<F), Not(nfaulty_y0<F)), rule0_y0+rule1_y0+rule2_y0+rule3_y0+rule4_y0+rule5_y0+rule6_y0+rule7_y0+rule8_y0+rule9_y0+rule10_y0+rule11_y0+rule12_y0+rule13_y0 <= 1))


####################################################################################

#Creating constraints for a run between the y1th and x2th configurations

################Step 1#################


#Creating many copies of variables for rules

rule0_y1 = Real('rule0_y1')
s.add(rule0_y1 >= 0)
rule1_y1 = Real('rule1_y1')
s.add(rule1_y1 >= 0)
rule2_y1 = Real('rule2_y1')
s.add(rule2_y1 >= 0)
rule3_y1 = Real('rule3_y1')
s.add(rule3_y1 >= 0)
rule4_y1 = Real('rule4_y1')
s.add(rule4_y1 >= 0)
rule5_y1 = Real('rule5_y1')
s.add(rule5_y1 >= 0)
rule6_y1 = Real('rule6_y1')
s.add(rule6_y1 >= 0)
rule7_y1 = Real('rule7_y1')
s.add(rule7_y1 >= 0)
rule8_y1 = Real('rule8_y1')
s.add(rule8_y1 >= 0)
rule9_y1 = Real('rule9_y1')
s.add(rule9_y1 >= 0)
rule10_y1 = Real('rule10_y1')
s.add(rule10_y1 >= 0)
rule11_y1 = Real('rule11_y1')
s.add(rule11_y1 >= 0)
rule12_y1 = Real('rule12_y1')
s.add(rule12_y1 >= 0)
rule13_y1 = Real('rule13_y1')
s.add(rule13_y1 >= 0)






###################Step 2####################


#Flow equations for the locations

s.add(0 - rule0_y1 ==  loc0_x2 - loc0_y1)
s.add(0 - rule1_y1 ==  loc1_x2 - loc1_y1)
s.add(0 + rule0_y1 + rule1_y1 - rule2_y1 - rule3_y1 - rule6_y1 - rule10_y1 + rule10_y1 ==  locP0_x2 - locP0_y1)
s.add(0 + rule2_y1 + rule3_y1 - rule4_y1 - rule5_y1 - rule7_y1 - rule11_y1 + rule11_y1 ==  locP1_x2 - locP1_y1)
s.add(0 + rule4_y1 - rule8_y1 - rule12_y1 + rule12_y1 ==  locAC0_x2 - locAC0_y1)
s.add(0 + rule5_y1 - rule9_y1 - rule13_y1 + rule13_y1 ==  locAC1_x2 - locAC1_y1)
s.add(0 + rule6_y1 + rule7_y1 + rule8_y1 + rule9_y1 ==  locCR_x2 - locCR_y1)






##################Step 3########################


#Flow equations for the shared variables

s.add(0 + rule0_y1 == nsnt00_x2 - nsnt00_y1)
s.add(0 + rule1_y1 == nsnt01_x2 - nsnt01_y1)
s.add(0 + rule2_y1 == nsnt10_x2 - nsnt10_y1)
s.add(0 + rule3_y1 == nsnt11_x2 - nsnt11_y1)
s.add(0 + rule0_y1 + rule1_y1 == nsnt00plus01_x2 - nsnt00plus01_y1)
s.add(0 + rule6_y1 + rule7_y1 + rule8_y1 + rule9_y1 == nfaulty_x2 - nfaulty_y1)






####################Step 4########################


#Rule is fired implies rule is enabled

s.add(Implies( (rule0_y1 > 0), And(True, ) ))
s.add(Implies( (rule1_y1 > 0), And(True, ) ))
s.add(Implies( (rule2_y1 > 0), And(nsnt00plus01_y1>=N-T, 2*nsnt00_y1>=N-T+1, ) ))
s.add(Implies( (rule3_y1 > 0), And(nsnt00plus01_y1>=N-T, 2*nsnt01_y1>=N-T+1, ) ))
s.add(Implies( (rule4_y1 > 0), And(2*nsnt10_y1>=N+1, ) ))
s.add(Implies( (rule5_y1 > 0), And(2*nsnt11_y1>=N+1, ) ))
s.add(Implies( (rule6_y1 > 0), And(nfaulty_y1<F, ) ))
s.add(Implies( (rule7_y1 > 0), And(nfaulty_y1<F, ) ))
s.add(Implies( (rule8_y1 > 0), And(nfaulty_y1<F, ) ))
s.add(Implies( (rule9_y1 > 0), And(nfaulty_y1<F, ) ))
s.add(Implies( (rule10_y1 > 0), And(True, ) ))
s.add(Implies( (rule11_y1 > 0), And(True, ) ))
s.add(Implies( (rule12_y1 > 0), And(True, ) ))
s.add(Implies( (rule13_y1 > 0), And(True, ) ))

##################Step 5########################


#Ensuring that at most one rule is fired alternating configurations y1 and x1, if a fall condition is present

s.add((nfaulty_x2<F) == (nfaulty_y1<F))
s.add(Implies(And((nfaulty_x2<F), Not(nfaulty_y1<F)), Or((rule0_y1 == 0), (rule0_y1 == 1))))
s.add(Implies(And((nfaulty_x2<F), Not(nfaulty_y1<F)), Or((rule1_y1 == 0), (rule1_y1 == 1))))
s.add(Implies(And((nfaulty_x2<F), Not(nfaulty_y1<F)), Or((rule2_y1 == 0), (rule2_y1 == 1))))
s.add(Implies(And((nfaulty_x2<F), Not(nfaulty_y1<F)), Or((rule3_y1 == 0), (rule3_y1 == 1))))
s.add(Implies(And((nfaulty_x2<F), Not(nfaulty_y1<F)), Or((rule4_y1 == 0), (rule4_y1 == 1))))
s.add(Implies(And((nfaulty_x2<F), Not(nfaulty_y1<F)), Or((rule5_y1 == 0), (rule5_y1 == 1))))
s.add(Implies(And((nfaulty_x2<F), Not(nfaulty_y1<F)), Or((rule6_y1 == 0), (rule6_y1 == 1))))
s.add(Implies(And((nfaulty_x2<F), Not(nfaulty_y1<F)), Or((rule7_y1 == 0), (rule7_y1 == 1))))
s.add(Implies(And((nfaulty_x2<F), Not(nfaulty_y1<F)), Or((rule8_y1 == 0), (rule8_y1 == 1))))
s.add(Implies(And((nfaulty_x2<F), Not(nfaulty_y1<F)), Or((rule9_y1 == 0), (rule9_y1 == 1))))
s.add(Implies(And((nfaulty_x2<F), Not(nfaulty_y1<F)), Or((rule10_y1 == 0), (rule10_y1 == 1))))
s.add(Implies(And((nfaulty_x2<F), Not(nfaulty_y1<F)), Or((rule11_y1 == 0), (rule11_y1 == 1))))
s.add(Implies(And((nfaulty_x2<F), Not(nfaulty_y1<F)), Or((rule12_y1 == 0), (rule12_y1 == 1))))
s.add(Implies(And((nfaulty_x2<F), Not(nfaulty_y1<F)), Or((rule13_y1 == 0), (rule13_y1 == 1))))
s.add(Implies(And((nfaulty_x2<F), Not(nfaulty_y1<F)), rule0_y1+rule1_y1+rule2_y1+rule3_y1+rule4_y1+rule5_y1+rule6_y1+rule7_y1+rule8_y1+rule9_y1+rule10_y1+rule11_y1+rule12_y1+rule13_y1 <= 1))


####################################################################################

#Creating constraints for a run between the y2th and x3th configurations

################Step 1#################


#Creating many copies of variables for rules

rule0_y2 = Real('rule0_y2')
s.add(rule0_y2 >= 0)
rule1_y2 = Real('rule1_y2')
s.add(rule1_y2 >= 0)
rule2_y2 = Real('rule2_y2')
s.add(rule2_y2 >= 0)
rule3_y2 = Real('rule3_y2')
s.add(rule3_y2 >= 0)
rule4_y2 = Real('rule4_y2')
s.add(rule4_y2 >= 0)
rule5_y2 = Real('rule5_y2')
s.add(rule5_y2 >= 0)
rule6_y2 = Real('rule6_y2')
s.add(rule6_y2 >= 0)
rule7_y2 = Real('rule7_y2')
s.add(rule7_y2 >= 0)
rule8_y2 = Real('rule8_y2')
s.add(rule8_y2 >= 0)
rule9_y2 = Real('rule9_y2')
s.add(rule9_y2 >= 0)
rule10_y2 = Real('rule10_y2')
s.add(rule10_y2 >= 0)
rule11_y2 = Real('rule11_y2')
s.add(rule11_y2 >= 0)
rule12_y2 = Real('rule12_y2')
s.add(rule12_y2 >= 0)
rule13_y2 = Real('rule13_y2')
s.add(rule13_y2 >= 0)






###################Step 2####################


#Flow equations for the locations

s.add(0 - rule0_y2 ==  loc0_x3 - loc0_y2)
s.add(0 - rule1_y2 ==  loc1_x3 - loc1_y2)
s.add(0 + rule0_y2 + rule1_y2 - rule2_y2 - rule3_y2 - rule6_y2 - rule10_y2 + rule10_y2 ==  locP0_x3 - locP0_y2)
s.add(0 + rule2_y2 + rule3_y2 - rule4_y2 - rule5_y2 - rule7_y2 - rule11_y2 + rule11_y2 ==  locP1_x3 - locP1_y2)
s.add(0 + rule4_y2 - rule8_y2 - rule12_y2 + rule12_y2 ==  locAC0_x3 - locAC0_y2)
s.add(0 + rule5_y2 - rule9_y2 - rule13_y2 + rule13_y2 ==  locAC1_x3 - locAC1_y2)
s.add(0 + rule6_y2 + rule7_y2 + rule8_y2 + rule9_y2 ==  locCR_x3 - locCR_y2)






##################Step 3########################


#Flow equations for the shared variables

s.add(0 + rule0_y2 == nsnt00_x3 - nsnt00_y2)
s.add(0 + rule1_y2 == nsnt01_x3 - nsnt01_y2)
s.add(0 + rule2_y2 == nsnt10_x3 - nsnt10_y2)
s.add(0 + rule3_y2 == nsnt11_x3 - nsnt11_y2)
s.add(0 + rule0_y2 + rule1_y2 == nsnt00plus01_x3 - nsnt00plus01_y2)
s.add(0 + rule6_y2 + rule7_y2 + rule8_y2 + rule9_y2 == nfaulty_x3 - nfaulty_y2)






####################Step 4########################


#Rule is fired implies rule is enabled

s.add(Implies( (rule0_y2 > 0), And(True, ) ))
s.add(Implies( (rule1_y2 > 0), And(True, ) ))
s.add(Implies( (rule2_y2 > 0), And(nsnt00plus01_y2>=N-T, 2*nsnt00_y2>=N-T+1, ) ))
s.add(Implies( (rule3_y2 > 0), And(nsnt00plus01_y2>=N-T, 2*nsnt01_y2>=N-T+1, ) ))
s.add(Implies( (rule4_y2 > 0), And(2*nsnt10_y2>=N+1, ) ))
s.add(Implies( (rule5_y2 > 0), And(2*nsnt11_y2>=N+1, ) ))
s.add(Implies( (rule6_y2 > 0), And(nfaulty_y2<F, ) ))
s.add(Implies( (rule7_y2 > 0), And(nfaulty_y2<F, ) ))
s.add(Implies( (rule8_y2 > 0), And(nfaulty_y2<F, ) ))
s.add(Implies( (rule9_y2 > 0), And(nfaulty_y2<F, ) ))
s.add(Implies( (rule10_y2 > 0), And(True, ) ))
s.add(Implies( (rule11_y2 > 0), And(True, ) ))
s.add(Implies( (rule12_y2 > 0), And(True, ) ))
s.add(Implies( (rule13_y2 > 0), And(True, ) ))

##################Step 5########################


#Ensuring that at most one rule is fired alternating configurations y2 and x2, if a fall condition is present

s.add((nfaulty_x3<F) == (nfaulty_y2<F))
s.add(Implies(And((nfaulty_x3<F), Not(nfaulty_y2<F)), Or((rule0_y2 == 0), (rule0_y2 == 1))))
s.add(Implies(And((nfaulty_x3<F), Not(nfaulty_y2<F)), Or((rule1_y2 == 0), (rule1_y2 == 1))))
s.add(Implies(And((nfaulty_x3<F), Not(nfaulty_y2<F)), Or((rule2_y2 == 0), (rule2_y2 == 1))))
s.add(Implies(And((nfaulty_x3<F), Not(nfaulty_y2<F)), Or((rule3_y2 == 0), (rule3_y2 == 1))))
s.add(Implies(And((nfaulty_x3<F), Not(nfaulty_y2<F)), Or((rule4_y2 == 0), (rule4_y2 == 1))))
s.add(Implies(And((nfaulty_x3<F), Not(nfaulty_y2<F)), Or((rule5_y2 == 0), (rule5_y2 == 1))))
s.add(Implies(And((nfaulty_x3<F), Not(nfaulty_y2<F)), Or((rule6_y2 == 0), (rule6_y2 == 1))))
s.add(Implies(And((nfaulty_x3<F), Not(nfaulty_y2<F)), Or((rule7_y2 == 0), (rule7_y2 == 1))))
s.add(Implies(And((nfaulty_x3<F), Not(nfaulty_y2<F)), Or((rule8_y2 == 0), (rule8_y2 == 1))))
s.add(Implies(And((nfaulty_x3<F), Not(nfaulty_y2<F)), Or((rule9_y2 == 0), (rule9_y2 == 1))))
s.add(Implies(And((nfaulty_x3<F), Not(nfaulty_y2<F)), Or((rule10_y2 == 0), (rule10_y2 == 1))))
s.add(Implies(And((nfaulty_x3<F), Not(nfaulty_y2<F)), Or((rule11_y2 == 0), (rule11_y2 == 1))))
s.add(Implies(And((nfaulty_x3<F), Not(nfaulty_y2<F)), Or((rule12_y2 == 0), (rule12_y2 == 1))))
s.add(Implies(And((nfaulty_x3<F), Not(nfaulty_y2<F)), Or((rule13_y2 == 0), (rule13_y2 == 1))))
s.add(Implies(And((nfaulty_x3<F), Not(nfaulty_y2<F)), rule0_y2+rule1_y2+rule2_y2+rule3_y2+rule4_y2+rule5_y2+rule6_y2+rule7_y2+rule8_y2+rule9_y2+rule10_y2+rule11_y2+rule12_y2+rule13_y2 <= 1))


####################################################################################

#Creating constraints for a run between the y3th and x4th configurations

################Step 1#################


#Creating many copies of variables for rules

rule0_y3 = Real('rule0_y3')
s.add(rule0_y3 >= 0)
rule1_y3 = Real('rule1_y3')
s.add(rule1_y3 >= 0)
rule2_y3 = Real('rule2_y3')
s.add(rule2_y3 >= 0)
rule3_y3 = Real('rule3_y3')
s.add(rule3_y3 >= 0)
rule4_y3 = Real('rule4_y3')
s.add(rule4_y3 >= 0)
rule5_y3 = Real('rule5_y3')
s.add(rule5_y3 >= 0)
rule6_y3 = Real('rule6_y3')
s.add(rule6_y3 >= 0)
rule7_y3 = Real('rule7_y3')
s.add(rule7_y3 >= 0)
rule8_y3 = Real('rule8_y3')
s.add(rule8_y3 >= 0)
rule9_y3 = Real('rule9_y3')
s.add(rule9_y3 >= 0)
rule10_y3 = Real('rule10_y3')
s.add(rule10_y3 >= 0)
rule11_y3 = Real('rule11_y3')
s.add(rule11_y3 >= 0)
rule12_y3 = Real('rule12_y3')
s.add(rule12_y3 >= 0)
rule13_y3 = Real('rule13_y3')
s.add(rule13_y3 >= 0)






###################Step 2####################


#Flow equations for the locations

s.add(0 - rule0_y3 ==  loc0_x4 - loc0_y3)
s.add(0 - rule1_y3 ==  loc1_x4 - loc1_y3)
s.add(0 + rule0_y3 + rule1_y3 - rule2_y3 - rule3_y3 - rule6_y3 - rule10_y3 + rule10_y3 ==  locP0_x4 - locP0_y3)
s.add(0 + rule2_y3 + rule3_y3 - rule4_y3 - rule5_y3 - rule7_y3 - rule11_y3 + rule11_y3 ==  locP1_x4 - locP1_y3)
s.add(0 + rule4_y3 - rule8_y3 - rule12_y3 + rule12_y3 ==  locAC0_x4 - locAC0_y3)
s.add(0 + rule5_y3 - rule9_y3 - rule13_y3 + rule13_y3 ==  locAC1_x4 - locAC1_y3)
s.add(0 + rule6_y3 + rule7_y3 + rule8_y3 + rule9_y3 ==  locCR_x4 - locCR_y3)






##################Step 3########################


#Flow equations for the shared variables

s.add(0 + rule0_y3 == nsnt00_x4 - nsnt00_y3)
s.add(0 + rule1_y3 == nsnt01_x4 - nsnt01_y3)
s.add(0 + rule2_y3 == nsnt10_x4 - nsnt10_y3)
s.add(0 + rule3_y3 == nsnt11_x4 - nsnt11_y3)
s.add(0 + rule0_y3 + rule1_y3 == nsnt00plus01_x4 - nsnt00plus01_y3)
s.add(0 + rule6_y3 + rule7_y3 + rule8_y3 + rule9_y3 == nfaulty_x4 - nfaulty_y3)






####################Step 4########################


#Rule is fired implies rule is enabled

s.add(Implies( (rule0_y3 > 0), And(True, ) ))
s.add(Implies( (rule1_y3 > 0), And(True, ) ))
s.add(Implies( (rule2_y3 > 0), And(nsnt00plus01_y3>=N-T, 2*nsnt00_y3>=N-T+1, ) ))
s.add(Implies( (rule3_y3 > 0), And(nsnt00plus01_y3>=N-T, 2*nsnt01_y3>=N-T+1, ) ))
s.add(Implies( (rule4_y3 > 0), And(2*nsnt10_y3>=N+1, ) ))
s.add(Implies( (rule5_y3 > 0), And(2*nsnt11_y3>=N+1, ) ))
s.add(Implies( (rule6_y3 > 0), And(nfaulty_y3<F, ) ))
s.add(Implies( (rule7_y3 > 0), And(nfaulty_y3<F, ) ))
s.add(Implies( (rule8_y3 > 0), And(nfaulty_y3<F, ) ))
s.add(Implies( (rule9_y3 > 0), And(nfaulty_y3<F, ) ))
s.add(Implies( (rule10_y3 > 0), And(True, ) ))
s.add(Implies( (rule11_y3 > 0), And(True, ) ))
s.add(Implies( (rule12_y3 > 0), And(True, ) ))
s.add(Implies( (rule13_y3 > 0), And(True, ) ))

##################Step 5########################


#Ensuring that at most one rule is fired alternating configurations y3 and x3, if a fall condition is present

s.add((nfaulty_x4<F) == (nfaulty_y3<F))
s.add(Implies(And((nfaulty_x4<F), Not(nfaulty_y3<F)), Or((rule0_y3 == 0), (rule0_y3 == 1))))
s.add(Implies(And((nfaulty_x4<F), Not(nfaulty_y3<F)), Or((rule1_y3 == 0), (rule1_y3 == 1))))
s.add(Implies(And((nfaulty_x4<F), Not(nfaulty_y3<F)), Or((rule2_y3 == 0), (rule2_y3 == 1))))
s.add(Implies(And((nfaulty_x4<F), Not(nfaulty_y3<F)), Or((rule3_y3 == 0), (rule3_y3 == 1))))
s.add(Implies(And((nfaulty_x4<F), Not(nfaulty_y3<F)), Or((rule4_y3 == 0), (rule4_y3 == 1))))
s.add(Implies(And((nfaulty_x4<F), Not(nfaulty_y3<F)), Or((rule5_y3 == 0), (rule5_y3 == 1))))
s.add(Implies(And((nfaulty_x4<F), Not(nfaulty_y3<F)), Or((rule6_y3 == 0), (rule6_y3 == 1))))
s.add(Implies(And((nfaulty_x4<F), Not(nfaulty_y3<F)), Or((rule7_y3 == 0), (rule7_y3 == 1))))
s.add(Implies(And((nfaulty_x4<F), Not(nfaulty_y3<F)), Or((rule8_y3 == 0), (rule8_y3 == 1))))
s.add(Implies(And((nfaulty_x4<F), Not(nfaulty_y3<F)), Or((rule9_y3 == 0), (rule9_y3 == 1))))
s.add(Implies(And((nfaulty_x4<F), Not(nfaulty_y3<F)), Or((rule10_y3 == 0), (rule10_y3 == 1))))
s.add(Implies(And((nfaulty_x4<F), Not(nfaulty_y3<F)), Or((rule11_y3 == 0), (rule11_y3 == 1))))
s.add(Implies(And((nfaulty_x4<F), Not(nfaulty_y3<F)), Or((rule12_y3 == 0), (rule12_y3 == 1))))
s.add(Implies(And((nfaulty_x4<F), Not(nfaulty_y3<F)), Or((rule13_y3 == 0), (rule13_y3 == 1))))
s.add(Implies(And((nfaulty_x4<F), Not(nfaulty_y3<F)), rule0_y3+rule1_y3+rule2_y3+rule3_y3+rule4_y3+rule5_y3+rule6_y3+rule7_y3+rule8_y3+rule9_y3+rule10_y3+rule11_y3+rule12_y3+rule13_y3 <= 1))


####################################################################################

#Creating constraints for a run between the y4th and x5th configurations

################Step 1#################


#Creating many copies of variables for rules

rule0_y4 = Real('rule0_y4')
s.add(rule0_y4 >= 0)
rule1_y4 = Real('rule1_y4')
s.add(rule1_y4 >= 0)
rule2_y4 = Real('rule2_y4')
s.add(rule2_y4 >= 0)
rule3_y4 = Real('rule3_y4')
s.add(rule3_y4 >= 0)
rule4_y4 = Real('rule4_y4')
s.add(rule4_y4 >= 0)
rule5_y4 = Real('rule5_y4')
s.add(rule5_y4 >= 0)
rule6_y4 = Real('rule6_y4')
s.add(rule6_y4 >= 0)
rule7_y4 = Real('rule7_y4')
s.add(rule7_y4 >= 0)
rule8_y4 = Real('rule8_y4')
s.add(rule8_y4 >= 0)
rule9_y4 = Real('rule9_y4')
s.add(rule9_y4 >= 0)
rule10_y4 = Real('rule10_y4')
s.add(rule10_y4 >= 0)
rule11_y4 = Real('rule11_y4')
s.add(rule11_y4 >= 0)
rule12_y4 = Real('rule12_y4')
s.add(rule12_y4 >= 0)
rule13_y4 = Real('rule13_y4')
s.add(rule13_y4 >= 0)






###################Step 2####################


#Flow equations for the locations

s.add(0 - rule0_y4 ==  loc0_x5 - loc0_y4)
s.add(0 - rule1_y4 ==  loc1_x5 - loc1_y4)
s.add(0 + rule0_y4 + rule1_y4 - rule2_y4 - rule3_y4 - rule6_y4 - rule10_y4 + rule10_y4 ==  locP0_x5 - locP0_y4)
s.add(0 + rule2_y4 + rule3_y4 - rule4_y4 - rule5_y4 - rule7_y4 - rule11_y4 + rule11_y4 ==  locP1_x5 - locP1_y4)
s.add(0 + rule4_y4 - rule8_y4 - rule12_y4 + rule12_y4 ==  locAC0_x5 - locAC0_y4)
s.add(0 + rule5_y4 - rule9_y4 - rule13_y4 + rule13_y4 ==  locAC1_x5 - locAC1_y4)
s.add(0 + rule6_y4 + rule7_y4 + rule8_y4 + rule9_y4 ==  locCR_x5 - locCR_y4)






##################Step 3########################


#Flow equations for the shared variables

s.add(0 + rule0_y4 == nsnt00_x5 - nsnt00_y4)
s.add(0 + rule1_y4 == nsnt01_x5 - nsnt01_y4)
s.add(0 + rule2_y4 == nsnt10_x5 - nsnt10_y4)
s.add(0 + rule3_y4 == nsnt11_x5 - nsnt11_y4)
s.add(0 + rule0_y4 + rule1_y4 == nsnt00plus01_x5 - nsnt00plus01_y4)
s.add(0 + rule6_y4 + rule7_y4 + rule8_y4 + rule9_y4 == nfaulty_x5 - nfaulty_y4)






####################Step 4########################


#Rule is fired implies rule is enabled

s.add(Implies( (rule0_y4 > 0), And(True, ) ))
s.add(Implies( (rule1_y4 > 0), And(True, ) ))
s.add(Implies( (rule2_y4 > 0), And(nsnt00plus01_y4>=N-T, 2*nsnt00_y4>=N-T+1, ) ))
s.add(Implies( (rule3_y4 > 0), And(nsnt00plus01_y4>=N-T, 2*nsnt01_y4>=N-T+1, ) ))
s.add(Implies( (rule4_y4 > 0), And(2*nsnt10_y4>=N+1, ) ))
s.add(Implies( (rule5_y4 > 0), And(2*nsnt11_y4>=N+1, ) ))
s.add(Implies( (rule6_y4 > 0), And(nfaulty_y4<F, ) ))
s.add(Implies( (rule7_y4 > 0), And(nfaulty_y4<F, ) ))
s.add(Implies( (rule8_y4 > 0), And(nfaulty_y4<F, ) ))
s.add(Implies( (rule9_y4 > 0), And(nfaulty_y4<F, ) ))
s.add(Implies( (rule10_y4 > 0), And(True, ) ))
s.add(Implies( (rule11_y4 > 0), And(True, ) ))
s.add(Implies( (rule12_y4 > 0), And(True, ) ))
s.add(Implies( (rule13_y4 > 0), And(True, ) ))

##################Step 5########################


#Ensuring that at most one rule is fired alternating configurations y4 and x4, if a fall condition is present

s.add((nfaulty_x5<F) == (nfaulty_y4<F))
s.add(Implies(And((nfaulty_x5<F), Not(nfaulty_y4<F)), Or((rule0_y4 == 0), (rule0_y4 == 1))))
s.add(Implies(And((nfaulty_x5<F), Not(nfaulty_y4<F)), Or((rule1_y4 == 0), (rule1_y4 == 1))))
s.add(Implies(And((nfaulty_x5<F), Not(nfaulty_y4<F)), Or((rule2_y4 == 0), (rule2_y4 == 1))))
s.add(Implies(And((nfaulty_x5<F), Not(nfaulty_y4<F)), Or((rule3_y4 == 0), (rule3_y4 == 1))))
s.add(Implies(And((nfaulty_x5<F), Not(nfaulty_y4<F)), Or((rule4_y4 == 0), (rule4_y4 == 1))))
s.add(Implies(And((nfaulty_x5<F), Not(nfaulty_y4<F)), Or((rule5_y4 == 0), (rule5_y4 == 1))))
s.add(Implies(And((nfaulty_x5<F), Not(nfaulty_y4<F)), Or((rule6_y4 == 0), (rule6_y4 == 1))))
s.add(Implies(And((nfaulty_x5<F), Not(nfaulty_y4<F)), Or((rule7_y4 == 0), (rule7_y4 == 1))))
s.add(Implies(And((nfaulty_x5<F), Not(nfaulty_y4<F)), Or((rule8_y4 == 0), (rule8_y4 == 1))))
s.add(Implies(And((nfaulty_x5<F), Not(nfaulty_y4<F)), Or((rule9_y4 == 0), (rule9_y4 == 1))))
s.add(Implies(And((nfaulty_x5<F), Not(nfaulty_y4<F)), Or((rule10_y4 == 0), (rule10_y4 == 1))))
s.add(Implies(And((nfaulty_x5<F), Not(nfaulty_y4<F)), Or((rule11_y4 == 0), (rule11_y4 == 1))))
s.add(Implies(And((nfaulty_x5<F), Not(nfaulty_y4<F)), Or((rule12_y4 == 0), (rule12_y4 == 1))))
s.add(Implies(And((nfaulty_x5<F), Not(nfaulty_y4<F)), Or((rule13_y4 == 0), (rule13_y4 == 1))))
s.add(Implies(And((nfaulty_x5<F), Not(nfaulty_y4<F)), rule0_y4+rule1_y4+rule2_y4+rule3_y4+rule4_y4+rule5_y4+rule6_y4+rule7_y4+rule8_y4+rule9_y4+rule10_y4+rule11_y4+rule12_y4+rule13_y4 <= 1))


####################################################################################

#Creating constraints for a run between the y5th and x6th configurations

################Step 1#################


#Creating many copies of variables for rules

rule0_y5 = Real('rule0_y5')
s.add(rule0_y5 >= 0)
rule1_y5 = Real('rule1_y5')
s.add(rule1_y5 >= 0)
rule2_y5 = Real('rule2_y5')
s.add(rule2_y5 >= 0)
rule3_y5 = Real('rule3_y5')
s.add(rule3_y5 >= 0)
rule4_y5 = Real('rule4_y5')
s.add(rule4_y5 >= 0)
rule5_y5 = Real('rule5_y5')
s.add(rule5_y5 >= 0)
rule6_y5 = Real('rule6_y5')
s.add(rule6_y5 >= 0)
rule7_y5 = Real('rule7_y5')
s.add(rule7_y5 >= 0)
rule8_y5 = Real('rule8_y5')
s.add(rule8_y5 >= 0)
rule9_y5 = Real('rule9_y5')
s.add(rule9_y5 >= 0)
rule10_y5 = Real('rule10_y5')
s.add(rule10_y5 >= 0)
rule11_y5 = Real('rule11_y5')
s.add(rule11_y5 >= 0)
rule12_y5 = Real('rule12_y5')
s.add(rule12_y5 >= 0)
rule13_y5 = Real('rule13_y5')
s.add(rule13_y5 >= 0)






###################Step 2####################


#Flow equations for the locations

s.add(0 - rule0_y5 ==  loc0_x6 - loc0_y5)
s.add(0 - rule1_y5 ==  loc1_x6 - loc1_y5)
s.add(0 + rule0_y5 + rule1_y5 - rule2_y5 - rule3_y5 - rule6_y5 - rule10_y5 + rule10_y5 ==  locP0_x6 - locP0_y5)
s.add(0 + rule2_y5 + rule3_y5 - rule4_y5 - rule5_y5 - rule7_y5 - rule11_y5 + rule11_y5 ==  locP1_x6 - locP1_y5)
s.add(0 + rule4_y5 - rule8_y5 - rule12_y5 + rule12_y5 ==  locAC0_x6 - locAC0_y5)
s.add(0 + rule5_y5 - rule9_y5 - rule13_y5 + rule13_y5 ==  locAC1_x6 - locAC1_y5)
s.add(0 + rule6_y5 + rule7_y5 + rule8_y5 + rule9_y5 ==  locCR_x6 - locCR_y5)






##################Step 3########################


#Flow equations for the shared variables

s.add(0 + rule0_y5 == nsnt00_x6 - nsnt00_y5)
s.add(0 + rule1_y5 == nsnt01_x6 - nsnt01_y5)
s.add(0 + rule2_y5 == nsnt10_x6 - nsnt10_y5)
s.add(0 + rule3_y5 == nsnt11_x6 - nsnt11_y5)
s.add(0 + rule0_y5 + rule1_y5 == nsnt00plus01_x6 - nsnt00plus01_y5)
s.add(0 + rule6_y5 + rule7_y5 + rule8_y5 + rule9_y5 == nfaulty_x6 - nfaulty_y5)






####################Step 4########################


#Rule is fired implies rule is enabled

s.add(Implies( (rule0_y5 > 0), And(True, ) ))
s.add(Implies( (rule1_y5 > 0), And(True, ) ))
s.add(Implies( (rule2_y5 > 0), And(nsnt00plus01_y5>=N-T, 2*nsnt00_y5>=N-T+1, ) ))
s.add(Implies( (rule3_y5 > 0), And(nsnt00plus01_y5>=N-T, 2*nsnt01_y5>=N-T+1, ) ))
s.add(Implies( (rule4_y5 > 0), And(2*nsnt10_y5>=N+1, ) ))
s.add(Implies( (rule5_y5 > 0), And(2*nsnt11_y5>=N+1, ) ))
s.add(Implies( (rule6_y5 > 0), And(nfaulty_y5<F, ) ))
s.add(Implies( (rule7_y5 > 0), And(nfaulty_y5<F, ) ))
s.add(Implies( (rule8_y5 > 0), And(nfaulty_y5<F, ) ))
s.add(Implies( (rule9_y5 > 0), And(nfaulty_y5<F, ) ))
s.add(Implies( (rule10_y5 > 0), And(True, ) ))
s.add(Implies( (rule11_y5 > 0), And(True, ) ))
s.add(Implies( (rule12_y5 > 0), And(True, ) ))
s.add(Implies( (rule13_y5 > 0), And(True, ) ))

##################Step 5########################


#Ensuring that at most one rule is fired alternating configurations y5 and x5, if a fall condition is present

s.add((nfaulty_x6<F) == (nfaulty_y5<F))
s.add(Implies(And((nfaulty_x6<F), Not(nfaulty_y5<F)), Or((rule0_y5 == 0), (rule0_y5 == 1))))
s.add(Implies(And((nfaulty_x6<F), Not(nfaulty_y5<F)), Or((rule1_y5 == 0), (rule1_y5 == 1))))
s.add(Implies(And((nfaulty_x6<F), Not(nfaulty_y5<F)), Or((rule2_y5 == 0), (rule2_y5 == 1))))
s.add(Implies(And((nfaulty_x6<F), Not(nfaulty_y5<F)), Or((rule3_y5 == 0), (rule3_y5 == 1))))
s.add(Implies(And((nfaulty_x6<F), Not(nfaulty_y5<F)), Or((rule4_y5 == 0), (rule4_y5 == 1))))
s.add(Implies(And((nfaulty_x6<F), Not(nfaulty_y5<F)), Or((rule5_y5 == 0), (rule5_y5 == 1))))
s.add(Implies(And((nfaulty_x6<F), Not(nfaulty_y5<F)), Or((rule6_y5 == 0), (rule6_y5 == 1))))
s.add(Implies(And((nfaulty_x6<F), Not(nfaulty_y5<F)), Or((rule7_y5 == 0), (rule7_y5 == 1))))
s.add(Implies(And((nfaulty_x6<F), Not(nfaulty_y5<F)), Or((rule8_y5 == 0), (rule8_y5 == 1))))
s.add(Implies(And((nfaulty_x6<F), Not(nfaulty_y5<F)), Or((rule9_y5 == 0), (rule9_y5 == 1))))
s.add(Implies(And((nfaulty_x6<F), Not(nfaulty_y5<F)), Or((rule10_y5 == 0), (rule10_y5 == 1))))
s.add(Implies(And((nfaulty_x6<F), Not(nfaulty_y5<F)), Or((rule11_y5 == 0), (rule11_y5 == 1))))
s.add(Implies(And((nfaulty_x6<F), Not(nfaulty_y5<F)), Or((rule12_y5 == 0), (rule12_y5 == 1))))
s.add(Implies(And((nfaulty_x6<F), Not(nfaulty_y5<F)), Or((rule13_y5 == 0), (rule13_y5 == 1))))
s.add(Implies(And((nfaulty_x6<F), Not(nfaulty_y5<F)), rule0_y5+rule1_y5+rule2_y5+rule3_y5+rule4_y5+rule5_y5+rule6_y5+rule7_y5+rule8_y5+rule9_y5+rule10_y5+rule11_y5+rule12_y5+rule13_y5 <= 1))


####################################################################################

#Creating constraints for a run between the y6th and x7th configurations

################Step 1#################


#Creating many copies of variables for rules

rule0_y6 = Real('rule0_y6')
s.add(rule0_y6 >= 0)
rule1_y6 = Real('rule1_y6')
s.add(rule1_y6 >= 0)
rule2_y6 = Real('rule2_y6')
s.add(rule2_y6 >= 0)
rule3_y6 = Real('rule3_y6')
s.add(rule3_y6 >= 0)
rule4_y6 = Real('rule4_y6')
s.add(rule4_y6 >= 0)
rule5_y6 = Real('rule5_y6')
s.add(rule5_y6 >= 0)
rule6_y6 = Real('rule6_y6')
s.add(rule6_y6 >= 0)
rule7_y6 = Real('rule7_y6')
s.add(rule7_y6 >= 0)
rule8_y6 = Real('rule8_y6')
s.add(rule8_y6 >= 0)
rule9_y6 = Real('rule9_y6')
s.add(rule9_y6 >= 0)
rule10_y6 = Real('rule10_y6')
s.add(rule10_y6 >= 0)
rule11_y6 = Real('rule11_y6')
s.add(rule11_y6 >= 0)
rule12_y6 = Real('rule12_y6')
s.add(rule12_y6 >= 0)
rule13_y6 = Real('rule13_y6')
s.add(rule13_y6 >= 0)






###################Step 2####################


#Flow equations for the locations

s.add(0 - rule0_y6 ==  loc0_x7 - loc0_y6)
s.add(0 - rule1_y6 ==  loc1_x7 - loc1_y6)
s.add(0 + rule0_y6 + rule1_y6 - rule2_y6 - rule3_y6 - rule6_y6 - rule10_y6 + rule10_y6 ==  locP0_x7 - locP0_y6)
s.add(0 + rule2_y6 + rule3_y6 - rule4_y6 - rule5_y6 - rule7_y6 - rule11_y6 + rule11_y6 ==  locP1_x7 - locP1_y6)
s.add(0 + rule4_y6 - rule8_y6 - rule12_y6 + rule12_y6 ==  locAC0_x7 - locAC0_y6)
s.add(0 + rule5_y6 - rule9_y6 - rule13_y6 + rule13_y6 ==  locAC1_x7 - locAC1_y6)
s.add(0 + rule6_y6 + rule7_y6 + rule8_y6 + rule9_y6 ==  locCR_x7 - locCR_y6)






##################Step 3########################


#Flow equations for the shared variables

s.add(0 + rule0_y6 == nsnt00_x7 - nsnt00_y6)
s.add(0 + rule1_y6 == nsnt01_x7 - nsnt01_y6)
s.add(0 + rule2_y6 == nsnt10_x7 - nsnt10_y6)
s.add(0 + rule3_y6 == nsnt11_x7 - nsnt11_y6)
s.add(0 + rule0_y6 + rule1_y6 == nsnt00plus01_x7 - nsnt00plus01_y6)
s.add(0 + rule6_y6 + rule7_y6 + rule8_y6 + rule9_y6 == nfaulty_x7 - nfaulty_y6)






####################Step 4########################


#Rule is fired implies rule is enabled

s.add(Implies( (rule0_y6 > 0), And(True, ) ))
s.add(Implies( (rule1_y6 > 0), And(True, ) ))
s.add(Implies( (rule2_y6 > 0), And(nsnt00plus01_y6>=N-T, 2*nsnt00_y6>=N-T+1, ) ))
s.add(Implies( (rule3_y6 > 0), And(nsnt00plus01_y6>=N-T, 2*nsnt01_y6>=N-T+1, ) ))
s.add(Implies( (rule4_y6 > 0), And(2*nsnt10_y6>=N+1, ) ))
s.add(Implies( (rule5_y6 > 0), And(2*nsnt11_y6>=N+1, ) ))
s.add(Implies( (rule6_y6 > 0), And(nfaulty_y6<F, ) ))
s.add(Implies( (rule7_y6 > 0), And(nfaulty_y6<F, ) ))
s.add(Implies( (rule8_y6 > 0), And(nfaulty_y6<F, ) ))
s.add(Implies( (rule9_y6 > 0), And(nfaulty_y6<F, ) ))
s.add(Implies( (rule10_y6 > 0), And(True, ) ))
s.add(Implies( (rule11_y6 > 0), And(True, ) ))
s.add(Implies( (rule12_y6 > 0), And(True, ) ))
s.add(Implies( (rule13_y6 > 0), And(True, ) ))

##################Step 5########################


#Ensuring that at most one rule is fired alternating configurations y6 and x6, if a fall condition is present

s.add((nfaulty_x7<F) == (nfaulty_y6<F))
s.add(Implies(And((nfaulty_x7<F), Not(nfaulty_y6<F)), Or((rule0_y6 == 0), (rule0_y6 == 1))))
s.add(Implies(And((nfaulty_x7<F), Not(nfaulty_y6<F)), Or((rule1_y6 == 0), (rule1_y6 == 1))))
s.add(Implies(And((nfaulty_x7<F), Not(nfaulty_y6<F)), Or((rule2_y6 == 0), (rule2_y6 == 1))))
s.add(Implies(And((nfaulty_x7<F), Not(nfaulty_y6<F)), Or((rule3_y6 == 0), (rule3_y6 == 1))))
s.add(Implies(And((nfaulty_x7<F), Not(nfaulty_y6<F)), Or((rule4_y6 == 0), (rule4_y6 == 1))))
s.add(Implies(And((nfaulty_x7<F), Not(nfaulty_y6<F)), Or((rule5_y6 == 0), (rule5_y6 == 1))))
s.add(Implies(And((nfaulty_x7<F), Not(nfaulty_y6<F)), Or((rule6_y6 == 0), (rule6_y6 == 1))))
s.add(Implies(And((nfaulty_x7<F), Not(nfaulty_y6<F)), Or((rule7_y6 == 0), (rule7_y6 == 1))))
s.add(Implies(And((nfaulty_x7<F), Not(nfaulty_y6<F)), Or((rule8_y6 == 0), (rule8_y6 == 1))))
s.add(Implies(And((nfaulty_x7<F), Not(nfaulty_y6<F)), Or((rule9_y6 == 0), (rule9_y6 == 1))))
s.add(Implies(And((nfaulty_x7<F), Not(nfaulty_y6<F)), Or((rule10_y6 == 0), (rule10_y6 == 1))))
s.add(Implies(And((nfaulty_x7<F), Not(nfaulty_y6<F)), Or((rule11_y6 == 0), (rule11_y6 == 1))))
s.add(Implies(And((nfaulty_x7<F), Not(nfaulty_y6<F)), Or((rule12_y6 == 0), (rule12_y6 == 1))))
s.add(Implies(And((nfaulty_x7<F), Not(nfaulty_y6<F)), Or((rule13_y6 == 0), (rule13_y6 == 1))))
s.add(Implies(And((nfaulty_x7<F), Not(nfaulty_y6<F)), rule0_y6+rule1_y6+rule2_y6+rule3_y6+rule4_y6+rule5_y6+rule6_y6+rule7_y6+rule8_y6+rule9_y6+rule10_y6+rule11_y6+rule12_y6+rule13_y6 <= 1))


#############Additional step for the final configuration#####################


###########Ensure that the last configuration satisfies the final condition#############

s.add(Or(locAC0_y7 != 0, locAC0_y7 != 0))






if s.check() == sat:

	print("Specification not satisfied")

else:

	print("Specification satisfied")
