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

s.add(N > 3 * T)
s.add(T >= F)
s.add(T >= 1)

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
locS0_x0 = Real('locS0_x0')
locS0_y0 = Real('locS0_y0')
s.add(locS0_x0 >= 0)
s.add(locS0_y0 >= 0)
locS1_x0 = Real('locS1_x0')
locS1_y0 = Real('locS1_y0')
s.add(locS1_x0 >= 0)
s.add(locS1_y0 >= 0)
locD0_x0 = Real('locD0_x0')
locD0_y0 = Real('locD0_y0')
s.add(locD0_x0 >= 0)
s.add(locD0_y0 >= 0)
locD1_x0 = Real('locD1_x0')
locD1_y0 = Real('locD1_y0')
s.add(locD1_x0 >= 0)
s.add(locD1_y0 >= 0)
locU0_x0 = Real('locU0_x0')
locU0_y0 = Real('locU0_y0')
s.add(locU0_x0 >= 0)
s.add(locU0_y0 >= 0)
locU1_x0 = Real('locU1_x0')
locU1_y0 = Real('locU1_y0')
s.add(locU1_x0 >= 0)
s.add(locU1_y0 >= 0)
locCR_x0 = Real('locCR_x0')
locCR_y0 = Real('locCR_y0')
s.add(locCR_x0 >= 0)
s.add(locCR_y0 >= 0)






#Creating many copies of shared variables

nsnt0_x0 = Real('nsnt0_x0')
nsnt0_y0 = Real('nsnt0_y0')
s.add(nsnt0_x0 >= 0)
s.add(nsnt0_y0 >= 0)
nsnt1_x0 = Real('nsnt1_x0')
nsnt1_y0 = Real('nsnt1_y0')
s.add(nsnt1_x0 >= 0)
s.add(nsnt1_y0 >= 0)
nsnt0CF_x0 = Real('nsnt0CF_x0')
nsnt0CF_y0 = Real('nsnt0CF_y0')
s.add(nsnt0CF_x0 >= 0)
s.add(nsnt0CF_y0 >= 0)
nsnt1CF_x0 = Real('nsnt1CF_x0')
nsnt1CF_y0 = Real('nsnt1CF_y0')
s.add(nsnt1CF_x0 >= 0)
s.add(nsnt1CF_y0 >= 0)
nsnt01_x0 = Real('nsnt01_x0')
nsnt01_y0 = Real('nsnt01_y0')
s.add(nsnt01_x0 >= 0)
s.add(nsnt01_y0 >= 0)
nsnt01CF_x0 = Real('nsnt01CF_x0')
nsnt01CF_y0 = Real('nsnt01CF_y0')
s.add(nsnt01CF_x0 >= 0)
s.add(nsnt01CF_y0 >= 0)
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
rule14_x0 = Real('rule14_x0')
s.add(rule14_x0 >= 0)
rule15_x0 = Real('rule15_x0')
s.add(rule15_x0 >= 0)
rule16_x0 = Real('rule16_x0')
s.add(rule16_x0 >= 0)
rule17_x0 = Real('rule17_x0')
s.add(rule17_x0 >= 0)
rule18_x0 = Real('rule18_x0')
s.add(rule18_x0 >= 0)
rule19_x0 = Real('rule19_x0')
s.add(rule19_x0 >= 0)
rule20_x0 = Real('rule20_x0')
s.add(rule20_x0 >= 0)
rule21_x0 = Real('rule21_x0')
s.add(rule21_x0 >= 0)
rule22_x0 = Real('rule22_x0')
s.add(rule22_x0 >= 0)
rule23_x0 = Real('rule23_x0')
s.add(rule23_x0 >= 0)
rule24_x0 = Real('rule24_x0')
s.add(rule24_x0 >= 0)
rule25_x0 = Real('rule25_x0')
s.add(rule25_x0 >= 0)
rule26_x0 = Real('rule26_x0')
s.add(rule26_x0 >= 0)
rule27_x0 = Real('rule27_x0')
s.add(rule27_x0 >= 0)
rule28_x0 = Real('rule28_x0')
s.add(rule28_x0 >= 0)
rule29_x0 = Real('rule29_x0')
s.add(rule29_x0 >= 0)






###################Step 2####################


#Flow equations for the locations

s.add(0 - rule0_x0 - rule1_x0 - rule14_x0 - rule22_x0 + rule22_x0 ==  loc0_y0 - loc0_x0)
s.add(0 - rule2_x0 - rule3_x0 - rule15_x0 - rule23_x0 + rule23_x0 ==  loc1_y0 - loc1_x0)
s.add(0 + rule0_x0 - rule4_x0 - rule6_x0 - rule8_x0 - rule10_x0 - rule12_x0 - rule16_x0 - rule24_x0 + rule24_x0 ==  locS0_y0 - locS0_x0)
s.add(0 + rule2_x0 - rule5_x0 - rule7_x0 - rule9_x0 - rule11_x0 - rule13_x0 - rule17_x0 - rule25_x0 + rule25_x0 ==  locS1_y0 - locS1_x0)
s.add(0 + rule4_x0 + rule5_x0 - rule18_x0 - rule26_x0 + rule26_x0 ==  locD0_y0 - locD0_x0)
s.add(0 + rule6_x0 + rule7_x0 - rule19_x0 - rule27_x0 + rule27_x0 ==  locD1_y0 - locD1_x0)
s.add(0 + rule8_x0 + rule9_x0 + rule12_x0 - rule20_x0 - rule28_x0 + rule28_x0 ==  locU0_y0 - locU0_x0)
s.add(0 + rule10_x0 + rule11_x0 + rule13_x0 - rule21_x0 - rule29_x0 + rule29_x0 ==  locU1_y0 - locU1_x0)
s.add(0 + rule1_x0 + rule3_x0 + rule14_x0 + rule15_x0 + rule16_x0 + rule17_x0 + rule18_x0 + rule19_x0 + rule20_x0 + rule21_x0 ==  locCR_y0 - locCR_x0)






##################Step 3########################


#Flow equations for the shared variables

s.add(0 + rule0_x0 == nsnt0_y0 - nsnt0_x0)
s.add(0 + rule2_x0 == nsnt1_y0 - nsnt1_x0)
s.add(0 + rule0_x0 + rule1_x0 == nsnt0CF_y0 - nsnt0CF_x0)
s.add(0 + rule2_x0 + rule3_x0 == nsnt1CF_y0 - nsnt1CF_x0)
s.add(0 + rule0_x0 + rule2_x0 == nsnt01_y0 - nsnt01_x0)
s.add(0 + rule0_x0 + rule1_x0 + rule2_x0 + rule3_x0 == nsnt01CF_y0 - nsnt01CF_x0)
s.add(0 + rule1_x0 + rule3_x0 + rule14_x0 + rule15_x0 + rule16_x0 + rule17_x0 + rule18_x0 + rule19_x0 + rule20_x0 + rule21_x0 == nfaulty_y0 - nfaulty_x0)






####################Step 4########################


#Rule is fired implies rule is enabled

s.add(Implies( (rule0_x0 > 0), And(True, ) ))
s.add(Implies( (rule1_x0 > 0), And(nfaulty_x0<F, ) ))
s.add(Implies( (rule2_x0 > 0), And(True, ) ))
s.add(Implies( (rule3_x0 > 0), And(nfaulty_x0<F, ) ))
s.add(Implies( (rule4_x0 > 0), And(nsnt0CF_x0>=N-T, ) ))
s.add(Implies( (rule5_x0 > 0), And(nsnt0CF_x0>=N-T, ) ))
s.add(Implies( (rule6_x0 > 0), And(nsnt1CF_x0>=N-T, ) ))
s.add(Implies( (rule7_x0 > 0), And(nsnt1CF_x0>=N-T, ) ))
s.add(Implies( (rule8_x0 > 0), And(nsnt01CF_x0>=N-T, nsnt0CF_x0>=N-2*T, nsnt1CF_x0>=1, ) ))
s.add(Implies( (rule9_x0 > 0), And(nsnt01CF_x0>=N-T, nsnt0CF_x0>=N-2*T, nsnt1CF_x0>=1, ) ))
s.add(Implies( (rule10_x0 > 0), And(nsnt01CF_x0>=N-T, nsnt1CF_x0>=N-2*T, nsnt0CF_x0>=1, ) ))
s.add(Implies( (rule11_x0 > 0), And(nsnt01CF_x0>=N-T, nsnt1CF_x0>=N-2*T, nsnt0CF_x0>=1, ) ))
s.add(Implies( (rule12_x0 > 0), And(nsnt01CF_x0>=N-T, nsnt0_x0<N-2*T, nsnt1_x0<N-2*T, ) ))
s.add(Implies( (rule13_x0 > 0), And(nsnt01CF_x0>=N-T, nsnt0_x0<N-2*T, nsnt1_x0<N-2*T, ) ))
s.add(Implies( (rule14_x0 > 0), And(nfaulty_x0<F, ) ))
s.add(Implies( (rule15_x0 > 0), And(nfaulty_x0<F, ) ))
s.add(Implies( (rule16_x0 > 0), And(nfaulty_x0<F, ) ))
s.add(Implies( (rule17_x0 > 0), And(nfaulty_x0<F, ) ))
s.add(Implies( (rule18_x0 > 0), And(nfaulty_x0<F, ) ))
s.add(Implies( (rule19_x0 > 0), And(nfaulty_x0<F, ) ))
s.add(Implies( (rule20_x0 > 0), And(nfaulty_x0<F, ) ))
s.add(Implies( (rule21_x0 > 0), And(nfaulty_x0<F, ) ))
s.add(Implies( (rule22_x0 > 0), And(True, ) ))
s.add(Implies( (rule23_x0 > 0), And(True, ) ))
s.add(Implies( (rule24_x0 > 0), And(True, ) ))
s.add(Implies( (rule25_x0 > 0), And(True, ) ))
s.add(Implies( (rule26_x0 > 0), And(True, ) ))
s.add(Implies( (rule27_x0 > 0), And(True, ) ))
s.add(Implies( (rule28_x0 > 0), And(True, ) ))
s.add(Implies( (rule29_x0 > 0), And(True, ) ))

##################Step 5#########################


#Ensuring that configurations x0 and y0 have the same context

s.add((nsnt1CF_x0>=1) == (nsnt1CF_y0>=1))
s.add((nsnt0CF_x0>=1) == (nsnt0CF_y0>=1))
s.add((nsnt1CF_x0>=N-2*T) == (nsnt1CF_y0>=N-2*T))
s.add((nsnt01CF_x0>=N-T) == (nsnt01CF_y0>=N-T))
s.add((nsnt1CF_x0>=N-T) == (nsnt1CF_y0>=N-T))
s.add((nsnt0_x0<N-2*T) == (nsnt0_y0<N-2*T))
s.add((nsnt0CF_x0>=N-T) == (nsnt0CF_y0>=N-T))
s.add((True) == (True))
s.add((nsnt1_x0<N-2*T) == (nsnt1_y0<N-2*T))
s.add((nfaulty_x0<F) == (nfaulty_y0<F))
s.add((nsnt0CF_x0>=N-2*T) == (nsnt0CF_y0>=N-2*T))

#############Additional step for the initial configuration#####################


#############Ensure that the first configuration only contains initial locations###########

s.add((loc0_x0 + loc1_x0) == N)
s.add(locS0_x0 == 0)
s.add(locS1_x0 == 0)
s.add(locD0_x0 == 0)
s.add(locD1_x0 == 0)
s.add(locU0_x0 == 0)
s.add(locU1_x0 == 0)
s.add(locCR_x0 == 0)
s.add(nsnt0_x0 == 0)
s.add(nsnt1_x0 == 0)
s.add(nsnt01_x0 == 0)
s.add(nsnt0CF_x0 == 0)
s.add(nsnt1CF_x0 == 0)
s.add(nsnt01CF_x0 == 0)
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
locS0_x1 = Real('locS0_x1')
locS0_y1 = Real('locS0_y1')
s.add(locS0_x1 >= 0)
s.add(locS0_y1 >= 0)
locS1_x1 = Real('locS1_x1')
locS1_y1 = Real('locS1_y1')
s.add(locS1_x1 >= 0)
s.add(locS1_y1 >= 0)
locD0_x1 = Real('locD0_x1')
locD0_y1 = Real('locD0_y1')
s.add(locD0_x1 >= 0)
s.add(locD0_y1 >= 0)
locD1_x1 = Real('locD1_x1')
locD1_y1 = Real('locD1_y1')
s.add(locD1_x1 >= 0)
s.add(locD1_y1 >= 0)
locU0_x1 = Real('locU0_x1')
locU0_y1 = Real('locU0_y1')
s.add(locU0_x1 >= 0)
s.add(locU0_y1 >= 0)
locU1_x1 = Real('locU1_x1')
locU1_y1 = Real('locU1_y1')
s.add(locU1_x1 >= 0)
s.add(locU1_y1 >= 0)
locCR_x1 = Real('locCR_x1')
locCR_y1 = Real('locCR_y1')
s.add(locCR_x1 >= 0)
s.add(locCR_y1 >= 0)






#Creating many copies of shared variables

nsnt0_x1 = Real('nsnt0_x1')
nsnt0_y1 = Real('nsnt0_y1')
s.add(nsnt0_x1 >= 0)
s.add(nsnt0_y1 >= 0)
nsnt1_x1 = Real('nsnt1_x1')
nsnt1_y1 = Real('nsnt1_y1')
s.add(nsnt1_x1 >= 0)
s.add(nsnt1_y1 >= 0)
nsnt0CF_x1 = Real('nsnt0CF_x1')
nsnt0CF_y1 = Real('nsnt0CF_y1')
s.add(nsnt0CF_x1 >= 0)
s.add(nsnt0CF_y1 >= 0)
nsnt1CF_x1 = Real('nsnt1CF_x1')
nsnt1CF_y1 = Real('nsnt1CF_y1')
s.add(nsnt1CF_x1 >= 0)
s.add(nsnt1CF_y1 >= 0)
nsnt01_x1 = Real('nsnt01_x1')
nsnt01_y1 = Real('nsnt01_y1')
s.add(nsnt01_x1 >= 0)
s.add(nsnt01_y1 >= 0)
nsnt01CF_x1 = Real('nsnt01CF_x1')
nsnt01CF_y1 = Real('nsnt01CF_y1')
s.add(nsnt01CF_x1 >= 0)
s.add(nsnt01CF_y1 >= 0)
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
rule14_x1 = Real('rule14_x1')
s.add(rule14_x1 >= 0)
rule15_x1 = Real('rule15_x1')
s.add(rule15_x1 >= 0)
rule16_x1 = Real('rule16_x1')
s.add(rule16_x1 >= 0)
rule17_x1 = Real('rule17_x1')
s.add(rule17_x1 >= 0)
rule18_x1 = Real('rule18_x1')
s.add(rule18_x1 >= 0)
rule19_x1 = Real('rule19_x1')
s.add(rule19_x1 >= 0)
rule20_x1 = Real('rule20_x1')
s.add(rule20_x1 >= 0)
rule21_x1 = Real('rule21_x1')
s.add(rule21_x1 >= 0)
rule22_x1 = Real('rule22_x1')
s.add(rule22_x1 >= 0)
rule23_x1 = Real('rule23_x1')
s.add(rule23_x1 >= 0)
rule24_x1 = Real('rule24_x1')
s.add(rule24_x1 >= 0)
rule25_x1 = Real('rule25_x1')
s.add(rule25_x1 >= 0)
rule26_x1 = Real('rule26_x1')
s.add(rule26_x1 >= 0)
rule27_x1 = Real('rule27_x1')
s.add(rule27_x1 >= 0)
rule28_x1 = Real('rule28_x1')
s.add(rule28_x1 >= 0)
rule29_x1 = Real('rule29_x1')
s.add(rule29_x1 >= 0)






###################Step 2####################


#Flow equations for the locations

s.add(0 - rule0_x1 - rule1_x1 - rule14_x1 - rule22_x1 + rule22_x1 ==  loc0_y1 - loc0_x1)
s.add(0 - rule2_x1 - rule3_x1 - rule15_x1 - rule23_x1 + rule23_x1 ==  loc1_y1 - loc1_x1)
s.add(0 + rule0_x1 - rule4_x1 - rule6_x1 - rule8_x1 - rule10_x1 - rule12_x1 - rule16_x1 - rule24_x1 + rule24_x1 ==  locS0_y1 - locS0_x1)
s.add(0 + rule2_x1 - rule5_x1 - rule7_x1 - rule9_x1 - rule11_x1 - rule13_x1 - rule17_x1 - rule25_x1 + rule25_x1 ==  locS1_y1 - locS1_x1)
s.add(0 + rule4_x1 + rule5_x1 - rule18_x1 - rule26_x1 + rule26_x1 ==  locD0_y1 - locD0_x1)
s.add(0 + rule6_x1 + rule7_x1 - rule19_x1 - rule27_x1 + rule27_x1 ==  locD1_y1 - locD1_x1)
s.add(0 + rule8_x1 + rule9_x1 + rule12_x1 - rule20_x1 - rule28_x1 + rule28_x1 ==  locU0_y1 - locU0_x1)
s.add(0 + rule10_x1 + rule11_x1 + rule13_x1 - rule21_x1 - rule29_x1 + rule29_x1 ==  locU1_y1 - locU1_x1)
s.add(0 + rule1_x1 + rule3_x1 + rule14_x1 + rule15_x1 + rule16_x1 + rule17_x1 + rule18_x1 + rule19_x1 + rule20_x1 + rule21_x1 ==  locCR_y1 - locCR_x1)






##################Step 3########################


#Flow equations for the shared variables

s.add(0 + rule0_x1 == nsnt0_y1 - nsnt0_x1)
s.add(0 + rule2_x1 == nsnt1_y1 - nsnt1_x1)
s.add(0 + rule0_x1 + rule1_x1 == nsnt0CF_y1 - nsnt0CF_x1)
s.add(0 + rule2_x1 + rule3_x1 == nsnt1CF_y1 - nsnt1CF_x1)
s.add(0 + rule0_x1 + rule2_x1 == nsnt01_y1 - nsnt01_x1)
s.add(0 + rule0_x1 + rule1_x1 + rule2_x1 + rule3_x1 == nsnt01CF_y1 - nsnt01CF_x1)
s.add(0 + rule1_x1 + rule3_x1 + rule14_x1 + rule15_x1 + rule16_x1 + rule17_x1 + rule18_x1 + rule19_x1 + rule20_x1 + rule21_x1 == nfaulty_y1 - nfaulty_x1)






####################Step 4########################


#Rule is fired implies rule is enabled

s.add(Implies( (rule0_x1 > 0), And(True, ) ))
s.add(Implies( (rule1_x1 > 0), And(nfaulty_x1<F, ) ))
s.add(Implies( (rule2_x1 > 0), And(True, ) ))
s.add(Implies( (rule3_x1 > 0), And(nfaulty_x1<F, ) ))
s.add(Implies( (rule4_x1 > 0), And(nsnt0CF_x1>=N-T, ) ))
s.add(Implies( (rule5_x1 > 0), And(nsnt0CF_x1>=N-T, ) ))
s.add(Implies( (rule6_x1 > 0), And(nsnt1CF_x1>=N-T, ) ))
s.add(Implies( (rule7_x1 > 0), And(nsnt1CF_x1>=N-T, ) ))
s.add(Implies( (rule8_x1 > 0), And(nsnt01CF_x1>=N-T, nsnt0CF_x1>=N-2*T, nsnt1CF_x1>=1, ) ))
s.add(Implies( (rule9_x1 > 0), And(nsnt01CF_x1>=N-T, nsnt0CF_x1>=N-2*T, nsnt1CF_x1>=1, ) ))
s.add(Implies( (rule10_x1 > 0), And(nsnt01CF_x1>=N-T, nsnt1CF_x1>=N-2*T, nsnt0CF_x1>=1, ) ))
s.add(Implies( (rule11_x1 > 0), And(nsnt01CF_x1>=N-T, nsnt1CF_x1>=N-2*T, nsnt0CF_x1>=1, ) ))
s.add(Implies( (rule12_x1 > 0), And(nsnt01CF_x1>=N-T, nsnt0_x1<N-2*T, nsnt1_x1<N-2*T, ) ))
s.add(Implies( (rule13_x1 > 0), And(nsnt01CF_x1>=N-T, nsnt0_x1<N-2*T, nsnt1_x1<N-2*T, ) ))
s.add(Implies( (rule14_x1 > 0), And(nfaulty_x1<F, ) ))
s.add(Implies( (rule15_x1 > 0), And(nfaulty_x1<F, ) ))
s.add(Implies( (rule16_x1 > 0), And(nfaulty_x1<F, ) ))
s.add(Implies( (rule17_x1 > 0), And(nfaulty_x1<F, ) ))
s.add(Implies( (rule18_x1 > 0), And(nfaulty_x1<F, ) ))
s.add(Implies( (rule19_x1 > 0), And(nfaulty_x1<F, ) ))
s.add(Implies( (rule20_x1 > 0), And(nfaulty_x1<F, ) ))
s.add(Implies( (rule21_x1 > 0), And(nfaulty_x1<F, ) ))
s.add(Implies( (rule22_x1 > 0), And(True, ) ))
s.add(Implies( (rule23_x1 > 0), And(True, ) ))
s.add(Implies( (rule24_x1 > 0), And(True, ) ))
s.add(Implies( (rule25_x1 > 0), And(True, ) ))
s.add(Implies( (rule26_x1 > 0), And(True, ) ))
s.add(Implies( (rule27_x1 > 0), And(True, ) ))
s.add(Implies( (rule28_x1 > 0), And(True, ) ))
s.add(Implies( (rule29_x1 > 0), And(True, ) ))

##################Step 5#########################


#Ensuring that configurations x1 and y1 have the same context

s.add((nsnt1CF_x1>=1) == (nsnt1CF_y1>=1))
s.add((nsnt0CF_x1>=1) == (nsnt0CF_y1>=1))
s.add((nsnt1CF_x1>=N-2*T) == (nsnt1CF_y1>=N-2*T))
s.add((nsnt01CF_x1>=N-T) == (nsnt01CF_y1>=N-T))
s.add((nsnt1CF_x1>=N-T) == (nsnt1CF_y1>=N-T))
s.add((nsnt0_x1<N-2*T) == (nsnt0_y1<N-2*T))
s.add((nsnt0CF_x1>=N-T) == (nsnt0CF_y1>=N-T))
s.add((True) == (True))
s.add((nsnt1_x1<N-2*T) == (nsnt1_y1<N-2*T))
s.add((nfaulty_x1<F) == (nfaulty_y1<F))
s.add((nsnt0CF_x1>=N-2*T) == (nsnt0CF_y1>=N-2*T))

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
locS0_x2 = Real('locS0_x2')
locS0_y2 = Real('locS0_y2')
s.add(locS0_x2 >= 0)
s.add(locS0_y2 >= 0)
locS1_x2 = Real('locS1_x2')
locS1_y2 = Real('locS1_y2')
s.add(locS1_x2 >= 0)
s.add(locS1_y2 >= 0)
locD0_x2 = Real('locD0_x2')
locD0_y2 = Real('locD0_y2')
s.add(locD0_x2 >= 0)
s.add(locD0_y2 >= 0)
locD1_x2 = Real('locD1_x2')
locD1_y2 = Real('locD1_y2')
s.add(locD1_x2 >= 0)
s.add(locD1_y2 >= 0)
locU0_x2 = Real('locU0_x2')
locU0_y2 = Real('locU0_y2')
s.add(locU0_x2 >= 0)
s.add(locU0_y2 >= 0)
locU1_x2 = Real('locU1_x2')
locU1_y2 = Real('locU1_y2')
s.add(locU1_x2 >= 0)
s.add(locU1_y2 >= 0)
locCR_x2 = Real('locCR_x2')
locCR_y2 = Real('locCR_y2')
s.add(locCR_x2 >= 0)
s.add(locCR_y2 >= 0)






#Creating many copies of shared variables

nsnt0_x2 = Real('nsnt0_x2')
nsnt0_y2 = Real('nsnt0_y2')
s.add(nsnt0_x2 >= 0)
s.add(nsnt0_y2 >= 0)
nsnt1_x2 = Real('nsnt1_x2')
nsnt1_y2 = Real('nsnt1_y2')
s.add(nsnt1_x2 >= 0)
s.add(nsnt1_y2 >= 0)
nsnt0CF_x2 = Real('nsnt0CF_x2')
nsnt0CF_y2 = Real('nsnt0CF_y2')
s.add(nsnt0CF_x2 >= 0)
s.add(nsnt0CF_y2 >= 0)
nsnt1CF_x2 = Real('nsnt1CF_x2')
nsnt1CF_y2 = Real('nsnt1CF_y2')
s.add(nsnt1CF_x2 >= 0)
s.add(nsnt1CF_y2 >= 0)
nsnt01_x2 = Real('nsnt01_x2')
nsnt01_y2 = Real('nsnt01_y2')
s.add(nsnt01_x2 >= 0)
s.add(nsnt01_y2 >= 0)
nsnt01CF_x2 = Real('nsnt01CF_x2')
nsnt01CF_y2 = Real('nsnt01CF_y2')
s.add(nsnt01CF_x2 >= 0)
s.add(nsnt01CF_y2 >= 0)
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
rule14_x2 = Real('rule14_x2')
s.add(rule14_x2 >= 0)
rule15_x2 = Real('rule15_x2')
s.add(rule15_x2 >= 0)
rule16_x2 = Real('rule16_x2')
s.add(rule16_x2 >= 0)
rule17_x2 = Real('rule17_x2')
s.add(rule17_x2 >= 0)
rule18_x2 = Real('rule18_x2')
s.add(rule18_x2 >= 0)
rule19_x2 = Real('rule19_x2')
s.add(rule19_x2 >= 0)
rule20_x2 = Real('rule20_x2')
s.add(rule20_x2 >= 0)
rule21_x2 = Real('rule21_x2')
s.add(rule21_x2 >= 0)
rule22_x2 = Real('rule22_x2')
s.add(rule22_x2 >= 0)
rule23_x2 = Real('rule23_x2')
s.add(rule23_x2 >= 0)
rule24_x2 = Real('rule24_x2')
s.add(rule24_x2 >= 0)
rule25_x2 = Real('rule25_x2')
s.add(rule25_x2 >= 0)
rule26_x2 = Real('rule26_x2')
s.add(rule26_x2 >= 0)
rule27_x2 = Real('rule27_x2')
s.add(rule27_x2 >= 0)
rule28_x2 = Real('rule28_x2')
s.add(rule28_x2 >= 0)
rule29_x2 = Real('rule29_x2')
s.add(rule29_x2 >= 0)






###################Step 2####################


#Flow equations for the locations

s.add(0 - rule0_x2 - rule1_x2 - rule14_x2 - rule22_x2 + rule22_x2 ==  loc0_y2 - loc0_x2)
s.add(0 - rule2_x2 - rule3_x2 - rule15_x2 - rule23_x2 + rule23_x2 ==  loc1_y2 - loc1_x2)
s.add(0 + rule0_x2 - rule4_x2 - rule6_x2 - rule8_x2 - rule10_x2 - rule12_x2 - rule16_x2 - rule24_x2 + rule24_x2 ==  locS0_y2 - locS0_x2)
s.add(0 + rule2_x2 - rule5_x2 - rule7_x2 - rule9_x2 - rule11_x2 - rule13_x2 - rule17_x2 - rule25_x2 + rule25_x2 ==  locS1_y2 - locS1_x2)
s.add(0 + rule4_x2 + rule5_x2 - rule18_x2 - rule26_x2 + rule26_x2 ==  locD0_y2 - locD0_x2)
s.add(0 + rule6_x2 + rule7_x2 - rule19_x2 - rule27_x2 + rule27_x2 ==  locD1_y2 - locD1_x2)
s.add(0 + rule8_x2 + rule9_x2 + rule12_x2 - rule20_x2 - rule28_x2 + rule28_x2 ==  locU0_y2 - locU0_x2)
s.add(0 + rule10_x2 + rule11_x2 + rule13_x2 - rule21_x2 - rule29_x2 + rule29_x2 ==  locU1_y2 - locU1_x2)
s.add(0 + rule1_x2 + rule3_x2 + rule14_x2 + rule15_x2 + rule16_x2 + rule17_x2 + rule18_x2 + rule19_x2 + rule20_x2 + rule21_x2 ==  locCR_y2 - locCR_x2)






##################Step 3########################


#Flow equations for the shared variables

s.add(0 + rule0_x2 == nsnt0_y2 - nsnt0_x2)
s.add(0 + rule2_x2 == nsnt1_y2 - nsnt1_x2)
s.add(0 + rule0_x2 + rule1_x2 == nsnt0CF_y2 - nsnt0CF_x2)
s.add(0 + rule2_x2 + rule3_x2 == nsnt1CF_y2 - nsnt1CF_x2)
s.add(0 + rule0_x2 + rule2_x2 == nsnt01_y2 - nsnt01_x2)
s.add(0 + rule0_x2 + rule1_x2 + rule2_x2 + rule3_x2 == nsnt01CF_y2 - nsnt01CF_x2)
s.add(0 + rule1_x2 + rule3_x2 + rule14_x2 + rule15_x2 + rule16_x2 + rule17_x2 + rule18_x2 + rule19_x2 + rule20_x2 + rule21_x2 == nfaulty_y2 - nfaulty_x2)






####################Step 4########################


#Rule is fired implies rule is enabled

s.add(Implies( (rule0_x2 > 0), And(True, ) ))
s.add(Implies( (rule1_x2 > 0), And(nfaulty_x2<F, ) ))
s.add(Implies( (rule2_x2 > 0), And(True, ) ))
s.add(Implies( (rule3_x2 > 0), And(nfaulty_x2<F, ) ))
s.add(Implies( (rule4_x2 > 0), And(nsnt0CF_x2>=N-T, ) ))
s.add(Implies( (rule5_x2 > 0), And(nsnt0CF_x2>=N-T, ) ))
s.add(Implies( (rule6_x2 > 0), And(nsnt1CF_x2>=N-T, ) ))
s.add(Implies( (rule7_x2 > 0), And(nsnt1CF_x2>=N-T, ) ))
s.add(Implies( (rule8_x2 > 0), And(nsnt01CF_x2>=N-T, nsnt0CF_x2>=N-2*T, nsnt1CF_x2>=1, ) ))
s.add(Implies( (rule9_x2 > 0), And(nsnt01CF_x2>=N-T, nsnt0CF_x2>=N-2*T, nsnt1CF_x2>=1, ) ))
s.add(Implies( (rule10_x2 > 0), And(nsnt01CF_x2>=N-T, nsnt1CF_x2>=N-2*T, nsnt0CF_x2>=1, ) ))
s.add(Implies( (rule11_x2 > 0), And(nsnt01CF_x2>=N-T, nsnt1CF_x2>=N-2*T, nsnt0CF_x2>=1, ) ))
s.add(Implies( (rule12_x2 > 0), And(nsnt01CF_x2>=N-T, nsnt0_x2<N-2*T, nsnt1_x2<N-2*T, ) ))
s.add(Implies( (rule13_x2 > 0), And(nsnt01CF_x2>=N-T, nsnt0_x2<N-2*T, nsnt1_x2<N-2*T, ) ))
s.add(Implies( (rule14_x2 > 0), And(nfaulty_x2<F, ) ))
s.add(Implies( (rule15_x2 > 0), And(nfaulty_x2<F, ) ))
s.add(Implies( (rule16_x2 > 0), And(nfaulty_x2<F, ) ))
s.add(Implies( (rule17_x2 > 0), And(nfaulty_x2<F, ) ))
s.add(Implies( (rule18_x2 > 0), And(nfaulty_x2<F, ) ))
s.add(Implies( (rule19_x2 > 0), And(nfaulty_x2<F, ) ))
s.add(Implies( (rule20_x2 > 0), And(nfaulty_x2<F, ) ))
s.add(Implies( (rule21_x2 > 0), And(nfaulty_x2<F, ) ))
s.add(Implies( (rule22_x2 > 0), And(True, ) ))
s.add(Implies( (rule23_x2 > 0), And(True, ) ))
s.add(Implies( (rule24_x2 > 0), And(True, ) ))
s.add(Implies( (rule25_x2 > 0), And(True, ) ))
s.add(Implies( (rule26_x2 > 0), And(True, ) ))
s.add(Implies( (rule27_x2 > 0), And(True, ) ))
s.add(Implies( (rule28_x2 > 0), And(True, ) ))
s.add(Implies( (rule29_x2 > 0), And(True, ) ))

##################Step 5#########################


#Ensuring that configurations x2 and y2 have the same context

s.add((nsnt1CF_x2>=1) == (nsnt1CF_y2>=1))
s.add((nsnt0CF_x2>=1) == (nsnt0CF_y2>=1))
s.add((nsnt1CF_x2>=N-2*T) == (nsnt1CF_y2>=N-2*T))
s.add((nsnt01CF_x2>=N-T) == (nsnt01CF_y2>=N-T))
s.add((nsnt1CF_x2>=N-T) == (nsnt1CF_y2>=N-T))
s.add((nsnt0_x2<N-2*T) == (nsnt0_y2<N-2*T))
s.add((nsnt0CF_x2>=N-T) == (nsnt0CF_y2>=N-T))
s.add((True) == (True))
s.add((nsnt1_x2<N-2*T) == (nsnt1_y2<N-2*T))
s.add((nfaulty_x2<F) == (nfaulty_y2<F))
s.add((nsnt0CF_x2>=N-2*T) == (nsnt0CF_y2>=N-2*T))

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
locS0_x3 = Real('locS0_x3')
locS0_y3 = Real('locS0_y3')
s.add(locS0_x3 >= 0)
s.add(locS0_y3 >= 0)
locS1_x3 = Real('locS1_x3')
locS1_y3 = Real('locS1_y3')
s.add(locS1_x3 >= 0)
s.add(locS1_y3 >= 0)
locD0_x3 = Real('locD0_x3')
locD0_y3 = Real('locD0_y3')
s.add(locD0_x3 >= 0)
s.add(locD0_y3 >= 0)
locD1_x3 = Real('locD1_x3')
locD1_y3 = Real('locD1_y3')
s.add(locD1_x3 >= 0)
s.add(locD1_y3 >= 0)
locU0_x3 = Real('locU0_x3')
locU0_y3 = Real('locU0_y3')
s.add(locU0_x3 >= 0)
s.add(locU0_y3 >= 0)
locU1_x3 = Real('locU1_x3')
locU1_y3 = Real('locU1_y3')
s.add(locU1_x3 >= 0)
s.add(locU1_y3 >= 0)
locCR_x3 = Real('locCR_x3')
locCR_y3 = Real('locCR_y3')
s.add(locCR_x3 >= 0)
s.add(locCR_y3 >= 0)






#Creating many copies of shared variables

nsnt0_x3 = Real('nsnt0_x3')
nsnt0_y3 = Real('nsnt0_y3')
s.add(nsnt0_x3 >= 0)
s.add(nsnt0_y3 >= 0)
nsnt1_x3 = Real('nsnt1_x3')
nsnt1_y3 = Real('nsnt1_y3')
s.add(nsnt1_x3 >= 0)
s.add(nsnt1_y3 >= 0)
nsnt0CF_x3 = Real('nsnt0CF_x3')
nsnt0CF_y3 = Real('nsnt0CF_y3')
s.add(nsnt0CF_x3 >= 0)
s.add(nsnt0CF_y3 >= 0)
nsnt1CF_x3 = Real('nsnt1CF_x3')
nsnt1CF_y3 = Real('nsnt1CF_y3')
s.add(nsnt1CF_x3 >= 0)
s.add(nsnt1CF_y3 >= 0)
nsnt01_x3 = Real('nsnt01_x3')
nsnt01_y3 = Real('nsnt01_y3')
s.add(nsnt01_x3 >= 0)
s.add(nsnt01_y3 >= 0)
nsnt01CF_x3 = Real('nsnt01CF_x3')
nsnt01CF_y3 = Real('nsnt01CF_y3')
s.add(nsnt01CF_x3 >= 0)
s.add(nsnt01CF_y3 >= 0)
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
rule14_x3 = Real('rule14_x3')
s.add(rule14_x3 >= 0)
rule15_x3 = Real('rule15_x3')
s.add(rule15_x3 >= 0)
rule16_x3 = Real('rule16_x3')
s.add(rule16_x3 >= 0)
rule17_x3 = Real('rule17_x3')
s.add(rule17_x3 >= 0)
rule18_x3 = Real('rule18_x3')
s.add(rule18_x3 >= 0)
rule19_x3 = Real('rule19_x3')
s.add(rule19_x3 >= 0)
rule20_x3 = Real('rule20_x3')
s.add(rule20_x3 >= 0)
rule21_x3 = Real('rule21_x3')
s.add(rule21_x3 >= 0)
rule22_x3 = Real('rule22_x3')
s.add(rule22_x3 >= 0)
rule23_x3 = Real('rule23_x3')
s.add(rule23_x3 >= 0)
rule24_x3 = Real('rule24_x3')
s.add(rule24_x3 >= 0)
rule25_x3 = Real('rule25_x3')
s.add(rule25_x3 >= 0)
rule26_x3 = Real('rule26_x3')
s.add(rule26_x3 >= 0)
rule27_x3 = Real('rule27_x3')
s.add(rule27_x3 >= 0)
rule28_x3 = Real('rule28_x3')
s.add(rule28_x3 >= 0)
rule29_x3 = Real('rule29_x3')
s.add(rule29_x3 >= 0)






###################Step 2####################


#Flow equations for the locations

s.add(0 - rule0_x3 - rule1_x3 - rule14_x3 - rule22_x3 + rule22_x3 ==  loc0_y3 - loc0_x3)
s.add(0 - rule2_x3 - rule3_x3 - rule15_x3 - rule23_x3 + rule23_x3 ==  loc1_y3 - loc1_x3)
s.add(0 + rule0_x3 - rule4_x3 - rule6_x3 - rule8_x3 - rule10_x3 - rule12_x3 - rule16_x3 - rule24_x3 + rule24_x3 ==  locS0_y3 - locS0_x3)
s.add(0 + rule2_x3 - rule5_x3 - rule7_x3 - rule9_x3 - rule11_x3 - rule13_x3 - rule17_x3 - rule25_x3 + rule25_x3 ==  locS1_y3 - locS1_x3)
s.add(0 + rule4_x3 + rule5_x3 - rule18_x3 - rule26_x3 + rule26_x3 ==  locD0_y3 - locD0_x3)
s.add(0 + rule6_x3 + rule7_x3 - rule19_x3 - rule27_x3 + rule27_x3 ==  locD1_y3 - locD1_x3)
s.add(0 + rule8_x3 + rule9_x3 + rule12_x3 - rule20_x3 - rule28_x3 + rule28_x3 ==  locU0_y3 - locU0_x3)
s.add(0 + rule10_x3 + rule11_x3 + rule13_x3 - rule21_x3 - rule29_x3 + rule29_x3 ==  locU1_y3 - locU1_x3)
s.add(0 + rule1_x3 + rule3_x3 + rule14_x3 + rule15_x3 + rule16_x3 + rule17_x3 + rule18_x3 + rule19_x3 + rule20_x3 + rule21_x3 ==  locCR_y3 - locCR_x3)






##################Step 3########################


#Flow equations for the shared variables

s.add(0 + rule0_x3 == nsnt0_y3 - nsnt0_x3)
s.add(0 + rule2_x3 == nsnt1_y3 - nsnt1_x3)
s.add(0 + rule0_x3 + rule1_x3 == nsnt0CF_y3 - nsnt0CF_x3)
s.add(0 + rule2_x3 + rule3_x3 == nsnt1CF_y3 - nsnt1CF_x3)
s.add(0 + rule0_x3 + rule2_x3 == nsnt01_y3 - nsnt01_x3)
s.add(0 + rule0_x3 + rule1_x3 + rule2_x3 + rule3_x3 == nsnt01CF_y3 - nsnt01CF_x3)
s.add(0 + rule1_x3 + rule3_x3 + rule14_x3 + rule15_x3 + rule16_x3 + rule17_x3 + rule18_x3 + rule19_x3 + rule20_x3 + rule21_x3 == nfaulty_y3 - nfaulty_x3)






####################Step 4########################


#Rule is fired implies rule is enabled

s.add(Implies( (rule0_x3 > 0), And(True, ) ))
s.add(Implies( (rule1_x3 > 0), And(nfaulty_x3<F, ) ))
s.add(Implies( (rule2_x3 > 0), And(True, ) ))
s.add(Implies( (rule3_x3 > 0), And(nfaulty_x3<F, ) ))
s.add(Implies( (rule4_x3 > 0), And(nsnt0CF_x3>=N-T, ) ))
s.add(Implies( (rule5_x3 > 0), And(nsnt0CF_x3>=N-T, ) ))
s.add(Implies( (rule6_x3 > 0), And(nsnt1CF_x3>=N-T, ) ))
s.add(Implies( (rule7_x3 > 0), And(nsnt1CF_x3>=N-T, ) ))
s.add(Implies( (rule8_x3 > 0), And(nsnt01CF_x3>=N-T, nsnt0CF_x3>=N-2*T, nsnt1CF_x3>=1, ) ))
s.add(Implies( (rule9_x3 > 0), And(nsnt01CF_x3>=N-T, nsnt0CF_x3>=N-2*T, nsnt1CF_x3>=1, ) ))
s.add(Implies( (rule10_x3 > 0), And(nsnt01CF_x3>=N-T, nsnt1CF_x3>=N-2*T, nsnt0CF_x3>=1, ) ))
s.add(Implies( (rule11_x3 > 0), And(nsnt01CF_x3>=N-T, nsnt1CF_x3>=N-2*T, nsnt0CF_x3>=1, ) ))
s.add(Implies( (rule12_x3 > 0), And(nsnt01CF_x3>=N-T, nsnt0_x3<N-2*T, nsnt1_x3<N-2*T, ) ))
s.add(Implies( (rule13_x3 > 0), And(nsnt01CF_x3>=N-T, nsnt0_x3<N-2*T, nsnt1_x3<N-2*T, ) ))
s.add(Implies( (rule14_x3 > 0), And(nfaulty_x3<F, ) ))
s.add(Implies( (rule15_x3 > 0), And(nfaulty_x3<F, ) ))
s.add(Implies( (rule16_x3 > 0), And(nfaulty_x3<F, ) ))
s.add(Implies( (rule17_x3 > 0), And(nfaulty_x3<F, ) ))
s.add(Implies( (rule18_x3 > 0), And(nfaulty_x3<F, ) ))
s.add(Implies( (rule19_x3 > 0), And(nfaulty_x3<F, ) ))
s.add(Implies( (rule20_x3 > 0), And(nfaulty_x3<F, ) ))
s.add(Implies( (rule21_x3 > 0), And(nfaulty_x3<F, ) ))
s.add(Implies( (rule22_x3 > 0), And(True, ) ))
s.add(Implies( (rule23_x3 > 0), And(True, ) ))
s.add(Implies( (rule24_x3 > 0), And(True, ) ))
s.add(Implies( (rule25_x3 > 0), And(True, ) ))
s.add(Implies( (rule26_x3 > 0), And(True, ) ))
s.add(Implies( (rule27_x3 > 0), And(True, ) ))
s.add(Implies( (rule28_x3 > 0), And(True, ) ))
s.add(Implies( (rule29_x3 > 0), And(True, ) ))

##################Step 5#########################


#Ensuring that configurations x3 and y3 have the same context

s.add((nsnt1CF_x3>=1) == (nsnt1CF_y3>=1))
s.add((nsnt0CF_x3>=1) == (nsnt0CF_y3>=1))
s.add((nsnt1CF_x3>=N-2*T) == (nsnt1CF_y3>=N-2*T))
s.add((nsnt01CF_x3>=N-T) == (nsnt01CF_y3>=N-T))
s.add((nsnt1CF_x3>=N-T) == (nsnt1CF_y3>=N-T))
s.add((nsnt0_x3<N-2*T) == (nsnt0_y3<N-2*T))
s.add((nsnt0CF_x3>=N-T) == (nsnt0CF_y3>=N-T))
s.add((True) == (True))
s.add((nsnt1_x3<N-2*T) == (nsnt1_y3<N-2*T))
s.add((nfaulty_x3<F) == (nfaulty_y3<F))
s.add((nsnt0CF_x3>=N-2*T) == (nsnt0CF_y3>=N-2*T))

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
locS0_x4 = Real('locS0_x4')
locS0_y4 = Real('locS0_y4')
s.add(locS0_x4 >= 0)
s.add(locS0_y4 >= 0)
locS1_x4 = Real('locS1_x4')
locS1_y4 = Real('locS1_y4')
s.add(locS1_x4 >= 0)
s.add(locS1_y4 >= 0)
locD0_x4 = Real('locD0_x4')
locD0_y4 = Real('locD0_y4')
s.add(locD0_x4 >= 0)
s.add(locD0_y4 >= 0)
locD1_x4 = Real('locD1_x4')
locD1_y4 = Real('locD1_y4')
s.add(locD1_x4 >= 0)
s.add(locD1_y4 >= 0)
locU0_x4 = Real('locU0_x4')
locU0_y4 = Real('locU0_y4')
s.add(locU0_x4 >= 0)
s.add(locU0_y4 >= 0)
locU1_x4 = Real('locU1_x4')
locU1_y4 = Real('locU1_y4')
s.add(locU1_x4 >= 0)
s.add(locU1_y4 >= 0)
locCR_x4 = Real('locCR_x4')
locCR_y4 = Real('locCR_y4')
s.add(locCR_x4 >= 0)
s.add(locCR_y4 >= 0)






#Creating many copies of shared variables

nsnt0_x4 = Real('nsnt0_x4')
nsnt0_y4 = Real('nsnt0_y4')
s.add(nsnt0_x4 >= 0)
s.add(nsnt0_y4 >= 0)
nsnt1_x4 = Real('nsnt1_x4')
nsnt1_y4 = Real('nsnt1_y4')
s.add(nsnt1_x4 >= 0)
s.add(nsnt1_y4 >= 0)
nsnt0CF_x4 = Real('nsnt0CF_x4')
nsnt0CF_y4 = Real('nsnt0CF_y4')
s.add(nsnt0CF_x4 >= 0)
s.add(nsnt0CF_y4 >= 0)
nsnt1CF_x4 = Real('nsnt1CF_x4')
nsnt1CF_y4 = Real('nsnt1CF_y4')
s.add(nsnt1CF_x4 >= 0)
s.add(nsnt1CF_y4 >= 0)
nsnt01_x4 = Real('nsnt01_x4')
nsnt01_y4 = Real('nsnt01_y4')
s.add(nsnt01_x4 >= 0)
s.add(nsnt01_y4 >= 0)
nsnt01CF_x4 = Real('nsnt01CF_x4')
nsnt01CF_y4 = Real('nsnt01CF_y4')
s.add(nsnt01CF_x4 >= 0)
s.add(nsnt01CF_y4 >= 0)
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
rule14_x4 = Real('rule14_x4')
s.add(rule14_x4 >= 0)
rule15_x4 = Real('rule15_x4')
s.add(rule15_x4 >= 0)
rule16_x4 = Real('rule16_x4')
s.add(rule16_x4 >= 0)
rule17_x4 = Real('rule17_x4')
s.add(rule17_x4 >= 0)
rule18_x4 = Real('rule18_x4')
s.add(rule18_x4 >= 0)
rule19_x4 = Real('rule19_x4')
s.add(rule19_x4 >= 0)
rule20_x4 = Real('rule20_x4')
s.add(rule20_x4 >= 0)
rule21_x4 = Real('rule21_x4')
s.add(rule21_x4 >= 0)
rule22_x4 = Real('rule22_x4')
s.add(rule22_x4 >= 0)
rule23_x4 = Real('rule23_x4')
s.add(rule23_x4 >= 0)
rule24_x4 = Real('rule24_x4')
s.add(rule24_x4 >= 0)
rule25_x4 = Real('rule25_x4')
s.add(rule25_x4 >= 0)
rule26_x4 = Real('rule26_x4')
s.add(rule26_x4 >= 0)
rule27_x4 = Real('rule27_x4')
s.add(rule27_x4 >= 0)
rule28_x4 = Real('rule28_x4')
s.add(rule28_x4 >= 0)
rule29_x4 = Real('rule29_x4')
s.add(rule29_x4 >= 0)






###################Step 2####################


#Flow equations for the locations

s.add(0 - rule0_x4 - rule1_x4 - rule14_x4 - rule22_x4 + rule22_x4 ==  loc0_y4 - loc0_x4)
s.add(0 - rule2_x4 - rule3_x4 - rule15_x4 - rule23_x4 + rule23_x4 ==  loc1_y4 - loc1_x4)
s.add(0 + rule0_x4 - rule4_x4 - rule6_x4 - rule8_x4 - rule10_x4 - rule12_x4 - rule16_x4 - rule24_x4 + rule24_x4 ==  locS0_y4 - locS0_x4)
s.add(0 + rule2_x4 - rule5_x4 - rule7_x4 - rule9_x4 - rule11_x4 - rule13_x4 - rule17_x4 - rule25_x4 + rule25_x4 ==  locS1_y4 - locS1_x4)
s.add(0 + rule4_x4 + rule5_x4 - rule18_x4 - rule26_x4 + rule26_x4 ==  locD0_y4 - locD0_x4)
s.add(0 + rule6_x4 + rule7_x4 - rule19_x4 - rule27_x4 + rule27_x4 ==  locD1_y4 - locD1_x4)
s.add(0 + rule8_x4 + rule9_x4 + rule12_x4 - rule20_x4 - rule28_x4 + rule28_x4 ==  locU0_y4 - locU0_x4)
s.add(0 + rule10_x4 + rule11_x4 + rule13_x4 - rule21_x4 - rule29_x4 + rule29_x4 ==  locU1_y4 - locU1_x4)
s.add(0 + rule1_x4 + rule3_x4 + rule14_x4 + rule15_x4 + rule16_x4 + rule17_x4 + rule18_x4 + rule19_x4 + rule20_x4 + rule21_x4 ==  locCR_y4 - locCR_x4)






##################Step 3########################


#Flow equations for the shared variables

s.add(0 + rule0_x4 == nsnt0_y4 - nsnt0_x4)
s.add(0 + rule2_x4 == nsnt1_y4 - nsnt1_x4)
s.add(0 + rule0_x4 + rule1_x4 == nsnt0CF_y4 - nsnt0CF_x4)
s.add(0 + rule2_x4 + rule3_x4 == nsnt1CF_y4 - nsnt1CF_x4)
s.add(0 + rule0_x4 + rule2_x4 == nsnt01_y4 - nsnt01_x4)
s.add(0 + rule0_x4 + rule1_x4 + rule2_x4 + rule3_x4 == nsnt01CF_y4 - nsnt01CF_x4)
s.add(0 + rule1_x4 + rule3_x4 + rule14_x4 + rule15_x4 + rule16_x4 + rule17_x4 + rule18_x4 + rule19_x4 + rule20_x4 + rule21_x4 == nfaulty_y4 - nfaulty_x4)






####################Step 4########################


#Rule is fired implies rule is enabled

s.add(Implies( (rule0_x4 > 0), And(True, ) ))
s.add(Implies( (rule1_x4 > 0), And(nfaulty_x4<F, ) ))
s.add(Implies( (rule2_x4 > 0), And(True, ) ))
s.add(Implies( (rule3_x4 > 0), And(nfaulty_x4<F, ) ))
s.add(Implies( (rule4_x4 > 0), And(nsnt0CF_x4>=N-T, ) ))
s.add(Implies( (rule5_x4 > 0), And(nsnt0CF_x4>=N-T, ) ))
s.add(Implies( (rule6_x4 > 0), And(nsnt1CF_x4>=N-T, ) ))
s.add(Implies( (rule7_x4 > 0), And(nsnt1CF_x4>=N-T, ) ))
s.add(Implies( (rule8_x4 > 0), And(nsnt01CF_x4>=N-T, nsnt0CF_x4>=N-2*T, nsnt1CF_x4>=1, ) ))
s.add(Implies( (rule9_x4 > 0), And(nsnt01CF_x4>=N-T, nsnt0CF_x4>=N-2*T, nsnt1CF_x4>=1, ) ))
s.add(Implies( (rule10_x4 > 0), And(nsnt01CF_x4>=N-T, nsnt1CF_x4>=N-2*T, nsnt0CF_x4>=1, ) ))
s.add(Implies( (rule11_x4 > 0), And(nsnt01CF_x4>=N-T, nsnt1CF_x4>=N-2*T, nsnt0CF_x4>=1, ) ))
s.add(Implies( (rule12_x4 > 0), And(nsnt01CF_x4>=N-T, nsnt0_x4<N-2*T, nsnt1_x4<N-2*T, ) ))
s.add(Implies( (rule13_x4 > 0), And(nsnt01CF_x4>=N-T, nsnt0_x4<N-2*T, nsnt1_x4<N-2*T, ) ))
s.add(Implies( (rule14_x4 > 0), And(nfaulty_x4<F, ) ))
s.add(Implies( (rule15_x4 > 0), And(nfaulty_x4<F, ) ))
s.add(Implies( (rule16_x4 > 0), And(nfaulty_x4<F, ) ))
s.add(Implies( (rule17_x4 > 0), And(nfaulty_x4<F, ) ))
s.add(Implies( (rule18_x4 > 0), And(nfaulty_x4<F, ) ))
s.add(Implies( (rule19_x4 > 0), And(nfaulty_x4<F, ) ))
s.add(Implies( (rule20_x4 > 0), And(nfaulty_x4<F, ) ))
s.add(Implies( (rule21_x4 > 0), And(nfaulty_x4<F, ) ))
s.add(Implies( (rule22_x4 > 0), And(True, ) ))
s.add(Implies( (rule23_x4 > 0), And(True, ) ))
s.add(Implies( (rule24_x4 > 0), And(True, ) ))
s.add(Implies( (rule25_x4 > 0), And(True, ) ))
s.add(Implies( (rule26_x4 > 0), And(True, ) ))
s.add(Implies( (rule27_x4 > 0), And(True, ) ))
s.add(Implies( (rule28_x4 > 0), And(True, ) ))
s.add(Implies( (rule29_x4 > 0), And(True, ) ))

##################Step 5#########################


#Ensuring that configurations x4 and y4 have the same context

s.add((nsnt1CF_x4>=1) == (nsnt1CF_y4>=1))
s.add((nsnt0CF_x4>=1) == (nsnt0CF_y4>=1))
s.add((nsnt1CF_x4>=N-2*T) == (nsnt1CF_y4>=N-2*T))
s.add((nsnt01CF_x4>=N-T) == (nsnt01CF_y4>=N-T))
s.add((nsnt1CF_x4>=N-T) == (nsnt1CF_y4>=N-T))
s.add((nsnt0_x4<N-2*T) == (nsnt0_y4<N-2*T))
s.add((nsnt0CF_x4>=N-T) == (nsnt0CF_y4>=N-T))
s.add((True) == (True))
s.add((nsnt1_x4<N-2*T) == (nsnt1_y4<N-2*T))
s.add((nfaulty_x4<F) == (nfaulty_y4<F))
s.add((nsnt0CF_x4>=N-2*T) == (nsnt0CF_y4>=N-2*T))

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
locS0_x5 = Real('locS0_x5')
locS0_y5 = Real('locS0_y5')
s.add(locS0_x5 >= 0)
s.add(locS0_y5 >= 0)
locS1_x5 = Real('locS1_x5')
locS1_y5 = Real('locS1_y5')
s.add(locS1_x5 >= 0)
s.add(locS1_y5 >= 0)
locD0_x5 = Real('locD0_x5')
locD0_y5 = Real('locD0_y5')
s.add(locD0_x5 >= 0)
s.add(locD0_y5 >= 0)
locD1_x5 = Real('locD1_x5')
locD1_y5 = Real('locD1_y5')
s.add(locD1_x5 >= 0)
s.add(locD1_y5 >= 0)
locU0_x5 = Real('locU0_x5')
locU0_y5 = Real('locU0_y5')
s.add(locU0_x5 >= 0)
s.add(locU0_y5 >= 0)
locU1_x5 = Real('locU1_x5')
locU1_y5 = Real('locU1_y5')
s.add(locU1_x5 >= 0)
s.add(locU1_y5 >= 0)
locCR_x5 = Real('locCR_x5')
locCR_y5 = Real('locCR_y5')
s.add(locCR_x5 >= 0)
s.add(locCR_y5 >= 0)






#Creating many copies of shared variables

nsnt0_x5 = Real('nsnt0_x5')
nsnt0_y5 = Real('nsnt0_y5')
s.add(nsnt0_x5 >= 0)
s.add(nsnt0_y5 >= 0)
nsnt1_x5 = Real('nsnt1_x5')
nsnt1_y5 = Real('nsnt1_y5')
s.add(nsnt1_x5 >= 0)
s.add(nsnt1_y5 >= 0)
nsnt0CF_x5 = Real('nsnt0CF_x5')
nsnt0CF_y5 = Real('nsnt0CF_y5')
s.add(nsnt0CF_x5 >= 0)
s.add(nsnt0CF_y5 >= 0)
nsnt1CF_x5 = Real('nsnt1CF_x5')
nsnt1CF_y5 = Real('nsnt1CF_y5')
s.add(nsnt1CF_x5 >= 0)
s.add(nsnt1CF_y5 >= 0)
nsnt01_x5 = Real('nsnt01_x5')
nsnt01_y5 = Real('nsnt01_y5')
s.add(nsnt01_x5 >= 0)
s.add(nsnt01_y5 >= 0)
nsnt01CF_x5 = Real('nsnt01CF_x5')
nsnt01CF_y5 = Real('nsnt01CF_y5')
s.add(nsnt01CF_x5 >= 0)
s.add(nsnt01CF_y5 >= 0)
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
rule14_x5 = Real('rule14_x5')
s.add(rule14_x5 >= 0)
rule15_x5 = Real('rule15_x5')
s.add(rule15_x5 >= 0)
rule16_x5 = Real('rule16_x5')
s.add(rule16_x5 >= 0)
rule17_x5 = Real('rule17_x5')
s.add(rule17_x5 >= 0)
rule18_x5 = Real('rule18_x5')
s.add(rule18_x5 >= 0)
rule19_x5 = Real('rule19_x5')
s.add(rule19_x5 >= 0)
rule20_x5 = Real('rule20_x5')
s.add(rule20_x5 >= 0)
rule21_x5 = Real('rule21_x5')
s.add(rule21_x5 >= 0)
rule22_x5 = Real('rule22_x5')
s.add(rule22_x5 >= 0)
rule23_x5 = Real('rule23_x5')
s.add(rule23_x5 >= 0)
rule24_x5 = Real('rule24_x5')
s.add(rule24_x5 >= 0)
rule25_x5 = Real('rule25_x5')
s.add(rule25_x5 >= 0)
rule26_x5 = Real('rule26_x5')
s.add(rule26_x5 >= 0)
rule27_x5 = Real('rule27_x5')
s.add(rule27_x5 >= 0)
rule28_x5 = Real('rule28_x5')
s.add(rule28_x5 >= 0)
rule29_x5 = Real('rule29_x5')
s.add(rule29_x5 >= 0)






###################Step 2####################


#Flow equations for the locations

s.add(0 - rule0_x5 - rule1_x5 - rule14_x5 - rule22_x5 + rule22_x5 ==  loc0_y5 - loc0_x5)
s.add(0 - rule2_x5 - rule3_x5 - rule15_x5 - rule23_x5 + rule23_x5 ==  loc1_y5 - loc1_x5)
s.add(0 + rule0_x5 - rule4_x5 - rule6_x5 - rule8_x5 - rule10_x5 - rule12_x5 - rule16_x5 - rule24_x5 + rule24_x5 ==  locS0_y5 - locS0_x5)
s.add(0 + rule2_x5 - rule5_x5 - rule7_x5 - rule9_x5 - rule11_x5 - rule13_x5 - rule17_x5 - rule25_x5 + rule25_x5 ==  locS1_y5 - locS1_x5)
s.add(0 + rule4_x5 + rule5_x5 - rule18_x5 - rule26_x5 + rule26_x5 ==  locD0_y5 - locD0_x5)
s.add(0 + rule6_x5 + rule7_x5 - rule19_x5 - rule27_x5 + rule27_x5 ==  locD1_y5 - locD1_x5)
s.add(0 + rule8_x5 + rule9_x5 + rule12_x5 - rule20_x5 - rule28_x5 + rule28_x5 ==  locU0_y5 - locU0_x5)
s.add(0 + rule10_x5 + rule11_x5 + rule13_x5 - rule21_x5 - rule29_x5 + rule29_x5 ==  locU1_y5 - locU1_x5)
s.add(0 + rule1_x5 + rule3_x5 + rule14_x5 + rule15_x5 + rule16_x5 + rule17_x5 + rule18_x5 + rule19_x5 + rule20_x5 + rule21_x5 ==  locCR_y5 - locCR_x5)






##################Step 3########################


#Flow equations for the shared variables

s.add(0 + rule0_x5 == nsnt0_y5 - nsnt0_x5)
s.add(0 + rule2_x5 == nsnt1_y5 - nsnt1_x5)
s.add(0 + rule0_x5 + rule1_x5 == nsnt0CF_y5 - nsnt0CF_x5)
s.add(0 + rule2_x5 + rule3_x5 == nsnt1CF_y5 - nsnt1CF_x5)
s.add(0 + rule0_x5 + rule2_x5 == nsnt01_y5 - nsnt01_x5)
s.add(0 + rule0_x5 + rule1_x5 + rule2_x5 + rule3_x5 == nsnt01CF_y5 - nsnt01CF_x5)
s.add(0 + rule1_x5 + rule3_x5 + rule14_x5 + rule15_x5 + rule16_x5 + rule17_x5 + rule18_x5 + rule19_x5 + rule20_x5 + rule21_x5 == nfaulty_y5 - nfaulty_x5)






####################Step 4########################


#Rule is fired implies rule is enabled

s.add(Implies( (rule0_x5 > 0), And(True, ) ))
s.add(Implies( (rule1_x5 > 0), And(nfaulty_x5<F, ) ))
s.add(Implies( (rule2_x5 > 0), And(True, ) ))
s.add(Implies( (rule3_x5 > 0), And(nfaulty_x5<F, ) ))
s.add(Implies( (rule4_x5 > 0), And(nsnt0CF_x5>=N-T, ) ))
s.add(Implies( (rule5_x5 > 0), And(nsnt0CF_x5>=N-T, ) ))
s.add(Implies( (rule6_x5 > 0), And(nsnt1CF_x5>=N-T, ) ))
s.add(Implies( (rule7_x5 > 0), And(nsnt1CF_x5>=N-T, ) ))
s.add(Implies( (rule8_x5 > 0), And(nsnt01CF_x5>=N-T, nsnt0CF_x5>=N-2*T, nsnt1CF_x5>=1, ) ))
s.add(Implies( (rule9_x5 > 0), And(nsnt01CF_x5>=N-T, nsnt0CF_x5>=N-2*T, nsnt1CF_x5>=1, ) ))
s.add(Implies( (rule10_x5 > 0), And(nsnt01CF_x5>=N-T, nsnt1CF_x5>=N-2*T, nsnt0CF_x5>=1, ) ))
s.add(Implies( (rule11_x5 > 0), And(nsnt01CF_x5>=N-T, nsnt1CF_x5>=N-2*T, nsnt0CF_x5>=1, ) ))
s.add(Implies( (rule12_x5 > 0), And(nsnt01CF_x5>=N-T, nsnt0_x5<N-2*T, nsnt1_x5<N-2*T, ) ))
s.add(Implies( (rule13_x5 > 0), And(nsnt01CF_x5>=N-T, nsnt0_x5<N-2*T, nsnt1_x5<N-2*T, ) ))
s.add(Implies( (rule14_x5 > 0), And(nfaulty_x5<F, ) ))
s.add(Implies( (rule15_x5 > 0), And(nfaulty_x5<F, ) ))
s.add(Implies( (rule16_x5 > 0), And(nfaulty_x5<F, ) ))
s.add(Implies( (rule17_x5 > 0), And(nfaulty_x5<F, ) ))
s.add(Implies( (rule18_x5 > 0), And(nfaulty_x5<F, ) ))
s.add(Implies( (rule19_x5 > 0), And(nfaulty_x5<F, ) ))
s.add(Implies( (rule20_x5 > 0), And(nfaulty_x5<F, ) ))
s.add(Implies( (rule21_x5 > 0), And(nfaulty_x5<F, ) ))
s.add(Implies( (rule22_x5 > 0), And(True, ) ))
s.add(Implies( (rule23_x5 > 0), And(True, ) ))
s.add(Implies( (rule24_x5 > 0), And(True, ) ))
s.add(Implies( (rule25_x5 > 0), And(True, ) ))
s.add(Implies( (rule26_x5 > 0), And(True, ) ))
s.add(Implies( (rule27_x5 > 0), And(True, ) ))
s.add(Implies( (rule28_x5 > 0), And(True, ) ))
s.add(Implies( (rule29_x5 > 0), And(True, ) ))

##################Step 5#########################


#Ensuring that configurations x5 and y5 have the same context

s.add((nsnt1CF_x5>=1) == (nsnt1CF_y5>=1))
s.add((nsnt0CF_x5>=1) == (nsnt0CF_y5>=1))
s.add((nsnt1CF_x5>=N-2*T) == (nsnt1CF_y5>=N-2*T))
s.add((nsnt01CF_x5>=N-T) == (nsnt01CF_y5>=N-T))
s.add((nsnt1CF_x5>=N-T) == (nsnt1CF_y5>=N-T))
s.add((nsnt0_x5<N-2*T) == (nsnt0_y5<N-2*T))
s.add((nsnt0CF_x5>=N-T) == (nsnt0CF_y5>=N-T))
s.add((True) == (True))
s.add((nsnt1_x5<N-2*T) == (nsnt1_y5<N-2*T))
s.add((nfaulty_x5<F) == (nfaulty_y5<F))
s.add((nsnt0CF_x5>=N-2*T) == (nsnt0CF_y5>=N-2*T))

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
locS0_x6 = Real('locS0_x6')
locS0_y6 = Real('locS0_y6')
s.add(locS0_x6 >= 0)
s.add(locS0_y6 >= 0)
locS1_x6 = Real('locS1_x6')
locS1_y6 = Real('locS1_y6')
s.add(locS1_x6 >= 0)
s.add(locS1_y6 >= 0)
locD0_x6 = Real('locD0_x6')
locD0_y6 = Real('locD0_y6')
s.add(locD0_x6 >= 0)
s.add(locD0_y6 >= 0)
locD1_x6 = Real('locD1_x6')
locD1_y6 = Real('locD1_y6')
s.add(locD1_x6 >= 0)
s.add(locD1_y6 >= 0)
locU0_x6 = Real('locU0_x6')
locU0_y6 = Real('locU0_y6')
s.add(locU0_x6 >= 0)
s.add(locU0_y6 >= 0)
locU1_x6 = Real('locU1_x6')
locU1_y6 = Real('locU1_y6')
s.add(locU1_x6 >= 0)
s.add(locU1_y6 >= 0)
locCR_x6 = Real('locCR_x6')
locCR_y6 = Real('locCR_y6')
s.add(locCR_x6 >= 0)
s.add(locCR_y6 >= 0)






#Creating many copies of shared variables

nsnt0_x6 = Real('nsnt0_x6')
nsnt0_y6 = Real('nsnt0_y6')
s.add(nsnt0_x6 >= 0)
s.add(nsnt0_y6 >= 0)
nsnt1_x6 = Real('nsnt1_x6')
nsnt1_y6 = Real('nsnt1_y6')
s.add(nsnt1_x6 >= 0)
s.add(nsnt1_y6 >= 0)
nsnt0CF_x6 = Real('nsnt0CF_x6')
nsnt0CF_y6 = Real('nsnt0CF_y6')
s.add(nsnt0CF_x6 >= 0)
s.add(nsnt0CF_y6 >= 0)
nsnt1CF_x6 = Real('nsnt1CF_x6')
nsnt1CF_y6 = Real('nsnt1CF_y6')
s.add(nsnt1CF_x6 >= 0)
s.add(nsnt1CF_y6 >= 0)
nsnt01_x6 = Real('nsnt01_x6')
nsnt01_y6 = Real('nsnt01_y6')
s.add(nsnt01_x6 >= 0)
s.add(nsnt01_y6 >= 0)
nsnt01CF_x6 = Real('nsnt01CF_x6')
nsnt01CF_y6 = Real('nsnt01CF_y6')
s.add(nsnt01CF_x6 >= 0)
s.add(nsnt01CF_y6 >= 0)
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
rule14_x6 = Real('rule14_x6')
s.add(rule14_x6 >= 0)
rule15_x6 = Real('rule15_x6')
s.add(rule15_x6 >= 0)
rule16_x6 = Real('rule16_x6')
s.add(rule16_x6 >= 0)
rule17_x6 = Real('rule17_x6')
s.add(rule17_x6 >= 0)
rule18_x6 = Real('rule18_x6')
s.add(rule18_x6 >= 0)
rule19_x6 = Real('rule19_x6')
s.add(rule19_x6 >= 0)
rule20_x6 = Real('rule20_x6')
s.add(rule20_x6 >= 0)
rule21_x6 = Real('rule21_x6')
s.add(rule21_x6 >= 0)
rule22_x6 = Real('rule22_x6')
s.add(rule22_x6 >= 0)
rule23_x6 = Real('rule23_x6')
s.add(rule23_x6 >= 0)
rule24_x6 = Real('rule24_x6')
s.add(rule24_x6 >= 0)
rule25_x6 = Real('rule25_x6')
s.add(rule25_x6 >= 0)
rule26_x6 = Real('rule26_x6')
s.add(rule26_x6 >= 0)
rule27_x6 = Real('rule27_x6')
s.add(rule27_x6 >= 0)
rule28_x6 = Real('rule28_x6')
s.add(rule28_x6 >= 0)
rule29_x6 = Real('rule29_x6')
s.add(rule29_x6 >= 0)






###################Step 2####################


#Flow equations for the locations

s.add(0 - rule0_x6 - rule1_x6 - rule14_x6 - rule22_x6 + rule22_x6 ==  loc0_y6 - loc0_x6)
s.add(0 - rule2_x6 - rule3_x6 - rule15_x6 - rule23_x6 + rule23_x6 ==  loc1_y6 - loc1_x6)
s.add(0 + rule0_x6 - rule4_x6 - rule6_x6 - rule8_x6 - rule10_x6 - rule12_x6 - rule16_x6 - rule24_x6 + rule24_x6 ==  locS0_y6 - locS0_x6)
s.add(0 + rule2_x6 - rule5_x6 - rule7_x6 - rule9_x6 - rule11_x6 - rule13_x6 - rule17_x6 - rule25_x6 + rule25_x6 ==  locS1_y6 - locS1_x6)
s.add(0 + rule4_x6 + rule5_x6 - rule18_x6 - rule26_x6 + rule26_x6 ==  locD0_y6 - locD0_x6)
s.add(0 + rule6_x6 + rule7_x6 - rule19_x6 - rule27_x6 + rule27_x6 ==  locD1_y6 - locD1_x6)
s.add(0 + rule8_x6 + rule9_x6 + rule12_x6 - rule20_x6 - rule28_x6 + rule28_x6 ==  locU0_y6 - locU0_x6)
s.add(0 + rule10_x6 + rule11_x6 + rule13_x6 - rule21_x6 - rule29_x6 + rule29_x6 ==  locU1_y6 - locU1_x6)
s.add(0 + rule1_x6 + rule3_x6 + rule14_x6 + rule15_x6 + rule16_x6 + rule17_x6 + rule18_x6 + rule19_x6 + rule20_x6 + rule21_x6 ==  locCR_y6 - locCR_x6)






##################Step 3########################


#Flow equations for the shared variables

s.add(0 + rule0_x6 == nsnt0_y6 - nsnt0_x6)
s.add(0 + rule2_x6 == nsnt1_y6 - nsnt1_x6)
s.add(0 + rule0_x6 + rule1_x6 == nsnt0CF_y6 - nsnt0CF_x6)
s.add(0 + rule2_x6 + rule3_x6 == nsnt1CF_y6 - nsnt1CF_x6)
s.add(0 + rule0_x6 + rule2_x6 == nsnt01_y6 - nsnt01_x6)
s.add(0 + rule0_x6 + rule1_x6 + rule2_x6 + rule3_x6 == nsnt01CF_y6 - nsnt01CF_x6)
s.add(0 + rule1_x6 + rule3_x6 + rule14_x6 + rule15_x6 + rule16_x6 + rule17_x6 + rule18_x6 + rule19_x6 + rule20_x6 + rule21_x6 == nfaulty_y6 - nfaulty_x6)






####################Step 4########################


#Rule is fired implies rule is enabled

s.add(Implies( (rule0_x6 > 0), And(True, ) ))
s.add(Implies( (rule1_x6 > 0), And(nfaulty_x6<F, ) ))
s.add(Implies( (rule2_x6 > 0), And(True, ) ))
s.add(Implies( (rule3_x6 > 0), And(nfaulty_x6<F, ) ))
s.add(Implies( (rule4_x6 > 0), And(nsnt0CF_x6>=N-T, ) ))
s.add(Implies( (rule5_x6 > 0), And(nsnt0CF_x6>=N-T, ) ))
s.add(Implies( (rule6_x6 > 0), And(nsnt1CF_x6>=N-T, ) ))
s.add(Implies( (rule7_x6 > 0), And(nsnt1CF_x6>=N-T, ) ))
s.add(Implies( (rule8_x6 > 0), And(nsnt01CF_x6>=N-T, nsnt0CF_x6>=N-2*T, nsnt1CF_x6>=1, ) ))
s.add(Implies( (rule9_x6 > 0), And(nsnt01CF_x6>=N-T, nsnt0CF_x6>=N-2*T, nsnt1CF_x6>=1, ) ))
s.add(Implies( (rule10_x6 > 0), And(nsnt01CF_x6>=N-T, nsnt1CF_x6>=N-2*T, nsnt0CF_x6>=1, ) ))
s.add(Implies( (rule11_x6 > 0), And(nsnt01CF_x6>=N-T, nsnt1CF_x6>=N-2*T, nsnt0CF_x6>=1, ) ))
s.add(Implies( (rule12_x6 > 0), And(nsnt01CF_x6>=N-T, nsnt0_x6<N-2*T, nsnt1_x6<N-2*T, ) ))
s.add(Implies( (rule13_x6 > 0), And(nsnt01CF_x6>=N-T, nsnt0_x6<N-2*T, nsnt1_x6<N-2*T, ) ))
s.add(Implies( (rule14_x6 > 0), And(nfaulty_x6<F, ) ))
s.add(Implies( (rule15_x6 > 0), And(nfaulty_x6<F, ) ))
s.add(Implies( (rule16_x6 > 0), And(nfaulty_x6<F, ) ))
s.add(Implies( (rule17_x6 > 0), And(nfaulty_x6<F, ) ))
s.add(Implies( (rule18_x6 > 0), And(nfaulty_x6<F, ) ))
s.add(Implies( (rule19_x6 > 0), And(nfaulty_x6<F, ) ))
s.add(Implies( (rule20_x6 > 0), And(nfaulty_x6<F, ) ))
s.add(Implies( (rule21_x6 > 0), And(nfaulty_x6<F, ) ))
s.add(Implies( (rule22_x6 > 0), And(True, ) ))
s.add(Implies( (rule23_x6 > 0), And(True, ) ))
s.add(Implies( (rule24_x6 > 0), And(True, ) ))
s.add(Implies( (rule25_x6 > 0), And(True, ) ))
s.add(Implies( (rule26_x6 > 0), And(True, ) ))
s.add(Implies( (rule27_x6 > 0), And(True, ) ))
s.add(Implies( (rule28_x6 > 0), And(True, ) ))
s.add(Implies( (rule29_x6 > 0), And(True, ) ))

##################Step 5#########################


#Ensuring that configurations x6 and y6 have the same context

s.add((nsnt1CF_x6>=1) == (nsnt1CF_y6>=1))
s.add((nsnt0CF_x6>=1) == (nsnt0CF_y6>=1))
s.add((nsnt1CF_x6>=N-2*T) == (nsnt1CF_y6>=N-2*T))
s.add((nsnt01CF_x6>=N-T) == (nsnt01CF_y6>=N-T))
s.add((nsnt1CF_x6>=N-T) == (nsnt1CF_y6>=N-T))
s.add((nsnt0_x6<N-2*T) == (nsnt0_y6<N-2*T))
s.add((nsnt0CF_x6>=N-T) == (nsnt0CF_y6>=N-T))
s.add((True) == (True))
s.add((nsnt1_x6<N-2*T) == (nsnt1_y6<N-2*T))
s.add((nfaulty_x6<F) == (nfaulty_y6<F))
s.add((nsnt0CF_x6>=N-2*T) == (nsnt0CF_y6>=N-2*T))

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
locS0_x7 = Real('locS0_x7')
locS0_y7 = Real('locS0_y7')
s.add(locS0_x7 >= 0)
s.add(locS0_y7 >= 0)
locS1_x7 = Real('locS1_x7')
locS1_y7 = Real('locS1_y7')
s.add(locS1_x7 >= 0)
s.add(locS1_y7 >= 0)
locD0_x7 = Real('locD0_x7')
locD0_y7 = Real('locD0_y7')
s.add(locD0_x7 >= 0)
s.add(locD0_y7 >= 0)
locD1_x7 = Real('locD1_x7')
locD1_y7 = Real('locD1_y7')
s.add(locD1_x7 >= 0)
s.add(locD1_y7 >= 0)
locU0_x7 = Real('locU0_x7')
locU0_y7 = Real('locU0_y7')
s.add(locU0_x7 >= 0)
s.add(locU0_y7 >= 0)
locU1_x7 = Real('locU1_x7')
locU1_y7 = Real('locU1_y7')
s.add(locU1_x7 >= 0)
s.add(locU1_y7 >= 0)
locCR_x7 = Real('locCR_x7')
locCR_y7 = Real('locCR_y7')
s.add(locCR_x7 >= 0)
s.add(locCR_y7 >= 0)






#Creating many copies of shared variables

nsnt0_x7 = Real('nsnt0_x7')
nsnt0_y7 = Real('nsnt0_y7')
s.add(nsnt0_x7 >= 0)
s.add(nsnt0_y7 >= 0)
nsnt1_x7 = Real('nsnt1_x7')
nsnt1_y7 = Real('nsnt1_y7')
s.add(nsnt1_x7 >= 0)
s.add(nsnt1_y7 >= 0)
nsnt0CF_x7 = Real('nsnt0CF_x7')
nsnt0CF_y7 = Real('nsnt0CF_y7')
s.add(nsnt0CF_x7 >= 0)
s.add(nsnt0CF_y7 >= 0)
nsnt1CF_x7 = Real('nsnt1CF_x7')
nsnt1CF_y7 = Real('nsnt1CF_y7')
s.add(nsnt1CF_x7 >= 0)
s.add(nsnt1CF_y7 >= 0)
nsnt01_x7 = Real('nsnt01_x7')
nsnt01_y7 = Real('nsnt01_y7')
s.add(nsnt01_x7 >= 0)
s.add(nsnt01_y7 >= 0)
nsnt01CF_x7 = Real('nsnt01CF_x7')
nsnt01CF_y7 = Real('nsnt01CF_y7')
s.add(nsnt01CF_x7 >= 0)
s.add(nsnt01CF_y7 >= 0)
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
rule14_x7 = Real('rule14_x7')
s.add(rule14_x7 >= 0)
rule15_x7 = Real('rule15_x7')
s.add(rule15_x7 >= 0)
rule16_x7 = Real('rule16_x7')
s.add(rule16_x7 >= 0)
rule17_x7 = Real('rule17_x7')
s.add(rule17_x7 >= 0)
rule18_x7 = Real('rule18_x7')
s.add(rule18_x7 >= 0)
rule19_x7 = Real('rule19_x7')
s.add(rule19_x7 >= 0)
rule20_x7 = Real('rule20_x7')
s.add(rule20_x7 >= 0)
rule21_x7 = Real('rule21_x7')
s.add(rule21_x7 >= 0)
rule22_x7 = Real('rule22_x7')
s.add(rule22_x7 >= 0)
rule23_x7 = Real('rule23_x7')
s.add(rule23_x7 >= 0)
rule24_x7 = Real('rule24_x7')
s.add(rule24_x7 >= 0)
rule25_x7 = Real('rule25_x7')
s.add(rule25_x7 >= 0)
rule26_x7 = Real('rule26_x7')
s.add(rule26_x7 >= 0)
rule27_x7 = Real('rule27_x7')
s.add(rule27_x7 >= 0)
rule28_x7 = Real('rule28_x7')
s.add(rule28_x7 >= 0)
rule29_x7 = Real('rule29_x7')
s.add(rule29_x7 >= 0)






###################Step 2####################


#Flow equations for the locations

s.add(0 - rule0_x7 - rule1_x7 - rule14_x7 - rule22_x7 + rule22_x7 ==  loc0_y7 - loc0_x7)
s.add(0 - rule2_x7 - rule3_x7 - rule15_x7 - rule23_x7 + rule23_x7 ==  loc1_y7 - loc1_x7)
s.add(0 + rule0_x7 - rule4_x7 - rule6_x7 - rule8_x7 - rule10_x7 - rule12_x7 - rule16_x7 - rule24_x7 + rule24_x7 ==  locS0_y7 - locS0_x7)
s.add(0 + rule2_x7 - rule5_x7 - rule7_x7 - rule9_x7 - rule11_x7 - rule13_x7 - rule17_x7 - rule25_x7 + rule25_x7 ==  locS1_y7 - locS1_x7)
s.add(0 + rule4_x7 + rule5_x7 - rule18_x7 - rule26_x7 + rule26_x7 ==  locD0_y7 - locD0_x7)
s.add(0 + rule6_x7 + rule7_x7 - rule19_x7 - rule27_x7 + rule27_x7 ==  locD1_y7 - locD1_x7)
s.add(0 + rule8_x7 + rule9_x7 + rule12_x7 - rule20_x7 - rule28_x7 + rule28_x7 ==  locU0_y7 - locU0_x7)
s.add(0 + rule10_x7 + rule11_x7 + rule13_x7 - rule21_x7 - rule29_x7 + rule29_x7 ==  locU1_y7 - locU1_x7)
s.add(0 + rule1_x7 + rule3_x7 + rule14_x7 + rule15_x7 + rule16_x7 + rule17_x7 + rule18_x7 + rule19_x7 + rule20_x7 + rule21_x7 ==  locCR_y7 - locCR_x7)






##################Step 3########################


#Flow equations for the shared variables

s.add(0 + rule0_x7 == nsnt0_y7 - nsnt0_x7)
s.add(0 + rule2_x7 == nsnt1_y7 - nsnt1_x7)
s.add(0 + rule0_x7 + rule1_x7 == nsnt0CF_y7 - nsnt0CF_x7)
s.add(0 + rule2_x7 + rule3_x7 == nsnt1CF_y7 - nsnt1CF_x7)
s.add(0 + rule0_x7 + rule2_x7 == nsnt01_y7 - nsnt01_x7)
s.add(0 + rule0_x7 + rule1_x7 + rule2_x7 + rule3_x7 == nsnt01CF_y7 - nsnt01CF_x7)
s.add(0 + rule1_x7 + rule3_x7 + rule14_x7 + rule15_x7 + rule16_x7 + rule17_x7 + rule18_x7 + rule19_x7 + rule20_x7 + rule21_x7 == nfaulty_y7 - nfaulty_x7)






####################Step 4########################


#Rule is fired implies rule is enabled

s.add(Implies( (rule0_x7 > 0), And(True, ) ))
s.add(Implies( (rule1_x7 > 0), And(nfaulty_x7<F, ) ))
s.add(Implies( (rule2_x7 > 0), And(True, ) ))
s.add(Implies( (rule3_x7 > 0), And(nfaulty_x7<F, ) ))
s.add(Implies( (rule4_x7 > 0), And(nsnt0CF_x7>=N-T, ) ))
s.add(Implies( (rule5_x7 > 0), And(nsnt0CF_x7>=N-T, ) ))
s.add(Implies( (rule6_x7 > 0), And(nsnt1CF_x7>=N-T, ) ))
s.add(Implies( (rule7_x7 > 0), And(nsnt1CF_x7>=N-T, ) ))
s.add(Implies( (rule8_x7 > 0), And(nsnt01CF_x7>=N-T, nsnt0CF_x7>=N-2*T, nsnt1CF_x7>=1, ) ))
s.add(Implies( (rule9_x7 > 0), And(nsnt01CF_x7>=N-T, nsnt0CF_x7>=N-2*T, nsnt1CF_x7>=1, ) ))
s.add(Implies( (rule10_x7 > 0), And(nsnt01CF_x7>=N-T, nsnt1CF_x7>=N-2*T, nsnt0CF_x7>=1, ) ))
s.add(Implies( (rule11_x7 > 0), And(nsnt01CF_x7>=N-T, nsnt1CF_x7>=N-2*T, nsnt0CF_x7>=1, ) ))
s.add(Implies( (rule12_x7 > 0), And(nsnt01CF_x7>=N-T, nsnt0_x7<N-2*T, nsnt1_x7<N-2*T, ) ))
s.add(Implies( (rule13_x7 > 0), And(nsnt01CF_x7>=N-T, nsnt0_x7<N-2*T, nsnt1_x7<N-2*T, ) ))
s.add(Implies( (rule14_x7 > 0), And(nfaulty_x7<F, ) ))
s.add(Implies( (rule15_x7 > 0), And(nfaulty_x7<F, ) ))
s.add(Implies( (rule16_x7 > 0), And(nfaulty_x7<F, ) ))
s.add(Implies( (rule17_x7 > 0), And(nfaulty_x7<F, ) ))
s.add(Implies( (rule18_x7 > 0), And(nfaulty_x7<F, ) ))
s.add(Implies( (rule19_x7 > 0), And(nfaulty_x7<F, ) ))
s.add(Implies( (rule20_x7 > 0), And(nfaulty_x7<F, ) ))
s.add(Implies( (rule21_x7 > 0), And(nfaulty_x7<F, ) ))
s.add(Implies( (rule22_x7 > 0), And(True, ) ))
s.add(Implies( (rule23_x7 > 0), And(True, ) ))
s.add(Implies( (rule24_x7 > 0), And(True, ) ))
s.add(Implies( (rule25_x7 > 0), And(True, ) ))
s.add(Implies( (rule26_x7 > 0), And(True, ) ))
s.add(Implies( (rule27_x7 > 0), And(True, ) ))
s.add(Implies( (rule28_x7 > 0), And(True, ) ))
s.add(Implies( (rule29_x7 > 0), And(True, ) ))

##################Step 5#########################


#Ensuring that configurations x7 and y7 have the same context

s.add((nsnt1CF_x7>=1) == (nsnt1CF_y7>=1))
s.add((nsnt0CF_x7>=1) == (nsnt0CF_y7>=1))
s.add((nsnt1CF_x7>=N-2*T) == (nsnt1CF_y7>=N-2*T))
s.add((nsnt01CF_x7>=N-T) == (nsnt01CF_y7>=N-T))
s.add((nsnt1CF_x7>=N-T) == (nsnt1CF_y7>=N-T))
s.add((nsnt0_x7<N-2*T) == (nsnt0_y7<N-2*T))
s.add((nsnt0CF_x7>=N-T) == (nsnt0CF_y7>=N-T))
s.add((True) == (True))
s.add((nsnt1_x7<N-2*T) == (nsnt1_y7<N-2*T))
s.add((nfaulty_x7<F) == (nfaulty_y7<F))
s.add((nsnt0CF_x7>=N-2*T) == (nsnt0CF_y7>=N-2*T))

####################################################################################

#Creating constraints for a run between the x8th and y8th configurations

################Step 1#################


#Creating many copies of location variables

loc0_x8 = Real('loc0_x8')
loc0_y8 = Real('loc0_y8')
s.add(loc0_x8 >= 0)
s.add(loc0_y8 >= 0)
loc1_x8 = Real('loc1_x8')
loc1_y8 = Real('loc1_y8')
s.add(loc1_x8 >= 0)
s.add(loc1_y8 >= 0)
locS0_x8 = Real('locS0_x8')
locS0_y8 = Real('locS0_y8')
s.add(locS0_x8 >= 0)
s.add(locS0_y8 >= 0)
locS1_x8 = Real('locS1_x8')
locS1_y8 = Real('locS1_y8')
s.add(locS1_x8 >= 0)
s.add(locS1_y8 >= 0)
locD0_x8 = Real('locD0_x8')
locD0_y8 = Real('locD0_y8')
s.add(locD0_x8 >= 0)
s.add(locD0_y8 >= 0)
locD1_x8 = Real('locD1_x8')
locD1_y8 = Real('locD1_y8')
s.add(locD1_x8 >= 0)
s.add(locD1_y8 >= 0)
locU0_x8 = Real('locU0_x8')
locU0_y8 = Real('locU0_y8')
s.add(locU0_x8 >= 0)
s.add(locU0_y8 >= 0)
locU1_x8 = Real('locU1_x8')
locU1_y8 = Real('locU1_y8')
s.add(locU1_x8 >= 0)
s.add(locU1_y8 >= 0)
locCR_x8 = Real('locCR_x8')
locCR_y8 = Real('locCR_y8')
s.add(locCR_x8 >= 0)
s.add(locCR_y8 >= 0)






#Creating many copies of shared variables

nsnt0_x8 = Real('nsnt0_x8')
nsnt0_y8 = Real('nsnt0_y8')
s.add(nsnt0_x8 >= 0)
s.add(nsnt0_y8 >= 0)
nsnt1_x8 = Real('nsnt1_x8')
nsnt1_y8 = Real('nsnt1_y8')
s.add(nsnt1_x8 >= 0)
s.add(nsnt1_y8 >= 0)
nsnt0CF_x8 = Real('nsnt0CF_x8')
nsnt0CF_y8 = Real('nsnt0CF_y8')
s.add(nsnt0CF_x8 >= 0)
s.add(nsnt0CF_y8 >= 0)
nsnt1CF_x8 = Real('nsnt1CF_x8')
nsnt1CF_y8 = Real('nsnt1CF_y8')
s.add(nsnt1CF_x8 >= 0)
s.add(nsnt1CF_y8 >= 0)
nsnt01_x8 = Real('nsnt01_x8')
nsnt01_y8 = Real('nsnt01_y8')
s.add(nsnt01_x8 >= 0)
s.add(nsnt01_y8 >= 0)
nsnt01CF_x8 = Real('nsnt01CF_x8')
nsnt01CF_y8 = Real('nsnt01CF_y8')
s.add(nsnt01CF_x8 >= 0)
s.add(nsnt01CF_y8 >= 0)
nfaulty_x8 = Real('nfaulty_x8')
nfaulty_y8 = Real('nfaulty_y8')
s.add(nfaulty_x8 >= 0)
s.add(nfaulty_y8 >= 0)






#Creating many copies of variables for rules

rule0_x8 = Real('rule0_x8')
s.add(rule0_x8 >= 0)
rule1_x8 = Real('rule1_x8')
s.add(rule1_x8 >= 0)
rule2_x8 = Real('rule2_x8')
s.add(rule2_x8 >= 0)
rule3_x8 = Real('rule3_x8')
s.add(rule3_x8 >= 0)
rule4_x8 = Real('rule4_x8')
s.add(rule4_x8 >= 0)
rule5_x8 = Real('rule5_x8')
s.add(rule5_x8 >= 0)
rule6_x8 = Real('rule6_x8')
s.add(rule6_x8 >= 0)
rule7_x8 = Real('rule7_x8')
s.add(rule7_x8 >= 0)
rule8_x8 = Real('rule8_x8')
s.add(rule8_x8 >= 0)
rule9_x8 = Real('rule9_x8')
s.add(rule9_x8 >= 0)
rule10_x8 = Real('rule10_x8')
s.add(rule10_x8 >= 0)
rule11_x8 = Real('rule11_x8')
s.add(rule11_x8 >= 0)
rule12_x8 = Real('rule12_x8')
s.add(rule12_x8 >= 0)
rule13_x8 = Real('rule13_x8')
s.add(rule13_x8 >= 0)
rule14_x8 = Real('rule14_x8')
s.add(rule14_x8 >= 0)
rule15_x8 = Real('rule15_x8')
s.add(rule15_x8 >= 0)
rule16_x8 = Real('rule16_x8')
s.add(rule16_x8 >= 0)
rule17_x8 = Real('rule17_x8')
s.add(rule17_x8 >= 0)
rule18_x8 = Real('rule18_x8')
s.add(rule18_x8 >= 0)
rule19_x8 = Real('rule19_x8')
s.add(rule19_x8 >= 0)
rule20_x8 = Real('rule20_x8')
s.add(rule20_x8 >= 0)
rule21_x8 = Real('rule21_x8')
s.add(rule21_x8 >= 0)
rule22_x8 = Real('rule22_x8')
s.add(rule22_x8 >= 0)
rule23_x8 = Real('rule23_x8')
s.add(rule23_x8 >= 0)
rule24_x8 = Real('rule24_x8')
s.add(rule24_x8 >= 0)
rule25_x8 = Real('rule25_x8')
s.add(rule25_x8 >= 0)
rule26_x8 = Real('rule26_x8')
s.add(rule26_x8 >= 0)
rule27_x8 = Real('rule27_x8')
s.add(rule27_x8 >= 0)
rule28_x8 = Real('rule28_x8')
s.add(rule28_x8 >= 0)
rule29_x8 = Real('rule29_x8')
s.add(rule29_x8 >= 0)






###################Step 2####################


#Flow equations for the locations

s.add(0 - rule0_x8 - rule1_x8 - rule14_x8 - rule22_x8 + rule22_x8 ==  loc0_y8 - loc0_x8)
s.add(0 - rule2_x8 - rule3_x8 - rule15_x8 - rule23_x8 + rule23_x8 ==  loc1_y8 - loc1_x8)
s.add(0 + rule0_x8 - rule4_x8 - rule6_x8 - rule8_x8 - rule10_x8 - rule12_x8 - rule16_x8 - rule24_x8 + rule24_x8 ==  locS0_y8 - locS0_x8)
s.add(0 + rule2_x8 - rule5_x8 - rule7_x8 - rule9_x8 - rule11_x8 - rule13_x8 - rule17_x8 - rule25_x8 + rule25_x8 ==  locS1_y8 - locS1_x8)
s.add(0 + rule4_x8 + rule5_x8 - rule18_x8 - rule26_x8 + rule26_x8 ==  locD0_y8 - locD0_x8)
s.add(0 + rule6_x8 + rule7_x8 - rule19_x8 - rule27_x8 + rule27_x8 ==  locD1_y8 - locD1_x8)
s.add(0 + rule8_x8 + rule9_x8 + rule12_x8 - rule20_x8 - rule28_x8 + rule28_x8 ==  locU0_y8 - locU0_x8)
s.add(0 + rule10_x8 + rule11_x8 + rule13_x8 - rule21_x8 - rule29_x8 + rule29_x8 ==  locU1_y8 - locU1_x8)
s.add(0 + rule1_x8 + rule3_x8 + rule14_x8 + rule15_x8 + rule16_x8 + rule17_x8 + rule18_x8 + rule19_x8 + rule20_x8 + rule21_x8 ==  locCR_y8 - locCR_x8)






##################Step 3########################


#Flow equations for the shared variables

s.add(0 + rule0_x8 == nsnt0_y8 - nsnt0_x8)
s.add(0 + rule2_x8 == nsnt1_y8 - nsnt1_x8)
s.add(0 + rule0_x8 + rule1_x8 == nsnt0CF_y8 - nsnt0CF_x8)
s.add(0 + rule2_x8 + rule3_x8 == nsnt1CF_y8 - nsnt1CF_x8)
s.add(0 + rule0_x8 + rule2_x8 == nsnt01_y8 - nsnt01_x8)
s.add(0 + rule0_x8 + rule1_x8 + rule2_x8 + rule3_x8 == nsnt01CF_y8 - nsnt01CF_x8)
s.add(0 + rule1_x8 + rule3_x8 + rule14_x8 + rule15_x8 + rule16_x8 + rule17_x8 + rule18_x8 + rule19_x8 + rule20_x8 + rule21_x8 == nfaulty_y8 - nfaulty_x8)






####################Step 4########################


#Rule is fired implies rule is enabled

s.add(Implies( (rule0_x8 > 0), And(True, ) ))
s.add(Implies( (rule1_x8 > 0), And(nfaulty_x8<F, ) ))
s.add(Implies( (rule2_x8 > 0), And(True, ) ))
s.add(Implies( (rule3_x8 > 0), And(nfaulty_x8<F, ) ))
s.add(Implies( (rule4_x8 > 0), And(nsnt0CF_x8>=N-T, ) ))
s.add(Implies( (rule5_x8 > 0), And(nsnt0CF_x8>=N-T, ) ))
s.add(Implies( (rule6_x8 > 0), And(nsnt1CF_x8>=N-T, ) ))
s.add(Implies( (rule7_x8 > 0), And(nsnt1CF_x8>=N-T, ) ))
s.add(Implies( (rule8_x8 > 0), And(nsnt01CF_x8>=N-T, nsnt0CF_x8>=N-2*T, nsnt1CF_x8>=1, ) ))
s.add(Implies( (rule9_x8 > 0), And(nsnt01CF_x8>=N-T, nsnt0CF_x8>=N-2*T, nsnt1CF_x8>=1, ) ))
s.add(Implies( (rule10_x8 > 0), And(nsnt01CF_x8>=N-T, nsnt1CF_x8>=N-2*T, nsnt0CF_x8>=1, ) ))
s.add(Implies( (rule11_x8 > 0), And(nsnt01CF_x8>=N-T, nsnt1CF_x8>=N-2*T, nsnt0CF_x8>=1, ) ))
s.add(Implies( (rule12_x8 > 0), And(nsnt01CF_x8>=N-T, nsnt0_x8<N-2*T, nsnt1_x8<N-2*T, ) ))
s.add(Implies( (rule13_x8 > 0), And(nsnt01CF_x8>=N-T, nsnt0_x8<N-2*T, nsnt1_x8<N-2*T, ) ))
s.add(Implies( (rule14_x8 > 0), And(nfaulty_x8<F, ) ))
s.add(Implies( (rule15_x8 > 0), And(nfaulty_x8<F, ) ))
s.add(Implies( (rule16_x8 > 0), And(nfaulty_x8<F, ) ))
s.add(Implies( (rule17_x8 > 0), And(nfaulty_x8<F, ) ))
s.add(Implies( (rule18_x8 > 0), And(nfaulty_x8<F, ) ))
s.add(Implies( (rule19_x8 > 0), And(nfaulty_x8<F, ) ))
s.add(Implies( (rule20_x8 > 0), And(nfaulty_x8<F, ) ))
s.add(Implies( (rule21_x8 > 0), And(nfaulty_x8<F, ) ))
s.add(Implies( (rule22_x8 > 0), And(True, ) ))
s.add(Implies( (rule23_x8 > 0), And(True, ) ))
s.add(Implies( (rule24_x8 > 0), And(True, ) ))
s.add(Implies( (rule25_x8 > 0), And(True, ) ))
s.add(Implies( (rule26_x8 > 0), And(True, ) ))
s.add(Implies( (rule27_x8 > 0), And(True, ) ))
s.add(Implies( (rule28_x8 > 0), And(True, ) ))
s.add(Implies( (rule29_x8 > 0), And(True, ) ))

##################Step 5#########################


#Ensuring that configurations x8 and y8 have the same context

s.add((nsnt1CF_x8>=1) == (nsnt1CF_y8>=1))
s.add((nsnt0CF_x8>=1) == (nsnt0CF_y8>=1))
s.add((nsnt1CF_x8>=N-2*T) == (nsnt1CF_y8>=N-2*T))
s.add((nsnt01CF_x8>=N-T) == (nsnt01CF_y8>=N-T))
s.add((nsnt1CF_x8>=N-T) == (nsnt1CF_y8>=N-T))
s.add((nsnt0_x8<N-2*T) == (nsnt0_y8<N-2*T))
s.add((nsnt0CF_x8>=N-T) == (nsnt0CF_y8>=N-T))
s.add((True) == (True))
s.add((nsnt1_x8<N-2*T) == (nsnt1_y8<N-2*T))
s.add((nfaulty_x8<F) == (nfaulty_y8<F))
s.add((nsnt0CF_x8>=N-2*T) == (nsnt0CF_y8>=N-2*T))

####################################################################################

#Creating constraints for a run between the x9th and y9th configurations

################Step 1#################


#Creating many copies of location variables

loc0_x9 = Real('loc0_x9')
loc0_y9 = Real('loc0_y9')
s.add(loc0_x9 >= 0)
s.add(loc0_y9 >= 0)
loc1_x9 = Real('loc1_x9')
loc1_y9 = Real('loc1_y9')
s.add(loc1_x9 >= 0)
s.add(loc1_y9 >= 0)
locS0_x9 = Real('locS0_x9')
locS0_y9 = Real('locS0_y9')
s.add(locS0_x9 >= 0)
s.add(locS0_y9 >= 0)
locS1_x9 = Real('locS1_x9')
locS1_y9 = Real('locS1_y9')
s.add(locS1_x9 >= 0)
s.add(locS1_y9 >= 0)
locD0_x9 = Real('locD0_x9')
locD0_y9 = Real('locD0_y9')
s.add(locD0_x9 >= 0)
s.add(locD0_y9 >= 0)
locD1_x9 = Real('locD1_x9')
locD1_y9 = Real('locD1_y9')
s.add(locD1_x9 >= 0)
s.add(locD1_y9 >= 0)
locU0_x9 = Real('locU0_x9')
locU0_y9 = Real('locU0_y9')
s.add(locU0_x9 >= 0)
s.add(locU0_y9 >= 0)
locU1_x9 = Real('locU1_x9')
locU1_y9 = Real('locU1_y9')
s.add(locU1_x9 >= 0)
s.add(locU1_y9 >= 0)
locCR_x9 = Real('locCR_x9')
locCR_y9 = Real('locCR_y9')
s.add(locCR_x9 >= 0)
s.add(locCR_y9 >= 0)






#Creating many copies of shared variables

nsnt0_x9 = Real('nsnt0_x9')
nsnt0_y9 = Real('nsnt0_y9')
s.add(nsnt0_x9 >= 0)
s.add(nsnt0_y9 >= 0)
nsnt1_x9 = Real('nsnt1_x9')
nsnt1_y9 = Real('nsnt1_y9')
s.add(nsnt1_x9 >= 0)
s.add(nsnt1_y9 >= 0)
nsnt0CF_x9 = Real('nsnt0CF_x9')
nsnt0CF_y9 = Real('nsnt0CF_y9')
s.add(nsnt0CF_x9 >= 0)
s.add(nsnt0CF_y9 >= 0)
nsnt1CF_x9 = Real('nsnt1CF_x9')
nsnt1CF_y9 = Real('nsnt1CF_y9')
s.add(nsnt1CF_x9 >= 0)
s.add(nsnt1CF_y9 >= 0)
nsnt01_x9 = Real('nsnt01_x9')
nsnt01_y9 = Real('nsnt01_y9')
s.add(nsnt01_x9 >= 0)
s.add(nsnt01_y9 >= 0)
nsnt01CF_x9 = Real('nsnt01CF_x9')
nsnt01CF_y9 = Real('nsnt01CF_y9')
s.add(nsnt01CF_x9 >= 0)
s.add(nsnt01CF_y9 >= 0)
nfaulty_x9 = Real('nfaulty_x9')
nfaulty_y9 = Real('nfaulty_y9')
s.add(nfaulty_x9 >= 0)
s.add(nfaulty_y9 >= 0)






#Creating many copies of variables for rules

rule0_x9 = Real('rule0_x9')
s.add(rule0_x9 >= 0)
rule1_x9 = Real('rule1_x9')
s.add(rule1_x9 >= 0)
rule2_x9 = Real('rule2_x9')
s.add(rule2_x9 >= 0)
rule3_x9 = Real('rule3_x9')
s.add(rule3_x9 >= 0)
rule4_x9 = Real('rule4_x9')
s.add(rule4_x9 >= 0)
rule5_x9 = Real('rule5_x9')
s.add(rule5_x9 >= 0)
rule6_x9 = Real('rule6_x9')
s.add(rule6_x9 >= 0)
rule7_x9 = Real('rule7_x9')
s.add(rule7_x9 >= 0)
rule8_x9 = Real('rule8_x9')
s.add(rule8_x9 >= 0)
rule9_x9 = Real('rule9_x9')
s.add(rule9_x9 >= 0)
rule10_x9 = Real('rule10_x9')
s.add(rule10_x9 >= 0)
rule11_x9 = Real('rule11_x9')
s.add(rule11_x9 >= 0)
rule12_x9 = Real('rule12_x9')
s.add(rule12_x9 >= 0)
rule13_x9 = Real('rule13_x9')
s.add(rule13_x9 >= 0)
rule14_x9 = Real('rule14_x9')
s.add(rule14_x9 >= 0)
rule15_x9 = Real('rule15_x9')
s.add(rule15_x9 >= 0)
rule16_x9 = Real('rule16_x9')
s.add(rule16_x9 >= 0)
rule17_x9 = Real('rule17_x9')
s.add(rule17_x9 >= 0)
rule18_x9 = Real('rule18_x9')
s.add(rule18_x9 >= 0)
rule19_x9 = Real('rule19_x9')
s.add(rule19_x9 >= 0)
rule20_x9 = Real('rule20_x9')
s.add(rule20_x9 >= 0)
rule21_x9 = Real('rule21_x9')
s.add(rule21_x9 >= 0)
rule22_x9 = Real('rule22_x9')
s.add(rule22_x9 >= 0)
rule23_x9 = Real('rule23_x9')
s.add(rule23_x9 >= 0)
rule24_x9 = Real('rule24_x9')
s.add(rule24_x9 >= 0)
rule25_x9 = Real('rule25_x9')
s.add(rule25_x9 >= 0)
rule26_x9 = Real('rule26_x9')
s.add(rule26_x9 >= 0)
rule27_x9 = Real('rule27_x9')
s.add(rule27_x9 >= 0)
rule28_x9 = Real('rule28_x9')
s.add(rule28_x9 >= 0)
rule29_x9 = Real('rule29_x9')
s.add(rule29_x9 >= 0)






###################Step 2####################


#Flow equations for the locations

s.add(0 - rule0_x9 - rule1_x9 - rule14_x9 - rule22_x9 + rule22_x9 ==  loc0_y9 - loc0_x9)
s.add(0 - rule2_x9 - rule3_x9 - rule15_x9 - rule23_x9 + rule23_x9 ==  loc1_y9 - loc1_x9)
s.add(0 + rule0_x9 - rule4_x9 - rule6_x9 - rule8_x9 - rule10_x9 - rule12_x9 - rule16_x9 - rule24_x9 + rule24_x9 ==  locS0_y9 - locS0_x9)
s.add(0 + rule2_x9 - rule5_x9 - rule7_x9 - rule9_x9 - rule11_x9 - rule13_x9 - rule17_x9 - rule25_x9 + rule25_x9 ==  locS1_y9 - locS1_x9)
s.add(0 + rule4_x9 + rule5_x9 - rule18_x9 - rule26_x9 + rule26_x9 ==  locD0_y9 - locD0_x9)
s.add(0 + rule6_x9 + rule7_x9 - rule19_x9 - rule27_x9 + rule27_x9 ==  locD1_y9 - locD1_x9)
s.add(0 + rule8_x9 + rule9_x9 + rule12_x9 - rule20_x9 - rule28_x9 + rule28_x9 ==  locU0_y9 - locU0_x9)
s.add(0 + rule10_x9 + rule11_x9 + rule13_x9 - rule21_x9 - rule29_x9 + rule29_x9 ==  locU1_y9 - locU1_x9)
s.add(0 + rule1_x9 + rule3_x9 + rule14_x9 + rule15_x9 + rule16_x9 + rule17_x9 + rule18_x9 + rule19_x9 + rule20_x9 + rule21_x9 ==  locCR_y9 - locCR_x9)






##################Step 3########################


#Flow equations for the shared variables

s.add(0 + rule0_x9 == nsnt0_y9 - nsnt0_x9)
s.add(0 + rule2_x9 == nsnt1_y9 - nsnt1_x9)
s.add(0 + rule0_x9 + rule1_x9 == nsnt0CF_y9 - nsnt0CF_x9)
s.add(0 + rule2_x9 + rule3_x9 == nsnt1CF_y9 - nsnt1CF_x9)
s.add(0 + rule0_x9 + rule2_x9 == nsnt01_y9 - nsnt01_x9)
s.add(0 + rule0_x9 + rule1_x9 + rule2_x9 + rule3_x9 == nsnt01CF_y9 - nsnt01CF_x9)
s.add(0 + rule1_x9 + rule3_x9 + rule14_x9 + rule15_x9 + rule16_x9 + rule17_x9 + rule18_x9 + rule19_x9 + rule20_x9 + rule21_x9 == nfaulty_y9 - nfaulty_x9)






####################Step 4########################


#Rule is fired implies rule is enabled

s.add(Implies( (rule0_x9 > 0), And(True, ) ))
s.add(Implies( (rule1_x9 > 0), And(nfaulty_x9<F, ) ))
s.add(Implies( (rule2_x9 > 0), And(True, ) ))
s.add(Implies( (rule3_x9 > 0), And(nfaulty_x9<F, ) ))
s.add(Implies( (rule4_x9 > 0), And(nsnt0CF_x9>=N-T, ) ))
s.add(Implies( (rule5_x9 > 0), And(nsnt0CF_x9>=N-T, ) ))
s.add(Implies( (rule6_x9 > 0), And(nsnt1CF_x9>=N-T, ) ))
s.add(Implies( (rule7_x9 > 0), And(nsnt1CF_x9>=N-T, ) ))
s.add(Implies( (rule8_x9 > 0), And(nsnt01CF_x9>=N-T, nsnt0CF_x9>=N-2*T, nsnt1CF_x9>=1, ) ))
s.add(Implies( (rule9_x9 > 0), And(nsnt01CF_x9>=N-T, nsnt0CF_x9>=N-2*T, nsnt1CF_x9>=1, ) ))
s.add(Implies( (rule10_x9 > 0), And(nsnt01CF_x9>=N-T, nsnt1CF_x9>=N-2*T, nsnt0CF_x9>=1, ) ))
s.add(Implies( (rule11_x9 > 0), And(nsnt01CF_x9>=N-T, nsnt1CF_x9>=N-2*T, nsnt0CF_x9>=1, ) ))
s.add(Implies( (rule12_x9 > 0), And(nsnt01CF_x9>=N-T, nsnt0_x9<N-2*T, nsnt1_x9<N-2*T, ) ))
s.add(Implies( (rule13_x9 > 0), And(nsnt01CF_x9>=N-T, nsnt0_x9<N-2*T, nsnt1_x9<N-2*T, ) ))
s.add(Implies( (rule14_x9 > 0), And(nfaulty_x9<F, ) ))
s.add(Implies( (rule15_x9 > 0), And(nfaulty_x9<F, ) ))
s.add(Implies( (rule16_x9 > 0), And(nfaulty_x9<F, ) ))
s.add(Implies( (rule17_x9 > 0), And(nfaulty_x9<F, ) ))
s.add(Implies( (rule18_x9 > 0), And(nfaulty_x9<F, ) ))
s.add(Implies( (rule19_x9 > 0), And(nfaulty_x9<F, ) ))
s.add(Implies( (rule20_x9 > 0), And(nfaulty_x9<F, ) ))
s.add(Implies( (rule21_x9 > 0), And(nfaulty_x9<F, ) ))
s.add(Implies( (rule22_x9 > 0), And(True, ) ))
s.add(Implies( (rule23_x9 > 0), And(True, ) ))
s.add(Implies( (rule24_x9 > 0), And(True, ) ))
s.add(Implies( (rule25_x9 > 0), And(True, ) ))
s.add(Implies( (rule26_x9 > 0), And(True, ) ))
s.add(Implies( (rule27_x9 > 0), And(True, ) ))
s.add(Implies( (rule28_x9 > 0), And(True, ) ))
s.add(Implies( (rule29_x9 > 0), And(True, ) ))

##################Step 5#########################


#Ensuring that configurations x9 and y9 have the same context

s.add((nsnt1CF_x9>=1) == (nsnt1CF_y9>=1))
s.add((nsnt0CF_x9>=1) == (nsnt0CF_y9>=1))
s.add((nsnt1CF_x9>=N-2*T) == (nsnt1CF_y9>=N-2*T))
s.add((nsnt01CF_x9>=N-T) == (nsnt01CF_y9>=N-T))
s.add((nsnt1CF_x9>=N-T) == (nsnt1CF_y9>=N-T))
s.add((nsnt0_x9<N-2*T) == (nsnt0_y9<N-2*T))
s.add((nsnt0CF_x9>=N-T) == (nsnt0CF_y9>=N-T))
s.add((True) == (True))
s.add((nsnt1_x9<N-2*T) == (nsnt1_y9<N-2*T))
s.add((nfaulty_x9<F) == (nfaulty_y9<F))
s.add((nsnt0CF_x9>=N-2*T) == (nsnt0CF_y9>=N-2*T))

####################################################################################

#Creating constraints for a run between the x10th and y10th configurations

################Step 1#################


#Creating many copies of location variables

loc0_x10 = Real('loc0_x10')
loc0_y10 = Real('loc0_y10')
s.add(loc0_x10 >= 0)
s.add(loc0_y10 >= 0)
loc1_x10 = Real('loc1_x10')
loc1_y10 = Real('loc1_y10')
s.add(loc1_x10 >= 0)
s.add(loc1_y10 >= 0)
locS0_x10 = Real('locS0_x10')
locS0_y10 = Real('locS0_y10')
s.add(locS0_x10 >= 0)
s.add(locS0_y10 >= 0)
locS1_x10 = Real('locS1_x10')
locS1_y10 = Real('locS1_y10')
s.add(locS1_x10 >= 0)
s.add(locS1_y10 >= 0)
locD0_x10 = Real('locD0_x10')
locD0_y10 = Real('locD0_y10')
s.add(locD0_x10 >= 0)
s.add(locD0_y10 >= 0)
locD1_x10 = Real('locD1_x10')
locD1_y10 = Real('locD1_y10')
s.add(locD1_x10 >= 0)
s.add(locD1_y10 >= 0)
locU0_x10 = Real('locU0_x10')
locU0_y10 = Real('locU0_y10')
s.add(locU0_x10 >= 0)
s.add(locU0_y10 >= 0)
locU1_x10 = Real('locU1_x10')
locU1_y10 = Real('locU1_y10')
s.add(locU1_x10 >= 0)
s.add(locU1_y10 >= 0)
locCR_x10 = Real('locCR_x10')
locCR_y10 = Real('locCR_y10')
s.add(locCR_x10 >= 0)
s.add(locCR_y10 >= 0)






#Creating many copies of shared variables

nsnt0_x10 = Real('nsnt0_x10')
nsnt0_y10 = Real('nsnt0_y10')
s.add(nsnt0_x10 >= 0)
s.add(nsnt0_y10 >= 0)
nsnt1_x10 = Real('nsnt1_x10')
nsnt1_y10 = Real('nsnt1_y10')
s.add(nsnt1_x10 >= 0)
s.add(nsnt1_y10 >= 0)
nsnt0CF_x10 = Real('nsnt0CF_x10')
nsnt0CF_y10 = Real('nsnt0CF_y10')
s.add(nsnt0CF_x10 >= 0)
s.add(nsnt0CF_y10 >= 0)
nsnt1CF_x10 = Real('nsnt1CF_x10')
nsnt1CF_y10 = Real('nsnt1CF_y10')
s.add(nsnt1CF_x10 >= 0)
s.add(nsnt1CF_y10 >= 0)
nsnt01_x10 = Real('nsnt01_x10')
nsnt01_y10 = Real('nsnt01_y10')
s.add(nsnt01_x10 >= 0)
s.add(nsnt01_y10 >= 0)
nsnt01CF_x10 = Real('nsnt01CF_x10')
nsnt01CF_y10 = Real('nsnt01CF_y10')
s.add(nsnt01CF_x10 >= 0)
s.add(nsnt01CF_y10 >= 0)
nfaulty_x10 = Real('nfaulty_x10')
nfaulty_y10 = Real('nfaulty_y10')
s.add(nfaulty_x10 >= 0)
s.add(nfaulty_y10 >= 0)






#Creating many copies of variables for rules

rule0_x10 = Real('rule0_x10')
s.add(rule0_x10 >= 0)
rule1_x10 = Real('rule1_x10')
s.add(rule1_x10 >= 0)
rule2_x10 = Real('rule2_x10')
s.add(rule2_x10 >= 0)
rule3_x10 = Real('rule3_x10')
s.add(rule3_x10 >= 0)
rule4_x10 = Real('rule4_x10')
s.add(rule4_x10 >= 0)
rule5_x10 = Real('rule5_x10')
s.add(rule5_x10 >= 0)
rule6_x10 = Real('rule6_x10')
s.add(rule6_x10 >= 0)
rule7_x10 = Real('rule7_x10')
s.add(rule7_x10 >= 0)
rule8_x10 = Real('rule8_x10')
s.add(rule8_x10 >= 0)
rule9_x10 = Real('rule9_x10')
s.add(rule9_x10 >= 0)
rule10_x10 = Real('rule10_x10')
s.add(rule10_x10 >= 0)
rule11_x10 = Real('rule11_x10')
s.add(rule11_x10 >= 0)
rule12_x10 = Real('rule12_x10')
s.add(rule12_x10 >= 0)
rule13_x10 = Real('rule13_x10')
s.add(rule13_x10 >= 0)
rule14_x10 = Real('rule14_x10')
s.add(rule14_x10 >= 0)
rule15_x10 = Real('rule15_x10')
s.add(rule15_x10 >= 0)
rule16_x10 = Real('rule16_x10')
s.add(rule16_x10 >= 0)
rule17_x10 = Real('rule17_x10')
s.add(rule17_x10 >= 0)
rule18_x10 = Real('rule18_x10')
s.add(rule18_x10 >= 0)
rule19_x10 = Real('rule19_x10')
s.add(rule19_x10 >= 0)
rule20_x10 = Real('rule20_x10')
s.add(rule20_x10 >= 0)
rule21_x10 = Real('rule21_x10')
s.add(rule21_x10 >= 0)
rule22_x10 = Real('rule22_x10')
s.add(rule22_x10 >= 0)
rule23_x10 = Real('rule23_x10')
s.add(rule23_x10 >= 0)
rule24_x10 = Real('rule24_x10')
s.add(rule24_x10 >= 0)
rule25_x10 = Real('rule25_x10')
s.add(rule25_x10 >= 0)
rule26_x10 = Real('rule26_x10')
s.add(rule26_x10 >= 0)
rule27_x10 = Real('rule27_x10')
s.add(rule27_x10 >= 0)
rule28_x10 = Real('rule28_x10')
s.add(rule28_x10 >= 0)
rule29_x10 = Real('rule29_x10')
s.add(rule29_x10 >= 0)






###################Step 2####################


#Flow equations for the locations

s.add(0 - rule0_x10 - rule1_x10 - rule14_x10 - rule22_x10 + rule22_x10 ==  loc0_y10 - loc0_x10)
s.add(0 - rule2_x10 - rule3_x10 - rule15_x10 - rule23_x10 + rule23_x10 ==  loc1_y10 - loc1_x10)
s.add(0 + rule0_x10 - rule4_x10 - rule6_x10 - rule8_x10 - rule10_x10 - rule12_x10 - rule16_x10 - rule24_x10 + rule24_x10 ==  locS0_y10 - locS0_x10)
s.add(0 + rule2_x10 - rule5_x10 - rule7_x10 - rule9_x10 - rule11_x10 - rule13_x10 - rule17_x10 - rule25_x10 + rule25_x10 ==  locS1_y10 - locS1_x10)
s.add(0 + rule4_x10 + rule5_x10 - rule18_x10 - rule26_x10 + rule26_x10 ==  locD0_y10 - locD0_x10)
s.add(0 + rule6_x10 + rule7_x10 - rule19_x10 - rule27_x10 + rule27_x10 ==  locD1_y10 - locD1_x10)
s.add(0 + rule8_x10 + rule9_x10 + rule12_x10 - rule20_x10 - rule28_x10 + rule28_x10 ==  locU0_y10 - locU0_x10)
s.add(0 + rule10_x10 + rule11_x10 + rule13_x10 - rule21_x10 - rule29_x10 + rule29_x10 ==  locU1_y10 - locU1_x10)
s.add(0 + rule1_x10 + rule3_x10 + rule14_x10 + rule15_x10 + rule16_x10 + rule17_x10 + rule18_x10 + rule19_x10 + rule20_x10 + rule21_x10 ==  locCR_y10 - locCR_x10)






##################Step 3########################


#Flow equations for the shared variables

s.add(0 + rule0_x10 == nsnt0_y10 - nsnt0_x10)
s.add(0 + rule2_x10 == nsnt1_y10 - nsnt1_x10)
s.add(0 + rule0_x10 + rule1_x10 == nsnt0CF_y10 - nsnt0CF_x10)
s.add(0 + rule2_x10 + rule3_x10 == nsnt1CF_y10 - nsnt1CF_x10)
s.add(0 + rule0_x10 + rule2_x10 == nsnt01_y10 - nsnt01_x10)
s.add(0 + rule0_x10 + rule1_x10 + rule2_x10 + rule3_x10 == nsnt01CF_y10 - nsnt01CF_x10)
s.add(0 + rule1_x10 + rule3_x10 + rule14_x10 + rule15_x10 + rule16_x10 + rule17_x10 + rule18_x10 + rule19_x10 + rule20_x10 + rule21_x10 == nfaulty_y10 - nfaulty_x10)






####################Step 4########################


#Rule is fired implies rule is enabled

s.add(Implies( (rule0_x10 > 0), And(True, ) ))
s.add(Implies( (rule1_x10 > 0), And(nfaulty_x10<F, ) ))
s.add(Implies( (rule2_x10 > 0), And(True, ) ))
s.add(Implies( (rule3_x10 > 0), And(nfaulty_x10<F, ) ))
s.add(Implies( (rule4_x10 > 0), And(nsnt0CF_x10>=N-T, ) ))
s.add(Implies( (rule5_x10 > 0), And(nsnt0CF_x10>=N-T, ) ))
s.add(Implies( (rule6_x10 > 0), And(nsnt1CF_x10>=N-T, ) ))
s.add(Implies( (rule7_x10 > 0), And(nsnt1CF_x10>=N-T, ) ))
s.add(Implies( (rule8_x10 > 0), And(nsnt01CF_x10>=N-T, nsnt0CF_x10>=N-2*T, nsnt1CF_x10>=1, ) ))
s.add(Implies( (rule9_x10 > 0), And(nsnt01CF_x10>=N-T, nsnt0CF_x10>=N-2*T, nsnt1CF_x10>=1, ) ))
s.add(Implies( (rule10_x10 > 0), And(nsnt01CF_x10>=N-T, nsnt1CF_x10>=N-2*T, nsnt0CF_x10>=1, ) ))
s.add(Implies( (rule11_x10 > 0), And(nsnt01CF_x10>=N-T, nsnt1CF_x10>=N-2*T, nsnt0CF_x10>=1, ) ))
s.add(Implies( (rule12_x10 > 0), And(nsnt01CF_x10>=N-T, nsnt0_x10<N-2*T, nsnt1_x10<N-2*T, ) ))
s.add(Implies( (rule13_x10 > 0), And(nsnt01CF_x10>=N-T, nsnt0_x10<N-2*T, nsnt1_x10<N-2*T, ) ))
s.add(Implies( (rule14_x10 > 0), And(nfaulty_x10<F, ) ))
s.add(Implies( (rule15_x10 > 0), And(nfaulty_x10<F, ) ))
s.add(Implies( (rule16_x10 > 0), And(nfaulty_x10<F, ) ))
s.add(Implies( (rule17_x10 > 0), And(nfaulty_x10<F, ) ))
s.add(Implies( (rule18_x10 > 0), And(nfaulty_x10<F, ) ))
s.add(Implies( (rule19_x10 > 0), And(nfaulty_x10<F, ) ))
s.add(Implies( (rule20_x10 > 0), And(nfaulty_x10<F, ) ))
s.add(Implies( (rule21_x10 > 0), And(nfaulty_x10<F, ) ))
s.add(Implies( (rule22_x10 > 0), And(True, ) ))
s.add(Implies( (rule23_x10 > 0), And(True, ) ))
s.add(Implies( (rule24_x10 > 0), And(True, ) ))
s.add(Implies( (rule25_x10 > 0), And(True, ) ))
s.add(Implies( (rule26_x10 > 0), And(True, ) ))
s.add(Implies( (rule27_x10 > 0), And(True, ) ))
s.add(Implies( (rule28_x10 > 0), And(True, ) ))
s.add(Implies( (rule29_x10 > 0), And(True, ) ))

##################Step 5#########################


#Ensuring that configurations x10 and y10 have the same context

s.add((nsnt1CF_x10>=1) == (nsnt1CF_y10>=1))
s.add((nsnt0CF_x10>=1) == (nsnt0CF_y10>=1))
s.add((nsnt1CF_x10>=N-2*T) == (nsnt1CF_y10>=N-2*T))
s.add((nsnt01CF_x10>=N-T) == (nsnt01CF_y10>=N-T))
s.add((nsnt1CF_x10>=N-T) == (nsnt1CF_y10>=N-T))
s.add((nsnt0_x10<N-2*T) == (nsnt0_y10<N-2*T))
s.add((nsnt0CF_x10>=N-T) == (nsnt0CF_y10>=N-T))
s.add((True) == (True))
s.add((nsnt1_x10<N-2*T) == (nsnt1_y10<N-2*T))
s.add((nfaulty_x10<F) == (nfaulty_y10<F))
s.add((nsnt0CF_x10>=N-2*T) == (nsnt0CF_y10>=N-2*T))

####################################################################################

#Creating constraints for a run between the x11th and y11th configurations

################Step 1#################


#Creating many copies of location variables

loc0_x11 = Real('loc0_x11')
loc0_y11 = Real('loc0_y11')
s.add(loc0_x11 >= 0)
s.add(loc0_y11 >= 0)
loc1_x11 = Real('loc1_x11')
loc1_y11 = Real('loc1_y11')
s.add(loc1_x11 >= 0)
s.add(loc1_y11 >= 0)
locS0_x11 = Real('locS0_x11')
locS0_y11 = Real('locS0_y11')
s.add(locS0_x11 >= 0)
s.add(locS0_y11 >= 0)
locS1_x11 = Real('locS1_x11')
locS1_y11 = Real('locS1_y11')
s.add(locS1_x11 >= 0)
s.add(locS1_y11 >= 0)
locD0_x11 = Real('locD0_x11')
locD0_y11 = Real('locD0_y11')
s.add(locD0_x11 >= 0)
s.add(locD0_y11 >= 0)
locD1_x11 = Real('locD1_x11')
locD1_y11 = Real('locD1_y11')
s.add(locD1_x11 >= 0)
s.add(locD1_y11 >= 0)
locU0_x11 = Real('locU0_x11')
locU0_y11 = Real('locU0_y11')
s.add(locU0_x11 >= 0)
s.add(locU0_y11 >= 0)
locU1_x11 = Real('locU1_x11')
locU1_y11 = Real('locU1_y11')
s.add(locU1_x11 >= 0)
s.add(locU1_y11 >= 0)
locCR_x11 = Real('locCR_x11')
locCR_y11 = Real('locCR_y11')
s.add(locCR_x11 >= 0)
s.add(locCR_y11 >= 0)






#Creating many copies of shared variables

nsnt0_x11 = Real('nsnt0_x11')
nsnt0_y11 = Real('nsnt0_y11')
s.add(nsnt0_x11 >= 0)
s.add(nsnt0_y11 >= 0)
nsnt1_x11 = Real('nsnt1_x11')
nsnt1_y11 = Real('nsnt1_y11')
s.add(nsnt1_x11 >= 0)
s.add(nsnt1_y11 >= 0)
nsnt0CF_x11 = Real('nsnt0CF_x11')
nsnt0CF_y11 = Real('nsnt0CF_y11')
s.add(nsnt0CF_x11 >= 0)
s.add(nsnt0CF_y11 >= 0)
nsnt1CF_x11 = Real('nsnt1CF_x11')
nsnt1CF_y11 = Real('nsnt1CF_y11')
s.add(nsnt1CF_x11 >= 0)
s.add(nsnt1CF_y11 >= 0)
nsnt01_x11 = Real('nsnt01_x11')
nsnt01_y11 = Real('nsnt01_y11')
s.add(nsnt01_x11 >= 0)
s.add(nsnt01_y11 >= 0)
nsnt01CF_x11 = Real('nsnt01CF_x11')
nsnt01CF_y11 = Real('nsnt01CF_y11')
s.add(nsnt01CF_x11 >= 0)
s.add(nsnt01CF_y11 >= 0)
nfaulty_x11 = Real('nfaulty_x11')
nfaulty_y11 = Real('nfaulty_y11')
s.add(nfaulty_x11 >= 0)
s.add(nfaulty_y11 >= 0)






#Creating many copies of variables for rules

rule0_x11 = Real('rule0_x11')
s.add(rule0_x11 >= 0)
rule1_x11 = Real('rule1_x11')
s.add(rule1_x11 >= 0)
rule2_x11 = Real('rule2_x11')
s.add(rule2_x11 >= 0)
rule3_x11 = Real('rule3_x11')
s.add(rule3_x11 >= 0)
rule4_x11 = Real('rule4_x11')
s.add(rule4_x11 >= 0)
rule5_x11 = Real('rule5_x11')
s.add(rule5_x11 >= 0)
rule6_x11 = Real('rule6_x11')
s.add(rule6_x11 >= 0)
rule7_x11 = Real('rule7_x11')
s.add(rule7_x11 >= 0)
rule8_x11 = Real('rule8_x11')
s.add(rule8_x11 >= 0)
rule9_x11 = Real('rule9_x11')
s.add(rule9_x11 >= 0)
rule10_x11 = Real('rule10_x11')
s.add(rule10_x11 >= 0)
rule11_x11 = Real('rule11_x11')
s.add(rule11_x11 >= 0)
rule12_x11 = Real('rule12_x11')
s.add(rule12_x11 >= 0)
rule13_x11 = Real('rule13_x11')
s.add(rule13_x11 >= 0)
rule14_x11 = Real('rule14_x11')
s.add(rule14_x11 >= 0)
rule15_x11 = Real('rule15_x11')
s.add(rule15_x11 >= 0)
rule16_x11 = Real('rule16_x11')
s.add(rule16_x11 >= 0)
rule17_x11 = Real('rule17_x11')
s.add(rule17_x11 >= 0)
rule18_x11 = Real('rule18_x11')
s.add(rule18_x11 >= 0)
rule19_x11 = Real('rule19_x11')
s.add(rule19_x11 >= 0)
rule20_x11 = Real('rule20_x11')
s.add(rule20_x11 >= 0)
rule21_x11 = Real('rule21_x11')
s.add(rule21_x11 >= 0)
rule22_x11 = Real('rule22_x11')
s.add(rule22_x11 >= 0)
rule23_x11 = Real('rule23_x11')
s.add(rule23_x11 >= 0)
rule24_x11 = Real('rule24_x11')
s.add(rule24_x11 >= 0)
rule25_x11 = Real('rule25_x11')
s.add(rule25_x11 >= 0)
rule26_x11 = Real('rule26_x11')
s.add(rule26_x11 >= 0)
rule27_x11 = Real('rule27_x11')
s.add(rule27_x11 >= 0)
rule28_x11 = Real('rule28_x11')
s.add(rule28_x11 >= 0)
rule29_x11 = Real('rule29_x11')
s.add(rule29_x11 >= 0)






###################Step 2####################


#Flow equations for the locations

s.add(0 - rule0_x11 - rule1_x11 - rule14_x11 - rule22_x11 + rule22_x11 ==  loc0_y11 - loc0_x11)
s.add(0 - rule2_x11 - rule3_x11 - rule15_x11 - rule23_x11 + rule23_x11 ==  loc1_y11 - loc1_x11)
s.add(0 + rule0_x11 - rule4_x11 - rule6_x11 - rule8_x11 - rule10_x11 - rule12_x11 - rule16_x11 - rule24_x11 + rule24_x11 ==  locS0_y11 - locS0_x11)
s.add(0 + rule2_x11 - rule5_x11 - rule7_x11 - rule9_x11 - rule11_x11 - rule13_x11 - rule17_x11 - rule25_x11 + rule25_x11 ==  locS1_y11 - locS1_x11)
s.add(0 + rule4_x11 + rule5_x11 - rule18_x11 - rule26_x11 + rule26_x11 ==  locD0_y11 - locD0_x11)
s.add(0 + rule6_x11 + rule7_x11 - rule19_x11 - rule27_x11 + rule27_x11 ==  locD1_y11 - locD1_x11)
s.add(0 + rule8_x11 + rule9_x11 + rule12_x11 - rule20_x11 - rule28_x11 + rule28_x11 ==  locU0_y11 - locU0_x11)
s.add(0 + rule10_x11 + rule11_x11 + rule13_x11 - rule21_x11 - rule29_x11 + rule29_x11 ==  locU1_y11 - locU1_x11)
s.add(0 + rule1_x11 + rule3_x11 + rule14_x11 + rule15_x11 + rule16_x11 + rule17_x11 + rule18_x11 + rule19_x11 + rule20_x11 + rule21_x11 ==  locCR_y11 - locCR_x11)






##################Step 3########################


#Flow equations for the shared variables

s.add(0 + rule0_x11 == nsnt0_y11 - nsnt0_x11)
s.add(0 + rule2_x11 == nsnt1_y11 - nsnt1_x11)
s.add(0 + rule0_x11 + rule1_x11 == nsnt0CF_y11 - nsnt0CF_x11)
s.add(0 + rule2_x11 + rule3_x11 == nsnt1CF_y11 - nsnt1CF_x11)
s.add(0 + rule0_x11 + rule2_x11 == nsnt01_y11 - nsnt01_x11)
s.add(0 + rule0_x11 + rule1_x11 + rule2_x11 + rule3_x11 == nsnt01CF_y11 - nsnt01CF_x11)
s.add(0 + rule1_x11 + rule3_x11 + rule14_x11 + rule15_x11 + rule16_x11 + rule17_x11 + rule18_x11 + rule19_x11 + rule20_x11 + rule21_x11 == nfaulty_y11 - nfaulty_x11)






####################Step 4########################


#Rule is fired implies rule is enabled

s.add(Implies( (rule0_x11 > 0), And(True, ) ))
s.add(Implies( (rule1_x11 > 0), And(nfaulty_x11<F, ) ))
s.add(Implies( (rule2_x11 > 0), And(True, ) ))
s.add(Implies( (rule3_x11 > 0), And(nfaulty_x11<F, ) ))
s.add(Implies( (rule4_x11 > 0), And(nsnt0CF_x11>=N-T, ) ))
s.add(Implies( (rule5_x11 > 0), And(nsnt0CF_x11>=N-T, ) ))
s.add(Implies( (rule6_x11 > 0), And(nsnt1CF_x11>=N-T, ) ))
s.add(Implies( (rule7_x11 > 0), And(nsnt1CF_x11>=N-T, ) ))
s.add(Implies( (rule8_x11 > 0), And(nsnt01CF_x11>=N-T, nsnt0CF_x11>=N-2*T, nsnt1CF_x11>=1, ) ))
s.add(Implies( (rule9_x11 > 0), And(nsnt01CF_x11>=N-T, nsnt0CF_x11>=N-2*T, nsnt1CF_x11>=1, ) ))
s.add(Implies( (rule10_x11 > 0), And(nsnt01CF_x11>=N-T, nsnt1CF_x11>=N-2*T, nsnt0CF_x11>=1, ) ))
s.add(Implies( (rule11_x11 > 0), And(nsnt01CF_x11>=N-T, nsnt1CF_x11>=N-2*T, nsnt0CF_x11>=1, ) ))
s.add(Implies( (rule12_x11 > 0), And(nsnt01CF_x11>=N-T, nsnt0_x11<N-2*T, nsnt1_x11<N-2*T, ) ))
s.add(Implies( (rule13_x11 > 0), And(nsnt01CF_x11>=N-T, nsnt0_x11<N-2*T, nsnt1_x11<N-2*T, ) ))
s.add(Implies( (rule14_x11 > 0), And(nfaulty_x11<F, ) ))
s.add(Implies( (rule15_x11 > 0), And(nfaulty_x11<F, ) ))
s.add(Implies( (rule16_x11 > 0), And(nfaulty_x11<F, ) ))
s.add(Implies( (rule17_x11 > 0), And(nfaulty_x11<F, ) ))
s.add(Implies( (rule18_x11 > 0), And(nfaulty_x11<F, ) ))
s.add(Implies( (rule19_x11 > 0), And(nfaulty_x11<F, ) ))
s.add(Implies( (rule20_x11 > 0), And(nfaulty_x11<F, ) ))
s.add(Implies( (rule21_x11 > 0), And(nfaulty_x11<F, ) ))
s.add(Implies( (rule22_x11 > 0), And(True, ) ))
s.add(Implies( (rule23_x11 > 0), And(True, ) ))
s.add(Implies( (rule24_x11 > 0), And(True, ) ))
s.add(Implies( (rule25_x11 > 0), And(True, ) ))
s.add(Implies( (rule26_x11 > 0), And(True, ) ))
s.add(Implies( (rule27_x11 > 0), And(True, ) ))
s.add(Implies( (rule28_x11 > 0), And(True, ) ))
s.add(Implies( (rule29_x11 > 0), And(True, ) ))

##################Step 5#########################


#Ensuring that configurations x11 and y11 have the same context

s.add((nsnt1CF_x11>=1) == (nsnt1CF_y11>=1))
s.add((nsnt0CF_x11>=1) == (nsnt0CF_y11>=1))
s.add((nsnt1CF_x11>=N-2*T) == (nsnt1CF_y11>=N-2*T))
s.add((nsnt01CF_x11>=N-T) == (nsnt01CF_y11>=N-T))
s.add((nsnt1CF_x11>=N-T) == (nsnt1CF_y11>=N-T))
s.add((nsnt0_x11<N-2*T) == (nsnt0_y11<N-2*T))
s.add((nsnt0CF_x11>=N-T) == (nsnt0CF_y11>=N-T))
s.add((True) == (True))
s.add((nsnt1_x11<N-2*T) == (nsnt1_y11<N-2*T))
s.add((nfaulty_x11<F) == (nfaulty_y11<F))
s.add((nsnt0CF_x11>=N-2*T) == (nsnt0CF_y11>=N-2*T))

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
rule14_y0 = Real('rule14_y0')
s.add(rule14_y0 >= 0)
rule15_y0 = Real('rule15_y0')
s.add(rule15_y0 >= 0)
rule16_y0 = Real('rule16_y0')
s.add(rule16_y0 >= 0)
rule17_y0 = Real('rule17_y0')
s.add(rule17_y0 >= 0)
rule18_y0 = Real('rule18_y0')
s.add(rule18_y0 >= 0)
rule19_y0 = Real('rule19_y0')
s.add(rule19_y0 >= 0)
rule20_y0 = Real('rule20_y0')
s.add(rule20_y0 >= 0)
rule21_y0 = Real('rule21_y0')
s.add(rule21_y0 >= 0)
rule22_y0 = Real('rule22_y0')
s.add(rule22_y0 >= 0)
rule23_y0 = Real('rule23_y0')
s.add(rule23_y0 >= 0)
rule24_y0 = Real('rule24_y0')
s.add(rule24_y0 >= 0)
rule25_y0 = Real('rule25_y0')
s.add(rule25_y0 >= 0)
rule26_y0 = Real('rule26_y0')
s.add(rule26_y0 >= 0)
rule27_y0 = Real('rule27_y0')
s.add(rule27_y0 >= 0)
rule28_y0 = Real('rule28_y0')
s.add(rule28_y0 >= 0)
rule29_y0 = Real('rule29_y0')
s.add(rule29_y0 >= 0)






###################Step 2####################


#Flow equations for the locations

s.add(0 - rule0_y0 - rule1_y0 - rule14_y0 - rule22_y0 + rule22_y0 ==  loc0_x1 - loc0_y0)
s.add(0 - rule2_y0 - rule3_y0 - rule15_y0 - rule23_y0 + rule23_y0 ==  loc1_x1 - loc1_y0)
s.add(0 + rule0_y0 - rule4_y0 - rule6_y0 - rule8_y0 - rule10_y0 - rule12_y0 - rule16_y0 - rule24_y0 + rule24_y0 ==  locS0_x1 - locS0_y0)
s.add(0 + rule2_y0 - rule5_y0 - rule7_y0 - rule9_y0 - rule11_y0 - rule13_y0 - rule17_y0 - rule25_y0 + rule25_y0 ==  locS1_x1 - locS1_y0)
s.add(0 + rule4_y0 + rule5_y0 - rule18_y0 - rule26_y0 + rule26_y0 ==  locD0_x1 - locD0_y0)
s.add(0 + rule6_y0 + rule7_y0 - rule19_y0 - rule27_y0 + rule27_y0 ==  locD1_x1 - locD1_y0)
s.add(0 + rule8_y0 + rule9_y0 + rule12_y0 - rule20_y0 - rule28_y0 + rule28_y0 ==  locU0_x1 - locU0_y0)
s.add(0 + rule10_y0 + rule11_y0 + rule13_y0 - rule21_y0 - rule29_y0 + rule29_y0 ==  locU1_x1 - locU1_y0)
s.add(0 + rule1_y0 + rule3_y0 + rule14_y0 + rule15_y0 + rule16_y0 + rule17_y0 + rule18_y0 + rule19_y0 + rule20_y0 + rule21_y0 ==  locCR_x1 - locCR_y0)






##################Step 3########################


#Flow equations for the shared variables

s.add(0 + rule0_y0 == nsnt0_x1 - nsnt0_y0)
s.add(0 + rule2_y0 == nsnt1_x1 - nsnt1_y0)
s.add(0 + rule0_y0 + rule1_y0 == nsnt0CF_x1 - nsnt0CF_y0)
s.add(0 + rule2_y0 + rule3_y0 == nsnt1CF_x1 - nsnt1CF_y0)
s.add(0 + rule0_y0 + rule2_y0 == nsnt01_x1 - nsnt01_y0)
s.add(0 + rule0_y0 + rule1_y0 + rule2_y0 + rule3_y0 == nsnt01CF_x1 - nsnt01CF_y0)
s.add(0 + rule1_y0 + rule3_y0 + rule14_y0 + rule15_y0 + rule16_y0 + rule17_y0 + rule18_y0 + rule19_y0 + rule20_y0 + rule21_y0 == nfaulty_x1 - nfaulty_y0)






####################Step 4########################


#Rule is fired implies rule is enabled

s.add(Implies( (rule0_y0 > 0), And(True, ) ))
s.add(Implies( (rule1_y0 > 0), And(nfaulty_y0<F, ) ))
s.add(Implies( (rule2_y0 > 0), And(True, ) ))
s.add(Implies( (rule3_y0 > 0), And(nfaulty_y0<F, ) ))
s.add(Implies( (rule4_y0 > 0), And(nsnt0CF_y0>=N-T, ) ))
s.add(Implies( (rule5_y0 > 0), And(nsnt0CF_y0>=N-T, ) ))
s.add(Implies( (rule6_y0 > 0), And(nsnt1CF_y0>=N-T, ) ))
s.add(Implies( (rule7_y0 > 0), And(nsnt1CF_y0>=N-T, ) ))
s.add(Implies( (rule8_y0 > 0), And(nsnt01CF_y0>=N-T, nsnt0CF_y0>=N-2*T, nsnt1CF_y0>=1, ) ))
s.add(Implies( (rule9_y0 > 0), And(nsnt01CF_y0>=N-T, nsnt0CF_y0>=N-2*T, nsnt1CF_y0>=1, ) ))
s.add(Implies( (rule10_y0 > 0), And(nsnt01CF_y0>=N-T, nsnt1CF_y0>=N-2*T, nsnt0CF_y0>=1, ) ))
s.add(Implies( (rule11_y0 > 0), And(nsnt01CF_y0>=N-T, nsnt1CF_y0>=N-2*T, nsnt0CF_y0>=1, ) ))
s.add(Implies( (rule12_y0 > 0), And(nsnt01CF_y0>=N-T, nsnt0_y0<N-2*T, nsnt1_y0<N-2*T, ) ))
s.add(Implies( (rule13_y0 > 0), And(nsnt01CF_y0>=N-T, nsnt0_y0<N-2*T, nsnt1_y0<N-2*T, ) ))
s.add(Implies( (rule14_y0 > 0), And(nfaulty_y0<F, ) ))
s.add(Implies( (rule15_y0 > 0), And(nfaulty_y0<F, ) ))
s.add(Implies( (rule16_y0 > 0), And(nfaulty_y0<F, ) ))
s.add(Implies( (rule17_y0 > 0), And(nfaulty_y0<F, ) ))
s.add(Implies( (rule18_y0 > 0), And(nfaulty_y0<F, ) ))
s.add(Implies( (rule19_y0 > 0), And(nfaulty_y0<F, ) ))
s.add(Implies( (rule20_y0 > 0), And(nfaulty_y0<F, ) ))
s.add(Implies( (rule21_y0 > 0), And(nfaulty_y0<F, ) ))
s.add(Implies( (rule22_y0 > 0), And(True, ) ))
s.add(Implies( (rule23_y0 > 0), And(True, ) ))
s.add(Implies( (rule24_y0 > 0), And(True, ) ))
s.add(Implies( (rule25_y0 > 0), And(True, ) ))
s.add(Implies( (rule26_y0 > 0), And(True, ) ))
s.add(Implies( (rule27_y0 > 0), And(True, ) ))
s.add(Implies( (rule28_y0 > 0), And(True, ) ))
s.add(Implies( (rule29_y0 > 0), And(True, ) ))

##################Step 5########################


#Ensuring that at most one rule is fired alternating configurations y0 and x0, if a fall condition is present

s.add((nsnt1_x1<N-2*T) == (nsnt1_y0<N-2*T))
s.add(Implies(And((nsnt1_x1<N-2*T), Not(nsnt1_y0<N-2*T)), Or((rule0_y0 == 0), (rule0_y0 == 1))))
s.add(Implies(And((nsnt1_x1<N-2*T), Not(nsnt1_y0<N-2*T)), Or((rule1_y0 == 0), (rule1_y0 == 1))))
s.add(Implies(And((nsnt1_x1<N-2*T), Not(nsnt1_y0<N-2*T)), Or((rule2_y0 == 0), (rule2_y0 == 1))))
s.add(Implies(And((nsnt1_x1<N-2*T), Not(nsnt1_y0<N-2*T)), Or((rule3_y0 == 0), (rule3_y0 == 1))))
s.add(Implies(And((nsnt1_x1<N-2*T), Not(nsnt1_y0<N-2*T)), Or((rule4_y0 == 0), (rule4_y0 == 1))))
s.add(Implies(And((nsnt1_x1<N-2*T), Not(nsnt1_y0<N-2*T)), Or((rule5_y0 == 0), (rule5_y0 == 1))))
s.add(Implies(And((nsnt1_x1<N-2*T), Not(nsnt1_y0<N-2*T)), Or((rule6_y0 == 0), (rule6_y0 == 1))))
s.add(Implies(And((nsnt1_x1<N-2*T), Not(nsnt1_y0<N-2*T)), Or((rule7_y0 == 0), (rule7_y0 == 1))))
s.add(Implies(And((nsnt1_x1<N-2*T), Not(nsnt1_y0<N-2*T)), Or((rule8_y0 == 0), (rule8_y0 == 1))))
s.add(Implies(And((nsnt1_x1<N-2*T), Not(nsnt1_y0<N-2*T)), Or((rule9_y0 == 0), (rule9_y0 == 1))))
s.add(Implies(And((nsnt1_x1<N-2*T), Not(nsnt1_y0<N-2*T)), Or((rule10_y0 == 0), (rule10_y0 == 1))))
s.add(Implies(And((nsnt1_x1<N-2*T), Not(nsnt1_y0<N-2*T)), Or((rule11_y0 == 0), (rule11_y0 == 1))))
s.add(Implies(And((nsnt1_x1<N-2*T), Not(nsnt1_y0<N-2*T)), Or((rule12_y0 == 0), (rule12_y0 == 1))))
s.add(Implies(And((nsnt1_x1<N-2*T), Not(nsnt1_y0<N-2*T)), Or((rule13_y0 == 0), (rule13_y0 == 1))))
s.add(Implies(And((nsnt1_x1<N-2*T), Not(nsnt1_y0<N-2*T)), Or((rule14_y0 == 0), (rule14_y0 == 1))))
s.add(Implies(And((nsnt1_x1<N-2*T), Not(nsnt1_y0<N-2*T)), Or((rule15_y0 == 0), (rule15_y0 == 1))))
s.add(Implies(And((nsnt1_x1<N-2*T), Not(nsnt1_y0<N-2*T)), Or((rule16_y0 == 0), (rule16_y0 == 1))))
s.add(Implies(And((nsnt1_x1<N-2*T), Not(nsnt1_y0<N-2*T)), Or((rule17_y0 == 0), (rule17_y0 == 1))))
s.add(Implies(And((nsnt1_x1<N-2*T), Not(nsnt1_y0<N-2*T)), Or((rule18_y0 == 0), (rule18_y0 == 1))))
s.add(Implies(And((nsnt1_x1<N-2*T), Not(nsnt1_y0<N-2*T)), Or((rule19_y0 == 0), (rule19_y0 == 1))))
s.add(Implies(And((nsnt1_x1<N-2*T), Not(nsnt1_y0<N-2*T)), Or((rule20_y0 == 0), (rule20_y0 == 1))))
s.add(Implies(And((nsnt1_x1<N-2*T), Not(nsnt1_y0<N-2*T)), Or((rule21_y0 == 0), (rule21_y0 == 1))))
s.add(Implies(And((nsnt1_x1<N-2*T), Not(nsnt1_y0<N-2*T)), Or((rule22_y0 == 0), (rule22_y0 == 1))))
s.add(Implies(And((nsnt1_x1<N-2*T), Not(nsnt1_y0<N-2*T)), Or((rule23_y0 == 0), (rule23_y0 == 1))))
s.add(Implies(And((nsnt1_x1<N-2*T), Not(nsnt1_y0<N-2*T)), Or((rule24_y0 == 0), (rule24_y0 == 1))))
s.add(Implies(And((nsnt1_x1<N-2*T), Not(nsnt1_y0<N-2*T)), Or((rule25_y0 == 0), (rule25_y0 == 1))))
s.add(Implies(And((nsnt1_x1<N-2*T), Not(nsnt1_y0<N-2*T)), Or((rule26_y0 == 0), (rule26_y0 == 1))))
s.add(Implies(And((nsnt1_x1<N-2*T), Not(nsnt1_y0<N-2*T)), Or((rule27_y0 == 0), (rule27_y0 == 1))))
s.add(Implies(And((nsnt1_x1<N-2*T), Not(nsnt1_y0<N-2*T)), Or((rule28_y0 == 0), (rule28_y0 == 1))))
s.add(Implies(And((nsnt1_x1<N-2*T), Not(nsnt1_y0<N-2*T)), Or((rule29_y0 == 0), (rule29_y0 == 1))))
s.add(Implies(And((nsnt1_x1<N-2*T), Not(nsnt1_y0<N-2*T)), rule0_y0+rule1_y0+rule2_y0+rule3_y0+rule4_y0+rule5_y0+rule6_y0+rule7_y0+rule8_y0+rule9_y0+rule10_y0+rule11_y0+rule12_y0+rule13_y0+rule14_y0+rule15_y0+rule16_y0+rule17_y0+rule18_y0+rule19_y0+rule20_y0+rule21_y0+rule22_y0+rule23_y0+rule24_y0+rule25_y0+rule26_y0+rule27_y0+rule28_y0+rule29_y0 <= 1))

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
s.add(Implies(And((nfaulty_x1<F), Not(nfaulty_y0<F)), Or((rule14_y0 == 0), (rule14_y0 == 1))))
s.add(Implies(And((nfaulty_x1<F), Not(nfaulty_y0<F)), Or((rule15_y0 == 0), (rule15_y0 == 1))))
s.add(Implies(And((nfaulty_x1<F), Not(nfaulty_y0<F)), Or((rule16_y0 == 0), (rule16_y0 == 1))))
s.add(Implies(And((nfaulty_x1<F), Not(nfaulty_y0<F)), Or((rule17_y0 == 0), (rule17_y0 == 1))))
s.add(Implies(And((nfaulty_x1<F), Not(nfaulty_y0<F)), Or((rule18_y0 == 0), (rule18_y0 == 1))))
s.add(Implies(And((nfaulty_x1<F), Not(nfaulty_y0<F)), Or((rule19_y0 == 0), (rule19_y0 == 1))))
s.add(Implies(And((nfaulty_x1<F), Not(nfaulty_y0<F)), Or((rule20_y0 == 0), (rule20_y0 == 1))))
s.add(Implies(And((nfaulty_x1<F), Not(nfaulty_y0<F)), Or((rule21_y0 == 0), (rule21_y0 == 1))))
s.add(Implies(And((nfaulty_x1<F), Not(nfaulty_y0<F)), Or((rule22_y0 == 0), (rule22_y0 == 1))))
s.add(Implies(And((nfaulty_x1<F), Not(nfaulty_y0<F)), Or((rule23_y0 == 0), (rule23_y0 == 1))))
s.add(Implies(And((nfaulty_x1<F), Not(nfaulty_y0<F)), Or((rule24_y0 == 0), (rule24_y0 == 1))))
s.add(Implies(And((nfaulty_x1<F), Not(nfaulty_y0<F)), Or((rule25_y0 == 0), (rule25_y0 == 1))))
s.add(Implies(And((nfaulty_x1<F), Not(nfaulty_y0<F)), Or((rule26_y0 == 0), (rule26_y0 == 1))))
s.add(Implies(And((nfaulty_x1<F), Not(nfaulty_y0<F)), Or((rule27_y0 == 0), (rule27_y0 == 1))))
s.add(Implies(And((nfaulty_x1<F), Not(nfaulty_y0<F)), Or((rule28_y0 == 0), (rule28_y0 == 1))))
s.add(Implies(And((nfaulty_x1<F), Not(nfaulty_y0<F)), Or((rule29_y0 == 0), (rule29_y0 == 1))))
s.add(Implies(And((nfaulty_x1<F), Not(nfaulty_y0<F)), rule0_y0+rule1_y0+rule2_y0+rule3_y0+rule4_y0+rule5_y0+rule6_y0+rule7_y0+rule8_y0+rule9_y0+rule10_y0+rule11_y0+rule12_y0+rule13_y0+rule14_y0+rule15_y0+rule16_y0+rule17_y0+rule18_y0+rule19_y0+rule20_y0+rule21_y0+rule22_y0+rule23_y0+rule24_y0+rule25_y0+rule26_y0+rule27_y0+rule28_y0+rule29_y0 <= 1))

s.add((nsnt0_x1<N-2*T) == (nsnt0_y0<N-2*T))
s.add(Implies(And((nsnt0_x1<N-2*T), Not(nsnt0_y0<N-2*T)), Or((rule0_y0 == 0), (rule0_y0 == 1))))
s.add(Implies(And((nsnt0_x1<N-2*T), Not(nsnt0_y0<N-2*T)), Or((rule1_y0 == 0), (rule1_y0 == 1))))
s.add(Implies(And((nsnt0_x1<N-2*T), Not(nsnt0_y0<N-2*T)), Or((rule2_y0 == 0), (rule2_y0 == 1))))
s.add(Implies(And((nsnt0_x1<N-2*T), Not(nsnt0_y0<N-2*T)), Or((rule3_y0 == 0), (rule3_y0 == 1))))
s.add(Implies(And((nsnt0_x1<N-2*T), Not(nsnt0_y0<N-2*T)), Or((rule4_y0 == 0), (rule4_y0 == 1))))
s.add(Implies(And((nsnt0_x1<N-2*T), Not(nsnt0_y0<N-2*T)), Or((rule5_y0 == 0), (rule5_y0 == 1))))
s.add(Implies(And((nsnt0_x1<N-2*T), Not(nsnt0_y0<N-2*T)), Or((rule6_y0 == 0), (rule6_y0 == 1))))
s.add(Implies(And((nsnt0_x1<N-2*T), Not(nsnt0_y0<N-2*T)), Or((rule7_y0 == 0), (rule7_y0 == 1))))
s.add(Implies(And((nsnt0_x1<N-2*T), Not(nsnt0_y0<N-2*T)), Or((rule8_y0 == 0), (rule8_y0 == 1))))
s.add(Implies(And((nsnt0_x1<N-2*T), Not(nsnt0_y0<N-2*T)), Or((rule9_y0 == 0), (rule9_y0 == 1))))
s.add(Implies(And((nsnt0_x1<N-2*T), Not(nsnt0_y0<N-2*T)), Or((rule10_y0 == 0), (rule10_y0 == 1))))
s.add(Implies(And((nsnt0_x1<N-2*T), Not(nsnt0_y0<N-2*T)), Or((rule11_y0 == 0), (rule11_y0 == 1))))
s.add(Implies(And((nsnt0_x1<N-2*T), Not(nsnt0_y0<N-2*T)), Or((rule12_y0 == 0), (rule12_y0 == 1))))
s.add(Implies(And((nsnt0_x1<N-2*T), Not(nsnt0_y0<N-2*T)), Or((rule13_y0 == 0), (rule13_y0 == 1))))
s.add(Implies(And((nsnt0_x1<N-2*T), Not(nsnt0_y0<N-2*T)), Or((rule14_y0 == 0), (rule14_y0 == 1))))
s.add(Implies(And((nsnt0_x1<N-2*T), Not(nsnt0_y0<N-2*T)), Or((rule15_y0 == 0), (rule15_y0 == 1))))
s.add(Implies(And((nsnt0_x1<N-2*T), Not(nsnt0_y0<N-2*T)), Or((rule16_y0 == 0), (rule16_y0 == 1))))
s.add(Implies(And((nsnt0_x1<N-2*T), Not(nsnt0_y0<N-2*T)), Or((rule17_y0 == 0), (rule17_y0 == 1))))
s.add(Implies(And((nsnt0_x1<N-2*T), Not(nsnt0_y0<N-2*T)), Or((rule18_y0 == 0), (rule18_y0 == 1))))
s.add(Implies(And((nsnt0_x1<N-2*T), Not(nsnt0_y0<N-2*T)), Or((rule19_y0 == 0), (rule19_y0 == 1))))
s.add(Implies(And((nsnt0_x1<N-2*T), Not(nsnt0_y0<N-2*T)), Or((rule20_y0 == 0), (rule20_y0 == 1))))
s.add(Implies(And((nsnt0_x1<N-2*T), Not(nsnt0_y0<N-2*T)), Or((rule21_y0 == 0), (rule21_y0 == 1))))
s.add(Implies(And((nsnt0_x1<N-2*T), Not(nsnt0_y0<N-2*T)), Or((rule22_y0 == 0), (rule22_y0 == 1))))
s.add(Implies(And((nsnt0_x1<N-2*T), Not(nsnt0_y0<N-2*T)), Or((rule23_y0 == 0), (rule23_y0 == 1))))
s.add(Implies(And((nsnt0_x1<N-2*T), Not(nsnt0_y0<N-2*T)), Or((rule24_y0 == 0), (rule24_y0 == 1))))
s.add(Implies(And((nsnt0_x1<N-2*T), Not(nsnt0_y0<N-2*T)), Or((rule25_y0 == 0), (rule25_y0 == 1))))
s.add(Implies(And((nsnt0_x1<N-2*T), Not(nsnt0_y0<N-2*T)), Or((rule26_y0 == 0), (rule26_y0 == 1))))
s.add(Implies(And((nsnt0_x1<N-2*T), Not(nsnt0_y0<N-2*T)), Or((rule27_y0 == 0), (rule27_y0 == 1))))
s.add(Implies(And((nsnt0_x1<N-2*T), Not(nsnt0_y0<N-2*T)), Or((rule28_y0 == 0), (rule28_y0 == 1))))
s.add(Implies(And((nsnt0_x1<N-2*T), Not(nsnt0_y0<N-2*T)), Or((rule29_y0 == 0), (rule29_y0 == 1))))
s.add(Implies(And((nsnt0_x1<N-2*T), Not(nsnt0_y0<N-2*T)), rule0_y0+rule1_y0+rule2_y0+rule3_y0+rule4_y0+rule5_y0+rule6_y0+rule7_y0+rule8_y0+rule9_y0+rule10_y0+rule11_y0+rule12_y0+rule13_y0+rule14_y0+rule15_y0+rule16_y0+rule17_y0+rule18_y0+rule19_y0+rule20_y0+rule21_y0+rule22_y0+rule23_y0+rule24_y0+rule25_y0+rule26_y0+rule27_y0+rule28_y0+rule29_y0 <= 1))


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
rule14_y1 = Real('rule14_y1')
s.add(rule14_y1 >= 0)
rule15_y1 = Real('rule15_y1')
s.add(rule15_y1 >= 0)
rule16_y1 = Real('rule16_y1')
s.add(rule16_y1 >= 0)
rule17_y1 = Real('rule17_y1')
s.add(rule17_y1 >= 0)
rule18_y1 = Real('rule18_y1')
s.add(rule18_y1 >= 0)
rule19_y1 = Real('rule19_y1')
s.add(rule19_y1 >= 0)
rule20_y1 = Real('rule20_y1')
s.add(rule20_y1 >= 0)
rule21_y1 = Real('rule21_y1')
s.add(rule21_y1 >= 0)
rule22_y1 = Real('rule22_y1')
s.add(rule22_y1 >= 0)
rule23_y1 = Real('rule23_y1')
s.add(rule23_y1 >= 0)
rule24_y1 = Real('rule24_y1')
s.add(rule24_y1 >= 0)
rule25_y1 = Real('rule25_y1')
s.add(rule25_y1 >= 0)
rule26_y1 = Real('rule26_y1')
s.add(rule26_y1 >= 0)
rule27_y1 = Real('rule27_y1')
s.add(rule27_y1 >= 0)
rule28_y1 = Real('rule28_y1')
s.add(rule28_y1 >= 0)
rule29_y1 = Real('rule29_y1')
s.add(rule29_y1 >= 0)






###################Step 2####################


#Flow equations for the locations

s.add(0 - rule0_y1 - rule1_y1 - rule14_y1 - rule22_y1 + rule22_y1 ==  loc0_x2 - loc0_y1)
s.add(0 - rule2_y1 - rule3_y1 - rule15_y1 - rule23_y1 + rule23_y1 ==  loc1_x2 - loc1_y1)
s.add(0 + rule0_y1 - rule4_y1 - rule6_y1 - rule8_y1 - rule10_y1 - rule12_y1 - rule16_y1 - rule24_y1 + rule24_y1 ==  locS0_x2 - locS0_y1)
s.add(0 + rule2_y1 - rule5_y1 - rule7_y1 - rule9_y1 - rule11_y1 - rule13_y1 - rule17_y1 - rule25_y1 + rule25_y1 ==  locS1_x2 - locS1_y1)
s.add(0 + rule4_y1 + rule5_y1 - rule18_y1 - rule26_y1 + rule26_y1 ==  locD0_x2 - locD0_y1)
s.add(0 + rule6_y1 + rule7_y1 - rule19_y1 - rule27_y1 + rule27_y1 ==  locD1_x2 - locD1_y1)
s.add(0 + rule8_y1 + rule9_y1 + rule12_y1 - rule20_y1 - rule28_y1 + rule28_y1 ==  locU0_x2 - locU0_y1)
s.add(0 + rule10_y1 + rule11_y1 + rule13_y1 - rule21_y1 - rule29_y1 + rule29_y1 ==  locU1_x2 - locU1_y1)
s.add(0 + rule1_y1 + rule3_y1 + rule14_y1 + rule15_y1 + rule16_y1 + rule17_y1 + rule18_y1 + rule19_y1 + rule20_y1 + rule21_y1 ==  locCR_x2 - locCR_y1)






##################Step 3########################


#Flow equations for the shared variables

s.add(0 + rule0_y1 == nsnt0_x2 - nsnt0_y1)
s.add(0 + rule2_y1 == nsnt1_x2 - nsnt1_y1)
s.add(0 + rule0_y1 + rule1_y1 == nsnt0CF_x2 - nsnt0CF_y1)
s.add(0 + rule2_y1 + rule3_y1 == nsnt1CF_x2 - nsnt1CF_y1)
s.add(0 + rule0_y1 + rule2_y1 == nsnt01_x2 - nsnt01_y1)
s.add(0 + rule0_y1 + rule1_y1 + rule2_y1 + rule3_y1 == nsnt01CF_x2 - nsnt01CF_y1)
s.add(0 + rule1_y1 + rule3_y1 + rule14_y1 + rule15_y1 + rule16_y1 + rule17_y1 + rule18_y1 + rule19_y1 + rule20_y1 + rule21_y1 == nfaulty_x2 - nfaulty_y1)






####################Step 4########################


#Rule is fired implies rule is enabled

s.add(Implies( (rule0_y1 > 0), And(True, ) ))
s.add(Implies( (rule1_y1 > 0), And(nfaulty_y1<F, ) ))
s.add(Implies( (rule2_y1 > 0), And(True, ) ))
s.add(Implies( (rule3_y1 > 0), And(nfaulty_y1<F, ) ))
s.add(Implies( (rule4_y1 > 0), And(nsnt0CF_y1>=N-T, ) ))
s.add(Implies( (rule5_y1 > 0), And(nsnt0CF_y1>=N-T, ) ))
s.add(Implies( (rule6_y1 > 0), And(nsnt1CF_y1>=N-T, ) ))
s.add(Implies( (rule7_y1 > 0), And(nsnt1CF_y1>=N-T, ) ))
s.add(Implies( (rule8_y1 > 0), And(nsnt01CF_y1>=N-T, nsnt0CF_y1>=N-2*T, nsnt1CF_y1>=1, ) ))
s.add(Implies( (rule9_y1 > 0), And(nsnt01CF_y1>=N-T, nsnt0CF_y1>=N-2*T, nsnt1CF_y1>=1, ) ))
s.add(Implies( (rule10_y1 > 0), And(nsnt01CF_y1>=N-T, nsnt1CF_y1>=N-2*T, nsnt0CF_y1>=1, ) ))
s.add(Implies( (rule11_y1 > 0), And(nsnt01CF_y1>=N-T, nsnt1CF_y1>=N-2*T, nsnt0CF_y1>=1, ) ))
s.add(Implies( (rule12_y1 > 0), And(nsnt01CF_y1>=N-T, nsnt0_y1<N-2*T, nsnt1_y1<N-2*T, ) ))
s.add(Implies( (rule13_y1 > 0), And(nsnt01CF_y1>=N-T, nsnt0_y1<N-2*T, nsnt1_y1<N-2*T, ) ))
s.add(Implies( (rule14_y1 > 0), And(nfaulty_y1<F, ) ))
s.add(Implies( (rule15_y1 > 0), And(nfaulty_y1<F, ) ))
s.add(Implies( (rule16_y1 > 0), And(nfaulty_y1<F, ) ))
s.add(Implies( (rule17_y1 > 0), And(nfaulty_y1<F, ) ))
s.add(Implies( (rule18_y1 > 0), And(nfaulty_y1<F, ) ))
s.add(Implies( (rule19_y1 > 0), And(nfaulty_y1<F, ) ))
s.add(Implies( (rule20_y1 > 0), And(nfaulty_y1<F, ) ))
s.add(Implies( (rule21_y1 > 0), And(nfaulty_y1<F, ) ))
s.add(Implies( (rule22_y1 > 0), And(True, ) ))
s.add(Implies( (rule23_y1 > 0), And(True, ) ))
s.add(Implies( (rule24_y1 > 0), And(True, ) ))
s.add(Implies( (rule25_y1 > 0), And(True, ) ))
s.add(Implies( (rule26_y1 > 0), And(True, ) ))
s.add(Implies( (rule27_y1 > 0), And(True, ) ))
s.add(Implies( (rule28_y1 > 0), And(True, ) ))
s.add(Implies( (rule29_y1 > 0), And(True, ) ))

##################Step 5########################


#Ensuring that at most one rule is fired alternating configurations y1 and x1, if a fall condition is present

s.add((nsnt1_x2<N-2*T) == (nsnt1_y1<N-2*T))
s.add(Implies(And((nsnt1_x2<N-2*T), Not(nsnt1_y1<N-2*T)), Or((rule0_y1 == 0), (rule0_y1 == 1))))
s.add(Implies(And((nsnt1_x2<N-2*T), Not(nsnt1_y1<N-2*T)), Or((rule1_y1 == 0), (rule1_y1 == 1))))
s.add(Implies(And((nsnt1_x2<N-2*T), Not(nsnt1_y1<N-2*T)), Or((rule2_y1 == 0), (rule2_y1 == 1))))
s.add(Implies(And((nsnt1_x2<N-2*T), Not(nsnt1_y1<N-2*T)), Or((rule3_y1 == 0), (rule3_y1 == 1))))
s.add(Implies(And((nsnt1_x2<N-2*T), Not(nsnt1_y1<N-2*T)), Or((rule4_y1 == 0), (rule4_y1 == 1))))
s.add(Implies(And((nsnt1_x2<N-2*T), Not(nsnt1_y1<N-2*T)), Or((rule5_y1 == 0), (rule5_y1 == 1))))
s.add(Implies(And((nsnt1_x2<N-2*T), Not(nsnt1_y1<N-2*T)), Or((rule6_y1 == 0), (rule6_y1 == 1))))
s.add(Implies(And((nsnt1_x2<N-2*T), Not(nsnt1_y1<N-2*T)), Or((rule7_y1 == 0), (rule7_y1 == 1))))
s.add(Implies(And((nsnt1_x2<N-2*T), Not(nsnt1_y1<N-2*T)), Or((rule8_y1 == 0), (rule8_y1 == 1))))
s.add(Implies(And((nsnt1_x2<N-2*T), Not(nsnt1_y1<N-2*T)), Or((rule9_y1 == 0), (rule9_y1 == 1))))
s.add(Implies(And((nsnt1_x2<N-2*T), Not(nsnt1_y1<N-2*T)), Or((rule10_y1 == 0), (rule10_y1 == 1))))
s.add(Implies(And((nsnt1_x2<N-2*T), Not(nsnt1_y1<N-2*T)), Or((rule11_y1 == 0), (rule11_y1 == 1))))
s.add(Implies(And((nsnt1_x2<N-2*T), Not(nsnt1_y1<N-2*T)), Or((rule12_y1 == 0), (rule12_y1 == 1))))
s.add(Implies(And((nsnt1_x2<N-2*T), Not(nsnt1_y1<N-2*T)), Or((rule13_y1 == 0), (rule13_y1 == 1))))
s.add(Implies(And((nsnt1_x2<N-2*T), Not(nsnt1_y1<N-2*T)), Or((rule14_y1 == 0), (rule14_y1 == 1))))
s.add(Implies(And((nsnt1_x2<N-2*T), Not(nsnt1_y1<N-2*T)), Or((rule15_y1 == 0), (rule15_y1 == 1))))
s.add(Implies(And((nsnt1_x2<N-2*T), Not(nsnt1_y1<N-2*T)), Or((rule16_y1 == 0), (rule16_y1 == 1))))
s.add(Implies(And((nsnt1_x2<N-2*T), Not(nsnt1_y1<N-2*T)), Or((rule17_y1 == 0), (rule17_y1 == 1))))
s.add(Implies(And((nsnt1_x2<N-2*T), Not(nsnt1_y1<N-2*T)), Or((rule18_y1 == 0), (rule18_y1 == 1))))
s.add(Implies(And((nsnt1_x2<N-2*T), Not(nsnt1_y1<N-2*T)), Or((rule19_y1 == 0), (rule19_y1 == 1))))
s.add(Implies(And((nsnt1_x2<N-2*T), Not(nsnt1_y1<N-2*T)), Or((rule20_y1 == 0), (rule20_y1 == 1))))
s.add(Implies(And((nsnt1_x2<N-2*T), Not(nsnt1_y1<N-2*T)), Or((rule21_y1 == 0), (rule21_y1 == 1))))
s.add(Implies(And((nsnt1_x2<N-2*T), Not(nsnt1_y1<N-2*T)), Or((rule22_y1 == 0), (rule22_y1 == 1))))
s.add(Implies(And((nsnt1_x2<N-2*T), Not(nsnt1_y1<N-2*T)), Or((rule23_y1 == 0), (rule23_y1 == 1))))
s.add(Implies(And((nsnt1_x2<N-2*T), Not(nsnt1_y1<N-2*T)), Or((rule24_y1 == 0), (rule24_y1 == 1))))
s.add(Implies(And((nsnt1_x2<N-2*T), Not(nsnt1_y1<N-2*T)), Or((rule25_y1 == 0), (rule25_y1 == 1))))
s.add(Implies(And((nsnt1_x2<N-2*T), Not(nsnt1_y1<N-2*T)), Or((rule26_y1 == 0), (rule26_y1 == 1))))
s.add(Implies(And((nsnt1_x2<N-2*T), Not(nsnt1_y1<N-2*T)), Or((rule27_y1 == 0), (rule27_y1 == 1))))
s.add(Implies(And((nsnt1_x2<N-2*T), Not(nsnt1_y1<N-2*T)), Or((rule28_y1 == 0), (rule28_y1 == 1))))
s.add(Implies(And((nsnt1_x2<N-2*T), Not(nsnt1_y1<N-2*T)), Or((rule29_y1 == 0), (rule29_y1 == 1))))
s.add(Implies(And((nsnt1_x2<N-2*T), Not(nsnt1_y1<N-2*T)), rule0_y1+rule1_y1+rule2_y1+rule3_y1+rule4_y1+rule5_y1+rule6_y1+rule7_y1+rule8_y1+rule9_y1+rule10_y1+rule11_y1+rule12_y1+rule13_y1+rule14_y1+rule15_y1+rule16_y1+rule17_y1+rule18_y1+rule19_y1+rule20_y1+rule21_y1+rule22_y1+rule23_y1+rule24_y1+rule25_y1+rule26_y1+rule27_y1+rule28_y1+rule29_y1 <= 1))

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
s.add(Implies(And((nfaulty_x2<F), Not(nfaulty_y1<F)), Or((rule14_y1 == 0), (rule14_y1 == 1))))
s.add(Implies(And((nfaulty_x2<F), Not(nfaulty_y1<F)), Or((rule15_y1 == 0), (rule15_y1 == 1))))
s.add(Implies(And((nfaulty_x2<F), Not(nfaulty_y1<F)), Or((rule16_y1 == 0), (rule16_y1 == 1))))
s.add(Implies(And((nfaulty_x2<F), Not(nfaulty_y1<F)), Or((rule17_y1 == 0), (rule17_y1 == 1))))
s.add(Implies(And((nfaulty_x2<F), Not(nfaulty_y1<F)), Or((rule18_y1 == 0), (rule18_y1 == 1))))
s.add(Implies(And((nfaulty_x2<F), Not(nfaulty_y1<F)), Or((rule19_y1 == 0), (rule19_y1 == 1))))
s.add(Implies(And((nfaulty_x2<F), Not(nfaulty_y1<F)), Or((rule20_y1 == 0), (rule20_y1 == 1))))
s.add(Implies(And((nfaulty_x2<F), Not(nfaulty_y1<F)), Or((rule21_y1 == 0), (rule21_y1 == 1))))
s.add(Implies(And((nfaulty_x2<F), Not(nfaulty_y1<F)), Or((rule22_y1 == 0), (rule22_y1 == 1))))
s.add(Implies(And((nfaulty_x2<F), Not(nfaulty_y1<F)), Or((rule23_y1 == 0), (rule23_y1 == 1))))
s.add(Implies(And((nfaulty_x2<F), Not(nfaulty_y1<F)), Or((rule24_y1 == 0), (rule24_y1 == 1))))
s.add(Implies(And((nfaulty_x2<F), Not(nfaulty_y1<F)), Or((rule25_y1 == 0), (rule25_y1 == 1))))
s.add(Implies(And((nfaulty_x2<F), Not(nfaulty_y1<F)), Or((rule26_y1 == 0), (rule26_y1 == 1))))
s.add(Implies(And((nfaulty_x2<F), Not(nfaulty_y1<F)), Or((rule27_y1 == 0), (rule27_y1 == 1))))
s.add(Implies(And((nfaulty_x2<F), Not(nfaulty_y1<F)), Or((rule28_y1 == 0), (rule28_y1 == 1))))
s.add(Implies(And((nfaulty_x2<F), Not(nfaulty_y1<F)), Or((rule29_y1 == 0), (rule29_y1 == 1))))
s.add(Implies(And((nfaulty_x2<F), Not(nfaulty_y1<F)), rule0_y1+rule1_y1+rule2_y1+rule3_y1+rule4_y1+rule5_y1+rule6_y1+rule7_y1+rule8_y1+rule9_y1+rule10_y1+rule11_y1+rule12_y1+rule13_y1+rule14_y1+rule15_y1+rule16_y1+rule17_y1+rule18_y1+rule19_y1+rule20_y1+rule21_y1+rule22_y1+rule23_y1+rule24_y1+rule25_y1+rule26_y1+rule27_y1+rule28_y1+rule29_y1 <= 1))

s.add((nsnt0_x2<N-2*T) == (nsnt0_y1<N-2*T))
s.add(Implies(And((nsnt0_x2<N-2*T), Not(nsnt0_y1<N-2*T)), Or((rule0_y1 == 0), (rule0_y1 == 1))))
s.add(Implies(And((nsnt0_x2<N-2*T), Not(nsnt0_y1<N-2*T)), Or((rule1_y1 == 0), (rule1_y1 == 1))))
s.add(Implies(And((nsnt0_x2<N-2*T), Not(nsnt0_y1<N-2*T)), Or((rule2_y1 == 0), (rule2_y1 == 1))))
s.add(Implies(And((nsnt0_x2<N-2*T), Not(nsnt0_y1<N-2*T)), Or((rule3_y1 == 0), (rule3_y1 == 1))))
s.add(Implies(And((nsnt0_x2<N-2*T), Not(nsnt0_y1<N-2*T)), Or((rule4_y1 == 0), (rule4_y1 == 1))))
s.add(Implies(And((nsnt0_x2<N-2*T), Not(nsnt0_y1<N-2*T)), Or((rule5_y1 == 0), (rule5_y1 == 1))))
s.add(Implies(And((nsnt0_x2<N-2*T), Not(nsnt0_y1<N-2*T)), Or((rule6_y1 == 0), (rule6_y1 == 1))))
s.add(Implies(And((nsnt0_x2<N-2*T), Not(nsnt0_y1<N-2*T)), Or((rule7_y1 == 0), (rule7_y1 == 1))))
s.add(Implies(And((nsnt0_x2<N-2*T), Not(nsnt0_y1<N-2*T)), Or((rule8_y1 == 0), (rule8_y1 == 1))))
s.add(Implies(And((nsnt0_x2<N-2*T), Not(nsnt0_y1<N-2*T)), Or((rule9_y1 == 0), (rule9_y1 == 1))))
s.add(Implies(And((nsnt0_x2<N-2*T), Not(nsnt0_y1<N-2*T)), Or((rule10_y1 == 0), (rule10_y1 == 1))))
s.add(Implies(And((nsnt0_x2<N-2*T), Not(nsnt0_y1<N-2*T)), Or((rule11_y1 == 0), (rule11_y1 == 1))))
s.add(Implies(And((nsnt0_x2<N-2*T), Not(nsnt0_y1<N-2*T)), Or((rule12_y1 == 0), (rule12_y1 == 1))))
s.add(Implies(And((nsnt0_x2<N-2*T), Not(nsnt0_y1<N-2*T)), Or((rule13_y1 == 0), (rule13_y1 == 1))))
s.add(Implies(And((nsnt0_x2<N-2*T), Not(nsnt0_y1<N-2*T)), Or((rule14_y1 == 0), (rule14_y1 == 1))))
s.add(Implies(And((nsnt0_x2<N-2*T), Not(nsnt0_y1<N-2*T)), Or((rule15_y1 == 0), (rule15_y1 == 1))))
s.add(Implies(And((nsnt0_x2<N-2*T), Not(nsnt0_y1<N-2*T)), Or((rule16_y1 == 0), (rule16_y1 == 1))))
s.add(Implies(And((nsnt0_x2<N-2*T), Not(nsnt0_y1<N-2*T)), Or((rule17_y1 == 0), (rule17_y1 == 1))))
s.add(Implies(And((nsnt0_x2<N-2*T), Not(nsnt0_y1<N-2*T)), Or((rule18_y1 == 0), (rule18_y1 == 1))))
s.add(Implies(And((nsnt0_x2<N-2*T), Not(nsnt0_y1<N-2*T)), Or((rule19_y1 == 0), (rule19_y1 == 1))))
s.add(Implies(And((nsnt0_x2<N-2*T), Not(nsnt0_y1<N-2*T)), Or((rule20_y1 == 0), (rule20_y1 == 1))))
s.add(Implies(And((nsnt0_x2<N-2*T), Not(nsnt0_y1<N-2*T)), Or((rule21_y1 == 0), (rule21_y1 == 1))))
s.add(Implies(And((nsnt0_x2<N-2*T), Not(nsnt0_y1<N-2*T)), Or((rule22_y1 == 0), (rule22_y1 == 1))))
s.add(Implies(And((nsnt0_x2<N-2*T), Not(nsnt0_y1<N-2*T)), Or((rule23_y1 == 0), (rule23_y1 == 1))))
s.add(Implies(And((nsnt0_x2<N-2*T), Not(nsnt0_y1<N-2*T)), Or((rule24_y1 == 0), (rule24_y1 == 1))))
s.add(Implies(And((nsnt0_x2<N-2*T), Not(nsnt0_y1<N-2*T)), Or((rule25_y1 == 0), (rule25_y1 == 1))))
s.add(Implies(And((nsnt0_x2<N-2*T), Not(nsnt0_y1<N-2*T)), Or((rule26_y1 == 0), (rule26_y1 == 1))))
s.add(Implies(And((nsnt0_x2<N-2*T), Not(nsnt0_y1<N-2*T)), Or((rule27_y1 == 0), (rule27_y1 == 1))))
s.add(Implies(And((nsnt0_x2<N-2*T), Not(nsnt0_y1<N-2*T)), Or((rule28_y1 == 0), (rule28_y1 == 1))))
s.add(Implies(And((nsnt0_x2<N-2*T), Not(nsnt0_y1<N-2*T)), Or((rule29_y1 == 0), (rule29_y1 == 1))))
s.add(Implies(And((nsnt0_x2<N-2*T), Not(nsnt0_y1<N-2*T)), rule0_y1+rule1_y1+rule2_y1+rule3_y1+rule4_y1+rule5_y1+rule6_y1+rule7_y1+rule8_y1+rule9_y1+rule10_y1+rule11_y1+rule12_y1+rule13_y1+rule14_y1+rule15_y1+rule16_y1+rule17_y1+rule18_y1+rule19_y1+rule20_y1+rule21_y1+rule22_y1+rule23_y1+rule24_y1+rule25_y1+rule26_y1+rule27_y1+rule28_y1+rule29_y1 <= 1))


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
rule14_y2 = Real('rule14_y2')
s.add(rule14_y2 >= 0)
rule15_y2 = Real('rule15_y2')
s.add(rule15_y2 >= 0)
rule16_y2 = Real('rule16_y2')
s.add(rule16_y2 >= 0)
rule17_y2 = Real('rule17_y2')
s.add(rule17_y2 >= 0)
rule18_y2 = Real('rule18_y2')
s.add(rule18_y2 >= 0)
rule19_y2 = Real('rule19_y2')
s.add(rule19_y2 >= 0)
rule20_y2 = Real('rule20_y2')
s.add(rule20_y2 >= 0)
rule21_y2 = Real('rule21_y2')
s.add(rule21_y2 >= 0)
rule22_y2 = Real('rule22_y2')
s.add(rule22_y2 >= 0)
rule23_y2 = Real('rule23_y2')
s.add(rule23_y2 >= 0)
rule24_y2 = Real('rule24_y2')
s.add(rule24_y2 >= 0)
rule25_y2 = Real('rule25_y2')
s.add(rule25_y2 >= 0)
rule26_y2 = Real('rule26_y2')
s.add(rule26_y2 >= 0)
rule27_y2 = Real('rule27_y2')
s.add(rule27_y2 >= 0)
rule28_y2 = Real('rule28_y2')
s.add(rule28_y2 >= 0)
rule29_y2 = Real('rule29_y2')
s.add(rule29_y2 >= 0)






###################Step 2####################


#Flow equations for the locations

s.add(0 - rule0_y2 - rule1_y2 - rule14_y2 - rule22_y2 + rule22_y2 ==  loc0_x3 - loc0_y2)
s.add(0 - rule2_y2 - rule3_y2 - rule15_y2 - rule23_y2 + rule23_y2 ==  loc1_x3 - loc1_y2)
s.add(0 + rule0_y2 - rule4_y2 - rule6_y2 - rule8_y2 - rule10_y2 - rule12_y2 - rule16_y2 - rule24_y2 + rule24_y2 ==  locS0_x3 - locS0_y2)
s.add(0 + rule2_y2 - rule5_y2 - rule7_y2 - rule9_y2 - rule11_y2 - rule13_y2 - rule17_y2 - rule25_y2 + rule25_y2 ==  locS1_x3 - locS1_y2)
s.add(0 + rule4_y2 + rule5_y2 - rule18_y2 - rule26_y2 + rule26_y2 ==  locD0_x3 - locD0_y2)
s.add(0 + rule6_y2 + rule7_y2 - rule19_y2 - rule27_y2 + rule27_y2 ==  locD1_x3 - locD1_y2)
s.add(0 + rule8_y2 + rule9_y2 + rule12_y2 - rule20_y2 - rule28_y2 + rule28_y2 ==  locU0_x3 - locU0_y2)
s.add(0 + rule10_y2 + rule11_y2 + rule13_y2 - rule21_y2 - rule29_y2 + rule29_y2 ==  locU1_x3 - locU1_y2)
s.add(0 + rule1_y2 + rule3_y2 + rule14_y2 + rule15_y2 + rule16_y2 + rule17_y2 + rule18_y2 + rule19_y2 + rule20_y2 + rule21_y2 ==  locCR_x3 - locCR_y2)






##################Step 3########################


#Flow equations for the shared variables

s.add(0 + rule0_y2 == nsnt0_x3 - nsnt0_y2)
s.add(0 + rule2_y2 == nsnt1_x3 - nsnt1_y2)
s.add(0 + rule0_y2 + rule1_y2 == nsnt0CF_x3 - nsnt0CF_y2)
s.add(0 + rule2_y2 + rule3_y2 == nsnt1CF_x3 - nsnt1CF_y2)
s.add(0 + rule0_y2 + rule2_y2 == nsnt01_x3 - nsnt01_y2)
s.add(0 + rule0_y2 + rule1_y2 + rule2_y2 + rule3_y2 == nsnt01CF_x3 - nsnt01CF_y2)
s.add(0 + rule1_y2 + rule3_y2 + rule14_y2 + rule15_y2 + rule16_y2 + rule17_y2 + rule18_y2 + rule19_y2 + rule20_y2 + rule21_y2 == nfaulty_x3 - nfaulty_y2)






####################Step 4########################


#Rule is fired implies rule is enabled

s.add(Implies( (rule0_y2 > 0), And(True, ) ))
s.add(Implies( (rule1_y2 > 0), And(nfaulty_y2<F, ) ))
s.add(Implies( (rule2_y2 > 0), And(True, ) ))
s.add(Implies( (rule3_y2 > 0), And(nfaulty_y2<F, ) ))
s.add(Implies( (rule4_y2 > 0), And(nsnt0CF_y2>=N-T, ) ))
s.add(Implies( (rule5_y2 > 0), And(nsnt0CF_y2>=N-T, ) ))
s.add(Implies( (rule6_y2 > 0), And(nsnt1CF_y2>=N-T, ) ))
s.add(Implies( (rule7_y2 > 0), And(nsnt1CF_y2>=N-T, ) ))
s.add(Implies( (rule8_y2 > 0), And(nsnt01CF_y2>=N-T, nsnt0CF_y2>=N-2*T, nsnt1CF_y2>=1, ) ))
s.add(Implies( (rule9_y2 > 0), And(nsnt01CF_y2>=N-T, nsnt0CF_y2>=N-2*T, nsnt1CF_y2>=1, ) ))
s.add(Implies( (rule10_y2 > 0), And(nsnt01CF_y2>=N-T, nsnt1CF_y2>=N-2*T, nsnt0CF_y2>=1, ) ))
s.add(Implies( (rule11_y2 > 0), And(nsnt01CF_y2>=N-T, nsnt1CF_y2>=N-2*T, nsnt0CF_y2>=1, ) ))
s.add(Implies( (rule12_y2 > 0), And(nsnt01CF_y2>=N-T, nsnt0_y2<N-2*T, nsnt1_y2<N-2*T, ) ))
s.add(Implies( (rule13_y2 > 0), And(nsnt01CF_y2>=N-T, nsnt0_y2<N-2*T, nsnt1_y2<N-2*T, ) ))
s.add(Implies( (rule14_y2 > 0), And(nfaulty_y2<F, ) ))
s.add(Implies( (rule15_y2 > 0), And(nfaulty_y2<F, ) ))
s.add(Implies( (rule16_y2 > 0), And(nfaulty_y2<F, ) ))
s.add(Implies( (rule17_y2 > 0), And(nfaulty_y2<F, ) ))
s.add(Implies( (rule18_y2 > 0), And(nfaulty_y2<F, ) ))
s.add(Implies( (rule19_y2 > 0), And(nfaulty_y2<F, ) ))
s.add(Implies( (rule20_y2 > 0), And(nfaulty_y2<F, ) ))
s.add(Implies( (rule21_y2 > 0), And(nfaulty_y2<F, ) ))
s.add(Implies( (rule22_y2 > 0), And(True, ) ))
s.add(Implies( (rule23_y2 > 0), And(True, ) ))
s.add(Implies( (rule24_y2 > 0), And(True, ) ))
s.add(Implies( (rule25_y2 > 0), And(True, ) ))
s.add(Implies( (rule26_y2 > 0), And(True, ) ))
s.add(Implies( (rule27_y2 > 0), And(True, ) ))
s.add(Implies( (rule28_y2 > 0), And(True, ) ))
s.add(Implies( (rule29_y2 > 0), And(True, ) ))

##################Step 5########################


#Ensuring that at most one rule is fired alternating configurations y2 and x2, if a fall condition is present

s.add((nsnt1_x3<N-2*T) == (nsnt1_y2<N-2*T))
s.add(Implies(And((nsnt1_x3<N-2*T), Not(nsnt1_y2<N-2*T)), Or((rule0_y2 == 0), (rule0_y2 == 1))))
s.add(Implies(And((nsnt1_x3<N-2*T), Not(nsnt1_y2<N-2*T)), Or((rule1_y2 == 0), (rule1_y2 == 1))))
s.add(Implies(And((nsnt1_x3<N-2*T), Not(nsnt1_y2<N-2*T)), Or((rule2_y2 == 0), (rule2_y2 == 1))))
s.add(Implies(And((nsnt1_x3<N-2*T), Not(nsnt1_y2<N-2*T)), Or((rule3_y2 == 0), (rule3_y2 == 1))))
s.add(Implies(And((nsnt1_x3<N-2*T), Not(nsnt1_y2<N-2*T)), Or((rule4_y2 == 0), (rule4_y2 == 1))))
s.add(Implies(And((nsnt1_x3<N-2*T), Not(nsnt1_y2<N-2*T)), Or((rule5_y2 == 0), (rule5_y2 == 1))))
s.add(Implies(And((nsnt1_x3<N-2*T), Not(nsnt1_y2<N-2*T)), Or((rule6_y2 == 0), (rule6_y2 == 1))))
s.add(Implies(And((nsnt1_x3<N-2*T), Not(nsnt1_y2<N-2*T)), Or((rule7_y2 == 0), (rule7_y2 == 1))))
s.add(Implies(And((nsnt1_x3<N-2*T), Not(nsnt1_y2<N-2*T)), Or((rule8_y2 == 0), (rule8_y2 == 1))))
s.add(Implies(And((nsnt1_x3<N-2*T), Not(nsnt1_y2<N-2*T)), Or((rule9_y2 == 0), (rule9_y2 == 1))))
s.add(Implies(And((nsnt1_x3<N-2*T), Not(nsnt1_y2<N-2*T)), Or((rule10_y2 == 0), (rule10_y2 == 1))))
s.add(Implies(And((nsnt1_x3<N-2*T), Not(nsnt1_y2<N-2*T)), Or((rule11_y2 == 0), (rule11_y2 == 1))))
s.add(Implies(And((nsnt1_x3<N-2*T), Not(nsnt1_y2<N-2*T)), Or((rule12_y2 == 0), (rule12_y2 == 1))))
s.add(Implies(And((nsnt1_x3<N-2*T), Not(nsnt1_y2<N-2*T)), Or((rule13_y2 == 0), (rule13_y2 == 1))))
s.add(Implies(And((nsnt1_x3<N-2*T), Not(nsnt1_y2<N-2*T)), Or((rule14_y2 == 0), (rule14_y2 == 1))))
s.add(Implies(And((nsnt1_x3<N-2*T), Not(nsnt1_y2<N-2*T)), Or((rule15_y2 == 0), (rule15_y2 == 1))))
s.add(Implies(And((nsnt1_x3<N-2*T), Not(nsnt1_y2<N-2*T)), Or((rule16_y2 == 0), (rule16_y2 == 1))))
s.add(Implies(And((nsnt1_x3<N-2*T), Not(nsnt1_y2<N-2*T)), Or((rule17_y2 == 0), (rule17_y2 == 1))))
s.add(Implies(And((nsnt1_x3<N-2*T), Not(nsnt1_y2<N-2*T)), Or((rule18_y2 == 0), (rule18_y2 == 1))))
s.add(Implies(And((nsnt1_x3<N-2*T), Not(nsnt1_y2<N-2*T)), Or((rule19_y2 == 0), (rule19_y2 == 1))))
s.add(Implies(And((nsnt1_x3<N-2*T), Not(nsnt1_y2<N-2*T)), Or((rule20_y2 == 0), (rule20_y2 == 1))))
s.add(Implies(And((nsnt1_x3<N-2*T), Not(nsnt1_y2<N-2*T)), Or((rule21_y2 == 0), (rule21_y2 == 1))))
s.add(Implies(And((nsnt1_x3<N-2*T), Not(nsnt1_y2<N-2*T)), Or((rule22_y2 == 0), (rule22_y2 == 1))))
s.add(Implies(And((nsnt1_x3<N-2*T), Not(nsnt1_y2<N-2*T)), Or((rule23_y2 == 0), (rule23_y2 == 1))))
s.add(Implies(And((nsnt1_x3<N-2*T), Not(nsnt1_y2<N-2*T)), Or((rule24_y2 == 0), (rule24_y2 == 1))))
s.add(Implies(And((nsnt1_x3<N-2*T), Not(nsnt1_y2<N-2*T)), Or((rule25_y2 == 0), (rule25_y2 == 1))))
s.add(Implies(And((nsnt1_x3<N-2*T), Not(nsnt1_y2<N-2*T)), Or((rule26_y2 == 0), (rule26_y2 == 1))))
s.add(Implies(And((nsnt1_x3<N-2*T), Not(nsnt1_y2<N-2*T)), Or((rule27_y2 == 0), (rule27_y2 == 1))))
s.add(Implies(And((nsnt1_x3<N-2*T), Not(nsnt1_y2<N-2*T)), Or((rule28_y2 == 0), (rule28_y2 == 1))))
s.add(Implies(And((nsnt1_x3<N-2*T), Not(nsnt1_y2<N-2*T)), Or((rule29_y2 == 0), (rule29_y2 == 1))))
s.add(Implies(And((nsnt1_x3<N-2*T), Not(nsnt1_y2<N-2*T)), rule0_y2+rule1_y2+rule2_y2+rule3_y2+rule4_y2+rule5_y2+rule6_y2+rule7_y2+rule8_y2+rule9_y2+rule10_y2+rule11_y2+rule12_y2+rule13_y2+rule14_y2+rule15_y2+rule16_y2+rule17_y2+rule18_y2+rule19_y2+rule20_y2+rule21_y2+rule22_y2+rule23_y2+rule24_y2+rule25_y2+rule26_y2+rule27_y2+rule28_y2+rule29_y2 <= 1))

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
s.add(Implies(And((nfaulty_x3<F), Not(nfaulty_y2<F)), Or((rule14_y2 == 0), (rule14_y2 == 1))))
s.add(Implies(And((nfaulty_x3<F), Not(nfaulty_y2<F)), Or((rule15_y2 == 0), (rule15_y2 == 1))))
s.add(Implies(And((nfaulty_x3<F), Not(nfaulty_y2<F)), Or((rule16_y2 == 0), (rule16_y2 == 1))))
s.add(Implies(And((nfaulty_x3<F), Not(nfaulty_y2<F)), Or((rule17_y2 == 0), (rule17_y2 == 1))))
s.add(Implies(And((nfaulty_x3<F), Not(nfaulty_y2<F)), Or((rule18_y2 == 0), (rule18_y2 == 1))))
s.add(Implies(And((nfaulty_x3<F), Not(nfaulty_y2<F)), Or((rule19_y2 == 0), (rule19_y2 == 1))))
s.add(Implies(And((nfaulty_x3<F), Not(nfaulty_y2<F)), Or((rule20_y2 == 0), (rule20_y2 == 1))))
s.add(Implies(And((nfaulty_x3<F), Not(nfaulty_y2<F)), Or((rule21_y2 == 0), (rule21_y2 == 1))))
s.add(Implies(And((nfaulty_x3<F), Not(nfaulty_y2<F)), Or((rule22_y2 == 0), (rule22_y2 == 1))))
s.add(Implies(And((nfaulty_x3<F), Not(nfaulty_y2<F)), Or((rule23_y2 == 0), (rule23_y2 == 1))))
s.add(Implies(And((nfaulty_x3<F), Not(nfaulty_y2<F)), Or((rule24_y2 == 0), (rule24_y2 == 1))))
s.add(Implies(And((nfaulty_x3<F), Not(nfaulty_y2<F)), Or((rule25_y2 == 0), (rule25_y2 == 1))))
s.add(Implies(And((nfaulty_x3<F), Not(nfaulty_y2<F)), Or((rule26_y2 == 0), (rule26_y2 == 1))))
s.add(Implies(And((nfaulty_x3<F), Not(nfaulty_y2<F)), Or((rule27_y2 == 0), (rule27_y2 == 1))))
s.add(Implies(And((nfaulty_x3<F), Not(nfaulty_y2<F)), Or((rule28_y2 == 0), (rule28_y2 == 1))))
s.add(Implies(And((nfaulty_x3<F), Not(nfaulty_y2<F)), Or((rule29_y2 == 0), (rule29_y2 == 1))))
s.add(Implies(And((nfaulty_x3<F), Not(nfaulty_y2<F)), rule0_y2+rule1_y2+rule2_y2+rule3_y2+rule4_y2+rule5_y2+rule6_y2+rule7_y2+rule8_y2+rule9_y2+rule10_y2+rule11_y2+rule12_y2+rule13_y2+rule14_y2+rule15_y2+rule16_y2+rule17_y2+rule18_y2+rule19_y2+rule20_y2+rule21_y2+rule22_y2+rule23_y2+rule24_y2+rule25_y2+rule26_y2+rule27_y2+rule28_y2+rule29_y2 <= 1))

s.add((nsnt0_x3<N-2*T) == (nsnt0_y2<N-2*T))
s.add(Implies(And((nsnt0_x3<N-2*T), Not(nsnt0_y2<N-2*T)), Or((rule0_y2 == 0), (rule0_y2 == 1))))
s.add(Implies(And((nsnt0_x3<N-2*T), Not(nsnt0_y2<N-2*T)), Or((rule1_y2 == 0), (rule1_y2 == 1))))
s.add(Implies(And((nsnt0_x3<N-2*T), Not(nsnt0_y2<N-2*T)), Or((rule2_y2 == 0), (rule2_y2 == 1))))
s.add(Implies(And((nsnt0_x3<N-2*T), Not(nsnt0_y2<N-2*T)), Or((rule3_y2 == 0), (rule3_y2 == 1))))
s.add(Implies(And((nsnt0_x3<N-2*T), Not(nsnt0_y2<N-2*T)), Or((rule4_y2 == 0), (rule4_y2 == 1))))
s.add(Implies(And((nsnt0_x3<N-2*T), Not(nsnt0_y2<N-2*T)), Or((rule5_y2 == 0), (rule5_y2 == 1))))
s.add(Implies(And((nsnt0_x3<N-2*T), Not(nsnt0_y2<N-2*T)), Or((rule6_y2 == 0), (rule6_y2 == 1))))
s.add(Implies(And((nsnt0_x3<N-2*T), Not(nsnt0_y2<N-2*T)), Or((rule7_y2 == 0), (rule7_y2 == 1))))
s.add(Implies(And((nsnt0_x3<N-2*T), Not(nsnt0_y2<N-2*T)), Or((rule8_y2 == 0), (rule8_y2 == 1))))
s.add(Implies(And((nsnt0_x3<N-2*T), Not(nsnt0_y2<N-2*T)), Or((rule9_y2 == 0), (rule9_y2 == 1))))
s.add(Implies(And((nsnt0_x3<N-2*T), Not(nsnt0_y2<N-2*T)), Or((rule10_y2 == 0), (rule10_y2 == 1))))
s.add(Implies(And((nsnt0_x3<N-2*T), Not(nsnt0_y2<N-2*T)), Or((rule11_y2 == 0), (rule11_y2 == 1))))
s.add(Implies(And((nsnt0_x3<N-2*T), Not(nsnt0_y2<N-2*T)), Or((rule12_y2 == 0), (rule12_y2 == 1))))
s.add(Implies(And((nsnt0_x3<N-2*T), Not(nsnt0_y2<N-2*T)), Or((rule13_y2 == 0), (rule13_y2 == 1))))
s.add(Implies(And((nsnt0_x3<N-2*T), Not(nsnt0_y2<N-2*T)), Or((rule14_y2 == 0), (rule14_y2 == 1))))
s.add(Implies(And((nsnt0_x3<N-2*T), Not(nsnt0_y2<N-2*T)), Or((rule15_y2 == 0), (rule15_y2 == 1))))
s.add(Implies(And((nsnt0_x3<N-2*T), Not(nsnt0_y2<N-2*T)), Or((rule16_y2 == 0), (rule16_y2 == 1))))
s.add(Implies(And((nsnt0_x3<N-2*T), Not(nsnt0_y2<N-2*T)), Or((rule17_y2 == 0), (rule17_y2 == 1))))
s.add(Implies(And((nsnt0_x3<N-2*T), Not(nsnt0_y2<N-2*T)), Or((rule18_y2 == 0), (rule18_y2 == 1))))
s.add(Implies(And((nsnt0_x3<N-2*T), Not(nsnt0_y2<N-2*T)), Or((rule19_y2 == 0), (rule19_y2 == 1))))
s.add(Implies(And((nsnt0_x3<N-2*T), Not(nsnt0_y2<N-2*T)), Or((rule20_y2 == 0), (rule20_y2 == 1))))
s.add(Implies(And((nsnt0_x3<N-2*T), Not(nsnt0_y2<N-2*T)), Or((rule21_y2 == 0), (rule21_y2 == 1))))
s.add(Implies(And((nsnt0_x3<N-2*T), Not(nsnt0_y2<N-2*T)), Or((rule22_y2 == 0), (rule22_y2 == 1))))
s.add(Implies(And((nsnt0_x3<N-2*T), Not(nsnt0_y2<N-2*T)), Or((rule23_y2 == 0), (rule23_y2 == 1))))
s.add(Implies(And((nsnt0_x3<N-2*T), Not(nsnt0_y2<N-2*T)), Or((rule24_y2 == 0), (rule24_y2 == 1))))
s.add(Implies(And((nsnt0_x3<N-2*T), Not(nsnt0_y2<N-2*T)), Or((rule25_y2 == 0), (rule25_y2 == 1))))
s.add(Implies(And((nsnt0_x3<N-2*T), Not(nsnt0_y2<N-2*T)), Or((rule26_y2 == 0), (rule26_y2 == 1))))
s.add(Implies(And((nsnt0_x3<N-2*T), Not(nsnt0_y2<N-2*T)), Or((rule27_y2 == 0), (rule27_y2 == 1))))
s.add(Implies(And((nsnt0_x3<N-2*T), Not(nsnt0_y2<N-2*T)), Or((rule28_y2 == 0), (rule28_y2 == 1))))
s.add(Implies(And((nsnt0_x3<N-2*T), Not(nsnt0_y2<N-2*T)), Or((rule29_y2 == 0), (rule29_y2 == 1))))
s.add(Implies(And((nsnt0_x3<N-2*T), Not(nsnt0_y2<N-2*T)), rule0_y2+rule1_y2+rule2_y2+rule3_y2+rule4_y2+rule5_y2+rule6_y2+rule7_y2+rule8_y2+rule9_y2+rule10_y2+rule11_y2+rule12_y2+rule13_y2+rule14_y2+rule15_y2+rule16_y2+rule17_y2+rule18_y2+rule19_y2+rule20_y2+rule21_y2+rule22_y2+rule23_y2+rule24_y2+rule25_y2+rule26_y2+rule27_y2+rule28_y2+rule29_y2 <= 1))


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
rule14_y3 = Real('rule14_y3')
s.add(rule14_y3 >= 0)
rule15_y3 = Real('rule15_y3')
s.add(rule15_y3 >= 0)
rule16_y3 = Real('rule16_y3')
s.add(rule16_y3 >= 0)
rule17_y3 = Real('rule17_y3')
s.add(rule17_y3 >= 0)
rule18_y3 = Real('rule18_y3')
s.add(rule18_y3 >= 0)
rule19_y3 = Real('rule19_y3')
s.add(rule19_y3 >= 0)
rule20_y3 = Real('rule20_y3')
s.add(rule20_y3 >= 0)
rule21_y3 = Real('rule21_y3')
s.add(rule21_y3 >= 0)
rule22_y3 = Real('rule22_y3')
s.add(rule22_y3 >= 0)
rule23_y3 = Real('rule23_y3')
s.add(rule23_y3 >= 0)
rule24_y3 = Real('rule24_y3')
s.add(rule24_y3 >= 0)
rule25_y3 = Real('rule25_y3')
s.add(rule25_y3 >= 0)
rule26_y3 = Real('rule26_y3')
s.add(rule26_y3 >= 0)
rule27_y3 = Real('rule27_y3')
s.add(rule27_y3 >= 0)
rule28_y3 = Real('rule28_y3')
s.add(rule28_y3 >= 0)
rule29_y3 = Real('rule29_y3')
s.add(rule29_y3 >= 0)






###################Step 2####################


#Flow equations for the locations

s.add(0 - rule0_y3 - rule1_y3 - rule14_y3 - rule22_y3 + rule22_y3 ==  loc0_x4 - loc0_y3)
s.add(0 - rule2_y3 - rule3_y3 - rule15_y3 - rule23_y3 + rule23_y3 ==  loc1_x4 - loc1_y3)
s.add(0 + rule0_y3 - rule4_y3 - rule6_y3 - rule8_y3 - rule10_y3 - rule12_y3 - rule16_y3 - rule24_y3 + rule24_y3 ==  locS0_x4 - locS0_y3)
s.add(0 + rule2_y3 - rule5_y3 - rule7_y3 - rule9_y3 - rule11_y3 - rule13_y3 - rule17_y3 - rule25_y3 + rule25_y3 ==  locS1_x4 - locS1_y3)
s.add(0 + rule4_y3 + rule5_y3 - rule18_y3 - rule26_y3 + rule26_y3 ==  locD0_x4 - locD0_y3)
s.add(0 + rule6_y3 + rule7_y3 - rule19_y3 - rule27_y3 + rule27_y3 ==  locD1_x4 - locD1_y3)
s.add(0 + rule8_y3 + rule9_y3 + rule12_y3 - rule20_y3 - rule28_y3 + rule28_y3 ==  locU0_x4 - locU0_y3)
s.add(0 + rule10_y3 + rule11_y3 + rule13_y3 - rule21_y3 - rule29_y3 + rule29_y3 ==  locU1_x4 - locU1_y3)
s.add(0 + rule1_y3 + rule3_y3 + rule14_y3 + rule15_y3 + rule16_y3 + rule17_y3 + rule18_y3 + rule19_y3 + rule20_y3 + rule21_y3 ==  locCR_x4 - locCR_y3)






##################Step 3########################


#Flow equations for the shared variables

s.add(0 + rule0_y3 == nsnt0_x4 - nsnt0_y3)
s.add(0 + rule2_y3 == nsnt1_x4 - nsnt1_y3)
s.add(0 + rule0_y3 + rule1_y3 == nsnt0CF_x4 - nsnt0CF_y3)
s.add(0 + rule2_y3 + rule3_y3 == nsnt1CF_x4 - nsnt1CF_y3)
s.add(0 + rule0_y3 + rule2_y3 == nsnt01_x4 - nsnt01_y3)
s.add(0 + rule0_y3 + rule1_y3 + rule2_y3 + rule3_y3 == nsnt01CF_x4 - nsnt01CF_y3)
s.add(0 + rule1_y3 + rule3_y3 + rule14_y3 + rule15_y3 + rule16_y3 + rule17_y3 + rule18_y3 + rule19_y3 + rule20_y3 + rule21_y3 == nfaulty_x4 - nfaulty_y3)






####################Step 4########################


#Rule is fired implies rule is enabled

s.add(Implies( (rule0_y3 > 0), And(True, ) ))
s.add(Implies( (rule1_y3 > 0), And(nfaulty_y3<F, ) ))
s.add(Implies( (rule2_y3 > 0), And(True, ) ))
s.add(Implies( (rule3_y3 > 0), And(nfaulty_y3<F, ) ))
s.add(Implies( (rule4_y3 > 0), And(nsnt0CF_y3>=N-T, ) ))
s.add(Implies( (rule5_y3 > 0), And(nsnt0CF_y3>=N-T, ) ))
s.add(Implies( (rule6_y3 > 0), And(nsnt1CF_y3>=N-T, ) ))
s.add(Implies( (rule7_y3 > 0), And(nsnt1CF_y3>=N-T, ) ))
s.add(Implies( (rule8_y3 > 0), And(nsnt01CF_y3>=N-T, nsnt0CF_y3>=N-2*T, nsnt1CF_y3>=1, ) ))
s.add(Implies( (rule9_y3 > 0), And(nsnt01CF_y3>=N-T, nsnt0CF_y3>=N-2*T, nsnt1CF_y3>=1, ) ))
s.add(Implies( (rule10_y3 > 0), And(nsnt01CF_y3>=N-T, nsnt1CF_y3>=N-2*T, nsnt0CF_y3>=1, ) ))
s.add(Implies( (rule11_y3 > 0), And(nsnt01CF_y3>=N-T, nsnt1CF_y3>=N-2*T, nsnt0CF_y3>=1, ) ))
s.add(Implies( (rule12_y3 > 0), And(nsnt01CF_y3>=N-T, nsnt0_y3<N-2*T, nsnt1_y3<N-2*T, ) ))
s.add(Implies( (rule13_y3 > 0), And(nsnt01CF_y3>=N-T, nsnt0_y3<N-2*T, nsnt1_y3<N-2*T, ) ))
s.add(Implies( (rule14_y3 > 0), And(nfaulty_y3<F, ) ))
s.add(Implies( (rule15_y3 > 0), And(nfaulty_y3<F, ) ))
s.add(Implies( (rule16_y3 > 0), And(nfaulty_y3<F, ) ))
s.add(Implies( (rule17_y3 > 0), And(nfaulty_y3<F, ) ))
s.add(Implies( (rule18_y3 > 0), And(nfaulty_y3<F, ) ))
s.add(Implies( (rule19_y3 > 0), And(nfaulty_y3<F, ) ))
s.add(Implies( (rule20_y3 > 0), And(nfaulty_y3<F, ) ))
s.add(Implies( (rule21_y3 > 0), And(nfaulty_y3<F, ) ))
s.add(Implies( (rule22_y3 > 0), And(True, ) ))
s.add(Implies( (rule23_y3 > 0), And(True, ) ))
s.add(Implies( (rule24_y3 > 0), And(True, ) ))
s.add(Implies( (rule25_y3 > 0), And(True, ) ))
s.add(Implies( (rule26_y3 > 0), And(True, ) ))
s.add(Implies( (rule27_y3 > 0), And(True, ) ))
s.add(Implies( (rule28_y3 > 0), And(True, ) ))
s.add(Implies( (rule29_y3 > 0), And(True, ) ))

##################Step 5########################


#Ensuring that at most one rule is fired alternating configurations y3 and x3, if a fall condition is present

s.add((nsnt1_x4<N-2*T) == (nsnt1_y3<N-2*T))
s.add(Implies(And((nsnt1_x4<N-2*T), Not(nsnt1_y3<N-2*T)), Or((rule0_y3 == 0), (rule0_y3 == 1))))
s.add(Implies(And((nsnt1_x4<N-2*T), Not(nsnt1_y3<N-2*T)), Or((rule1_y3 == 0), (rule1_y3 == 1))))
s.add(Implies(And((nsnt1_x4<N-2*T), Not(nsnt1_y3<N-2*T)), Or((rule2_y3 == 0), (rule2_y3 == 1))))
s.add(Implies(And((nsnt1_x4<N-2*T), Not(nsnt1_y3<N-2*T)), Or((rule3_y3 == 0), (rule3_y3 == 1))))
s.add(Implies(And((nsnt1_x4<N-2*T), Not(nsnt1_y3<N-2*T)), Or((rule4_y3 == 0), (rule4_y3 == 1))))
s.add(Implies(And((nsnt1_x4<N-2*T), Not(nsnt1_y3<N-2*T)), Or((rule5_y3 == 0), (rule5_y3 == 1))))
s.add(Implies(And((nsnt1_x4<N-2*T), Not(nsnt1_y3<N-2*T)), Or((rule6_y3 == 0), (rule6_y3 == 1))))
s.add(Implies(And((nsnt1_x4<N-2*T), Not(nsnt1_y3<N-2*T)), Or((rule7_y3 == 0), (rule7_y3 == 1))))
s.add(Implies(And((nsnt1_x4<N-2*T), Not(nsnt1_y3<N-2*T)), Or((rule8_y3 == 0), (rule8_y3 == 1))))
s.add(Implies(And((nsnt1_x4<N-2*T), Not(nsnt1_y3<N-2*T)), Or((rule9_y3 == 0), (rule9_y3 == 1))))
s.add(Implies(And((nsnt1_x4<N-2*T), Not(nsnt1_y3<N-2*T)), Or((rule10_y3 == 0), (rule10_y3 == 1))))
s.add(Implies(And((nsnt1_x4<N-2*T), Not(nsnt1_y3<N-2*T)), Or((rule11_y3 == 0), (rule11_y3 == 1))))
s.add(Implies(And((nsnt1_x4<N-2*T), Not(nsnt1_y3<N-2*T)), Or((rule12_y3 == 0), (rule12_y3 == 1))))
s.add(Implies(And((nsnt1_x4<N-2*T), Not(nsnt1_y3<N-2*T)), Or((rule13_y3 == 0), (rule13_y3 == 1))))
s.add(Implies(And((nsnt1_x4<N-2*T), Not(nsnt1_y3<N-2*T)), Or((rule14_y3 == 0), (rule14_y3 == 1))))
s.add(Implies(And((nsnt1_x4<N-2*T), Not(nsnt1_y3<N-2*T)), Or((rule15_y3 == 0), (rule15_y3 == 1))))
s.add(Implies(And((nsnt1_x4<N-2*T), Not(nsnt1_y3<N-2*T)), Or((rule16_y3 == 0), (rule16_y3 == 1))))
s.add(Implies(And((nsnt1_x4<N-2*T), Not(nsnt1_y3<N-2*T)), Or((rule17_y3 == 0), (rule17_y3 == 1))))
s.add(Implies(And((nsnt1_x4<N-2*T), Not(nsnt1_y3<N-2*T)), Or((rule18_y3 == 0), (rule18_y3 == 1))))
s.add(Implies(And((nsnt1_x4<N-2*T), Not(nsnt1_y3<N-2*T)), Or((rule19_y3 == 0), (rule19_y3 == 1))))
s.add(Implies(And((nsnt1_x4<N-2*T), Not(nsnt1_y3<N-2*T)), Or((rule20_y3 == 0), (rule20_y3 == 1))))
s.add(Implies(And((nsnt1_x4<N-2*T), Not(nsnt1_y3<N-2*T)), Or((rule21_y3 == 0), (rule21_y3 == 1))))
s.add(Implies(And((nsnt1_x4<N-2*T), Not(nsnt1_y3<N-2*T)), Or((rule22_y3 == 0), (rule22_y3 == 1))))
s.add(Implies(And((nsnt1_x4<N-2*T), Not(nsnt1_y3<N-2*T)), Or((rule23_y3 == 0), (rule23_y3 == 1))))
s.add(Implies(And((nsnt1_x4<N-2*T), Not(nsnt1_y3<N-2*T)), Or((rule24_y3 == 0), (rule24_y3 == 1))))
s.add(Implies(And((nsnt1_x4<N-2*T), Not(nsnt1_y3<N-2*T)), Or((rule25_y3 == 0), (rule25_y3 == 1))))
s.add(Implies(And((nsnt1_x4<N-2*T), Not(nsnt1_y3<N-2*T)), Or((rule26_y3 == 0), (rule26_y3 == 1))))
s.add(Implies(And((nsnt1_x4<N-2*T), Not(nsnt1_y3<N-2*T)), Or((rule27_y3 == 0), (rule27_y3 == 1))))
s.add(Implies(And((nsnt1_x4<N-2*T), Not(nsnt1_y3<N-2*T)), Or((rule28_y3 == 0), (rule28_y3 == 1))))
s.add(Implies(And((nsnt1_x4<N-2*T), Not(nsnt1_y3<N-2*T)), Or((rule29_y3 == 0), (rule29_y3 == 1))))
s.add(Implies(And((nsnt1_x4<N-2*T), Not(nsnt1_y3<N-2*T)), rule0_y3+rule1_y3+rule2_y3+rule3_y3+rule4_y3+rule5_y3+rule6_y3+rule7_y3+rule8_y3+rule9_y3+rule10_y3+rule11_y3+rule12_y3+rule13_y3+rule14_y3+rule15_y3+rule16_y3+rule17_y3+rule18_y3+rule19_y3+rule20_y3+rule21_y3+rule22_y3+rule23_y3+rule24_y3+rule25_y3+rule26_y3+rule27_y3+rule28_y3+rule29_y3 <= 1))

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
s.add(Implies(And((nfaulty_x4<F), Not(nfaulty_y3<F)), Or((rule14_y3 == 0), (rule14_y3 == 1))))
s.add(Implies(And((nfaulty_x4<F), Not(nfaulty_y3<F)), Or((rule15_y3 == 0), (rule15_y3 == 1))))
s.add(Implies(And((nfaulty_x4<F), Not(nfaulty_y3<F)), Or((rule16_y3 == 0), (rule16_y3 == 1))))
s.add(Implies(And((nfaulty_x4<F), Not(nfaulty_y3<F)), Or((rule17_y3 == 0), (rule17_y3 == 1))))
s.add(Implies(And((nfaulty_x4<F), Not(nfaulty_y3<F)), Or((rule18_y3 == 0), (rule18_y3 == 1))))
s.add(Implies(And((nfaulty_x4<F), Not(nfaulty_y3<F)), Or((rule19_y3 == 0), (rule19_y3 == 1))))
s.add(Implies(And((nfaulty_x4<F), Not(nfaulty_y3<F)), Or((rule20_y3 == 0), (rule20_y3 == 1))))
s.add(Implies(And((nfaulty_x4<F), Not(nfaulty_y3<F)), Or((rule21_y3 == 0), (rule21_y3 == 1))))
s.add(Implies(And((nfaulty_x4<F), Not(nfaulty_y3<F)), Or((rule22_y3 == 0), (rule22_y3 == 1))))
s.add(Implies(And((nfaulty_x4<F), Not(nfaulty_y3<F)), Or((rule23_y3 == 0), (rule23_y3 == 1))))
s.add(Implies(And((nfaulty_x4<F), Not(nfaulty_y3<F)), Or((rule24_y3 == 0), (rule24_y3 == 1))))
s.add(Implies(And((nfaulty_x4<F), Not(nfaulty_y3<F)), Or((rule25_y3 == 0), (rule25_y3 == 1))))
s.add(Implies(And((nfaulty_x4<F), Not(nfaulty_y3<F)), Or((rule26_y3 == 0), (rule26_y3 == 1))))
s.add(Implies(And((nfaulty_x4<F), Not(nfaulty_y3<F)), Or((rule27_y3 == 0), (rule27_y3 == 1))))
s.add(Implies(And((nfaulty_x4<F), Not(nfaulty_y3<F)), Or((rule28_y3 == 0), (rule28_y3 == 1))))
s.add(Implies(And((nfaulty_x4<F), Not(nfaulty_y3<F)), Or((rule29_y3 == 0), (rule29_y3 == 1))))
s.add(Implies(And((nfaulty_x4<F), Not(nfaulty_y3<F)), rule0_y3+rule1_y3+rule2_y3+rule3_y3+rule4_y3+rule5_y3+rule6_y3+rule7_y3+rule8_y3+rule9_y3+rule10_y3+rule11_y3+rule12_y3+rule13_y3+rule14_y3+rule15_y3+rule16_y3+rule17_y3+rule18_y3+rule19_y3+rule20_y3+rule21_y3+rule22_y3+rule23_y3+rule24_y3+rule25_y3+rule26_y3+rule27_y3+rule28_y3+rule29_y3 <= 1))

s.add((nsnt0_x4<N-2*T) == (nsnt0_y3<N-2*T))
s.add(Implies(And((nsnt0_x4<N-2*T), Not(nsnt0_y3<N-2*T)), Or((rule0_y3 == 0), (rule0_y3 == 1))))
s.add(Implies(And((nsnt0_x4<N-2*T), Not(nsnt0_y3<N-2*T)), Or((rule1_y3 == 0), (rule1_y3 == 1))))
s.add(Implies(And((nsnt0_x4<N-2*T), Not(nsnt0_y3<N-2*T)), Or((rule2_y3 == 0), (rule2_y3 == 1))))
s.add(Implies(And((nsnt0_x4<N-2*T), Not(nsnt0_y3<N-2*T)), Or((rule3_y3 == 0), (rule3_y3 == 1))))
s.add(Implies(And((nsnt0_x4<N-2*T), Not(nsnt0_y3<N-2*T)), Or((rule4_y3 == 0), (rule4_y3 == 1))))
s.add(Implies(And((nsnt0_x4<N-2*T), Not(nsnt0_y3<N-2*T)), Or((rule5_y3 == 0), (rule5_y3 == 1))))
s.add(Implies(And((nsnt0_x4<N-2*T), Not(nsnt0_y3<N-2*T)), Or((rule6_y3 == 0), (rule6_y3 == 1))))
s.add(Implies(And((nsnt0_x4<N-2*T), Not(nsnt0_y3<N-2*T)), Or((rule7_y3 == 0), (rule7_y3 == 1))))
s.add(Implies(And((nsnt0_x4<N-2*T), Not(nsnt0_y3<N-2*T)), Or((rule8_y3 == 0), (rule8_y3 == 1))))
s.add(Implies(And((nsnt0_x4<N-2*T), Not(nsnt0_y3<N-2*T)), Or((rule9_y3 == 0), (rule9_y3 == 1))))
s.add(Implies(And((nsnt0_x4<N-2*T), Not(nsnt0_y3<N-2*T)), Or((rule10_y3 == 0), (rule10_y3 == 1))))
s.add(Implies(And((nsnt0_x4<N-2*T), Not(nsnt0_y3<N-2*T)), Or((rule11_y3 == 0), (rule11_y3 == 1))))
s.add(Implies(And((nsnt0_x4<N-2*T), Not(nsnt0_y3<N-2*T)), Or((rule12_y3 == 0), (rule12_y3 == 1))))
s.add(Implies(And((nsnt0_x4<N-2*T), Not(nsnt0_y3<N-2*T)), Or((rule13_y3 == 0), (rule13_y3 == 1))))
s.add(Implies(And((nsnt0_x4<N-2*T), Not(nsnt0_y3<N-2*T)), Or((rule14_y3 == 0), (rule14_y3 == 1))))
s.add(Implies(And((nsnt0_x4<N-2*T), Not(nsnt0_y3<N-2*T)), Or((rule15_y3 == 0), (rule15_y3 == 1))))
s.add(Implies(And((nsnt0_x4<N-2*T), Not(nsnt0_y3<N-2*T)), Or((rule16_y3 == 0), (rule16_y3 == 1))))
s.add(Implies(And((nsnt0_x4<N-2*T), Not(nsnt0_y3<N-2*T)), Or((rule17_y3 == 0), (rule17_y3 == 1))))
s.add(Implies(And((nsnt0_x4<N-2*T), Not(nsnt0_y3<N-2*T)), Or((rule18_y3 == 0), (rule18_y3 == 1))))
s.add(Implies(And((nsnt0_x4<N-2*T), Not(nsnt0_y3<N-2*T)), Or((rule19_y3 == 0), (rule19_y3 == 1))))
s.add(Implies(And((nsnt0_x4<N-2*T), Not(nsnt0_y3<N-2*T)), Or((rule20_y3 == 0), (rule20_y3 == 1))))
s.add(Implies(And((nsnt0_x4<N-2*T), Not(nsnt0_y3<N-2*T)), Or((rule21_y3 == 0), (rule21_y3 == 1))))
s.add(Implies(And((nsnt0_x4<N-2*T), Not(nsnt0_y3<N-2*T)), Or((rule22_y3 == 0), (rule22_y3 == 1))))
s.add(Implies(And((nsnt0_x4<N-2*T), Not(nsnt0_y3<N-2*T)), Or((rule23_y3 == 0), (rule23_y3 == 1))))
s.add(Implies(And((nsnt0_x4<N-2*T), Not(nsnt0_y3<N-2*T)), Or((rule24_y3 == 0), (rule24_y3 == 1))))
s.add(Implies(And((nsnt0_x4<N-2*T), Not(nsnt0_y3<N-2*T)), Or((rule25_y3 == 0), (rule25_y3 == 1))))
s.add(Implies(And((nsnt0_x4<N-2*T), Not(nsnt0_y3<N-2*T)), Or((rule26_y3 == 0), (rule26_y3 == 1))))
s.add(Implies(And((nsnt0_x4<N-2*T), Not(nsnt0_y3<N-2*T)), Or((rule27_y3 == 0), (rule27_y3 == 1))))
s.add(Implies(And((nsnt0_x4<N-2*T), Not(nsnt0_y3<N-2*T)), Or((rule28_y3 == 0), (rule28_y3 == 1))))
s.add(Implies(And((nsnt0_x4<N-2*T), Not(nsnt0_y3<N-2*T)), Or((rule29_y3 == 0), (rule29_y3 == 1))))
s.add(Implies(And((nsnt0_x4<N-2*T), Not(nsnt0_y3<N-2*T)), rule0_y3+rule1_y3+rule2_y3+rule3_y3+rule4_y3+rule5_y3+rule6_y3+rule7_y3+rule8_y3+rule9_y3+rule10_y3+rule11_y3+rule12_y3+rule13_y3+rule14_y3+rule15_y3+rule16_y3+rule17_y3+rule18_y3+rule19_y3+rule20_y3+rule21_y3+rule22_y3+rule23_y3+rule24_y3+rule25_y3+rule26_y3+rule27_y3+rule28_y3+rule29_y3 <= 1))


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
rule14_y4 = Real('rule14_y4')
s.add(rule14_y4 >= 0)
rule15_y4 = Real('rule15_y4')
s.add(rule15_y4 >= 0)
rule16_y4 = Real('rule16_y4')
s.add(rule16_y4 >= 0)
rule17_y4 = Real('rule17_y4')
s.add(rule17_y4 >= 0)
rule18_y4 = Real('rule18_y4')
s.add(rule18_y4 >= 0)
rule19_y4 = Real('rule19_y4')
s.add(rule19_y4 >= 0)
rule20_y4 = Real('rule20_y4')
s.add(rule20_y4 >= 0)
rule21_y4 = Real('rule21_y4')
s.add(rule21_y4 >= 0)
rule22_y4 = Real('rule22_y4')
s.add(rule22_y4 >= 0)
rule23_y4 = Real('rule23_y4')
s.add(rule23_y4 >= 0)
rule24_y4 = Real('rule24_y4')
s.add(rule24_y4 >= 0)
rule25_y4 = Real('rule25_y4')
s.add(rule25_y4 >= 0)
rule26_y4 = Real('rule26_y4')
s.add(rule26_y4 >= 0)
rule27_y4 = Real('rule27_y4')
s.add(rule27_y4 >= 0)
rule28_y4 = Real('rule28_y4')
s.add(rule28_y4 >= 0)
rule29_y4 = Real('rule29_y4')
s.add(rule29_y4 >= 0)






###################Step 2####################


#Flow equations for the locations

s.add(0 - rule0_y4 - rule1_y4 - rule14_y4 - rule22_y4 + rule22_y4 ==  loc0_x5 - loc0_y4)
s.add(0 - rule2_y4 - rule3_y4 - rule15_y4 - rule23_y4 + rule23_y4 ==  loc1_x5 - loc1_y4)
s.add(0 + rule0_y4 - rule4_y4 - rule6_y4 - rule8_y4 - rule10_y4 - rule12_y4 - rule16_y4 - rule24_y4 + rule24_y4 ==  locS0_x5 - locS0_y4)
s.add(0 + rule2_y4 - rule5_y4 - rule7_y4 - rule9_y4 - rule11_y4 - rule13_y4 - rule17_y4 - rule25_y4 + rule25_y4 ==  locS1_x5 - locS1_y4)
s.add(0 + rule4_y4 + rule5_y4 - rule18_y4 - rule26_y4 + rule26_y4 ==  locD0_x5 - locD0_y4)
s.add(0 + rule6_y4 + rule7_y4 - rule19_y4 - rule27_y4 + rule27_y4 ==  locD1_x5 - locD1_y4)
s.add(0 + rule8_y4 + rule9_y4 + rule12_y4 - rule20_y4 - rule28_y4 + rule28_y4 ==  locU0_x5 - locU0_y4)
s.add(0 + rule10_y4 + rule11_y4 + rule13_y4 - rule21_y4 - rule29_y4 + rule29_y4 ==  locU1_x5 - locU1_y4)
s.add(0 + rule1_y4 + rule3_y4 + rule14_y4 + rule15_y4 + rule16_y4 + rule17_y4 + rule18_y4 + rule19_y4 + rule20_y4 + rule21_y4 ==  locCR_x5 - locCR_y4)






##################Step 3########################


#Flow equations for the shared variables

s.add(0 + rule0_y4 == nsnt0_x5 - nsnt0_y4)
s.add(0 + rule2_y4 == nsnt1_x5 - nsnt1_y4)
s.add(0 + rule0_y4 + rule1_y4 == nsnt0CF_x5 - nsnt0CF_y4)
s.add(0 + rule2_y4 + rule3_y4 == nsnt1CF_x5 - nsnt1CF_y4)
s.add(0 + rule0_y4 + rule2_y4 == nsnt01_x5 - nsnt01_y4)
s.add(0 + rule0_y4 + rule1_y4 + rule2_y4 + rule3_y4 == nsnt01CF_x5 - nsnt01CF_y4)
s.add(0 + rule1_y4 + rule3_y4 + rule14_y4 + rule15_y4 + rule16_y4 + rule17_y4 + rule18_y4 + rule19_y4 + rule20_y4 + rule21_y4 == nfaulty_x5 - nfaulty_y4)






####################Step 4########################


#Rule is fired implies rule is enabled

s.add(Implies( (rule0_y4 > 0), And(True, ) ))
s.add(Implies( (rule1_y4 > 0), And(nfaulty_y4<F, ) ))
s.add(Implies( (rule2_y4 > 0), And(True, ) ))
s.add(Implies( (rule3_y4 > 0), And(nfaulty_y4<F, ) ))
s.add(Implies( (rule4_y4 > 0), And(nsnt0CF_y4>=N-T, ) ))
s.add(Implies( (rule5_y4 > 0), And(nsnt0CF_y4>=N-T, ) ))
s.add(Implies( (rule6_y4 > 0), And(nsnt1CF_y4>=N-T, ) ))
s.add(Implies( (rule7_y4 > 0), And(nsnt1CF_y4>=N-T, ) ))
s.add(Implies( (rule8_y4 > 0), And(nsnt01CF_y4>=N-T, nsnt0CF_y4>=N-2*T, nsnt1CF_y4>=1, ) ))
s.add(Implies( (rule9_y4 > 0), And(nsnt01CF_y4>=N-T, nsnt0CF_y4>=N-2*T, nsnt1CF_y4>=1, ) ))
s.add(Implies( (rule10_y4 > 0), And(nsnt01CF_y4>=N-T, nsnt1CF_y4>=N-2*T, nsnt0CF_y4>=1, ) ))
s.add(Implies( (rule11_y4 > 0), And(nsnt01CF_y4>=N-T, nsnt1CF_y4>=N-2*T, nsnt0CF_y4>=1, ) ))
s.add(Implies( (rule12_y4 > 0), And(nsnt01CF_y4>=N-T, nsnt0_y4<N-2*T, nsnt1_y4<N-2*T, ) ))
s.add(Implies( (rule13_y4 > 0), And(nsnt01CF_y4>=N-T, nsnt0_y4<N-2*T, nsnt1_y4<N-2*T, ) ))
s.add(Implies( (rule14_y4 > 0), And(nfaulty_y4<F, ) ))
s.add(Implies( (rule15_y4 > 0), And(nfaulty_y4<F, ) ))
s.add(Implies( (rule16_y4 > 0), And(nfaulty_y4<F, ) ))
s.add(Implies( (rule17_y4 > 0), And(nfaulty_y4<F, ) ))
s.add(Implies( (rule18_y4 > 0), And(nfaulty_y4<F, ) ))
s.add(Implies( (rule19_y4 > 0), And(nfaulty_y4<F, ) ))
s.add(Implies( (rule20_y4 > 0), And(nfaulty_y4<F, ) ))
s.add(Implies( (rule21_y4 > 0), And(nfaulty_y4<F, ) ))
s.add(Implies( (rule22_y4 > 0), And(True, ) ))
s.add(Implies( (rule23_y4 > 0), And(True, ) ))
s.add(Implies( (rule24_y4 > 0), And(True, ) ))
s.add(Implies( (rule25_y4 > 0), And(True, ) ))
s.add(Implies( (rule26_y4 > 0), And(True, ) ))
s.add(Implies( (rule27_y4 > 0), And(True, ) ))
s.add(Implies( (rule28_y4 > 0), And(True, ) ))
s.add(Implies( (rule29_y4 > 0), And(True, ) ))

##################Step 5########################


#Ensuring that at most one rule is fired alternating configurations y4 and x4, if a fall condition is present

s.add((nsnt1_x5<N-2*T) == (nsnt1_y4<N-2*T))
s.add(Implies(And((nsnt1_x5<N-2*T), Not(nsnt1_y4<N-2*T)), Or((rule0_y4 == 0), (rule0_y4 == 1))))
s.add(Implies(And((nsnt1_x5<N-2*T), Not(nsnt1_y4<N-2*T)), Or((rule1_y4 == 0), (rule1_y4 == 1))))
s.add(Implies(And((nsnt1_x5<N-2*T), Not(nsnt1_y4<N-2*T)), Or((rule2_y4 == 0), (rule2_y4 == 1))))
s.add(Implies(And((nsnt1_x5<N-2*T), Not(nsnt1_y4<N-2*T)), Or((rule3_y4 == 0), (rule3_y4 == 1))))
s.add(Implies(And((nsnt1_x5<N-2*T), Not(nsnt1_y4<N-2*T)), Or((rule4_y4 == 0), (rule4_y4 == 1))))
s.add(Implies(And((nsnt1_x5<N-2*T), Not(nsnt1_y4<N-2*T)), Or((rule5_y4 == 0), (rule5_y4 == 1))))
s.add(Implies(And((nsnt1_x5<N-2*T), Not(nsnt1_y4<N-2*T)), Or((rule6_y4 == 0), (rule6_y4 == 1))))
s.add(Implies(And((nsnt1_x5<N-2*T), Not(nsnt1_y4<N-2*T)), Or((rule7_y4 == 0), (rule7_y4 == 1))))
s.add(Implies(And((nsnt1_x5<N-2*T), Not(nsnt1_y4<N-2*T)), Or((rule8_y4 == 0), (rule8_y4 == 1))))
s.add(Implies(And((nsnt1_x5<N-2*T), Not(nsnt1_y4<N-2*T)), Or((rule9_y4 == 0), (rule9_y4 == 1))))
s.add(Implies(And((nsnt1_x5<N-2*T), Not(nsnt1_y4<N-2*T)), Or((rule10_y4 == 0), (rule10_y4 == 1))))
s.add(Implies(And((nsnt1_x5<N-2*T), Not(nsnt1_y4<N-2*T)), Or((rule11_y4 == 0), (rule11_y4 == 1))))
s.add(Implies(And((nsnt1_x5<N-2*T), Not(nsnt1_y4<N-2*T)), Or((rule12_y4 == 0), (rule12_y4 == 1))))
s.add(Implies(And((nsnt1_x5<N-2*T), Not(nsnt1_y4<N-2*T)), Or((rule13_y4 == 0), (rule13_y4 == 1))))
s.add(Implies(And((nsnt1_x5<N-2*T), Not(nsnt1_y4<N-2*T)), Or((rule14_y4 == 0), (rule14_y4 == 1))))
s.add(Implies(And((nsnt1_x5<N-2*T), Not(nsnt1_y4<N-2*T)), Or((rule15_y4 == 0), (rule15_y4 == 1))))
s.add(Implies(And((nsnt1_x5<N-2*T), Not(nsnt1_y4<N-2*T)), Or((rule16_y4 == 0), (rule16_y4 == 1))))
s.add(Implies(And((nsnt1_x5<N-2*T), Not(nsnt1_y4<N-2*T)), Or((rule17_y4 == 0), (rule17_y4 == 1))))
s.add(Implies(And((nsnt1_x5<N-2*T), Not(nsnt1_y4<N-2*T)), Or((rule18_y4 == 0), (rule18_y4 == 1))))
s.add(Implies(And((nsnt1_x5<N-2*T), Not(nsnt1_y4<N-2*T)), Or((rule19_y4 == 0), (rule19_y4 == 1))))
s.add(Implies(And((nsnt1_x5<N-2*T), Not(nsnt1_y4<N-2*T)), Or((rule20_y4 == 0), (rule20_y4 == 1))))
s.add(Implies(And((nsnt1_x5<N-2*T), Not(nsnt1_y4<N-2*T)), Or((rule21_y4 == 0), (rule21_y4 == 1))))
s.add(Implies(And((nsnt1_x5<N-2*T), Not(nsnt1_y4<N-2*T)), Or((rule22_y4 == 0), (rule22_y4 == 1))))
s.add(Implies(And((nsnt1_x5<N-2*T), Not(nsnt1_y4<N-2*T)), Or((rule23_y4 == 0), (rule23_y4 == 1))))
s.add(Implies(And((nsnt1_x5<N-2*T), Not(nsnt1_y4<N-2*T)), Or((rule24_y4 == 0), (rule24_y4 == 1))))
s.add(Implies(And((nsnt1_x5<N-2*T), Not(nsnt1_y4<N-2*T)), Or((rule25_y4 == 0), (rule25_y4 == 1))))
s.add(Implies(And((nsnt1_x5<N-2*T), Not(nsnt1_y4<N-2*T)), Or((rule26_y4 == 0), (rule26_y4 == 1))))
s.add(Implies(And((nsnt1_x5<N-2*T), Not(nsnt1_y4<N-2*T)), Or((rule27_y4 == 0), (rule27_y4 == 1))))
s.add(Implies(And((nsnt1_x5<N-2*T), Not(nsnt1_y4<N-2*T)), Or((rule28_y4 == 0), (rule28_y4 == 1))))
s.add(Implies(And((nsnt1_x5<N-2*T), Not(nsnt1_y4<N-2*T)), Or((rule29_y4 == 0), (rule29_y4 == 1))))
s.add(Implies(And((nsnt1_x5<N-2*T), Not(nsnt1_y4<N-2*T)), rule0_y4+rule1_y4+rule2_y4+rule3_y4+rule4_y4+rule5_y4+rule6_y4+rule7_y4+rule8_y4+rule9_y4+rule10_y4+rule11_y4+rule12_y4+rule13_y4+rule14_y4+rule15_y4+rule16_y4+rule17_y4+rule18_y4+rule19_y4+rule20_y4+rule21_y4+rule22_y4+rule23_y4+rule24_y4+rule25_y4+rule26_y4+rule27_y4+rule28_y4+rule29_y4 <= 1))

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
s.add(Implies(And((nfaulty_x5<F), Not(nfaulty_y4<F)), Or((rule14_y4 == 0), (rule14_y4 == 1))))
s.add(Implies(And((nfaulty_x5<F), Not(nfaulty_y4<F)), Or((rule15_y4 == 0), (rule15_y4 == 1))))
s.add(Implies(And((nfaulty_x5<F), Not(nfaulty_y4<F)), Or((rule16_y4 == 0), (rule16_y4 == 1))))
s.add(Implies(And((nfaulty_x5<F), Not(nfaulty_y4<F)), Or((rule17_y4 == 0), (rule17_y4 == 1))))
s.add(Implies(And((nfaulty_x5<F), Not(nfaulty_y4<F)), Or((rule18_y4 == 0), (rule18_y4 == 1))))
s.add(Implies(And((nfaulty_x5<F), Not(nfaulty_y4<F)), Or((rule19_y4 == 0), (rule19_y4 == 1))))
s.add(Implies(And((nfaulty_x5<F), Not(nfaulty_y4<F)), Or((rule20_y4 == 0), (rule20_y4 == 1))))
s.add(Implies(And((nfaulty_x5<F), Not(nfaulty_y4<F)), Or((rule21_y4 == 0), (rule21_y4 == 1))))
s.add(Implies(And((nfaulty_x5<F), Not(nfaulty_y4<F)), Or((rule22_y4 == 0), (rule22_y4 == 1))))
s.add(Implies(And((nfaulty_x5<F), Not(nfaulty_y4<F)), Or((rule23_y4 == 0), (rule23_y4 == 1))))
s.add(Implies(And((nfaulty_x5<F), Not(nfaulty_y4<F)), Or((rule24_y4 == 0), (rule24_y4 == 1))))
s.add(Implies(And((nfaulty_x5<F), Not(nfaulty_y4<F)), Or((rule25_y4 == 0), (rule25_y4 == 1))))
s.add(Implies(And((nfaulty_x5<F), Not(nfaulty_y4<F)), Or((rule26_y4 == 0), (rule26_y4 == 1))))
s.add(Implies(And((nfaulty_x5<F), Not(nfaulty_y4<F)), Or((rule27_y4 == 0), (rule27_y4 == 1))))
s.add(Implies(And((nfaulty_x5<F), Not(nfaulty_y4<F)), Or((rule28_y4 == 0), (rule28_y4 == 1))))
s.add(Implies(And((nfaulty_x5<F), Not(nfaulty_y4<F)), Or((rule29_y4 == 0), (rule29_y4 == 1))))
s.add(Implies(And((nfaulty_x5<F), Not(nfaulty_y4<F)), rule0_y4+rule1_y4+rule2_y4+rule3_y4+rule4_y4+rule5_y4+rule6_y4+rule7_y4+rule8_y4+rule9_y4+rule10_y4+rule11_y4+rule12_y4+rule13_y4+rule14_y4+rule15_y4+rule16_y4+rule17_y4+rule18_y4+rule19_y4+rule20_y4+rule21_y4+rule22_y4+rule23_y4+rule24_y4+rule25_y4+rule26_y4+rule27_y4+rule28_y4+rule29_y4 <= 1))

s.add((nsnt0_x5<N-2*T) == (nsnt0_y4<N-2*T))
s.add(Implies(And((nsnt0_x5<N-2*T), Not(nsnt0_y4<N-2*T)), Or((rule0_y4 == 0), (rule0_y4 == 1))))
s.add(Implies(And((nsnt0_x5<N-2*T), Not(nsnt0_y4<N-2*T)), Or((rule1_y4 == 0), (rule1_y4 == 1))))
s.add(Implies(And((nsnt0_x5<N-2*T), Not(nsnt0_y4<N-2*T)), Or((rule2_y4 == 0), (rule2_y4 == 1))))
s.add(Implies(And((nsnt0_x5<N-2*T), Not(nsnt0_y4<N-2*T)), Or((rule3_y4 == 0), (rule3_y4 == 1))))
s.add(Implies(And((nsnt0_x5<N-2*T), Not(nsnt0_y4<N-2*T)), Or((rule4_y4 == 0), (rule4_y4 == 1))))
s.add(Implies(And((nsnt0_x5<N-2*T), Not(nsnt0_y4<N-2*T)), Or((rule5_y4 == 0), (rule5_y4 == 1))))
s.add(Implies(And((nsnt0_x5<N-2*T), Not(nsnt0_y4<N-2*T)), Or((rule6_y4 == 0), (rule6_y4 == 1))))
s.add(Implies(And((nsnt0_x5<N-2*T), Not(nsnt0_y4<N-2*T)), Or((rule7_y4 == 0), (rule7_y4 == 1))))
s.add(Implies(And((nsnt0_x5<N-2*T), Not(nsnt0_y4<N-2*T)), Or((rule8_y4 == 0), (rule8_y4 == 1))))
s.add(Implies(And((nsnt0_x5<N-2*T), Not(nsnt0_y4<N-2*T)), Or((rule9_y4 == 0), (rule9_y4 == 1))))
s.add(Implies(And((nsnt0_x5<N-2*T), Not(nsnt0_y4<N-2*T)), Or((rule10_y4 == 0), (rule10_y4 == 1))))
s.add(Implies(And((nsnt0_x5<N-2*T), Not(nsnt0_y4<N-2*T)), Or((rule11_y4 == 0), (rule11_y4 == 1))))
s.add(Implies(And((nsnt0_x5<N-2*T), Not(nsnt0_y4<N-2*T)), Or((rule12_y4 == 0), (rule12_y4 == 1))))
s.add(Implies(And((nsnt0_x5<N-2*T), Not(nsnt0_y4<N-2*T)), Or((rule13_y4 == 0), (rule13_y4 == 1))))
s.add(Implies(And((nsnt0_x5<N-2*T), Not(nsnt0_y4<N-2*T)), Or((rule14_y4 == 0), (rule14_y4 == 1))))
s.add(Implies(And((nsnt0_x5<N-2*T), Not(nsnt0_y4<N-2*T)), Or((rule15_y4 == 0), (rule15_y4 == 1))))
s.add(Implies(And((nsnt0_x5<N-2*T), Not(nsnt0_y4<N-2*T)), Or((rule16_y4 == 0), (rule16_y4 == 1))))
s.add(Implies(And((nsnt0_x5<N-2*T), Not(nsnt0_y4<N-2*T)), Or((rule17_y4 == 0), (rule17_y4 == 1))))
s.add(Implies(And((nsnt0_x5<N-2*T), Not(nsnt0_y4<N-2*T)), Or((rule18_y4 == 0), (rule18_y4 == 1))))
s.add(Implies(And((nsnt0_x5<N-2*T), Not(nsnt0_y4<N-2*T)), Or((rule19_y4 == 0), (rule19_y4 == 1))))
s.add(Implies(And((nsnt0_x5<N-2*T), Not(nsnt0_y4<N-2*T)), Or((rule20_y4 == 0), (rule20_y4 == 1))))
s.add(Implies(And((nsnt0_x5<N-2*T), Not(nsnt0_y4<N-2*T)), Or((rule21_y4 == 0), (rule21_y4 == 1))))
s.add(Implies(And((nsnt0_x5<N-2*T), Not(nsnt0_y4<N-2*T)), Or((rule22_y4 == 0), (rule22_y4 == 1))))
s.add(Implies(And((nsnt0_x5<N-2*T), Not(nsnt0_y4<N-2*T)), Or((rule23_y4 == 0), (rule23_y4 == 1))))
s.add(Implies(And((nsnt0_x5<N-2*T), Not(nsnt0_y4<N-2*T)), Or((rule24_y4 == 0), (rule24_y4 == 1))))
s.add(Implies(And((nsnt0_x5<N-2*T), Not(nsnt0_y4<N-2*T)), Or((rule25_y4 == 0), (rule25_y4 == 1))))
s.add(Implies(And((nsnt0_x5<N-2*T), Not(nsnt0_y4<N-2*T)), Or((rule26_y4 == 0), (rule26_y4 == 1))))
s.add(Implies(And((nsnt0_x5<N-2*T), Not(nsnt0_y4<N-2*T)), Or((rule27_y4 == 0), (rule27_y4 == 1))))
s.add(Implies(And((nsnt0_x5<N-2*T), Not(nsnt0_y4<N-2*T)), Or((rule28_y4 == 0), (rule28_y4 == 1))))
s.add(Implies(And((nsnt0_x5<N-2*T), Not(nsnt0_y4<N-2*T)), Or((rule29_y4 == 0), (rule29_y4 == 1))))
s.add(Implies(And((nsnt0_x5<N-2*T), Not(nsnt0_y4<N-2*T)), rule0_y4+rule1_y4+rule2_y4+rule3_y4+rule4_y4+rule5_y4+rule6_y4+rule7_y4+rule8_y4+rule9_y4+rule10_y4+rule11_y4+rule12_y4+rule13_y4+rule14_y4+rule15_y4+rule16_y4+rule17_y4+rule18_y4+rule19_y4+rule20_y4+rule21_y4+rule22_y4+rule23_y4+rule24_y4+rule25_y4+rule26_y4+rule27_y4+rule28_y4+rule29_y4 <= 1))


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
rule14_y5 = Real('rule14_y5')
s.add(rule14_y5 >= 0)
rule15_y5 = Real('rule15_y5')
s.add(rule15_y5 >= 0)
rule16_y5 = Real('rule16_y5')
s.add(rule16_y5 >= 0)
rule17_y5 = Real('rule17_y5')
s.add(rule17_y5 >= 0)
rule18_y5 = Real('rule18_y5')
s.add(rule18_y5 >= 0)
rule19_y5 = Real('rule19_y5')
s.add(rule19_y5 >= 0)
rule20_y5 = Real('rule20_y5')
s.add(rule20_y5 >= 0)
rule21_y5 = Real('rule21_y5')
s.add(rule21_y5 >= 0)
rule22_y5 = Real('rule22_y5')
s.add(rule22_y5 >= 0)
rule23_y5 = Real('rule23_y5')
s.add(rule23_y5 >= 0)
rule24_y5 = Real('rule24_y5')
s.add(rule24_y5 >= 0)
rule25_y5 = Real('rule25_y5')
s.add(rule25_y5 >= 0)
rule26_y5 = Real('rule26_y5')
s.add(rule26_y5 >= 0)
rule27_y5 = Real('rule27_y5')
s.add(rule27_y5 >= 0)
rule28_y5 = Real('rule28_y5')
s.add(rule28_y5 >= 0)
rule29_y5 = Real('rule29_y5')
s.add(rule29_y5 >= 0)






###################Step 2####################


#Flow equations for the locations

s.add(0 - rule0_y5 - rule1_y5 - rule14_y5 - rule22_y5 + rule22_y5 ==  loc0_x6 - loc0_y5)
s.add(0 - rule2_y5 - rule3_y5 - rule15_y5 - rule23_y5 + rule23_y5 ==  loc1_x6 - loc1_y5)
s.add(0 + rule0_y5 - rule4_y5 - rule6_y5 - rule8_y5 - rule10_y5 - rule12_y5 - rule16_y5 - rule24_y5 + rule24_y5 ==  locS0_x6 - locS0_y5)
s.add(0 + rule2_y5 - rule5_y5 - rule7_y5 - rule9_y5 - rule11_y5 - rule13_y5 - rule17_y5 - rule25_y5 + rule25_y5 ==  locS1_x6 - locS1_y5)
s.add(0 + rule4_y5 + rule5_y5 - rule18_y5 - rule26_y5 + rule26_y5 ==  locD0_x6 - locD0_y5)
s.add(0 + rule6_y5 + rule7_y5 - rule19_y5 - rule27_y5 + rule27_y5 ==  locD1_x6 - locD1_y5)
s.add(0 + rule8_y5 + rule9_y5 + rule12_y5 - rule20_y5 - rule28_y5 + rule28_y5 ==  locU0_x6 - locU0_y5)
s.add(0 + rule10_y5 + rule11_y5 + rule13_y5 - rule21_y5 - rule29_y5 + rule29_y5 ==  locU1_x6 - locU1_y5)
s.add(0 + rule1_y5 + rule3_y5 + rule14_y5 + rule15_y5 + rule16_y5 + rule17_y5 + rule18_y5 + rule19_y5 + rule20_y5 + rule21_y5 ==  locCR_x6 - locCR_y5)






##################Step 3########################


#Flow equations for the shared variables

s.add(0 + rule0_y5 == nsnt0_x6 - nsnt0_y5)
s.add(0 + rule2_y5 == nsnt1_x6 - nsnt1_y5)
s.add(0 + rule0_y5 + rule1_y5 == nsnt0CF_x6 - nsnt0CF_y5)
s.add(0 + rule2_y5 + rule3_y5 == nsnt1CF_x6 - nsnt1CF_y5)
s.add(0 + rule0_y5 + rule2_y5 == nsnt01_x6 - nsnt01_y5)
s.add(0 + rule0_y5 + rule1_y5 + rule2_y5 + rule3_y5 == nsnt01CF_x6 - nsnt01CF_y5)
s.add(0 + rule1_y5 + rule3_y5 + rule14_y5 + rule15_y5 + rule16_y5 + rule17_y5 + rule18_y5 + rule19_y5 + rule20_y5 + rule21_y5 == nfaulty_x6 - nfaulty_y5)






####################Step 4########################


#Rule is fired implies rule is enabled

s.add(Implies( (rule0_y5 > 0), And(True, ) ))
s.add(Implies( (rule1_y5 > 0), And(nfaulty_y5<F, ) ))
s.add(Implies( (rule2_y5 > 0), And(True, ) ))
s.add(Implies( (rule3_y5 > 0), And(nfaulty_y5<F, ) ))
s.add(Implies( (rule4_y5 > 0), And(nsnt0CF_y5>=N-T, ) ))
s.add(Implies( (rule5_y5 > 0), And(nsnt0CF_y5>=N-T, ) ))
s.add(Implies( (rule6_y5 > 0), And(nsnt1CF_y5>=N-T, ) ))
s.add(Implies( (rule7_y5 > 0), And(nsnt1CF_y5>=N-T, ) ))
s.add(Implies( (rule8_y5 > 0), And(nsnt01CF_y5>=N-T, nsnt0CF_y5>=N-2*T, nsnt1CF_y5>=1, ) ))
s.add(Implies( (rule9_y5 > 0), And(nsnt01CF_y5>=N-T, nsnt0CF_y5>=N-2*T, nsnt1CF_y5>=1, ) ))
s.add(Implies( (rule10_y5 > 0), And(nsnt01CF_y5>=N-T, nsnt1CF_y5>=N-2*T, nsnt0CF_y5>=1, ) ))
s.add(Implies( (rule11_y5 > 0), And(nsnt01CF_y5>=N-T, nsnt1CF_y5>=N-2*T, nsnt0CF_y5>=1, ) ))
s.add(Implies( (rule12_y5 > 0), And(nsnt01CF_y5>=N-T, nsnt0_y5<N-2*T, nsnt1_y5<N-2*T, ) ))
s.add(Implies( (rule13_y5 > 0), And(nsnt01CF_y5>=N-T, nsnt0_y5<N-2*T, nsnt1_y5<N-2*T, ) ))
s.add(Implies( (rule14_y5 > 0), And(nfaulty_y5<F, ) ))
s.add(Implies( (rule15_y5 > 0), And(nfaulty_y5<F, ) ))
s.add(Implies( (rule16_y5 > 0), And(nfaulty_y5<F, ) ))
s.add(Implies( (rule17_y5 > 0), And(nfaulty_y5<F, ) ))
s.add(Implies( (rule18_y5 > 0), And(nfaulty_y5<F, ) ))
s.add(Implies( (rule19_y5 > 0), And(nfaulty_y5<F, ) ))
s.add(Implies( (rule20_y5 > 0), And(nfaulty_y5<F, ) ))
s.add(Implies( (rule21_y5 > 0), And(nfaulty_y5<F, ) ))
s.add(Implies( (rule22_y5 > 0), And(True, ) ))
s.add(Implies( (rule23_y5 > 0), And(True, ) ))
s.add(Implies( (rule24_y5 > 0), And(True, ) ))
s.add(Implies( (rule25_y5 > 0), And(True, ) ))
s.add(Implies( (rule26_y5 > 0), And(True, ) ))
s.add(Implies( (rule27_y5 > 0), And(True, ) ))
s.add(Implies( (rule28_y5 > 0), And(True, ) ))
s.add(Implies( (rule29_y5 > 0), And(True, ) ))

##################Step 5########################


#Ensuring that at most one rule is fired alternating configurations y5 and x5, if a fall condition is present

s.add((nsnt1_x6<N-2*T) == (nsnt1_y5<N-2*T))
s.add(Implies(And((nsnt1_x6<N-2*T), Not(nsnt1_y5<N-2*T)), Or((rule0_y5 == 0), (rule0_y5 == 1))))
s.add(Implies(And((nsnt1_x6<N-2*T), Not(nsnt1_y5<N-2*T)), Or((rule1_y5 == 0), (rule1_y5 == 1))))
s.add(Implies(And((nsnt1_x6<N-2*T), Not(nsnt1_y5<N-2*T)), Or((rule2_y5 == 0), (rule2_y5 == 1))))
s.add(Implies(And((nsnt1_x6<N-2*T), Not(nsnt1_y5<N-2*T)), Or((rule3_y5 == 0), (rule3_y5 == 1))))
s.add(Implies(And((nsnt1_x6<N-2*T), Not(nsnt1_y5<N-2*T)), Or((rule4_y5 == 0), (rule4_y5 == 1))))
s.add(Implies(And((nsnt1_x6<N-2*T), Not(nsnt1_y5<N-2*T)), Or((rule5_y5 == 0), (rule5_y5 == 1))))
s.add(Implies(And((nsnt1_x6<N-2*T), Not(nsnt1_y5<N-2*T)), Or((rule6_y5 == 0), (rule6_y5 == 1))))
s.add(Implies(And((nsnt1_x6<N-2*T), Not(nsnt1_y5<N-2*T)), Or((rule7_y5 == 0), (rule7_y5 == 1))))
s.add(Implies(And((nsnt1_x6<N-2*T), Not(nsnt1_y5<N-2*T)), Or((rule8_y5 == 0), (rule8_y5 == 1))))
s.add(Implies(And((nsnt1_x6<N-2*T), Not(nsnt1_y5<N-2*T)), Or((rule9_y5 == 0), (rule9_y5 == 1))))
s.add(Implies(And((nsnt1_x6<N-2*T), Not(nsnt1_y5<N-2*T)), Or((rule10_y5 == 0), (rule10_y5 == 1))))
s.add(Implies(And((nsnt1_x6<N-2*T), Not(nsnt1_y5<N-2*T)), Or((rule11_y5 == 0), (rule11_y5 == 1))))
s.add(Implies(And((nsnt1_x6<N-2*T), Not(nsnt1_y5<N-2*T)), Or((rule12_y5 == 0), (rule12_y5 == 1))))
s.add(Implies(And((nsnt1_x6<N-2*T), Not(nsnt1_y5<N-2*T)), Or((rule13_y5 == 0), (rule13_y5 == 1))))
s.add(Implies(And((nsnt1_x6<N-2*T), Not(nsnt1_y5<N-2*T)), Or((rule14_y5 == 0), (rule14_y5 == 1))))
s.add(Implies(And((nsnt1_x6<N-2*T), Not(nsnt1_y5<N-2*T)), Or((rule15_y5 == 0), (rule15_y5 == 1))))
s.add(Implies(And((nsnt1_x6<N-2*T), Not(nsnt1_y5<N-2*T)), Or((rule16_y5 == 0), (rule16_y5 == 1))))
s.add(Implies(And((nsnt1_x6<N-2*T), Not(nsnt1_y5<N-2*T)), Or((rule17_y5 == 0), (rule17_y5 == 1))))
s.add(Implies(And((nsnt1_x6<N-2*T), Not(nsnt1_y5<N-2*T)), Or((rule18_y5 == 0), (rule18_y5 == 1))))
s.add(Implies(And((nsnt1_x6<N-2*T), Not(nsnt1_y5<N-2*T)), Or((rule19_y5 == 0), (rule19_y5 == 1))))
s.add(Implies(And((nsnt1_x6<N-2*T), Not(nsnt1_y5<N-2*T)), Or((rule20_y5 == 0), (rule20_y5 == 1))))
s.add(Implies(And((nsnt1_x6<N-2*T), Not(nsnt1_y5<N-2*T)), Or((rule21_y5 == 0), (rule21_y5 == 1))))
s.add(Implies(And((nsnt1_x6<N-2*T), Not(nsnt1_y5<N-2*T)), Or((rule22_y5 == 0), (rule22_y5 == 1))))
s.add(Implies(And((nsnt1_x6<N-2*T), Not(nsnt1_y5<N-2*T)), Or((rule23_y5 == 0), (rule23_y5 == 1))))
s.add(Implies(And((nsnt1_x6<N-2*T), Not(nsnt1_y5<N-2*T)), Or((rule24_y5 == 0), (rule24_y5 == 1))))
s.add(Implies(And((nsnt1_x6<N-2*T), Not(nsnt1_y5<N-2*T)), Or((rule25_y5 == 0), (rule25_y5 == 1))))
s.add(Implies(And((nsnt1_x6<N-2*T), Not(nsnt1_y5<N-2*T)), Or((rule26_y5 == 0), (rule26_y5 == 1))))
s.add(Implies(And((nsnt1_x6<N-2*T), Not(nsnt1_y5<N-2*T)), Or((rule27_y5 == 0), (rule27_y5 == 1))))
s.add(Implies(And((nsnt1_x6<N-2*T), Not(nsnt1_y5<N-2*T)), Or((rule28_y5 == 0), (rule28_y5 == 1))))
s.add(Implies(And((nsnt1_x6<N-2*T), Not(nsnt1_y5<N-2*T)), Or((rule29_y5 == 0), (rule29_y5 == 1))))
s.add(Implies(And((nsnt1_x6<N-2*T), Not(nsnt1_y5<N-2*T)), rule0_y5+rule1_y5+rule2_y5+rule3_y5+rule4_y5+rule5_y5+rule6_y5+rule7_y5+rule8_y5+rule9_y5+rule10_y5+rule11_y5+rule12_y5+rule13_y5+rule14_y5+rule15_y5+rule16_y5+rule17_y5+rule18_y5+rule19_y5+rule20_y5+rule21_y5+rule22_y5+rule23_y5+rule24_y5+rule25_y5+rule26_y5+rule27_y5+rule28_y5+rule29_y5 <= 1))

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
s.add(Implies(And((nfaulty_x6<F), Not(nfaulty_y5<F)), Or((rule14_y5 == 0), (rule14_y5 == 1))))
s.add(Implies(And((nfaulty_x6<F), Not(nfaulty_y5<F)), Or((rule15_y5 == 0), (rule15_y5 == 1))))
s.add(Implies(And((nfaulty_x6<F), Not(nfaulty_y5<F)), Or((rule16_y5 == 0), (rule16_y5 == 1))))
s.add(Implies(And((nfaulty_x6<F), Not(nfaulty_y5<F)), Or((rule17_y5 == 0), (rule17_y5 == 1))))
s.add(Implies(And((nfaulty_x6<F), Not(nfaulty_y5<F)), Or((rule18_y5 == 0), (rule18_y5 == 1))))
s.add(Implies(And((nfaulty_x6<F), Not(nfaulty_y5<F)), Or((rule19_y5 == 0), (rule19_y5 == 1))))
s.add(Implies(And((nfaulty_x6<F), Not(nfaulty_y5<F)), Or((rule20_y5 == 0), (rule20_y5 == 1))))
s.add(Implies(And((nfaulty_x6<F), Not(nfaulty_y5<F)), Or((rule21_y5 == 0), (rule21_y5 == 1))))
s.add(Implies(And((nfaulty_x6<F), Not(nfaulty_y5<F)), Or((rule22_y5 == 0), (rule22_y5 == 1))))
s.add(Implies(And((nfaulty_x6<F), Not(nfaulty_y5<F)), Or((rule23_y5 == 0), (rule23_y5 == 1))))
s.add(Implies(And((nfaulty_x6<F), Not(nfaulty_y5<F)), Or((rule24_y5 == 0), (rule24_y5 == 1))))
s.add(Implies(And((nfaulty_x6<F), Not(nfaulty_y5<F)), Or((rule25_y5 == 0), (rule25_y5 == 1))))
s.add(Implies(And((nfaulty_x6<F), Not(nfaulty_y5<F)), Or((rule26_y5 == 0), (rule26_y5 == 1))))
s.add(Implies(And((nfaulty_x6<F), Not(nfaulty_y5<F)), Or((rule27_y5 == 0), (rule27_y5 == 1))))
s.add(Implies(And((nfaulty_x6<F), Not(nfaulty_y5<F)), Or((rule28_y5 == 0), (rule28_y5 == 1))))
s.add(Implies(And((nfaulty_x6<F), Not(nfaulty_y5<F)), Or((rule29_y5 == 0), (rule29_y5 == 1))))
s.add(Implies(And((nfaulty_x6<F), Not(nfaulty_y5<F)), rule0_y5+rule1_y5+rule2_y5+rule3_y5+rule4_y5+rule5_y5+rule6_y5+rule7_y5+rule8_y5+rule9_y5+rule10_y5+rule11_y5+rule12_y5+rule13_y5+rule14_y5+rule15_y5+rule16_y5+rule17_y5+rule18_y5+rule19_y5+rule20_y5+rule21_y5+rule22_y5+rule23_y5+rule24_y5+rule25_y5+rule26_y5+rule27_y5+rule28_y5+rule29_y5 <= 1))

s.add((nsnt0_x6<N-2*T) == (nsnt0_y5<N-2*T))
s.add(Implies(And((nsnt0_x6<N-2*T), Not(nsnt0_y5<N-2*T)), Or((rule0_y5 == 0), (rule0_y5 == 1))))
s.add(Implies(And((nsnt0_x6<N-2*T), Not(nsnt0_y5<N-2*T)), Or((rule1_y5 == 0), (rule1_y5 == 1))))
s.add(Implies(And((nsnt0_x6<N-2*T), Not(nsnt0_y5<N-2*T)), Or((rule2_y5 == 0), (rule2_y5 == 1))))
s.add(Implies(And((nsnt0_x6<N-2*T), Not(nsnt0_y5<N-2*T)), Or((rule3_y5 == 0), (rule3_y5 == 1))))
s.add(Implies(And((nsnt0_x6<N-2*T), Not(nsnt0_y5<N-2*T)), Or((rule4_y5 == 0), (rule4_y5 == 1))))
s.add(Implies(And((nsnt0_x6<N-2*T), Not(nsnt0_y5<N-2*T)), Or((rule5_y5 == 0), (rule5_y5 == 1))))
s.add(Implies(And((nsnt0_x6<N-2*T), Not(nsnt0_y5<N-2*T)), Or((rule6_y5 == 0), (rule6_y5 == 1))))
s.add(Implies(And((nsnt0_x6<N-2*T), Not(nsnt0_y5<N-2*T)), Or((rule7_y5 == 0), (rule7_y5 == 1))))
s.add(Implies(And((nsnt0_x6<N-2*T), Not(nsnt0_y5<N-2*T)), Or((rule8_y5 == 0), (rule8_y5 == 1))))
s.add(Implies(And((nsnt0_x6<N-2*T), Not(nsnt0_y5<N-2*T)), Or((rule9_y5 == 0), (rule9_y5 == 1))))
s.add(Implies(And((nsnt0_x6<N-2*T), Not(nsnt0_y5<N-2*T)), Or((rule10_y5 == 0), (rule10_y5 == 1))))
s.add(Implies(And((nsnt0_x6<N-2*T), Not(nsnt0_y5<N-2*T)), Or((rule11_y5 == 0), (rule11_y5 == 1))))
s.add(Implies(And((nsnt0_x6<N-2*T), Not(nsnt0_y5<N-2*T)), Or((rule12_y5 == 0), (rule12_y5 == 1))))
s.add(Implies(And((nsnt0_x6<N-2*T), Not(nsnt0_y5<N-2*T)), Or((rule13_y5 == 0), (rule13_y5 == 1))))
s.add(Implies(And((nsnt0_x6<N-2*T), Not(nsnt0_y5<N-2*T)), Or((rule14_y5 == 0), (rule14_y5 == 1))))
s.add(Implies(And((nsnt0_x6<N-2*T), Not(nsnt0_y5<N-2*T)), Or((rule15_y5 == 0), (rule15_y5 == 1))))
s.add(Implies(And((nsnt0_x6<N-2*T), Not(nsnt0_y5<N-2*T)), Or((rule16_y5 == 0), (rule16_y5 == 1))))
s.add(Implies(And((nsnt0_x6<N-2*T), Not(nsnt0_y5<N-2*T)), Or((rule17_y5 == 0), (rule17_y5 == 1))))
s.add(Implies(And((nsnt0_x6<N-2*T), Not(nsnt0_y5<N-2*T)), Or((rule18_y5 == 0), (rule18_y5 == 1))))
s.add(Implies(And((nsnt0_x6<N-2*T), Not(nsnt0_y5<N-2*T)), Or((rule19_y5 == 0), (rule19_y5 == 1))))
s.add(Implies(And((nsnt0_x6<N-2*T), Not(nsnt0_y5<N-2*T)), Or((rule20_y5 == 0), (rule20_y5 == 1))))
s.add(Implies(And((nsnt0_x6<N-2*T), Not(nsnt0_y5<N-2*T)), Or((rule21_y5 == 0), (rule21_y5 == 1))))
s.add(Implies(And((nsnt0_x6<N-2*T), Not(nsnt0_y5<N-2*T)), Or((rule22_y5 == 0), (rule22_y5 == 1))))
s.add(Implies(And((nsnt0_x6<N-2*T), Not(nsnt0_y5<N-2*T)), Or((rule23_y5 == 0), (rule23_y5 == 1))))
s.add(Implies(And((nsnt0_x6<N-2*T), Not(nsnt0_y5<N-2*T)), Or((rule24_y5 == 0), (rule24_y5 == 1))))
s.add(Implies(And((nsnt0_x6<N-2*T), Not(nsnt0_y5<N-2*T)), Or((rule25_y5 == 0), (rule25_y5 == 1))))
s.add(Implies(And((nsnt0_x6<N-2*T), Not(nsnt0_y5<N-2*T)), Or((rule26_y5 == 0), (rule26_y5 == 1))))
s.add(Implies(And((nsnt0_x6<N-2*T), Not(nsnt0_y5<N-2*T)), Or((rule27_y5 == 0), (rule27_y5 == 1))))
s.add(Implies(And((nsnt0_x6<N-2*T), Not(nsnt0_y5<N-2*T)), Or((rule28_y5 == 0), (rule28_y5 == 1))))
s.add(Implies(And((nsnt0_x6<N-2*T), Not(nsnt0_y5<N-2*T)), Or((rule29_y5 == 0), (rule29_y5 == 1))))
s.add(Implies(And((nsnt0_x6<N-2*T), Not(nsnt0_y5<N-2*T)), rule0_y5+rule1_y5+rule2_y5+rule3_y5+rule4_y5+rule5_y5+rule6_y5+rule7_y5+rule8_y5+rule9_y5+rule10_y5+rule11_y5+rule12_y5+rule13_y5+rule14_y5+rule15_y5+rule16_y5+rule17_y5+rule18_y5+rule19_y5+rule20_y5+rule21_y5+rule22_y5+rule23_y5+rule24_y5+rule25_y5+rule26_y5+rule27_y5+rule28_y5+rule29_y5 <= 1))


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
rule14_y6 = Real('rule14_y6')
s.add(rule14_y6 >= 0)
rule15_y6 = Real('rule15_y6')
s.add(rule15_y6 >= 0)
rule16_y6 = Real('rule16_y6')
s.add(rule16_y6 >= 0)
rule17_y6 = Real('rule17_y6')
s.add(rule17_y6 >= 0)
rule18_y6 = Real('rule18_y6')
s.add(rule18_y6 >= 0)
rule19_y6 = Real('rule19_y6')
s.add(rule19_y6 >= 0)
rule20_y6 = Real('rule20_y6')
s.add(rule20_y6 >= 0)
rule21_y6 = Real('rule21_y6')
s.add(rule21_y6 >= 0)
rule22_y6 = Real('rule22_y6')
s.add(rule22_y6 >= 0)
rule23_y6 = Real('rule23_y6')
s.add(rule23_y6 >= 0)
rule24_y6 = Real('rule24_y6')
s.add(rule24_y6 >= 0)
rule25_y6 = Real('rule25_y6')
s.add(rule25_y6 >= 0)
rule26_y6 = Real('rule26_y6')
s.add(rule26_y6 >= 0)
rule27_y6 = Real('rule27_y6')
s.add(rule27_y6 >= 0)
rule28_y6 = Real('rule28_y6')
s.add(rule28_y6 >= 0)
rule29_y6 = Real('rule29_y6')
s.add(rule29_y6 >= 0)






###################Step 2####################


#Flow equations for the locations

s.add(0 - rule0_y6 - rule1_y6 - rule14_y6 - rule22_y6 + rule22_y6 ==  loc0_x7 - loc0_y6)
s.add(0 - rule2_y6 - rule3_y6 - rule15_y6 - rule23_y6 + rule23_y6 ==  loc1_x7 - loc1_y6)
s.add(0 + rule0_y6 - rule4_y6 - rule6_y6 - rule8_y6 - rule10_y6 - rule12_y6 - rule16_y6 - rule24_y6 + rule24_y6 ==  locS0_x7 - locS0_y6)
s.add(0 + rule2_y6 - rule5_y6 - rule7_y6 - rule9_y6 - rule11_y6 - rule13_y6 - rule17_y6 - rule25_y6 + rule25_y6 ==  locS1_x7 - locS1_y6)
s.add(0 + rule4_y6 + rule5_y6 - rule18_y6 - rule26_y6 + rule26_y6 ==  locD0_x7 - locD0_y6)
s.add(0 + rule6_y6 + rule7_y6 - rule19_y6 - rule27_y6 + rule27_y6 ==  locD1_x7 - locD1_y6)
s.add(0 + rule8_y6 + rule9_y6 + rule12_y6 - rule20_y6 - rule28_y6 + rule28_y6 ==  locU0_x7 - locU0_y6)
s.add(0 + rule10_y6 + rule11_y6 + rule13_y6 - rule21_y6 - rule29_y6 + rule29_y6 ==  locU1_x7 - locU1_y6)
s.add(0 + rule1_y6 + rule3_y6 + rule14_y6 + rule15_y6 + rule16_y6 + rule17_y6 + rule18_y6 + rule19_y6 + rule20_y6 + rule21_y6 ==  locCR_x7 - locCR_y6)






##################Step 3########################


#Flow equations for the shared variables

s.add(0 + rule0_y6 == nsnt0_x7 - nsnt0_y6)
s.add(0 + rule2_y6 == nsnt1_x7 - nsnt1_y6)
s.add(0 + rule0_y6 + rule1_y6 == nsnt0CF_x7 - nsnt0CF_y6)
s.add(0 + rule2_y6 + rule3_y6 == nsnt1CF_x7 - nsnt1CF_y6)
s.add(0 + rule0_y6 + rule2_y6 == nsnt01_x7 - nsnt01_y6)
s.add(0 + rule0_y6 + rule1_y6 + rule2_y6 + rule3_y6 == nsnt01CF_x7 - nsnt01CF_y6)
s.add(0 + rule1_y6 + rule3_y6 + rule14_y6 + rule15_y6 + rule16_y6 + rule17_y6 + rule18_y6 + rule19_y6 + rule20_y6 + rule21_y6 == nfaulty_x7 - nfaulty_y6)






####################Step 4########################


#Rule is fired implies rule is enabled

s.add(Implies( (rule0_y6 > 0), And(True, ) ))
s.add(Implies( (rule1_y6 > 0), And(nfaulty_y6<F, ) ))
s.add(Implies( (rule2_y6 > 0), And(True, ) ))
s.add(Implies( (rule3_y6 > 0), And(nfaulty_y6<F, ) ))
s.add(Implies( (rule4_y6 > 0), And(nsnt0CF_y6>=N-T, ) ))
s.add(Implies( (rule5_y6 > 0), And(nsnt0CF_y6>=N-T, ) ))
s.add(Implies( (rule6_y6 > 0), And(nsnt1CF_y6>=N-T, ) ))
s.add(Implies( (rule7_y6 > 0), And(nsnt1CF_y6>=N-T, ) ))
s.add(Implies( (rule8_y6 > 0), And(nsnt01CF_y6>=N-T, nsnt0CF_y6>=N-2*T, nsnt1CF_y6>=1, ) ))
s.add(Implies( (rule9_y6 > 0), And(nsnt01CF_y6>=N-T, nsnt0CF_y6>=N-2*T, nsnt1CF_y6>=1, ) ))
s.add(Implies( (rule10_y6 > 0), And(nsnt01CF_y6>=N-T, nsnt1CF_y6>=N-2*T, nsnt0CF_y6>=1, ) ))
s.add(Implies( (rule11_y6 > 0), And(nsnt01CF_y6>=N-T, nsnt1CF_y6>=N-2*T, nsnt0CF_y6>=1, ) ))
s.add(Implies( (rule12_y6 > 0), And(nsnt01CF_y6>=N-T, nsnt0_y6<N-2*T, nsnt1_y6<N-2*T, ) ))
s.add(Implies( (rule13_y6 > 0), And(nsnt01CF_y6>=N-T, nsnt0_y6<N-2*T, nsnt1_y6<N-2*T, ) ))
s.add(Implies( (rule14_y6 > 0), And(nfaulty_y6<F, ) ))
s.add(Implies( (rule15_y6 > 0), And(nfaulty_y6<F, ) ))
s.add(Implies( (rule16_y6 > 0), And(nfaulty_y6<F, ) ))
s.add(Implies( (rule17_y6 > 0), And(nfaulty_y6<F, ) ))
s.add(Implies( (rule18_y6 > 0), And(nfaulty_y6<F, ) ))
s.add(Implies( (rule19_y6 > 0), And(nfaulty_y6<F, ) ))
s.add(Implies( (rule20_y6 > 0), And(nfaulty_y6<F, ) ))
s.add(Implies( (rule21_y6 > 0), And(nfaulty_y6<F, ) ))
s.add(Implies( (rule22_y6 > 0), And(True, ) ))
s.add(Implies( (rule23_y6 > 0), And(True, ) ))
s.add(Implies( (rule24_y6 > 0), And(True, ) ))
s.add(Implies( (rule25_y6 > 0), And(True, ) ))
s.add(Implies( (rule26_y6 > 0), And(True, ) ))
s.add(Implies( (rule27_y6 > 0), And(True, ) ))
s.add(Implies( (rule28_y6 > 0), And(True, ) ))
s.add(Implies( (rule29_y6 > 0), And(True, ) ))

##################Step 5########################


#Ensuring that at most one rule is fired alternating configurations y6 and x6, if a fall condition is present

s.add((nsnt1_x7<N-2*T) == (nsnt1_y6<N-2*T))
s.add(Implies(And((nsnt1_x7<N-2*T), Not(nsnt1_y6<N-2*T)), Or((rule0_y6 == 0), (rule0_y6 == 1))))
s.add(Implies(And((nsnt1_x7<N-2*T), Not(nsnt1_y6<N-2*T)), Or((rule1_y6 == 0), (rule1_y6 == 1))))
s.add(Implies(And((nsnt1_x7<N-2*T), Not(nsnt1_y6<N-2*T)), Or((rule2_y6 == 0), (rule2_y6 == 1))))
s.add(Implies(And((nsnt1_x7<N-2*T), Not(nsnt1_y6<N-2*T)), Or((rule3_y6 == 0), (rule3_y6 == 1))))
s.add(Implies(And((nsnt1_x7<N-2*T), Not(nsnt1_y6<N-2*T)), Or((rule4_y6 == 0), (rule4_y6 == 1))))
s.add(Implies(And((nsnt1_x7<N-2*T), Not(nsnt1_y6<N-2*T)), Or((rule5_y6 == 0), (rule5_y6 == 1))))
s.add(Implies(And((nsnt1_x7<N-2*T), Not(nsnt1_y6<N-2*T)), Or((rule6_y6 == 0), (rule6_y6 == 1))))
s.add(Implies(And((nsnt1_x7<N-2*T), Not(nsnt1_y6<N-2*T)), Or((rule7_y6 == 0), (rule7_y6 == 1))))
s.add(Implies(And((nsnt1_x7<N-2*T), Not(nsnt1_y6<N-2*T)), Or((rule8_y6 == 0), (rule8_y6 == 1))))
s.add(Implies(And((nsnt1_x7<N-2*T), Not(nsnt1_y6<N-2*T)), Or((rule9_y6 == 0), (rule9_y6 == 1))))
s.add(Implies(And((nsnt1_x7<N-2*T), Not(nsnt1_y6<N-2*T)), Or((rule10_y6 == 0), (rule10_y6 == 1))))
s.add(Implies(And((nsnt1_x7<N-2*T), Not(nsnt1_y6<N-2*T)), Or((rule11_y6 == 0), (rule11_y6 == 1))))
s.add(Implies(And((nsnt1_x7<N-2*T), Not(nsnt1_y6<N-2*T)), Or((rule12_y6 == 0), (rule12_y6 == 1))))
s.add(Implies(And((nsnt1_x7<N-2*T), Not(nsnt1_y6<N-2*T)), Or((rule13_y6 == 0), (rule13_y6 == 1))))
s.add(Implies(And((nsnt1_x7<N-2*T), Not(nsnt1_y6<N-2*T)), Or((rule14_y6 == 0), (rule14_y6 == 1))))
s.add(Implies(And((nsnt1_x7<N-2*T), Not(nsnt1_y6<N-2*T)), Or((rule15_y6 == 0), (rule15_y6 == 1))))
s.add(Implies(And((nsnt1_x7<N-2*T), Not(nsnt1_y6<N-2*T)), Or((rule16_y6 == 0), (rule16_y6 == 1))))
s.add(Implies(And((nsnt1_x7<N-2*T), Not(nsnt1_y6<N-2*T)), Or((rule17_y6 == 0), (rule17_y6 == 1))))
s.add(Implies(And((nsnt1_x7<N-2*T), Not(nsnt1_y6<N-2*T)), Or((rule18_y6 == 0), (rule18_y6 == 1))))
s.add(Implies(And((nsnt1_x7<N-2*T), Not(nsnt1_y6<N-2*T)), Or((rule19_y6 == 0), (rule19_y6 == 1))))
s.add(Implies(And((nsnt1_x7<N-2*T), Not(nsnt1_y6<N-2*T)), Or((rule20_y6 == 0), (rule20_y6 == 1))))
s.add(Implies(And((nsnt1_x7<N-2*T), Not(nsnt1_y6<N-2*T)), Or((rule21_y6 == 0), (rule21_y6 == 1))))
s.add(Implies(And((nsnt1_x7<N-2*T), Not(nsnt1_y6<N-2*T)), Or((rule22_y6 == 0), (rule22_y6 == 1))))
s.add(Implies(And((nsnt1_x7<N-2*T), Not(nsnt1_y6<N-2*T)), Or((rule23_y6 == 0), (rule23_y6 == 1))))
s.add(Implies(And((nsnt1_x7<N-2*T), Not(nsnt1_y6<N-2*T)), Or((rule24_y6 == 0), (rule24_y6 == 1))))
s.add(Implies(And((nsnt1_x7<N-2*T), Not(nsnt1_y6<N-2*T)), Or((rule25_y6 == 0), (rule25_y6 == 1))))
s.add(Implies(And((nsnt1_x7<N-2*T), Not(nsnt1_y6<N-2*T)), Or((rule26_y6 == 0), (rule26_y6 == 1))))
s.add(Implies(And((nsnt1_x7<N-2*T), Not(nsnt1_y6<N-2*T)), Or((rule27_y6 == 0), (rule27_y6 == 1))))
s.add(Implies(And((nsnt1_x7<N-2*T), Not(nsnt1_y6<N-2*T)), Or((rule28_y6 == 0), (rule28_y6 == 1))))
s.add(Implies(And((nsnt1_x7<N-2*T), Not(nsnt1_y6<N-2*T)), Or((rule29_y6 == 0), (rule29_y6 == 1))))
s.add(Implies(And((nsnt1_x7<N-2*T), Not(nsnt1_y6<N-2*T)), rule0_y6+rule1_y6+rule2_y6+rule3_y6+rule4_y6+rule5_y6+rule6_y6+rule7_y6+rule8_y6+rule9_y6+rule10_y6+rule11_y6+rule12_y6+rule13_y6+rule14_y6+rule15_y6+rule16_y6+rule17_y6+rule18_y6+rule19_y6+rule20_y6+rule21_y6+rule22_y6+rule23_y6+rule24_y6+rule25_y6+rule26_y6+rule27_y6+rule28_y6+rule29_y6 <= 1))

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
s.add(Implies(And((nfaulty_x7<F), Not(nfaulty_y6<F)), Or((rule14_y6 == 0), (rule14_y6 == 1))))
s.add(Implies(And((nfaulty_x7<F), Not(nfaulty_y6<F)), Or((rule15_y6 == 0), (rule15_y6 == 1))))
s.add(Implies(And((nfaulty_x7<F), Not(nfaulty_y6<F)), Or((rule16_y6 == 0), (rule16_y6 == 1))))
s.add(Implies(And((nfaulty_x7<F), Not(nfaulty_y6<F)), Or((rule17_y6 == 0), (rule17_y6 == 1))))
s.add(Implies(And((nfaulty_x7<F), Not(nfaulty_y6<F)), Or((rule18_y6 == 0), (rule18_y6 == 1))))
s.add(Implies(And((nfaulty_x7<F), Not(nfaulty_y6<F)), Or((rule19_y6 == 0), (rule19_y6 == 1))))
s.add(Implies(And((nfaulty_x7<F), Not(nfaulty_y6<F)), Or((rule20_y6 == 0), (rule20_y6 == 1))))
s.add(Implies(And((nfaulty_x7<F), Not(nfaulty_y6<F)), Or((rule21_y6 == 0), (rule21_y6 == 1))))
s.add(Implies(And((nfaulty_x7<F), Not(nfaulty_y6<F)), Or((rule22_y6 == 0), (rule22_y6 == 1))))
s.add(Implies(And((nfaulty_x7<F), Not(nfaulty_y6<F)), Or((rule23_y6 == 0), (rule23_y6 == 1))))
s.add(Implies(And((nfaulty_x7<F), Not(nfaulty_y6<F)), Or((rule24_y6 == 0), (rule24_y6 == 1))))
s.add(Implies(And((nfaulty_x7<F), Not(nfaulty_y6<F)), Or((rule25_y6 == 0), (rule25_y6 == 1))))
s.add(Implies(And((nfaulty_x7<F), Not(nfaulty_y6<F)), Or((rule26_y6 == 0), (rule26_y6 == 1))))
s.add(Implies(And((nfaulty_x7<F), Not(nfaulty_y6<F)), Or((rule27_y6 == 0), (rule27_y6 == 1))))
s.add(Implies(And((nfaulty_x7<F), Not(nfaulty_y6<F)), Or((rule28_y6 == 0), (rule28_y6 == 1))))
s.add(Implies(And((nfaulty_x7<F), Not(nfaulty_y6<F)), Or((rule29_y6 == 0), (rule29_y6 == 1))))
s.add(Implies(And((nfaulty_x7<F), Not(nfaulty_y6<F)), rule0_y6+rule1_y6+rule2_y6+rule3_y6+rule4_y6+rule5_y6+rule6_y6+rule7_y6+rule8_y6+rule9_y6+rule10_y6+rule11_y6+rule12_y6+rule13_y6+rule14_y6+rule15_y6+rule16_y6+rule17_y6+rule18_y6+rule19_y6+rule20_y6+rule21_y6+rule22_y6+rule23_y6+rule24_y6+rule25_y6+rule26_y6+rule27_y6+rule28_y6+rule29_y6 <= 1))

s.add((nsnt0_x7<N-2*T) == (nsnt0_y6<N-2*T))
s.add(Implies(And((nsnt0_x7<N-2*T), Not(nsnt0_y6<N-2*T)), Or((rule0_y6 == 0), (rule0_y6 == 1))))
s.add(Implies(And((nsnt0_x7<N-2*T), Not(nsnt0_y6<N-2*T)), Or((rule1_y6 == 0), (rule1_y6 == 1))))
s.add(Implies(And((nsnt0_x7<N-2*T), Not(nsnt0_y6<N-2*T)), Or((rule2_y6 == 0), (rule2_y6 == 1))))
s.add(Implies(And((nsnt0_x7<N-2*T), Not(nsnt0_y6<N-2*T)), Or((rule3_y6 == 0), (rule3_y6 == 1))))
s.add(Implies(And((nsnt0_x7<N-2*T), Not(nsnt0_y6<N-2*T)), Or((rule4_y6 == 0), (rule4_y6 == 1))))
s.add(Implies(And((nsnt0_x7<N-2*T), Not(nsnt0_y6<N-2*T)), Or((rule5_y6 == 0), (rule5_y6 == 1))))
s.add(Implies(And((nsnt0_x7<N-2*T), Not(nsnt0_y6<N-2*T)), Or((rule6_y6 == 0), (rule6_y6 == 1))))
s.add(Implies(And((nsnt0_x7<N-2*T), Not(nsnt0_y6<N-2*T)), Or((rule7_y6 == 0), (rule7_y6 == 1))))
s.add(Implies(And((nsnt0_x7<N-2*T), Not(nsnt0_y6<N-2*T)), Or((rule8_y6 == 0), (rule8_y6 == 1))))
s.add(Implies(And((nsnt0_x7<N-2*T), Not(nsnt0_y6<N-2*T)), Or((rule9_y6 == 0), (rule9_y6 == 1))))
s.add(Implies(And((nsnt0_x7<N-2*T), Not(nsnt0_y6<N-2*T)), Or((rule10_y6 == 0), (rule10_y6 == 1))))
s.add(Implies(And((nsnt0_x7<N-2*T), Not(nsnt0_y6<N-2*T)), Or((rule11_y6 == 0), (rule11_y6 == 1))))
s.add(Implies(And((nsnt0_x7<N-2*T), Not(nsnt0_y6<N-2*T)), Or((rule12_y6 == 0), (rule12_y6 == 1))))
s.add(Implies(And((nsnt0_x7<N-2*T), Not(nsnt0_y6<N-2*T)), Or((rule13_y6 == 0), (rule13_y6 == 1))))
s.add(Implies(And((nsnt0_x7<N-2*T), Not(nsnt0_y6<N-2*T)), Or((rule14_y6 == 0), (rule14_y6 == 1))))
s.add(Implies(And((nsnt0_x7<N-2*T), Not(nsnt0_y6<N-2*T)), Or((rule15_y6 == 0), (rule15_y6 == 1))))
s.add(Implies(And((nsnt0_x7<N-2*T), Not(nsnt0_y6<N-2*T)), Or((rule16_y6 == 0), (rule16_y6 == 1))))
s.add(Implies(And((nsnt0_x7<N-2*T), Not(nsnt0_y6<N-2*T)), Or((rule17_y6 == 0), (rule17_y6 == 1))))
s.add(Implies(And((nsnt0_x7<N-2*T), Not(nsnt0_y6<N-2*T)), Or((rule18_y6 == 0), (rule18_y6 == 1))))
s.add(Implies(And((nsnt0_x7<N-2*T), Not(nsnt0_y6<N-2*T)), Or((rule19_y6 == 0), (rule19_y6 == 1))))
s.add(Implies(And((nsnt0_x7<N-2*T), Not(nsnt0_y6<N-2*T)), Or((rule20_y6 == 0), (rule20_y6 == 1))))
s.add(Implies(And((nsnt0_x7<N-2*T), Not(nsnt0_y6<N-2*T)), Or((rule21_y6 == 0), (rule21_y6 == 1))))
s.add(Implies(And((nsnt0_x7<N-2*T), Not(nsnt0_y6<N-2*T)), Or((rule22_y6 == 0), (rule22_y6 == 1))))
s.add(Implies(And((nsnt0_x7<N-2*T), Not(nsnt0_y6<N-2*T)), Or((rule23_y6 == 0), (rule23_y6 == 1))))
s.add(Implies(And((nsnt0_x7<N-2*T), Not(nsnt0_y6<N-2*T)), Or((rule24_y6 == 0), (rule24_y6 == 1))))
s.add(Implies(And((nsnt0_x7<N-2*T), Not(nsnt0_y6<N-2*T)), Or((rule25_y6 == 0), (rule25_y6 == 1))))
s.add(Implies(And((nsnt0_x7<N-2*T), Not(nsnt0_y6<N-2*T)), Or((rule26_y6 == 0), (rule26_y6 == 1))))
s.add(Implies(And((nsnt0_x7<N-2*T), Not(nsnt0_y6<N-2*T)), Or((rule27_y6 == 0), (rule27_y6 == 1))))
s.add(Implies(And((nsnt0_x7<N-2*T), Not(nsnt0_y6<N-2*T)), Or((rule28_y6 == 0), (rule28_y6 == 1))))
s.add(Implies(And((nsnt0_x7<N-2*T), Not(nsnt0_y6<N-2*T)), Or((rule29_y6 == 0), (rule29_y6 == 1))))
s.add(Implies(And((nsnt0_x7<N-2*T), Not(nsnt0_y6<N-2*T)), rule0_y6+rule1_y6+rule2_y6+rule3_y6+rule4_y6+rule5_y6+rule6_y6+rule7_y6+rule8_y6+rule9_y6+rule10_y6+rule11_y6+rule12_y6+rule13_y6+rule14_y6+rule15_y6+rule16_y6+rule17_y6+rule18_y6+rule19_y6+rule20_y6+rule21_y6+rule22_y6+rule23_y6+rule24_y6+rule25_y6+rule26_y6+rule27_y6+rule28_y6+rule29_y6 <= 1))


####################################################################################

#Creating constraints for a run between the y7th and x8th configurations

################Step 1#################


#Creating many copies of variables for rules

rule0_y7 = Real('rule0_y7')
s.add(rule0_y7 >= 0)
rule1_y7 = Real('rule1_y7')
s.add(rule1_y7 >= 0)
rule2_y7 = Real('rule2_y7')
s.add(rule2_y7 >= 0)
rule3_y7 = Real('rule3_y7')
s.add(rule3_y7 >= 0)
rule4_y7 = Real('rule4_y7')
s.add(rule4_y7 >= 0)
rule5_y7 = Real('rule5_y7')
s.add(rule5_y7 >= 0)
rule6_y7 = Real('rule6_y7')
s.add(rule6_y7 >= 0)
rule7_y7 = Real('rule7_y7')
s.add(rule7_y7 >= 0)
rule8_y7 = Real('rule8_y7')
s.add(rule8_y7 >= 0)
rule9_y7 = Real('rule9_y7')
s.add(rule9_y7 >= 0)
rule10_y7 = Real('rule10_y7')
s.add(rule10_y7 >= 0)
rule11_y7 = Real('rule11_y7')
s.add(rule11_y7 >= 0)
rule12_y7 = Real('rule12_y7')
s.add(rule12_y7 >= 0)
rule13_y7 = Real('rule13_y7')
s.add(rule13_y7 >= 0)
rule14_y7 = Real('rule14_y7')
s.add(rule14_y7 >= 0)
rule15_y7 = Real('rule15_y7')
s.add(rule15_y7 >= 0)
rule16_y7 = Real('rule16_y7')
s.add(rule16_y7 >= 0)
rule17_y7 = Real('rule17_y7')
s.add(rule17_y7 >= 0)
rule18_y7 = Real('rule18_y7')
s.add(rule18_y7 >= 0)
rule19_y7 = Real('rule19_y7')
s.add(rule19_y7 >= 0)
rule20_y7 = Real('rule20_y7')
s.add(rule20_y7 >= 0)
rule21_y7 = Real('rule21_y7')
s.add(rule21_y7 >= 0)
rule22_y7 = Real('rule22_y7')
s.add(rule22_y7 >= 0)
rule23_y7 = Real('rule23_y7')
s.add(rule23_y7 >= 0)
rule24_y7 = Real('rule24_y7')
s.add(rule24_y7 >= 0)
rule25_y7 = Real('rule25_y7')
s.add(rule25_y7 >= 0)
rule26_y7 = Real('rule26_y7')
s.add(rule26_y7 >= 0)
rule27_y7 = Real('rule27_y7')
s.add(rule27_y7 >= 0)
rule28_y7 = Real('rule28_y7')
s.add(rule28_y7 >= 0)
rule29_y7 = Real('rule29_y7')
s.add(rule29_y7 >= 0)






###################Step 2####################


#Flow equations for the locations

s.add(0 - rule0_y7 - rule1_y7 - rule14_y7 - rule22_y7 + rule22_y7 ==  loc0_x8 - loc0_y7)
s.add(0 - rule2_y7 - rule3_y7 - rule15_y7 - rule23_y7 + rule23_y7 ==  loc1_x8 - loc1_y7)
s.add(0 + rule0_y7 - rule4_y7 - rule6_y7 - rule8_y7 - rule10_y7 - rule12_y7 - rule16_y7 - rule24_y7 + rule24_y7 ==  locS0_x8 - locS0_y7)
s.add(0 + rule2_y7 - rule5_y7 - rule7_y7 - rule9_y7 - rule11_y7 - rule13_y7 - rule17_y7 - rule25_y7 + rule25_y7 ==  locS1_x8 - locS1_y7)
s.add(0 + rule4_y7 + rule5_y7 - rule18_y7 - rule26_y7 + rule26_y7 ==  locD0_x8 - locD0_y7)
s.add(0 + rule6_y7 + rule7_y7 - rule19_y7 - rule27_y7 + rule27_y7 ==  locD1_x8 - locD1_y7)
s.add(0 + rule8_y7 + rule9_y7 + rule12_y7 - rule20_y7 - rule28_y7 + rule28_y7 ==  locU0_x8 - locU0_y7)
s.add(0 + rule10_y7 + rule11_y7 + rule13_y7 - rule21_y7 - rule29_y7 + rule29_y7 ==  locU1_x8 - locU1_y7)
s.add(0 + rule1_y7 + rule3_y7 + rule14_y7 + rule15_y7 + rule16_y7 + rule17_y7 + rule18_y7 + rule19_y7 + rule20_y7 + rule21_y7 ==  locCR_x8 - locCR_y7)






##################Step 3########################


#Flow equations for the shared variables

s.add(0 + rule0_y7 == nsnt0_x8 - nsnt0_y7)
s.add(0 + rule2_y7 == nsnt1_x8 - nsnt1_y7)
s.add(0 + rule0_y7 + rule1_y7 == nsnt0CF_x8 - nsnt0CF_y7)
s.add(0 + rule2_y7 + rule3_y7 == nsnt1CF_x8 - nsnt1CF_y7)
s.add(0 + rule0_y7 + rule2_y7 == nsnt01_x8 - nsnt01_y7)
s.add(0 + rule0_y7 + rule1_y7 + rule2_y7 + rule3_y7 == nsnt01CF_x8 - nsnt01CF_y7)
s.add(0 + rule1_y7 + rule3_y7 + rule14_y7 + rule15_y7 + rule16_y7 + rule17_y7 + rule18_y7 + rule19_y7 + rule20_y7 + rule21_y7 == nfaulty_x8 - nfaulty_y7)






####################Step 4########################


#Rule is fired implies rule is enabled

s.add(Implies( (rule0_y7 > 0), And(True, ) ))
s.add(Implies( (rule1_y7 > 0), And(nfaulty_y7<F, ) ))
s.add(Implies( (rule2_y7 > 0), And(True, ) ))
s.add(Implies( (rule3_y7 > 0), And(nfaulty_y7<F, ) ))
s.add(Implies( (rule4_y7 > 0), And(nsnt0CF_y7>=N-T, ) ))
s.add(Implies( (rule5_y7 > 0), And(nsnt0CF_y7>=N-T, ) ))
s.add(Implies( (rule6_y7 > 0), And(nsnt1CF_y7>=N-T, ) ))
s.add(Implies( (rule7_y7 > 0), And(nsnt1CF_y7>=N-T, ) ))
s.add(Implies( (rule8_y7 > 0), And(nsnt01CF_y7>=N-T, nsnt0CF_y7>=N-2*T, nsnt1CF_y7>=1, ) ))
s.add(Implies( (rule9_y7 > 0), And(nsnt01CF_y7>=N-T, nsnt0CF_y7>=N-2*T, nsnt1CF_y7>=1, ) ))
s.add(Implies( (rule10_y7 > 0), And(nsnt01CF_y7>=N-T, nsnt1CF_y7>=N-2*T, nsnt0CF_y7>=1, ) ))
s.add(Implies( (rule11_y7 > 0), And(nsnt01CF_y7>=N-T, nsnt1CF_y7>=N-2*T, nsnt0CF_y7>=1, ) ))
s.add(Implies( (rule12_y7 > 0), And(nsnt01CF_y7>=N-T, nsnt0_y7<N-2*T, nsnt1_y7<N-2*T, ) ))
s.add(Implies( (rule13_y7 > 0), And(nsnt01CF_y7>=N-T, nsnt0_y7<N-2*T, nsnt1_y7<N-2*T, ) ))
s.add(Implies( (rule14_y7 > 0), And(nfaulty_y7<F, ) ))
s.add(Implies( (rule15_y7 > 0), And(nfaulty_y7<F, ) ))
s.add(Implies( (rule16_y7 > 0), And(nfaulty_y7<F, ) ))
s.add(Implies( (rule17_y7 > 0), And(nfaulty_y7<F, ) ))
s.add(Implies( (rule18_y7 > 0), And(nfaulty_y7<F, ) ))
s.add(Implies( (rule19_y7 > 0), And(nfaulty_y7<F, ) ))
s.add(Implies( (rule20_y7 > 0), And(nfaulty_y7<F, ) ))
s.add(Implies( (rule21_y7 > 0), And(nfaulty_y7<F, ) ))
s.add(Implies( (rule22_y7 > 0), And(True, ) ))
s.add(Implies( (rule23_y7 > 0), And(True, ) ))
s.add(Implies( (rule24_y7 > 0), And(True, ) ))
s.add(Implies( (rule25_y7 > 0), And(True, ) ))
s.add(Implies( (rule26_y7 > 0), And(True, ) ))
s.add(Implies( (rule27_y7 > 0), And(True, ) ))
s.add(Implies( (rule28_y7 > 0), And(True, ) ))
s.add(Implies( (rule29_y7 > 0), And(True, ) ))

##################Step 5########################


#Ensuring that at most one rule is fired alternating configurations y7 and x7, if a fall condition is present

s.add((nsnt1_x8<N-2*T) == (nsnt1_y7<N-2*T))
s.add(Implies(And((nsnt1_x8<N-2*T), Not(nsnt1_y7<N-2*T)), Or((rule0_y7 == 0), (rule0_y7 == 1))))
s.add(Implies(And((nsnt1_x8<N-2*T), Not(nsnt1_y7<N-2*T)), Or((rule1_y7 == 0), (rule1_y7 == 1))))
s.add(Implies(And((nsnt1_x8<N-2*T), Not(nsnt1_y7<N-2*T)), Or((rule2_y7 == 0), (rule2_y7 == 1))))
s.add(Implies(And((nsnt1_x8<N-2*T), Not(nsnt1_y7<N-2*T)), Or((rule3_y7 == 0), (rule3_y7 == 1))))
s.add(Implies(And((nsnt1_x8<N-2*T), Not(nsnt1_y7<N-2*T)), Or((rule4_y7 == 0), (rule4_y7 == 1))))
s.add(Implies(And((nsnt1_x8<N-2*T), Not(nsnt1_y7<N-2*T)), Or((rule5_y7 == 0), (rule5_y7 == 1))))
s.add(Implies(And((nsnt1_x8<N-2*T), Not(nsnt1_y7<N-2*T)), Or((rule6_y7 == 0), (rule6_y7 == 1))))
s.add(Implies(And((nsnt1_x8<N-2*T), Not(nsnt1_y7<N-2*T)), Or((rule7_y7 == 0), (rule7_y7 == 1))))
s.add(Implies(And((nsnt1_x8<N-2*T), Not(nsnt1_y7<N-2*T)), Or((rule8_y7 == 0), (rule8_y7 == 1))))
s.add(Implies(And((nsnt1_x8<N-2*T), Not(nsnt1_y7<N-2*T)), Or((rule9_y7 == 0), (rule9_y7 == 1))))
s.add(Implies(And((nsnt1_x8<N-2*T), Not(nsnt1_y7<N-2*T)), Or((rule10_y7 == 0), (rule10_y7 == 1))))
s.add(Implies(And((nsnt1_x8<N-2*T), Not(nsnt1_y7<N-2*T)), Or((rule11_y7 == 0), (rule11_y7 == 1))))
s.add(Implies(And((nsnt1_x8<N-2*T), Not(nsnt1_y7<N-2*T)), Or((rule12_y7 == 0), (rule12_y7 == 1))))
s.add(Implies(And((nsnt1_x8<N-2*T), Not(nsnt1_y7<N-2*T)), Or((rule13_y7 == 0), (rule13_y7 == 1))))
s.add(Implies(And((nsnt1_x8<N-2*T), Not(nsnt1_y7<N-2*T)), Or((rule14_y7 == 0), (rule14_y7 == 1))))
s.add(Implies(And((nsnt1_x8<N-2*T), Not(nsnt1_y7<N-2*T)), Or((rule15_y7 == 0), (rule15_y7 == 1))))
s.add(Implies(And((nsnt1_x8<N-2*T), Not(nsnt1_y7<N-2*T)), Or((rule16_y7 == 0), (rule16_y7 == 1))))
s.add(Implies(And((nsnt1_x8<N-2*T), Not(nsnt1_y7<N-2*T)), Or((rule17_y7 == 0), (rule17_y7 == 1))))
s.add(Implies(And((nsnt1_x8<N-2*T), Not(nsnt1_y7<N-2*T)), Or((rule18_y7 == 0), (rule18_y7 == 1))))
s.add(Implies(And((nsnt1_x8<N-2*T), Not(nsnt1_y7<N-2*T)), Or((rule19_y7 == 0), (rule19_y7 == 1))))
s.add(Implies(And((nsnt1_x8<N-2*T), Not(nsnt1_y7<N-2*T)), Or((rule20_y7 == 0), (rule20_y7 == 1))))
s.add(Implies(And((nsnt1_x8<N-2*T), Not(nsnt1_y7<N-2*T)), Or((rule21_y7 == 0), (rule21_y7 == 1))))
s.add(Implies(And((nsnt1_x8<N-2*T), Not(nsnt1_y7<N-2*T)), Or((rule22_y7 == 0), (rule22_y7 == 1))))
s.add(Implies(And((nsnt1_x8<N-2*T), Not(nsnt1_y7<N-2*T)), Or((rule23_y7 == 0), (rule23_y7 == 1))))
s.add(Implies(And((nsnt1_x8<N-2*T), Not(nsnt1_y7<N-2*T)), Or((rule24_y7 == 0), (rule24_y7 == 1))))
s.add(Implies(And((nsnt1_x8<N-2*T), Not(nsnt1_y7<N-2*T)), Or((rule25_y7 == 0), (rule25_y7 == 1))))
s.add(Implies(And((nsnt1_x8<N-2*T), Not(nsnt1_y7<N-2*T)), Or((rule26_y7 == 0), (rule26_y7 == 1))))
s.add(Implies(And((nsnt1_x8<N-2*T), Not(nsnt1_y7<N-2*T)), Or((rule27_y7 == 0), (rule27_y7 == 1))))
s.add(Implies(And((nsnt1_x8<N-2*T), Not(nsnt1_y7<N-2*T)), Or((rule28_y7 == 0), (rule28_y7 == 1))))
s.add(Implies(And((nsnt1_x8<N-2*T), Not(nsnt1_y7<N-2*T)), Or((rule29_y7 == 0), (rule29_y7 == 1))))
s.add(Implies(And((nsnt1_x8<N-2*T), Not(nsnt1_y7<N-2*T)), rule0_y7+rule1_y7+rule2_y7+rule3_y7+rule4_y7+rule5_y7+rule6_y7+rule7_y7+rule8_y7+rule9_y7+rule10_y7+rule11_y7+rule12_y7+rule13_y7+rule14_y7+rule15_y7+rule16_y7+rule17_y7+rule18_y7+rule19_y7+rule20_y7+rule21_y7+rule22_y7+rule23_y7+rule24_y7+rule25_y7+rule26_y7+rule27_y7+rule28_y7+rule29_y7 <= 1))

s.add((nfaulty_x8<F) == (nfaulty_y7<F))
s.add(Implies(And((nfaulty_x8<F), Not(nfaulty_y7<F)), Or((rule0_y7 == 0), (rule0_y7 == 1))))
s.add(Implies(And((nfaulty_x8<F), Not(nfaulty_y7<F)), Or((rule1_y7 == 0), (rule1_y7 == 1))))
s.add(Implies(And((nfaulty_x8<F), Not(nfaulty_y7<F)), Or((rule2_y7 == 0), (rule2_y7 == 1))))
s.add(Implies(And((nfaulty_x8<F), Not(nfaulty_y7<F)), Or((rule3_y7 == 0), (rule3_y7 == 1))))
s.add(Implies(And((nfaulty_x8<F), Not(nfaulty_y7<F)), Or((rule4_y7 == 0), (rule4_y7 == 1))))
s.add(Implies(And((nfaulty_x8<F), Not(nfaulty_y7<F)), Or((rule5_y7 == 0), (rule5_y7 == 1))))
s.add(Implies(And((nfaulty_x8<F), Not(nfaulty_y7<F)), Or((rule6_y7 == 0), (rule6_y7 == 1))))
s.add(Implies(And((nfaulty_x8<F), Not(nfaulty_y7<F)), Or((rule7_y7 == 0), (rule7_y7 == 1))))
s.add(Implies(And((nfaulty_x8<F), Not(nfaulty_y7<F)), Or((rule8_y7 == 0), (rule8_y7 == 1))))
s.add(Implies(And((nfaulty_x8<F), Not(nfaulty_y7<F)), Or((rule9_y7 == 0), (rule9_y7 == 1))))
s.add(Implies(And((nfaulty_x8<F), Not(nfaulty_y7<F)), Or((rule10_y7 == 0), (rule10_y7 == 1))))
s.add(Implies(And((nfaulty_x8<F), Not(nfaulty_y7<F)), Or((rule11_y7 == 0), (rule11_y7 == 1))))
s.add(Implies(And((nfaulty_x8<F), Not(nfaulty_y7<F)), Or((rule12_y7 == 0), (rule12_y7 == 1))))
s.add(Implies(And((nfaulty_x8<F), Not(nfaulty_y7<F)), Or((rule13_y7 == 0), (rule13_y7 == 1))))
s.add(Implies(And((nfaulty_x8<F), Not(nfaulty_y7<F)), Or((rule14_y7 == 0), (rule14_y7 == 1))))
s.add(Implies(And((nfaulty_x8<F), Not(nfaulty_y7<F)), Or((rule15_y7 == 0), (rule15_y7 == 1))))
s.add(Implies(And((nfaulty_x8<F), Not(nfaulty_y7<F)), Or((rule16_y7 == 0), (rule16_y7 == 1))))
s.add(Implies(And((nfaulty_x8<F), Not(nfaulty_y7<F)), Or((rule17_y7 == 0), (rule17_y7 == 1))))
s.add(Implies(And((nfaulty_x8<F), Not(nfaulty_y7<F)), Or((rule18_y7 == 0), (rule18_y7 == 1))))
s.add(Implies(And((nfaulty_x8<F), Not(nfaulty_y7<F)), Or((rule19_y7 == 0), (rule19_y7 == 1))))
s.add(Implies(And((nfaulty_x8<F), Not(nfaulty_y7<F)), Or((rule20_y7 == 0), (rule20_y7 == 1))))
s.add(Implies(And((nfaulty_x8<F), Not(nfaulty_y7<F)), Or((rule21_y7 == 0), (rule21_y7 == 1))))
s.add(Implies(And((nfaulty_x8<F), Not(nfaulty_y7<F)), Or((rule22_y7 == 0), (rule22_y7 == 1))))
s.add(Implies(And((nfaulty_x8<F), Not(nfaulty_y7<F)), Or((rule23_y7 == 0), (rule23_y7 == 1))))
s.add(Implies(And((nfaulty_x8<F), Not(nfaulty_y7<F)), Or((rule24_y7 == 0), (rule24_y7 == 1))))
s.add(Implies(And((nfaulty_x8<F), Not(nfaulty_y7<F)), Or((rule25_y7 == 0), (rule25_y7 == 1))))
s.add(Implies(And((nfaulty_x8<F), Not(nfaulty_y7<F)), Or((rule26_y7 == 0), (rule26_y7 == 1))))
s.add(Implies(And((nfaulty_x8<F), Not(nfaulty_y7<F)), Or((rule27_y7 == 0), (rule27_y7 == 1))))
s.add(Implies(And((nfaulty_x8<F), Not(nfaulty_y7<F)), Or((rule28_y7 == 0), (rule28_y7 == 1))))
s.add(Implies(And((nfaulty_x8<F), Not(nfaulty_y7<F)), Or((rule29_y7 == 0), (rule29_y7 == 1))))
s.add(Implies(And((nfaulty_x8<F), Not(nfaulty_y7<F)), rule0_y7+rule1_y7+rule2_y7+rule3_y7+rule4_y7+rule5_y7+rule6_y7+rule7_y7+rule8_y7+rule9_y7+rule10_y7+rule11_y7+rule12_y7+rule13_y7+rule14_y7+rule15_y7+rule16_y7+rule17_y7+rule18_y7+rule19_y7+rule20_y7+rule21_y7+rule22_y7+rule23_y7+rule24_y7+rule25_y7+rule26_y7+rule27_y7+rule28_y7+rule29_y7 <= 1))

s.add((nsnt0_x8<N-2*T) == (nsnt0_y7<N-2*T))
s.add(Implies(And((nsnt0_x8<N-2*T), Not(nsnt0_y7<N-2*T)), Or((rule0_y7 == 0), (rule0_y7 == 1))))
s.add(Implies(And((nsnt0_x8<N-2*T), Not(nsnt0_y7<N-2*T)), Or((rule1_y7 == 0), (rule1_y7 == 1))))
s.add(Implies(And((nsnt0_x8<N-2*T), Not(nsnt0_y7<N-2*T)), Or((rule2_y7 == 0), (rule2_y7 == 1))))
s.add(Implies(And((nsnt0_x8<N-2*T), Not(nsnt0_y7<N-2*T)), Or((rule3_y7 == 0), (rule3_y7 == 1))))
s.add(Implies(And((nsnt0_x8<N-2*T), Not(nsnt0_y7<N-2*T)), Or((rule4_y7 == 0), (rule4_y7 == 1))))
s.add(Implies(And((nsnt0_x8<N-2*T), Not(nsnt0_y7<N-2*T)), Or((rule5_y7 == 0), (rule5_y7 == 1))))
s.add(Implies(And((nsnt0_x8<N-2*T), Not(nsnt0_y7<N-2*T)), Or((rule6_y7 == 0), (rule6_y7 == 1))))
s.add(Implies(And((nsnt0_x8<N-2*T), Not(nsnt0_y7<N-2*T)), Or((rule7_y7 == 0), (rule7_y7 == 1))))
s.add(Implies(And((nsnt0_x8<N-2*T), Not(nsnt0_y7<N-2*T)), Or((rule8_y7 == 0), (rule8_y7 == 1))))
s.add(Implies(And((nsnt0_x8<N-2*T), Not(nsnt0_y7<N-2*T)), Or((rule9_y7 == 0), (rule9_y7 == 1))))
s.add(Implies(And((nsnt0_x8<N-2*T), Not(nsnt0_y7<N-2*T)), Or((rule10_y7 == 0), (rule10_y7 == 1))))
s.add(Implies(And((nsnt0_x8<N-2*T), Not(nsnt0_y7<N-2*T)), Or((rule11_y7 == 0), (rule11_y7 == 1))))
s.add(Implies(And((nsnt0_x8<N-2*T), Not(nsnt0_y7<N-2*T)), Or((rule12_y7 == 0), (rule12_y7 == 1))))
s.add(Implies(And((nsnt0_x8<N-2*T), Not(nsnt0_y7<N-2*T)), Or((rule13_y7 == 0), (rule13_y7 == 1))))
s.add(Implies(And((nsnt0_x8<N-2*T), Not(nsnt0_y7<N-2*T)), Or((rule14_y7 == 0), (rule14_y7 == 1))))
s.add(Implies(And((nsnt0_x8<N-2*T), Not(nsnt0_y7<N-2*T)), Or((rule15_y7 == 0), (rule15_y7 == 1))))
s.add(Implies(And((nsnt0_x8<N-2*T), Not(nsnt0_y7<N-2*T)), Or((rule16_y7 == 0), (rule16_y7 == 1))))
s.add(Implies(And((nsnt0_x8<N-2*T), Not(nsnt0_y7<N-2*T)), Or((rule17_y7 == 0), (rule17_y7 == 1))))
s.add(Implies(And((nsnt0_x8<N-2*T), Not(nsnt0_y7<N-2*T)), Or((rule18_y7 == 0), (rule18_y7 == 1))))
s.add(Implies(And((nsnt0_x8<N-2*T), Not(nsnt0_y7<N-2*T)), Or((rule19_y7 == 0), (rule19_y7 == 1))))
s.add(Implies(And((nsnt0_x8<N-2*T), Not(nsnt0_y7<N-2*T)), Or((rule20_y7 == 0), (rule20_y7 == 1))))
s.add(Implies(And((nsnt0_x8<N-2*T), Not(nsnt0_y7<N-2*T)), Or((rule21_y7 == 0), (rule21_y7 == 1))))
s.add(Implies(And((nsnt0_x8<N-2*T), Not(nsnt0_y7<N-2*T)), Or((rule22_y7 == 0), (rule22_y7 == 1))))
s.add(Implies(And((nsnt0_x8<N-2*T), Not(nsnt0_y7<N-2*T)), Or((rule23_y7 == 0), (rule23_y7 == 1))))
s.add(Implies(And((nsnt0_x8<N-2*T), Not(nsnt0_y7<N-2*T)), Or((rule24_y7 == 0), (rule24_y7 == 1))))
s.add(Implies(And((nsnt0_x8<N-2*T), Not(nsnt0_y7<N-2*T)), Or((rule25_y7 == 0), (rule25_y7 == 1))))
s.add(Implies(And((nsnt0_x8<N-2*T), Not(nsnt0_y7<N-2*T)), Or((rule26_y7 == 0), (rule26_y7 == 1))))
s.add(Implies(And((nsnt0_x8<N-2*T), Not(nsnt0_y7<N-2*T)), Or((rule27_y7 == 0), (rule27_y7 == 1))))
s.add(Implies(And((nsnt0_x8<N-2*T), Not(nsnt0_y7<N-2*T)), Or((rule28_y7 == 0), (rule28_y7 == 1))))
s.add(Implies(And((nsnt0_x8<N-2*T), Not(nsnt0_y7<N-2*T)), Or((rule29_y7 == 0), (rule29_y7 == 1))))
s.add(Implies(And((nsnt0_x8<N-2*T), Not(nsnt0_y7<N-2*T)), rule0_y7+rule1_y7+rule2_y7+rule3_y7+rule4_y7+rule5_y7+rule6_y7+rule7_y7+rule8_y7+rule9_y7+rule10_y7+rule11_y7+rule12_y7+rule13_y7+rule14_y7+rule15_y7+rule16_y7+rule17_y7+rule18_y7+rule19_y7+rule20_y7+rule21_y7+rule22_y7+rule23_y7+rule24_y7+rule25_y7+rule26_y7+rule27_y7+rule28_y7+rule29_y7 <= 1))


####################################################################################

#Creating constraints for a run between the y8th and x9th configurations

################Step 1#################


#Creating many copies of variables for rules

rule0_y8 = Real('rule0_y8')
s.add(rule0_y8 >= 0)
rule1_y8 = Real('rule1_y8')
s.add(rule1_y8 >= 0)
rule2_y8 = Real('rule2_y8')
s.add(rule2_y8 >= 0)
rule3_y8 = Real('rule3_y8')
s.add(rule3_y8 >= 0)
rule4_y8 = Real('rule4_y8')
s.add(rule4_y8 >= 0)
rule5_y8 = Real('rule5_y8')
s.add(rule5_y8 >= 0)
rule6_y8 = Real('rule6_y8')
s.add(rule6_y8 >= 0)
rule7_y8 = Real('rule7_y8')
s.add(rule7_y8 >= 0)
rule8_y8 = Real('rule8_y8')
s.add(rule8_y8 >= 0)
rule9_y8 = Real('rule9_y8')
s.add(rule9_y8 >= 0)
rule10_y8 = Real('rule10_y8')
s.add(rule10_y8 >= 0)
rule11_y8 = Real('rule11_y8')
s.add(rule11_y8 >= 0)
rule12_y8 = Real('rule12_y8')
s.add(rule12_y8 >= 0)
rule13_y8 = Real('rule13_y8')
s.add(rule13_y8 >= 0)
rule14_y8 = Real('rule14_y8')
s.add(rule14_y8 >= 0)
rule15_y8 = Real('rule15_y8')
s.add(rule15_y8 >= 0)
rule16_y8 = Real('rule16_y8')
s.add(rule16_y8 >= 0)
rule17_y8 = Real('rule17_y8')
s.add(rule17_y8 >= 0)
rule18_y8 = Real('rule18_y8')
s.add(rule18_y8 >= 0)
rule19_y8 = Real('rule19_y8')
s.add(rule19_y8 >= 0)
rule20_y8 = Real('rule20_y8')
s.add(rule20_y8 >= 0)
rule21_y8 = Real('rule21_y8')
s.add(rule21_y8 >= 0)
rule22_y8 = Real('rule22_y8')
s.add(rule22_y8 >= 0)
rule23_y8 = Real('rule23_y8')
s.add(rule23_y8 >= 0)
rule24_y8 = Real('rule24_y8')
s.add(rule24_y8 >= 0)
rule25_y8 = Real('rule25_y8')
s.add(rule25_y8 >= 0)
rule26_y8 = Real('rule26_y8')
s.add(rule26_y8 >= 0)
rule27_y8 = Real('rule27_y8')
s.add(rule27_y8 >= 0)
rule28_y8 = Real('rule28_y8')
s.add(rule28_y8 >= 0)
rule29_y8 = Real('rule29_y8')
s.add(rule29_y8 >= 0)






###################Step 2####################


#Flow equations for the locations

s.add(0 - rule0_y8 - rule1_y8 - rule14_y8 - rule22_y8 + rule22_y8 ==  loc0_x9 - loc0_y8)
s.add(0 - rule2_y8 - rule3_y8 - rule15_y8 - rule23_y8 + rule23_y8 ==  loc1_x9 - loc1_y8)
s.add(0 + rule0_y8 - rule4_y8 - rule6_y8 - rule8_y8 - rule10_y8 - rule12_y8 - rule16_y8 - rule24_y8 + rule24_y8 ==  locS0_x9 - locS0_y8)
s.add(0 + rule2_y8 - rule5_y8 - rule7_y8 - rule9_y8 - rule11_y8 - rule13_y8 - rule17_y8 - rule25_y8 + rule25_y8 ==  locS1_x9 - locS1_y8)
s.add(0 + rule4_y8 + rule5_y8 - rule18_y8 - rule26_y8 + rule26_y8 ==  locD0_x9 - locD0_y8)
s.add(0 + rule6_y8 + rule7_y8 - rule19_y8 - rule27_y8 + rule27_y8 ==  locD1_x9 - locD1_y8)
s.add(0 + rule8_y8 + rule9_y8 + rule12_y8 - rule20_y8 - rule28_y8 + rule28_y8 ==  locU0_x9 - locU0_y8)
s.add(0 + rule10_y8 + rule11_y8 + rule13_y8 - rule21_y8 - rule29_y8 + rule29_y8 ==  locU1_x9 - locU1_y8)
s.add(0 + rule1_y8 + rule3_y8 + rule14_y8 + rule15_y8 + rule16_y8 + rule17_y8 + rule18_y8 + rule19_y8 + rule20_y8 + rule21_y8 ==  locCR_x9 - locCR_y8)






##################Step 3########################


#Flow equations for the shared variables

s.add(0 + rule0_y8 == nsnt0_x9 - nsnt0_y8)
s.add(0 + rule2_y8 == nsnt1_x9 - nsnt1_y8)
s.add(0 + rule0_y8 + rule1_y8 == nsnt0CF_x9 - nsnt0CF_y8)
s.add(0 + rule2_y8 + rule3_y8 == nsnt1CF_x9 - nsnt1CF_y8)
s.add(0 + rule0_y8 + rule2_y8 == nsnt01_x9 - nsnt01_y8)
s.add(0 + rule0_y8 + rule1_y8 + rule2_y8 + rule3_y8 == nsnt01CF_x9 - nsnt01CF_y8)
s.add(0 + rule1_y8 + rule3_y8 + rule14_y8 + rule15_y8 + rule16_y8 + rule17_y8 + rule18_y8 + rule19_y8 + rule20_y8 + rule21_y8 == nfaulty_x9 - nfaulty_y8)






####################Step 4########################


#Rule is fired implies rule is enabled

s.add(Implies( (rule0_y8 > 0), And(True, ) ))
s.add(Implies( (rule1_y8 > 0), And(nfaulty_y8<F, ) ))
s.add(Implies( (rule2_y8 > 0), And(True, ) ))
s.add(Implies( (rule3_y8 > 0), And(nfaulty_y8<F, ) ))
s.add(Implies( (rule4_y8 > 0), And(nsnt0CF_y8>=N-T, ) ))
s.add(Implies( (rule5_y8 > 0), And(nsnt0CF_y8>=N-T, ) ))
s.add(Implies( (rule6_y8 > 0), And(nsnt1CF_y8>=N-T, ) ))
s.add(Implies( (rule7_y8 > 0), And(nsnt1CF_y8>=N-T, ) ))
s.add(Implies( (rule8_y8 > 0), And(nsnt01CF_y8>=N-T, nsnt0CF_y8>=N-2*T, nsnt1CF_y8>=1, ) ))
s.add(Implies( (rule9_y8 > 0), And(nsnt01CF_y8>=N-T, nsnt0CF_y8>=N-2*T, nsnt1CF_y8>=1, ) ))
s.add(Implies( (rule10_y8 > 0), And(nsnt01CF_y8>=N-T, nsnt1CF_y8>=N-2*T, nsnt0CF_y8>=1, ) ))
s.add(Implies( (rule11_y8 > 0), And(nsnt01CF_y8>=N-T, nsnt1CF_y8>=N-2*T, nsnt0CF_y8>=1, ) ))
s.add(Implies( (rule12_y8 > 0), And(nsnt01CF_y8>=N-T, nsnt0_y8<N-2*T, nsnt1_y8<N-2*T, ) ))
s.add(Implies( (rule13_y8 > 0), And(nsnt01CF_y8>=N-T, nsnt0_y8<N-2*T, nsnt1_y8<N-2*T, ) ))
s.add(Implies( (rule14_y8 > 0), And(nfaulty_y8<F, ) ))
s.add(Implies( (rule15_y8 > 0), And(nfaulty_y8<F, ) ))
s.add(Implies( (rule16_y8 > 0), And(nfaulty_y8<F, ) ))
s.add(Implies( (rule17_y8 > 0), And(nfaulty_y8<F, ) ))
s.add(Implies( (rule18_y8 > 0), And(nfaulty_y8<F, ) ))
s.add(Implies( (rule19_y8 > 0), And(nfaulty_y8<F, ) ))
s.add(Implies( (rule20_y8 > 0), And(nfaulty_y8<F, ) ))
s.add(Implies( (rule21_y8 > 0), And(nfaulty_y8<F, ) ))
s.add(Implies( (rule22_y8 > 0), And(True, ) ))
s.add(Implies( (rule23_y8 > 0), And(True, ) ))
s.add(Implies( (rule24_y8 > 0), And(True, ) ))
s.add(Implies( (rule25_y8 > 0), And(True, ) ))
s.add(Implies( (rule26_y8 > 0), And(True, ) ))
s.add(Implies( (rule27_y8 > 0), And(True, ) ))
s.add(Implies( (rule28_y8 > 0), And(True, ) ))
s.add(Implies( (rule29_y8 > 0), And(True, ) ))

##################Step 5########################


#Ensuring that at most one rule is fired alternating configurations y8 and x8, if a fall condition is present

s.add((nsnt1_x9<N-2*T) == (nsnt1_y8<N-2*T))
s.add(Implies(And((nsnt1_x9<N-2*T), Not(nsnt1_y8<N-2*T)), Or((rule0_y8 == 0), (rule0_y8 == 1))))
s.add(Implies(And((nsnt1_x9<N-2*T), Not(nsnt1_y8<N-2*T)), Or((rule1_y8 == 0), (rule1_y8 == 1))))
s.add(Implies(And((nsnt1_x9<N-2*T), Not(nsnt1_y8<N-2*T)), Or((rule2_y8 == 0), (rule2_y8 == 1))))
s.add(Implies(And((nsnt1_x9<N-2*T), Not(nsnt1_y8<N-2*T)), Or((rule3_y8 == 0), (rule3_y8 == 1))))
s.add(Implies(And((nsnt1_x9<N-2*T), Not(nsnt1_y8<N-2*T)), Or((rule4_y8 == 0), (rule4_y8 == 1))))
s.add(Implies(And((nsnt1_x9<N-2*T), Not(nsnt1_y8<N-2*T)), Or((rule5_y8 == 0), (rule5_y8 == 1))))
s.add(Implies(And((nsnt1_x9<N-2*T), Not(nsnt1_y8<N-2*T)), Or((rule6_y8 == 0), (rule6_y8 == 1))))
s.add(Implies(And((nsnt1_x9<N-2*T), Not(nsnt1_y8<N-2*T)), Or((rule7_y8 == 0), (rule7_y8 == 1))))
s.add(Implies(And((nsnt1_x9<N-2*T), Not(nsnt1_y8<N-2*T)), Or((rule8_y8 == 0), (rule8_y8 == 1))))
s.add(Implies(And((nsnt1_x9<N-2*T), Not(nsnt1_y8<N-2*T)), Or((rule9_y8 == 0), (rule9_y8 == 1))))
s.add(Implies(And((nsnt1_x9<N-2*T), Not(nsnt1_y8<N-2*T)), Or((rule10_y8 == 0), (rule10_y8 == 1))))
s.add(Implies(And((nsnt1_x9<N-2*T), Not(nsnt1_y8<N-2*T)), Or((rule11_y8 == 0), (rule11_y8 == 1))))
s.add(Implies(And((nsnt1_x9<N-2*T), Not(nsnt1_y8<N-2*T)), Or((rule12_y8 == 0), (rule12_y8 == 1))))
s.add(Implies(And((nsnt1_x9<N-2*T), Not(nsnt1_y8<N-2*T)), Or((rule13_y8 == 0), (rule13_y8 == 1))))
s.add(Implies(And((nsnt1_x9<N-2*T), Not(nsnt1_y8<N-2*T)), Or((rule14_y8 == 0), (rule14_y8 == 1))))
s.add(Implies(And((nsnt1_x9<N-2*T), Not(nsnt1_y8<N-2*T)), Or((rule15_y8 == 0), (rule15_y8 == 1))))
s.add(Implies(And((nsnt1_x9<N-2*T), Not(nsnt1_y8<N-2*T)), Or((rule16_y8 == 0), (rule16_y8 == 1))))
s.add(Implies(And((nsnt1_x9<N-2*T), Not(nsnt1_y8<N-2*T)), Or((rule17_y8 == 0), (rule17_y8 == 1))))
s.add(Implies(And((nsnt1_x9<N-2*T), Not(nsnt1_y8<N-2*T)), Or((rule18_y8 == 0), (rule18_y8 == 1))))
s.add(Implies(And((nsnt1_x9<N-2*T), Not(nsnt1_y8<N-2*T)), Or((rule19_y8 == 0), (rule19_y8 == 1))))
s.add(Implies(And((nsnt1_x9<N-2*T), Not(nsnt1_y8<N-2*T)), Or((rule20_y8 == 0), (rule20_y8 == 1))))
s.add(Implies(And((nsnt1_x9<N-2*T), Not(nsnt1_y8<N-2*T)), Or((rule21_y8 == 0), (rule21_y8 == 1))))
s.add(Implies(And((nsnt1_x9<N-2*T), Not(nsnt1_y8<N-2*T)), Or((rule22_y8 == 0), (rule22_y8 == 1))))
s.add(Implies(And((nsnt1_x9<N-2*T), Not(nsnt1_y8<N-2*T)), Or((rule23_y8 == 0), (rule23_y8 == 1))))
s.add(Implies(And((nsnt1_x9<N-2*T), Not(nsnt1_y8<N-2*T)), Or((rule24_y8 == 0), (rule24_y8 == 1))))
s.add(Implies(And((nsnt1_x9<N-2*T), Not(nsnt1_y8<N-2*T)), Or((rule25_y8 == 0), (rule25_y8 == 1))))
s.add(Implies(And((nsnt1_x9<N-2*T), Not(nsnt1_y8<N-2*T)), Or((rule26_y8 == 0), (rule26_y8 == 1))))
s.add(Implies(And((nsnt1_x9<N-2*T), Not(nsnt1_y8<N-2*T)), Or((rule27_y8 == 0), (rule27_y8 == 1))))
s.add(Implies(And((nsnt1_x9<N-2*T), Not(nsnt1_y8<N-2*T)), Or((rule28_y8 == 0), (rule28_y8 == 1))))
s.add(Implies(And((nsnt1_x9<N-2*T), Not(nsnt1_y8<N-2*T)), Or((rule29_y8 == 0), (rule29_y8 == 1))))
s.add(Implies(And((nsnt1_x9<N-2*T), Not(nsnt1_y8<N-2*T)), rule0_y8+rule1_y8+rule2_y8+rule3_y8+rule4_y8+rule5_y8+rule6_y8+rule7_y8+rule8_y8+rule9_y8+rule10_y8+rule11_y8+rule12_y8+rule13_y8+rule14_y8+rule15_y8+rule16_y8+rule17_y8+rule18_y8+rule19_y8+rule20_y8+rule21_y8+rule22_y8+rule23_y8+rule24_y8+rule25_y8+rule26_y8+rule27_y8+rule28_y8+rule29_y8 <= 1))

s.add((nfaulty_x9<F) == (nfaulty_y8<F))
s.add(Implies(And((nfaulty_x9<F), Not(nfaulty_y8<F)), Or((rule0_y8 == 0), (rule0_y8 == 1))))
s.add(Implies(And((nfaulty_x9<F), Not(nfaulty_y8<F)), Or((rule1_y8 == 0), (rule1_y8 == 1))))
s.add(Implies(And((nfaulty_x9<F), Not(nfaulty_y8<F)), Or((rule2_y8 == 0), (rule2_y8 == 1))))
s.add(Implies(And((nfaulty_x9<F), Not(nfaulty_y8<F)), Or((rule3_y8 == 0), (rule3_y8 == 1))))
s.add(Implies(And((nfaulty_x9<F), Not(nfaulty_y8<F)), Or((rule4_y8 == 0), (rule4_y8 == 1))))
s.add(Implies(And((nfaulty_x9<F), Not(nfaulty_y8<F)), Or((rule5_y8 == 0), (rule5_y8 == 1))))
s.add(Implies(And((nfaulty_x9<F), Not(nfaulty_y8<F)), Or((rule6_y8 == 0), (rule6_y8 == 1))))
s.add(Implies(And((nfaulty_x9<F), Not(nfaulty_y8<F)), Or((rule7_y8 == 0), (rule7_y8 == 1))))
s.add(Implies(And((nfaulty_x9<F), Not(nfaulty_y8<F)), Or((rule8_y8 == 0), (rule8_y8 == 1))))
s.add(Implies(And((nfaulty_x9<F), Not(nfaulty_y8<F)), Or((rule9_y8 == 0), (rule9_y8 == 1))))
s.add(Implies(And((nfaulty_x9<F), Not(nfaulty_y8<F)), Or((rule10_y8 == 0), (rule10_y8 == 1))))
s.add(Implies(And((nfaulty_x9<F), Not(nfaulty_y8<F)), Or((rule11_y8 == 0), (rule11_y8 == 1))))
s.add(Implies(And((nfaulty_x9<F), Not(nfaulty_y8<F)), Or((rule12_y8 == 0), (rule12_y8 == 1))))
s.add(Implies(And((nfaulty_x9<F), Not(nfaulty_y8<F)), Or((rule13_y8 == 0), (rule13_y8 == 1))))
s.add(Implies(And((nfaulty_x9<F), Not(nfaulty_y8<F)), Or((rule14_y8 == 0), (rule14_y8 == 1))))
s.add(Implies(And((nfaulty_x9<F), Not(nfaulty_y8<F)), Or((rule15_y8 == 0), (rule15_y8 == 1))))
s.add(Implies(And((nfaulty_x9<F), Not(nfaulty_y8<F)), Or((rule16_y8 == 0), (rule16_y8 == 1))))
s.add(Implies(And((nfaulty_x9<F), Not(nfaulty_y8<F)), Or((rule17_y8 == 0), (rule17_y8 == 1))))
s.add(Implies(And((nfaulty_x9<F), Not(nfaulty_y8<F)), Or((rule18_y8 == 0), (rule18_y8 == 1))))
s.add(Implies(And((nfaulty_x9<F), Not(nfaulty_y8<F)), Or((rule19_y8 == 0), (rule19_y8 == 1))))
s.add(Implies(And((nfaulty_x9<F), Not(nfaulty_y8<F)), Or((rule20_y8 == 0), (rule20_y8 == 1))))
s.add(Implies(And((nfaulty_x9<F), Not(nfaulty_y8<F)), Or((rule21_y8 == 0), (rule21_y8 == 1))))
s.add(Implies(And((nfaulty_x9<F), Not(nfaulty_y8<F)), Or((rule22_y8 == 0), (rule22_y8 == 1))))
s.add(Implies(And((nfaulty_x9<F), Not(nfaulty_y8<F)), Or((rule23_y8 == 0), (rule23_y8 == 1))))
s.add(Implies(And((nfaulty_x9<F), Not(nfaulty_y8<F)), Or((rule24_y8 == 0), (rule24_y8 == 1))))
s.add(Implies(And((nfaulty_x9<F), Not(nfaulty_y8<F)), Or((rule25_y8 == 0), (rule25_y8 == 1))))
s.add(Implies(And((nfaulty_x9<F), Not(nfaulty_y8<F)), Or((rule26_y8 == 0), (rule26_y8 == 1))))
s.add(Implies(And((nfaulty_x9<F), Not(nfaulty_y8<F)), Or((rule27_y8 == 0), (rule27_y8 == 1))))
s.add(Implies(And((nfaulty_x9<F), Not(nfaulty_y8<F)), Or((rule28_y8 == 0), (rule28_y8 == 1))))
s.add(Implies(And((nfaulty_x9<F), Not(nfaulty_y8<F)), Or((rule29_y8 == 0), (rule29_y8 == 1))))
s.add(Implies(And((nfaulty_x9<F), Not(nfaulty_y8<F)), rule0_y8+rule1_y8+rule2_y8+rule3_y8+rule4_y8+rule5_y8+rule6_y8+rule7_y8+rule8_y8+rule9_y8+rule10_y8+rule11_y8+rule12_y8+rule13_y8+rule14_y8+rule15_y8+rule16_y8+rule17_y8+rule18_y8+rule19_y8+rule20_y8+rule21_y8+rule22_y8+rule23_y8+rule24_y8+rule25_y8+rule26_y8+rule27_y8+rule28_y8+rule29_y8 <= 1))

s.add((nsnt0_x9<N-2*T) == (nsnt0_y8<N-2*T))
s.add(Implies(And((nsnt0_x9<N-2*T), Not(nsnt0_y8<N-2*T)), Or((rule0_y8 == 0), (rule0_y8 == 1))))
s.add(Implies(And((nsnt0_x9<N-2*T), Not(nsnt0_y8<N-2*T)), Or((rule1_y8 == 0), (rule1_y8 == 1))))
s.add(Implies(And((nsnt0_x9<N-2*T), Not(nsnt0_y8<N-2*T)), Or((rule2_y8 == 0), (rule2_y8 == 1))))
s.add(Implies(And((nsnt0_x9<N-2*T), Not(nsnt0_y8<N-2*T)), Or((rule3_y8 == 0), (rule3_y8 == 1))))
s.add(Implies(And((nsnt0_x9<N-2*T), Not(nsnt0_y8<N-2*T)), Or((rule4_y8 == 0), (rule4_y8 == 1))))
s.add(Implies(And((nsnt0_x9<N-2*T), Not(nsnt0_y8<N-2*T)), Or((rule5_y8 == 0), (rule5_y8 == 1))))
s.add(Implies(And((nsnt0_x9<N-2*T), Not(nsnt0_y8<N-2*T)), Or((rule6_y8 == 0), (rule6_y8 == 1))))
s.add(Implies(And((nsnt0_x9<N-2*T), Not(nsnt0_y8<N-2*T)), Or((rule7_y8 == 0), (rule7_y8 == 1))))
s.add(Implies(And((nsnt0_x9<N-2*T), Not(nsnt0_y8<N-2*T)), Or((rule8_y8 == 0), (rule8_y8 == 1))))
s.add(Implies(And((nsnt0_x9<N-2*T), Not(nsnt0_y8<N-2*T)), Or((rule9_y8 == 0), (rule9_y8 == 1))))
s.add(Implies(And((nsnt0_x9<N-2*T), Not(nsnt0_y8<N-2*T)), Or((rule10_y8 == 0), (rule10_y8 == 1))))
s.add(Implies(And((nsnt0_x9<N-2*T), Not(nsnt0_y8<N-2*T)), Or((rule11_y8 == 0), (rule11_y8 == 1))))
s.add(Implies(And((nsnt0_x9<N-2*T), Not(nsnt0_y8<N-2*T)), Or((rule12_y8 == 0), (rule12_y8 == 1))))
s.add(Implies(And((nsnt0_x9<N-2*T), Not(nsnt0_y8<N-2*T)), Or((rule13_y8 == 0), (rule13_y8 == 1))))
s.add(Implies(And((nsnt0_x9<N-2*T), Not(nsnt0_y8<N-2*T)), Or((rule14_y8 == 0), (rule14_y8 == 1))))
s.add(Implies(And((nsnt0_x9<N-2*T), Not(nsnt0_y8<N-2*T)), Or((rule15_y8 == 0), (rule15_y8 == 1))))
s.add(Implies(And((nsnt0_x9<N-2*T), Not(nsnt0_y8<N-2*T)), Or((rule16_y8 == 0), (rule16_y8 == 1))))
s.add(Implies(And((nsnt0_x9<N-2*T), Not(nsnt0_y8<N-2*T)), Or((rule17_y8 == 0), (rule17_y8 == 1))))
s.add(Implies(And((nsnt0_x9<N-2*T), Not(nsnt0_y8<N-2*T)), Or((rule18_y8 == 0), (rule18_y8 == 1))))
s.add(Implies(And((nsnt0_x9<N-2*T), Not(nsnt0_y8<N-2*T)), Or((rule19_y8 == 0), (rule19_y8 == 1))))
s.add(Implies(And((nsnt0_x9<N-2*T), Not(nsnt0_y8<N-2*T)), Or((rule20_y8 == 0), (rule20_y8 == 1))))
s.add(Implies(And((nsnt0_x9<N-2*T), Not(nsnt0_y8<N-2*T)), Or((rule21_y8 == 0), (rule21_y8 == 1))))
s.add(Implies(And((nsnt0_x9<N-2*T), Not(nsnt0_y8<N-2*T)), Or((rule22_y8 == 0), (rule22_y8 == 1))))
s.add(Implies(And((nsnt0_x9<N-2*T), Not(nsnt0_y8<N-2*T)), Or((rule23_y8 == 0), (rule23_y8 == 1))))
s.add(Implies(And((nsnt0_x9<N-2*T), Not(nsnt0_y8<N-2*T)), Or((rule24_y8 == 0), (rule24_y8 == 1))))
s.add(Implies(And((nsnt0_x9<N-2*T), Not(nsnt0_y8<N-2*T)), Or((rule25_y8 == 0), (rule25_y8 == 1))))
s.add(Implies(And((nsnt0_x9<N-2*T), Not(nsnt0_y8<N-2*T)), Or((rule26_y8 == 0), (rule26_y8 == 1))))
s.add(Implies(And((nsnt0_x9<N-2*T), Not(nsnt0_y8<N-2*T)), Or((rule27_y8 == 0), (rule27_y8 == 1))))
s.add(Implies(And((nsnt0_x9<N-2*T), Not(nsnt0_y8<N-2*T)), Or((rule28_y8 == 0), (rule28_y8 == 1))))
s.add(Implies(And((nsnt0_x9<N-2*T), Not(nsnt0_y8<N-2*T)), Or((rule29_y8 == 0), (rule29_y8 == 1))))
s.add(Implies(And((nsnt0_x9<N-2*T), Not(nsnt0_y8<N-2*T)), rule0_y8+rule1_y8+rule2_y8+rule3_y8+rule4_y8+rule5_y8+rule6_y8+rule7_y8+rule8_y8+rule9_y8+rule10_y8+rule11_y8+rule12_y8+rule13_y8+rule14_y8+rule15_y8+rule16_y8+rule17_y8+rule18_y8+rule19_y8+rule20_y8+rule21_y8+rule22_y8+rule23_y8+rule24_y8+rule25_y8+rule26_y8+rule27_y8+rule28_y8+rule29_y8 <= 1))


####################################################################################

#Creating constraints for a run between the y9th and x10th configurations

################Step 1#################


#Creating many copies of variables for rules

rule0_y9 = Real('rule0_y9')
s.add(rule0_y9 >= 0)
rule1_y9 = Real('rule1_y9')
s.add(rule1_y9 >= 0)
rule2_y9 = Real('rule2_y9')
s.add(rule2_y9 >= 0)
rule3_y9 = Real('rule3_y9')
s.add(rule3_y9 >= 0)
rule4_y9 = Real('rule4_y9')
s.add(rule4_y9 >= 0)
rule5_y9 = Real('rule5_y9')
s.add(rule5_y9 >= 0)
rule6_y9 = Real('rule6_y9')
s.add(rule6_y9 >= 0)
rule7_y9 = Real('rule7_y9')
s.add(rule7_y9 >= 0)
rule8_y9 = Real('rule8_y9')
s.add(rule8_y9 >= 0)
rule9_y9 = Real('rule9_y9')
s.add(rule9_y9 >= 0)
rule10_y9 = Real('rule10_y9')
s.add(rule10_y9 >= 0)
rule11_y9 = Real('rule11_y9')
s.add(rule11_y9 >= 0)
rule12_y9 = Real('rule12_y9')
s.add(rule12_y9 >= 0)
rule13_y9 = Real('rule13_y9')
s.add(rule13_y9 >= 0)
rule14_y9 = Real('rule14_y9')
s.add(rule14_y9 >= 0)
rule15_y9 = Real('rule15_y9')
s.add(rule15_y9 >= 0)
rule16_y9 = Real('rule16_y9')
s.add(rule16_y9 >= 0)
rule17_y9 = Real('rule17_y9')
s.add(rule17_y9 >= 0)
rule18_y9 = Real('rule18_y9')
s.add(rule18_y9 >= 0)
rule19_y9 = Real('rule19_y9')
s.add(rule19_y9 >= 0)
rule20_y9 = Real('rule20_y9')
s.add(rule20_y9 >= 0)
rule21_y9 = Real('rule21_y9')
s.add(rule21_y9 >= 0)
rule22_y9 = Real('rule22_y9')
s.add(rule22_y9 >= 0)
rule23_y9 = Real('rule23_y9')
s.add(rule23_y9 >= 0)
rule24_y9 = Real('rule24_y9')
s.add(rule24_y9 >= 0)
rule25_y9 = Real('rule25_y9')
s.add(rule25_y9 >= 0)
rule26_y9 = Real('rule26_y9')
s.add(rule26_y9 >= 0)
rule27_y9 = Real('rule27_y9')
s.add(rule27_y9 >= 0)
rule28_y9 = Real('rule28_y9')
s.add(rule28_y9 >= 0)
rule29_y9 = Real('rule29_y9')
s.add(rule29_y9 >= 0)






###################Step 2####################


#Flow equations for the locations

s.add(0 - rule0_y9 - rule1_y9 - rule14_y9 - rule22_y9 + rule22_y9 ==  loc0_x10 - loc0_y9)
s.add(0 - rule2_y9 - rule3_y9 - rule15_y9 - rule23_y9 + rule23_y9 ==  loc1_x10 - loc1_y9)
s.add(0 + rule0_y9 - rule4_y9 - rule6_y9 - rule8_y9 - rule10_y9 - rule12_y9 - rule16_y9 - rule24_y9 + rule24_y9 ==  locS0_x10 - locS0_y9)
s.add(0 + rule2_y9 - rule5_y9 - rule7_y9 - rule9_y9 - rule11_y9 - rule13_y9 - rule17_y9 - rule25_y9 + rule25_y9 ==  locS1_x10 - locS1_y9)
s.add(0 + rule4_y9 + rule5_y9 - rule18_y9 - rule26_y9 + rule26_y9 ==  locD0_x10 - locD0_y9)
s.add(0 + rule6_y9 + rule7_y9 - rule19_y9 - rule27_y9 + rule27_y9 ==  locD1_x10 - locD1_y9)
s.add(0 + rule8_y9 + rule9_y9 + rule12_y9 - rule20_y9 - rule28_y9 + rule28_y9 ==  locU0_x10 - locU0_y9)
s.add(0 + rule10_y9 + rule11_y9 + rule13_y9 - rule21_y9 - rule29_y9 + rule29_y9 ==  locU1_x10 - locU1_y9)
s.add(0 + rule1_y9 + rule3_y9 + rule14_y9 + rule15_y9 + rule16_y9 + rule17_y9 + rule18_y9 + rule19_y9 + rule20_y9 + rule21_y9 ==  locCR_x10 - locCR_y9)






##################Step 3########################


#Flow equations for the shared variables

s.add(0 + rule0_y9 == nsnt0_x10 - nsnt0_y9)
s.add(0 + rule2_y9 == nsnt1_x10 - nsnt1_y9)
s.add(0 + rule0_y9 + rule1_y9 == nsnt0CF_x10 - nsnt0CF_y9)
s.add(0 + rule2_y9 + rule3_y9 == nsnt1CF_x10 - nsnt1CF_y9)
s.add(0 + rule0_y9 + rule2_y9 == nsnt01_x10 - nsnt01_y9)
s.add(0 + rule0_y9 + rule1_y9 + rule2_y9 + rule3_y9 == nsnt01CF_x10 - nsnt01CF_y9)
s.add(0 + rule1_y9 + rule3_y9 + rule14_y9 + rule15_y9 + rule16_y9 + rule17_y9 + rule18_y9 + rule19_y9 + rule20_y9 + rule21_y9 == nfaulty_x10 - nfaulty_y9)






####################Step 4########################


#Rule is fired implies rule is enabled

s.add(Implies( (rule0_y9 > 0), And(True, ) ))
s.add(Implies( (rule1_y9 > 0), And(nfaulty_y9<F, ) ))
s.add(Implies( (rule2_y9 > 0), And(True, ) ))
s.add(Implies( (rule3_y9 > 0), And(nfaulty_y9<F, ) ))
s.add(Implies( (rule4_y9 > 0), And(nsnt0CF_y9>=N-T, ) ))
s.add(Implies( (rule5_y9 > 0), And(nsnt0CF_y9>=N-T, ) ))
s.add(Implies( (rule6_y9 > 0), And(nsnt1CF_y9>=N-T, ) ))
s.add(Implies( (rule7_y9 > 0), And(nsnt1CF_y9>=N-T, ) ))
s.add(Implies( (rule8_y9 > 0), And(nsnt01CF_y9>=N-T, nsnt0CF_y9>=N-2*T, nsnt1CF_y9>=1, ) ))
s.add(Implies( (rule9_y9 > 0), And(nsnt01CF_y9>=N-T, nsnt0CF_y9>=N-2*T, nsnt1CF_y9>=1, ) ))
s.add(Implies( (rule10_y9 > 0), And(nsnt01CF_y9>=N-T, nsnt1CF_y9>=N-2*T, nsnt0CF_y9>=1, ) ))
s.add(Implies( (rule11_y9 > 0), And(nsnt01CF_y9>=N-T, nsnt1CF_y9>=N-2*T, nsnt0CF_y9>=1, ) ))
s.add(Implies( (rule12_y9 > 0), And(nsnt01CF_y9>=N-T, nsnt0_y9<N-2*T, nsnt1_y9<N-2*T, ) ))
s.add(Implies( (rule13_y9 > 0), And(nsnt01CF_y9>=N-T, nsnt0_y9<N-2*T, nsnt1_y9<N-2*T, ) ))
s.add(Implies( (rule14_y9 > 0), And(nfaulty_y9<F, ) ))
s.add(Implies( (rule15_y9 > 0), And(nfaulty_y9<F, ) ))
s.add(Implies( (rule16_y9 > 0), And(nfaulty_y9<F, ) ))
s.add(Implies( (rule17_y9 > 0), And(nfaulty_y9<F, ) ))
s.add(Implies( (rule18_y9 > 0), And(nfaulty_y9<F, ) ))
s.add(Implies( (rule19_y9 > 0), And(nfaulty_y9<F, ) ))
s.add(Implies( (rule20_y9 > 0), And(nfaulty_y9<F, ) ))
s.add(Implies( (rule21_y9 > 0), And(nfaulty_y9<F, ) ))
s.add(Implies( (rule22_y9 > 0), And(True, ) ))
s.add(Implies( (rule23_y9 > 0), And(True, ) ))
s.add(Implies( (rule24_y9 > 0), And(True, ) ))
s.add(Implies( (rule25_y9 > 0), And(True, ) ))
s.add(Implies( (rule26_y9 > 0), And(True, ) ))
s.add(Implies( (rule27_y9 > 0), And(True, ) ))
s.add(Implies( (rule28_y9 > 0), And(True, ) ))
s.add(Implies( (rule29_y9 > 0), And(True, ) ))

##################Step 5########################


#Ensuring that at most one rule is fired alternating configurations y9 and x9, if a fall condition is present

s.add((nsnt1_x10<N-2*T) == (nsnt1_y9<N-2*T))
s.add(Implies(And((nsnt1_x10<N-2*T), Not(nsnt1_y9<N-2*T)), Or((rule0_y9 == 0), (rule0_y9 == 1))))
s.add(Implies(And((nsnt1_x10<N-2*T), Not(nsnt1_y9<N-2*T)), Or((rule1_y9 == 0), (rule1_y9 == 1))))
s.add(Implies(And((nsnt1_x10<N-2*T), Not(nsnt1_y9<N-2*T)), Or((rule2_y9 == 0), (rule2_y9 == 1))))
s.add(Implies(And((nsnt1_x10<N-2*T), Not(nsnt1_y9<N-2*T)), Or((rule3_y9 == 0), (rule3_y9 == 1))))
s.add(Implies(And((nsnt1_x10<N-2*T), Not(nsnt1_y9<N-2*T)), Or((rule4_y9 == 0), (rule4_y9 == 1))))
s.add(Implies(And((nsnt1_x10<N-2*T), Not(nsnt1_y9<N-2*T)), Or((rule5_y9 == 0), (rule5_y9 == 1))))
s.add(Implies(And((nsnt1_x10<N-2*T), Not(nsnt1_y9<N-2*T)), Or((rule6_y9 == 0), (rule6_y9 == 1))))
s.add(Implies(And((nsnt1_x10<N-2*T), Not(nsnt1_y9<N-2*T)), Or((rule7_y9 == 0), (rule7_y9 == 1))))
s.add(Implies(And((nsnt1_x10<N-2*T), Not(nsnt1_y9<N-2*T)), Or((rule8_y9 == 0), (rule8_y9 == 1))))
s.add(Implies(And((nsnt1_x10<N-2*T), Not(nsnt1_y9<N-2*T)), Or((rule9_y9 == 0), (rule9_y9 == 1))))
s.add(Implies(And((nsnt1_x10<N-2*T), Not(nsnt1_y9<N-2*T)), Or((rule10_y9 == 0), (rule10_y9 == 1))))
s.add(Implies(And((nsnt1_x10<N-2*T), Not(nsnt1_y9<N-2*T)), Or((rule11_y9 == 0), (rule11_y9 == 1))))
s.add(Implies(And((nsnt1_x10<N-2*T), Not(nsnt1_y9<N-2*T)), Or((rule12_y9 == 0), (rule12_y9 == 1))))
s.add(Implies(And((nsnt1_x10<N-2*T), Not(nsnt1_y9<N-2*T)), Or((rule13_y9 == 0), (rule13_y9 == 1))))
s.add(Implies(And((nsnt1_x10<N-2*T), Not(nsnt1_y9<N-2*T)), Or((rule14_y9 == 0), (rule14_y9 == 1))))
s.add(Implies(And((nsnt1_x10<N-2*T), Not(nsnt1_y9<N-2*T)), Or((rule15_y9 == 0), (rule15_y9 == 1))))
s.add(Implies(And((nsnt1_x10<N-2*T), Not(nsnt1_y9<N-2*T)), Or((rule16_y9 == 0), (rule16_y9 == 1))))
s.add(Implies(And((nsnt1_x10<N-2*T), Not(nsnt1_y9<N-2*T)), Or((rule17_y9 == 0), (rule17_y9 == 1))))
s.add(Implies(And((nsnt1_x10<N-2*T), Not(nsnt1_y9<N-2*T)), Or((rule18_y9 == 0), (rule18_y9 == 1))))
s.add(Implies(And((nsnt1_x10<N-2*T), Not(nsnt1_y9<N-2*T)), Or((rule19_y9 == 0), (rule19_y9 == 1))))
s.add(Implies(And((nsnt1_x10<N-2*T), Not(nsnt1_y9<N-2*T)), Or((rule20_y9 == 0), (rule20_y9 == 1))))
s.add(Implies(And((nsnt1_x10<N-2*T), Not(nsnt1_y9<N-2*T)), Or((rule21_y9 == 0), (rule21_y9 == 1))))
s.add(Implies(And((nsnt1_x10<N-2*T), Not(nsnt1_y9<N-2*T)), Or((rule22_y9 == 0), (rule22_y9 == 1))))
s.add(Implies(And((nsnt1_x10<N-2*T), Not(nsnt1_y9<N-2*T)), Or((rule23_y9 == 0), (rule23_y9 == 1))))
s.add(Implies(And((nsnt1_x10<N-2*T), Not(nsnt1_y9<N-2*T)), Or((rule24_y9 == 0), (rule24_y9 == 1))))
s.add(Implies(And((nsnt1_x10<N-2*T), Not(nsnt1_y9<N-2*T)), Or((rule25_y9 == 0), (rule25_y9 == 1))))
s.add(Implies(And((nsnt1_x10<N-2*T), Not(nsnt1_y9<N-2*T)), Or((rule26_y9 == 0), (rule26_y9 == 1))))
s.add(Implies(And((nsnt1_x10<N-2*T), Not(nsnt1_y9<N-2*T)), Or((rule27_y9 == 0), (rule27_y9 == 1))))
s.add(Implies(And((nsnt1_x10<N-2*T), Not(nsnt1_y9<N-2*T)), Or((rule28_y9 == 0), (rule28_y9 == 1))))
s.add(Implies(And((nsnt1_x10<N-2*T), Not(nsnt1_y9<N-2*T)), Or((rule29_y9 == 0), (rule29_y9 == 1))))
s.add(Implies(And((nsnt1_x10<N-2*T), Not(nsnt1_y9<N-2*T)), rule0_y9+rule1_y9+rule2_y9+rule3_y9+rule4_y9+rule5_y9+rule6_y9+rule7_y9+rule8_y9+rule9_y9+rule10_y9+rule11_y9+rule12_y9+rule13_y9+rule14_y9+rule15_y9+rule16_y9+rule17_y9+rule18_y9+rule19_y9+rule20_y9+rule21_y9+rule22_y9+rule23_y9+rule24_y9+rule25_y9+rule26_y9+rule27_y9+rule28_y9+rule29_y9 <= 1))

s.add((nfaulty_x10<F) == (nfaulty_y9<F))
s.add(Implies(And((nfaulty_x10<F), Not(nfaulty_y9<F)), Or((rule0_y9 == 0), (rule0_y9 == 1))))
s.add(Implies(And((nfaulty_x10<F), Not(nfaulty_y9<F)), Or((rule1_y9 == 0), (rule1_y9 == 1))))
s.add(Implies(And((nfaulty_x10<F), Not(nfaulty_y9<F)), Or((rule2_y9 == 0), (rule2_y9 == 1))))
s.add(Implies(And((nfaulty_x10<F), Not(nfaulty_y9<F)), Or((rule3_y9 == 0), (rule3_y9 == 1))))
s.add(Implies(And((nfaulty_x10<F), Not(nfaulty_y9<F)), Or((rule4_y9 == 0), (rule4_y9 == 1))))
s.add(Implies(And((nfaulty_x10<F), Not(nfaulty_y9<F)), Or((rule5_y9 == 0), (rule5_y9 == 1))))
s.add(Implies(And((nfaulty_x10<F), Not(nfaulty_y9<F)), Or((rule6_y9 == 0), (rule6_y9 == 1))))
s.add(Implies(And((nfaulty_x10<F), Not(nfaulty_y9<F)), Or((rule7_y9 == 0), (rule7_y9 == 1))))
s.add(Implies(And((nfaulty_x10<F), Not(nfaulty_y9<F)), Or((rule8_y9 == 0), (rule8_y9 == 1))))
s.add(Implies(And((nfaulty_x10<F), Not(nfaulty_y9<F)), Or((rule9_y9 == 0), (rule9_y9 == 1))))
s.add(Implies(And((nfaulty_x10<F), Not(nfaulty_y9<F)), Or((rule10_y9 == 0), (rule10_y9 == 1))))
s.add(Implies(And((nfaulty_x10<F), Not(nfaulty_y9<F)), Or((rule11_y9 == 0), (rule11_y9 == 1))))
s.add(Implies(And((nfaulty_x10<F), Not(nfaulty_y9<F)), Or((rule12_y9 == 0), (rule12_y9 == 1))))
s.add(Implies(And((nfaulty_x10<F), Not(nfaulty_y9<F)), Or((rule13_y9 == 0), (rule13_y9 == 1))))
s.add(Implies(And((nfaulty_x10<F), Not(nfaulty_y9<F)), Or((rule14_y9 == 0), (rule14_y9 == 1))))
s.add(Implies(And((nfaulty_x10<F), Not(nfaulty_y9<F)), Or((rule15_y9 == 0), (rule15_y9 == 1))))
s.add(Implies(And((nfaulty_x10<F), Not(nfaulty_y9<F)), Or((rule16_y9 == 0), (rule16_y9 == 1))))
s.add(Implies(And((nfaulty_x10<F), Not(nfaulty_y9<F)), Or((rule17_y9 == 0), (rule17_y9 == 1))))
s.add(Implies(And((nfaulty_x10<F), Not(nfaulty_y9<F)), Or((rule18_y9 == 0), (rule18_y9 == 1))))
s.add(Implies(And((nfaulty_x10<F), Not(nfaulty_y9<F)), Or((rule19_y9 == 0), (rule19_y9 == 1))))
s.add(Implies(And((nfaulty_x10<F), Not(nfaulty_y9<F)), Or((rule20_y9 == 0), (rule20_y9 == 1))))
s.add(Implies(And((nfaulty_x10<F), Not(nfaulty_y9<F)), Or((rule21_y9 == 0), (rule21_y9 == 1))))
s.add(Implies(And((nfaulty_x10<F), Not(nfaulty_y9<F)), Or((rule22_y9 == 0), (rule22_y9 == 1))))
s.add(Implies(And((nfaulty_x10<F), Not(nfaulty_y9<F)), Or((rule23_y9 == 0), (rule23_y9 == 1))))
s.add(Implies(And((nfaulty_x10<F), Not(nfaulty_y9<F)), Or((rule24_y9 == 0), (rule24_y9 == 1))))
s.add(Implies(And((nfaulty_x10<F), Not(nfaulty_y9<F)), Or((rule25_y9 == 0), (rule25_y9 == 1))))
s.add(Implies(And((nfaulty_x10<F), Not(nfaulty_y9<F)), Or((rule26_y9 == 0), (rule26_y9 == 1))))
s.add(Implies(And((nfaulty_x10<F), Not(nfaulty_y9<F)), Or((rule27_y9 == 0), (rule27_y9 == 1))))
s.add(Implies(And((nfaulty_x10<F), Not(nfaulty_y9<F)), Or((rule28_y9 == 0), (rule28_y9 == 1))))
s.add(Implies(And((nfaulty_x10<F), Not(nfaulty_y9<F)), Or((rule29_y9 == 0), (rule29_y9 == 1))))
s.add(Implies(And((nfaulty_x10<F), Not(nfaulty_y9<F)), rule0_y9+rule1_y9+rule2_y9+rule3_y9+rule4_y9+rule5_y9+rule6_y9+rule7_y9+rule8_y9+rule9_y9+rule10_y9+rule11_y9+rule12_y9+rule13_y9+rule14_y9+rule15_y9+rule16_y9+rule17_y9+rule18_y9+rule19_y9+rule20_y9+rule21_y9+rule22_y9+rule23_y9+rule24_y9+rule25_y9+rule26_y9+rule27_y9+rule28_y9+rule29_y9 <= 1))

s.add((nsnt0_x10<N-2*T) == (nsnt0_y9<N-2*T))
s.add(Implies(And((nsnt0_x10<N-2*T), Not(nsnt0_y9<N-2*T)), Or((rule0_y9 == 0), (rule0_y9 == 1))))
s.add(Implies(And((nsnt0_x10<N-2*T), Not(nsnt0_y9<N-2*T)), Or((rule1_y9 == 0), (rule1_y9 == 1))))
s.add(Implies(And((nsnt0_x10<N-2*T), Not(nsnt0_y9<N-2*T)), Or((rule2_y9 == 0), (rule2_y9 == 1))))
s.add(Implies(And((nsnt0_x10<N-2*T), Not(nsnt0_y9<N-2*T)), Or((rule3_y9 == 0), (rule3_y9 == 1))))
s.add(Implies(And((nsnt0_x10<N-2*T), Not(nsnt0_y9<N-2*T)), Or((rule4_y9 == 0), (rule4_y9 == 1))))
s.add(Implies(And((nsnt0_x10<N-2*T), Not(nsnt0_y9<N-2*T)), Or((rule5_y9 == 0), (rule5_y9 == 1))))
s.add(Implies(And((nsnt0_x10<N-2*T), Not(nsnt0_y9<N-2*T)), Or((rule6_y9 == 0), (rule6_y9 == 1))))
s.add(Implies(And((nsnt0_x10<N-2*T), Not(nsnt0_y9<N-2*T)), Or((rule7_y9 == 0), (rule7_y9 == 1))))
s.add(Implies(And((nsnt0_x10<N-2*T), Not(nsnt0_y9<N-2*T)), Or((rule8_y9 == 0), (rule8_y9 == 1))))
s.add(Implies(And((nsnt0_x10<N-2*T), Not(nsnt0_y9<N-2*T)), Or((rule9_y9 == 0), (rule9_y9 == 1))))
s.add(Implies(And((nsnt0_x10<N-2*T), Not(nsnt0_y9<N-2*T)), Or((rule10_y9 == 0), (rule10_y9 == 1))))
s.add(Implies(And((nsnt0_x10<N-2*T), Not(nsnt0_y9<N-2*T)), Or((rule11_y9 == 0), (rule11_y9 == 1))))
s.add(Implies(And((nsnt0_x10<N-2*T), Not(nsnt0_y9<N-2*T)), Or((rule12_y9 == 0), (rule12_y9 == 1))))
s.add(Implies(And((nsnt0_x10<N-2*T), Not(nsnt0_y9<N-2*T)), Or((rule13_y9 == 0), (rule13_y9 == 1))))
s.add(Implies(And((nsnt0_x10<N-2*T), Not(nsnt0_y9<N-2*T)), Or((rule14_y9 == 0), (rule14_y9 == 1))))
s.add(Implies(And((nsnt0_x10<N-2*T), Not(nsnt0_y9<N-2*T)), Or((rule15_y9 == 0), (rule15_y9 == 1))))
s.add(Implies(And((nsnt0_x10<N-2*T), Not(nsnt0_y9<N-2*T)), Or((rule16_y9 == 0), (rule16_y9 == 1))))
s.add(Implies(And((nsnt0_x10<N-2*T), Not(nsnt0_y9<N-2*T)), Or((rule17_y9 == 0), (rule17_y9 == 1))))
s.add(Implies(And((nsnt0_x10<N-2*T), Not(nsnt0_y9<N-2*T)), Or((rule18_y9 == 0), (rule18_y9 == 1))))
s.add(Implies(And((nsnt0_x10<N-2*T), Not(nsnt0_y9<N-2*T)), Or((rule19_y9 == 0), (rule19_y9 == 1))))
s.add(Implies(And((nsnt0_x10<N-2*T), Not(nsnt0_y9<N-2*T)), Or((rule20_y9 == 0), (rule20_y9 == 1))))
s.add(Implies(And((nsnt0_x10<N-2*T), Not(nsnt0_y9<N-2*T)), Or((rule21_y9 == 0), (rule21_y9 == 1))))
s.add(Implies(And((nsnt0_x10<N-2*T), Not(nsnt0_y9<N-2*T)), Or((rule22_y9 == 0), (rule22_y9 == 1))))
s.add(Implies(And((nsnt0_x10<N-2*T), Not(nsnt0_y9<N-2*T)), Or((rule23_y9 == 0), (rule23_y9 == 1))))
s.add(Implies(And((nsnt0_x10<N-2*T), Not(nsnt0_y9<N-2*T)), Or((rule24_y9 == 0), (rule24_y9 == 1))))
s.add(Implies(And((nsnt0_x10<N-2*T), Not(nsnt0_y9<N-2*T)), Or((rule25_y9 == 0), (rule25_y9 == 1))))
s.add(Implies(And((nsnt0_x10<N-2*T), Not(nsnt0_y9<N-2*T)), Or((rule26_y9 == 0), (rule26_y9 == 1))))
s.add(Implies(And((nsnt0_x10<N-2*T), Not(nsnt0_y9<N-2*T)), Or((rule27_y9 == 0), (rule27_y9 == 1))))
s.add(Implies(And((nsnt0_x10<N-2*T), Not(nsnt0_y9<N-2*T)), Or((rule28_y9 == 0), (rule28_y9 == 1))))
s.add(Implies(And((nsnt0_x10<N-2*T), Not(nsnt0_y9<N-2*T)), Or((rule29_y9 == 0), (rule29_y9 == 1))))
s.add(Implies(And((nsnt0_x10<N-2*T), Not(nsnt0_y9<N-2*T)), rule0_y9+rule1_y9+rule2_y9+rule3_y9+rule4_y9+rule5_y9+rule6_y9+rule7_y9+rule8_y9+rule9_y9+rule10_y9+rule11_y9+rule12_y9+rule13_y9+rule14_y9+rule15_y9+rule16_y9+rule17_y9+rule18_y9+rule19_y9+rule20_y9+rule21_y9+rule22_y9+rule23_y9+rule24_y9+rule25_y9+rule26_y9+rule27_y9+rule28_y9+rule29_y9 <= 1))


####################################################################################

#Creating constraints for a run between the y10th and x11th configurations

################Step 1#################


#Creating many copies of variables for rules

rule0_y10 = Real('rule0_y10')
s.add(rule0_y10 >= 0)
rule1_y10 = Real('rule1_y10')
s.add(rule1_y10 >= 0)
rule2_y10 = Real('rule2_y10')
s.add(rule2_y10 >= 0)
rule3_y10 = Real('rule3_y10')
s.add(rule3_y10 >= 0)
rule4_y10 = Real('rule4_y10')
s.add(rule4_y10 >= 0)
rule5_y10 = Real('rule5_y10')
s.add(rule5_y10 >= 0)
rule6_y10 = Real('rule6_y10')
s.add(rule6_y10 >= 0)
rule7_y10 = Real('rule7_y10')
s.add(rule7_y10 >= 0)
rule8_y10 = Real('rule8_y10')
s.add(rule8_y10 >= 0)
rule9_y10 = Real('rule9_y10')
s.add(rule9_y10 >= 0)
rule10_y10 = Real('rule10_y10')
s.add(rule10_y10 >= 0)
rule11_y10 = Real('rule11_y10')
s.add(rule11_y10 >= 0)
rule12_y10 = Real('rule12_y10')
s.add(rule12_y10 >= 0)
rule13_y10 = Real('rule13_y10')
s.add(rule13_y10 >= 0)
rule14_y10 = Real('rule14_y10')
s.add(rule14_y10 >= 0)
rule15_y10 = Real('rule15_y10')
s.add(rule15_y10 >= 0)
rule16_y10 = Real('rule16_y10')
s.add(rule16_y10 >= 0)
rule17_y10 = Real('rule17_y10')
s.add(rule17_y10 >= 0)
rule18_y10 = Real('rule18_y10')
s.add(rule18_y10 >= 0)
rule19_y10 = Real('rule19_y10')
s.add(rule19_y10 >= 0)
rule20_y10 = Real('rule20_y10')
s.add(rule20_y10 >= 0)
rule21_y10 = Real('rule21_y10')
s.add(rule21_y10 >= 0)
rule22_y10 = Real('rule22_y10')
s.add(rule22_y10 >= 0)
rule23_y10 = Real('rule23_y10')
s.add(rule23_y10 >= 0)
rule24_y10 = Real('rule24_y10')
s.add(rule24_y10 >= 0)
rule25_y10 = Real('rule25_y10')
s.add(rule25_y10 >= 0)
rule26_y10 = Real('rule26_y10')
s.add(rule26_y10 >= 0)
rule27_y10 = Real('rule27_y10')
s.add(rule27_y10 >= 0)
rule28_y10 = Real('rule28_y10')
s.add(rule28_y10 >= 0)
rule29_y10 = Real('rule29_y10')
s.add(rule29_y10 >= 0)






###################Step 2####################


#Flow equations for the locations

s.add(0 - rule0_y10 - rule1_y10 - rule14_y10 - rule22_y10 + rule22_y10 ==  loc0_x11 - loc0_y10)
s.add(0 - rule2_y10 - rule3_y10 - rule15_y10 - rule23_y10 + rule23_y10 ==  loc1_x11 - loc1_y10)
s.add(0 + rule0_y10 - rule4_y10 - rule6_y10 - rule8_y10 - rule10_y10 - rule12_y10 - rule16_y10 - rule24_y10 + rule24_y10 ==  locS0_x11 - locS0_y10)
s.add(0 + rule2_y10 - rule5_y10 - rule7_y10 - rule9_y10 - rule11_y10 - rule13_y10 - rule17_y10 - rule25_y10 + rule25_y10 ==  locS1_x11 - locS1_y10)
s.add(0 + rule4_y10 + rule5_y10 - rule18_y10 - rule26_y10 + rule26_y10 ==  locD0_x11 - locD0_y10)
s.add(0 + rule6_y10 + rule7_y10 - rule19_y10 - rule27_y10 + rule27_y10 ==  locD1_x11 - locD1_y10)
s.add(0 + rule8_y10 + rule9_y10 + rule12_y10 - rule20_y10 - rule28_y10 + rule28_y10 ==  locU0_x11 - locU0_y10)
s.add(0 + rule10_y10 + rule11_y10 + rule13_y10 - rule21_y10 - rule29_y10 + rule29_y10 ==  locU1_x11 - locU1_y10)
s.add(0 + rule1_y10 + rule3_y10 + rule14_y10 + rule15_y10 + rule16_y10 + rule17_y10 + rule18_y10 + rule19_y10 + rule20_y10 + rule21_y10 ==  locCR_x11 - locCR_y10)






##################Step 3########################


#Flow equations for the shared variables

s.add(0 + rule0_y10 == nsnt0_x11 - nsnt0_y10)
s.add(0 + rule2_y10 == nsnt1_x11 - nsnt1_y10)
s.add(0 + rule0_y10 + rule1_y10 == nsnt0CF_x11 - nsnt0CF_y10)
s.add(0 + rule2_y10 + rule3_y10 == nsnt1CF_x11 - nsnt1CF_y10)
s.add(0 + rule0_y10 + rule2_y10 == nsnt01_x11 - nsnt01_y10)
s.add(0 + rule0_y10 + rule1_y10 + rule2_y10 + rule3_y10 == nsnt01CF_x11 - nsnt01CF_y10)
s.add(0 + rule1_y10 + rule3_y10 + rule14_y10 + rule15_y10 + rule16_y10 + rule17_y10 + rule18_y10 + rule19_y10 + rule20_y10 + rule21_y10 == nfaulty_x11 - nfaulty_y10)






####################Step 4########################


#Rule is fired implies rule is enabled

s.add(Implies( (rule0_y10 > 0), And(True, ) ))
s.add(Implies( (rule1_y10 > 0), And(nfaulty_y10<F, ) ))
s.add(Implies( (rule2_y10 > 0), And(True, ) ))
s.add(Implies( (rule3_y10 > 0), And(nfaulty_y10<F, ) ))
s.add(Implies( (rule4_y10 > 0), And(nsnt0CF_y10>=N-T, ) ))
s.add(Implies( (rule5_y10 > 0), And(nsnt0CF_y10>=N-T, ) ))
s.add(Implies( (rule6_y10 > 0), And(nsnt1CF_y10>=N-T, ) ))
s.add(Implies( (rule7_y10 > 0), And(nsnt1CF_y10>=N-T, ) ))
s.add(Implies( (rule8_y10 > 0), And(nsnt01CF_y10>=N-T, nsnt0CF_y10>=N-2*T, nsnt1CF_y10>=1, ) ))
s.add(Implies( (rule9_y10 > 0), And(nsnt01CF_y10>=N-T, nsnt0CF_y10>=N-2*T, nsnt1CF_y10>=1, ) ))
s.add(Implies( (rule10_y10 > 0), And(nsnt01CF_y10>=N-T, nsnt1CF_y10>=N-2*T, nsnt0CF_y10>=1, ) ))
s.add(Implies( (rule11_y10 > 0), And(nsnt01CF_y10>=N-T, nsnt1CF_y10>=N-2*T, nsnt0CF_y10>=1, ) ))
s.add(Implies( (rule12_y10 > 0), And(nsnt01CF_y10>=N-T, nsnt0_y10<N-2*T, nsnt1_y10<N-2*T, ) ))
s.add(Implies( (rule13_y10 > 0), And(nsnt01CF_y10>=N-T, nsnt0_y10<N-2*T, nsnt1_y10<N-2*T, ) ))
s.add(Implies( (rule14_y10 > 0), And(nfaulty_y10<F, ) ))
s.add(Implies( (rule15_y10 > 0), And(nfaulty_y10<F, ) ))
s.add(Implies( (rule16_y10 > 0), And(nfaulty_y10<F, ) ))
s.add(Implies( (rule17_y10 > 0), And(nfaulty_y10<F, ) ))
s.add(Implies( (rule18_y10 > 0), And(nfaulty_y10<F, ) ))
s.add(Implies( (rule19_y10 > 0), And(nfaulty_y10<F, ) ))
s.add(Implies( (rule20_y10 > 0), And(nfaulty_y10<F, ) ))
s.add(Implies( (rule21_y10 > 0), And(nfaulty_y10<F, ) ))
s.add(Implies( (rule22_y10 > 0), And(True, ) ))
s.add(Implies( (rule23_y10 > 0), And(True, ) ))
s.add(Implies( (rule24_y10 > 0), And(True, ) ))
s.add(Implies( (rule25_y10 > 0), And(True, ) ))
s.add(Implies( (rule26_y10 > 0), And(True, ) ))
s.add(Implies( (rule27_y10 > 0), And(True, ) ))
s.add(Implies( (rule28_y10 > 0), And(True, ) ))
s.add(Implies( (rule29_y10 > 0), And(True, ) ))

##################Step 5########################


#Ensuring that at most one rule is fired alternating configurations y10 and x10, if a fall condition is present

s.add((nsnt1_x11<N-2*T) == (nsnt1_y10<N-2*T))
s.add(Implies(And((nsnt1_x11<N-2*T), Not(nsnt1_y10<N-2*T)), Or((rule0_y10 == 0), (rule0_y10 == 1))))
s.add(Implies(And((nsnt1_x11<N-2*T), Not(nsnt1_y10<N-2*T)), Or((rule1_y10 == 0), (rule1_y10 == 1))))
s.add(Implies(And((nsnt1_x11<N-2*T), Not(nsnt1_y10<N-2*T)), Or((rule2_y10 == 0), (rule2_y10 == 1))))
s.add(Implies(And((nsnt1_x11<N-2*T), Not(nsnt1_y10<N-2*T)), Or((rule3_y10 == 0), (rule3_y10 == 1))))
s.add(Implies(And((nsnt1_x11<N-2*T), Not(nsnt1_y10<N-2*T)), Or((rule4_y10 == 0), (rule4_y10 == 1))))
s.add(Implies(And((nsnt1_x11<N-2*T), Not(nsnt1_y10<N-2*T)), Or((rule5_y10 == 0), (rule5_y10 == 1))))
s.add(Implies(And((nsnt1_x11<N-2*T), Not(nsnt1_y10<N-2*T)), Or((rule6_y10 == 0), (rule6_y10 == 1))))
s.add(Implies(And((nsnt1_x11<N-2*T), Not(nsnt1_y10<N-2*T)), Or((rule7_y10 == 0), (rule7_y10 == 1))))
s.add(Implies(And((nsnt1_x11<N-2*T), Not(nsnt1_y10<N-2*T)), Or((rule8_y10 == 0), (rule8_y10 == 1))))
s.add(Implies(And((nsnt1_x11<N-2*T), Not(nsnt1_y10<N-2*T)), Or((rule9_y10 == 0), (rule9_y10 == 1))))
s.add(Implies(And((nsnt1_x11<N-2*T), Not(nsnt1_y10<N-2*T)), Or((rule10_y10 == 0), (rule10_y10 == 1))))
s.add(Implies(And((nsnt1_x11<N-2*T), Not(nsnt1_y10<N-2*T)), Or((rule11_y10 == 0), (rule11_y10 == 1))))
s.add(Implies(And((nsnt1_x11<N-2*T), Not(nsnt1_y10<N-2*T)), Or((rule12_y10 == 0), (rule12_y10 == 1))))
s.add(Implies(And((nsnt1_x11<N-2*T), Not(nsnt1_y10<N-2*T)), Or((rule13_y10 == 0), (rule13_y10 == 1))))
s.add(Implies(And((nsnt1_x11<N-2*T), Not(nsnt1_y10<N-2*T)), Or((rule14_y10 == 0), (rule14_y10 == 1))))
s.add(Implies(And((nsnt1_x11<N-2*T), Not(nsnt1_y10<N-2*T)), Or((rule15_y10 == 0), (rule15_y10 == 1))))
s.add(Implies(And((nsnt1_x11<N-2*T), Not(nsnt1_y10<N-2*T)), Or((rule16_y10 == 0), (rule16_y10 == 1))))
s.add(Implies(And((nsnt1_x11<N-2*T), Not(nsnt1_y10<N-2*T)), Or((rule17_y10 == 0), (rule17_y10 == 1))))
s.add(Implies(And((nsnt1_x11<N-2*T), Not(nsnt1_y10<N-2*T)), Or((rule18_y10 == 0), (rule18_y10 == 1))))
s.add(Implies(And((nsnt1_x11<N-2*T), Not(nsnt1_y10<N-2*T)), Or((rule19_y10 == 0), (rule19_y10 == 1))))
s.add(Implies(And((nsnt1_x11<N-2*T), Not(nsnt1_y10<N-2*T)), Or((rule20_y10 == 0), (rule20_y10 == 1))))
s.add(Implies(And((nsnt1_x11<N-2*T), Not(nsnt1_y10<N-2*T)), Or((rule21_y10 == 0), (rule21_y10 == 1))))
s.add(Implies(And((nsnt1_x11<N-2*T), Not(nsnt1_y10<N-2*T)), Or((rule22_y10 == 0), (rule22_y10 == 1))))
s.add(Implies(And((nsnt1_x11<N-2*T), Not(nsnt1_y10<N-2*T)), Or((rule23_y10 == 0), (rule23_y10 == 1))))
s.add(Implies(And((nsnt1_x11<N-2*T), Not(nsnt1_y10<N-2*T)), Or((rule24_y10 == 0), (rule24_y10 == 1))))
s.add(Implies(And((nsnt1_x11<N-2*T), Not(nsnt1_y10<N-2*T)), Or((rule25_y10 == 0), (rule25_y10 == 1))))
s.add(Implies(And((nsnt1_x11<N-2*T), Not(nsnt1_y10<N-2*T)), Or((rule26_y10 == 0), (rule26_y10 == 1))))
s.add(Implies(And((nsnt1_x11<N-2*T), Not(nsnt1_y10<N-2*T)), Or((rule27_y10 == 0), (rule27_y10 == 1))))
s.add(Implies(And((nsnt1_x11<N-2*T), Not(nsnt1_y10<N-2*T)), Or((rule28_y10 == 0), (rule28_y10 == 1))))
s.add(Implies(And((nsnt1_x11<N-2*T), Not(nsnt1_y10<N-2*T)), Or((rule29_y10 == 0), (rule29_y10 == 1))))
s.add(Implies(And((nsnt1_x11<N-2*T), Not(nsnt1_y10<N-2*T)), rule0_y10+rule1_y10+rule2_y10+rule3_y10+rule4_y10+rule5_y10+rule6_y10+rule7_y10+rule8_y10+rule9_y10+rule10_y10+rule11_y10+rule12_y10+rule13_y10+rule14_y10+rule15_y10+rule16_y10+rule17_y10+rule18_y10+rule19_y10+rule20_y10+rule21_y10+rule22_y10+rule23_y10+rule24_y10+rule25_y10+rule26_y10+rule27_y10+rule28_y10+rule29_y10 <= 1))

s.add((nfaulty_x11<F) == (nfaulty_y10<F))
s.add(Implies(And((nfaulty_x11<F), Not(nfaulty_y10<F)), Or((rule0_y10 == 0), (rule0_y10 == 1))))
s.add(Implies(And((nfaulty_x11<F), Not(nfaulty_y10<F)), Or((rule1_y10 == 0), (rule1_y10 == 1))))
s.add(Implies(And((nfaulty_x11<F), Not(nfaulty_y10<F)), Or((rule2_y10 == 0), (rule2_y10 == 1))))
s.add(Implies(And((nfaulty_x11<F), Not(nfaulty_y10<F)), Or((rule3_y10 == 0), (rule3_y10 == 1))))
s.add(Implies(And((nfaulty_x11<F), Not(nfaulty_y10<F)), Or((rule4_y10 == 0), (rule4_y10 == 1))))
s.add(Implies(And((nfaulty_x11<F), Not(nfaulty_y10<F)), Or((rule5_y10 == 0), (rule5_y10 == 1))))
s.add(Implies(And((nfaulty_x11<F), Not(nfaulty_y10<F)), Or((rule6_y10 == 0), (rule6_y10 == 1))))
s.add(Implies(And((nfaulty_x11<F), Not(nfaulty_y10<F)), Or((rule7_y10 == 0), (rule7_y10 == 1))))
s.add(Implies(And((nfaulty_x11<F), Not(nfaulty_y10<F)), Or((rule8_y10 == 0), (rule8_y10 == 1))))
s.add(Implies(And((nfaulty_x11<F), Not(nfaulty_y10<F)), Or((rule9_y10 == 0), (rule9_y10 == 1))))
s.add(Implies(And((nfaulty_x11<F), Not(nfaulty_y10<F)), Or((rule10_y10 == 0), (rule10_y10 == 1))))
s.add(Implies(And((nfaulty_x11<F), Not(nfaulty_y10<F)), Or((rule11_y10 == 0), (rule11_y10 == 1))))
s.add(Implies(And((nfaulty_x11<F), Not(nfaulty_y10<F)), Or((rule12_y10 == 0), (rule12_y10 == 1))))
s.add(Implies(And((nfaulty_x11<F), Not(nfaulty_y10<F)), Or((rule13_y10 == 0), (rule13_y10 == 1))))
s.add(Implies(And((nfaulty_x11<F), Not(nfaulty_y10<F)), Or((rule14_y10 == 0), (rule14_y10 == 1))))
s.add(Implies(And((nfaulty_x11<F), Not(nfaulty_y10<F)), Or((rule15_y10 == 0), (rule15_y10 == 1))))
s.add(Implies(And((nfaulty_x11<F), Not(nfaulty_y10<F)), Or((rule16_y10 == 0), (rule16_y10 == 1))))
s.add(Implies(And((nfaulty_x11<F), Not(nfaulty_y10<F)), Or((rule17_y10 == 0), (rule17_y10 == 1))))
s.add(Implies(And((nfaulty_x11<F), Not(nfaulty_y10<F)), Or((rule18_y10 == 0), (rule18_y10 == 1))))
s.add(Implies(And((nfaulty_x11<F), Not(nfaulty_y10<F)), Or((rule19_y10 == 0), (rule19_y10 == 1))))
s.add(Implies(And((nfaulty_x11<F), Not(nfaulty_y10<F)), Or((rule20_y10 == 0), (rule20_y10 == 1))))
s.add(Implies(And((nfaulty_x11<F), Not(nfaulty_y10<F)), Or((rule21_y10 == 0), (rule21_y10 == 1))))
s.add(Implies(And((nfaulty_x11<F), Not(nfaulty_y10<F)), Or((rule22_y10 == 0), (rule22_y10 == 1))))
s.add(Implies(And((nfaulty_x11<F), Not(nfaulty_y10<F)), Or((rule23_y10 == 0), (rule23_y10 == 1))))
s.add(Implies(And((nfaulty_x11<F), Not(nfaulty_y10<F)), Or((rule24_y10 == 0), (rule24_y10 == 1))))
s.add(Implies(And((nfaulty_x11<F), Not(nfaulty_y10<F)), Or((rule25_y10 == 0), (rule25_y10 == 1))))
s.add(Implies(And((nfaulty_x11<F), Not(nfaulty_y10<F)), Or((rule26_y10 == 0), (rule26_y10 == 1))))
s.add(Implies(And((nfaulty_x11<F), Not(nfaulty_y10<F)), Or((rule27_y10 == 0), (rule27_y10 == 1))))
s.add(Implies(And((nfaulty_x11<F), Not(nfaulty_y10<F)), Or((rule28_y10 == 0), (rule28_y10 == 1))))
s.add(Implies(And((nfaulty_x11<F), Not(nfaulty_y10<F)), Or((rule29_y10 == 0), (rule29_y10 == 1))))
s.add(Implies(And((nfaulty_x11<F), Not(nfaulty_y10<F)), rule0_y10+rule1_y10+rule2_y10+rule3_y10+rule4_y10+rule5_y10+rule6_y10+rule7_y10+rule8_y10+rule9_y10+rule10_y10+rule11_y10+rule12_y10+rule13_y10+rule14_y10+rule15_y10+rule16_y10+rule17_y10+rule18_y10+rule19_y10+rule20_y10+rule21_y10+rule22_y10+rule23_y10+rule24_y10+rule25_y10+rule26_y10+rule27_y10+rule28_y10+rule29_y10 <= 1))

s.add((nsnt0_x11<N-2*T) == (nsnt0_y10<N-2*T))
s.add(Implies(And((nsnt0_x11<N-2*T), Not(nsnt0_y10<N-2*T)), Or((rule0_y10 == 0), (rule0_y10 == 1))))
s.add(Implies(And((nsnt0_x11<N-2*T), Not(nsnt0_y10<N-2*T)), Or((rule1_y10 == 0), (rule1_y10 == 1))))
s.add(Implies(And((nsnt0_x11<N-2*T), Not(nsnt0_y10<N-2*T)), Or((rule2_y10 == 0), (rule2_y10 == 1))))
s.add(Implies(And((nsnt0_x11<N-2*T), Not(nsnt0_y10<N-2*T)), Or((rule3_y10 == 0), (rule3_y10 == 1))))
s.add(Implies(And((nsnt0_x11<N-2*T), Not(nsnt0_y10<N-2*T)), Or((rule4_y10 == 0), (rule4_y10 == 1))))
s.add(Implies(And((nsnt0_x11<N-2*T), Not(nsnt0_y10<N-2*T)), Or((rule5_y10 == 0), (rule5_y10 == 1))))
s.add(Implies(And((nsnt0_x11<N-2*T), Not(nsnt0_y10<N-2*T)), Or((rule6_y10 == 0), (rule6_y10 == 1))))
s.add(Implies(And((nsnt0_x11<N-2*T), Not(nsnt0_y10<N-2*T)), Or((rule7_y10 == 0), (rule7_y10 == 1))))
s.add(Implies(And((nsnt0_x11<N-2*T), Not(nsnt0_y10<N-2*T)), Or((rule8_y10 == 0), (rule8_y10 == 1))))
s.add(Implies(And((nsnt0_x11<N-2*T), Not(nsnt0_y10<N-2*T)), Or((rule9_y10 == 0), (rule9_y10 == 1))))
s.add(Implies(And((nsnt0_x11<N-2*T), Not(nsnt0_y10<N-2*T)), Or((rule10_y10 == 0), (rule10_y10 == 1))))
s.add(Implies(And((nsnt0_x11<N-2*T), Not(nsnt0_y10<N-2*T)), Or((rule11_y10 == 0), (rule11_y10 == 1))))
s.add(Implies(And((nsnt0_x11<N-2*T), Not(nsnt0_y10<N-2*T)), Or((rule12_y10 == 0), (rule12_y10 == 1))))
s.add(Implies(And((nsnt0_x11<N-2*T), Not(nsnt0_y10<N-2*T)), Or((rule13_y10 == 0), (rule13_y10 == 1))))
s.add(Implies(And((nsnt0_x11<N-2*T), Not(nsnt0_y10<N-2*T)), Or((rule14_y10 == 0), (rule14_y10 == 1))))
s.add(Implies(And((nsnt0_x11<N-2*T), Not(nsnt0_y10<N-2*T)), Or((rule15_y10 == 0), (rule15_y10 == 1))))
s.add(Implies(And((nsnt0_x11<N-2*T), Not(nsnt0_y10<N-2*T)), Or((rule16_y10 == 0), (rule16_y10 == 1))))
s.add(Implies(And((nsnt0_x11<N-2*T), Not(nsnt0_y10<N-2*T)), Or((rule17_y10 == 0), (rule17_y10 == 1))))
s.add(Implies(And((nsnt0_x11<N-2*T), Not(nsnt0_y10<N-2*T)), Or((rule18_y10 == 0), (rule18_y10 == 1))))
s.add(Implies(And((nsnt0_x11<N-2*T), Not(nsnt0_y10<N-2*T)), Or((rule19_y10 == 0), (rule19_y10 == 1))))
s.add(Implies(And((nsnt0_x11<N-2*T), Not(nsnt0_y10<N-2*T)), Or((rule20_y10 == 0), (rule20_y10 == 1))))
s.add(Implies(And((nsnt0_x11<N-2*T), Not(nsnt0_y10<N-2*T)), Or((rule21_y10 == 0), (rule21_y10 == 1))))
s.add(Implies(And((nsnt0_x11<N-2*T), Not(nsnt0_y10<N-2*T)), Or((rule22_y10 == 0), (rule22_y10 == 1))))
s.add(Implies(And((nsnt0_x11<N-2*T), Not(nsnt0_y10<N-2*T)), Or((rule23_y10 == 0), (rule23_y10 == 1))))
s.add(Implies(And((nsnt0_x11<N-2*T), Not(nsnt0_y10<N-2*T)), Or((rule24_y10 == 0), (rule24_y10 == 1))))
s.add(Implies(And((nsnt0_x11<N-2*T), Not(nsnt0_y10<N-2*T)), Or((rule25_y10 == 0), (rule25_y10 == 1))))
s.add(Implies(And((nsnt0_x11<N-2*T), Not(nsnt0_y10<N-2*T)), Or((rule26_y10 == 0), (rule26_y10 == 1))))
s.add(Implies(And((nsnt0_x11<N-2*T), Not(nsnt0_y10<N-2*T)), Or((rule27_y10 == 0), (rule27_y10 == 1))))
s.add(Implies(And((nsnt0_x11<N-2*T), Not(nsnt0_y10<N-2*T)), Or((rule28_y10 == 0), (rule28_y10 == 1))))
s.add(Implies(And((nsnt0_x11<N-2*T), Not(nsnt0_y10<N-2*T)), Or((rule29_y10 == 0), (rule29_y10 == 1))))
s.add(Implies(And((nsnt0_x11<N-2*T), Not(nsnt0_y10<N-2*T)), rule0_y10+rule1_y10+rule2_y10+rule3_y10+rule4_y10+rule5_y10+rule6_y10+rule7_y10+rule8_y10+rule9_y10+rule10_y10+rule11_y10+rule12_y10+rule13_y10+rule14_y10+rule15_y10+rule16_y10+rule17_y10+rule18_y10+rule19_y10+rule20_y10+rule21_y10+rule22_y10+rule23_y10+rule24_y10+rule25_y10+rule26_y10+rule27_y10+rule28_y10+rule29_y10 <= 1))


#############Additional step for the final configuration#####################


###########Ensure that the last configuration satisfies the final condition#############

s.add(Or(locD0_y11 != 0, locU0_y11 != 0, locU1_y11 != 0))






if s.check() == sat:

	print("Specification not satisfied")

else:

	print("Specification satisfied")
