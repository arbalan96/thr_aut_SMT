from z3 import *
s = Solver()

#Declaring parameter variables

N = Real('N')
s.add(N >= 0)

#Adding the resilience condition

s.add(N > 1)

####################################################################################

#Creating constraints for a run between the x0th and y0th configurations

################Step 1#################


#Creating many copies of location variables

locNO_x0 = Real('locNO_x0')
locNO_y0 = Real('locNO_y0')
s.add(locNO_x0 >= 0)
s.add(locNO_y0 >= 0)
locYES_x0 = Real('locYES_x0')
locYES_y0 = Real('locYES_y0')
s.add(locYES_x0 >= 0)
s.add(locYES_y0 >= 0)
locFDNO_x0 = Real('locFDNO_x0')
locFDNO_y0 = Real('locFDNO_y0')
s.add(locFDNO_x0 >= 0)
s.add(locFDNO_y0 >= 0)
locFDYES_x0 = Real('locFDYES_x0')
locFDYES_y0 = Real('locFDYES_y0')
s.add(locFDYES_x0 >= 0)
s.add(locFDYES_y0 >= 0)
locSE_x0 = Real('locSE_x0')
locSE_y0 = Real('locSE_y0')
s.add(locSE_x0 >= 0)
s.add(locSE_y0 >= 0)
locCMT_x0 = Real('locCMT_x0')
locCMT_y0 = Real('locCMT_y0')
s.add(locCMT_x0 >= 0)
s.add(locCMT_y0 >= 0)
locABR_x0 = Real('locABR_x0')
locABR_y0 = Real('locABR_y0')
s.add(locABR_x0 >= 0)
s.add(locABR_y0 >= 0)
locCR_x0 = Real('locCR_x0')
locCR_y0 = Real('locCR_y0')
s.add(locCR_x0 >= 0)
s.add(locCR_y0 >= 0)






#Creating many copies of shared variables

nsntNoCF_x0 = Real('nsntNoCF_x0')
nsntNoCF_y0 = Real('nsntNoCF_y0')
s.add(nsntNoCF_x0 >= 0)
s.add(nsntNoCF_y0 >= 0)
nsntYesCF_x0 = Real('nsntYesCF_x0')
nsntYesCF_y0 = Real('nsntYesCF_y0')
s.add(nsntYesCF_x0 >= 0)
s.add(nsntYesCF_y0 >= 0)






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






###################Step 2####################


#Flow equations for the locations

s.add(0 - rule0_x0 - rule6_x0 ==  locNO_y0 - locNO_x0)
s.add(0 - rule1_x0 - rule8_x0 ==  locYES_y0 - locYES_x0)
s.add(0 - rule2_x0 - rule7_x0 ==  locFDNO_y0 - locFDNO_x0)
s.add(0 - rule3_x0 - rule9_x0 ==  locFDYES_y0 - locFDYES_x0)
s.add(0 + rule0_x0 + rule1_x0 - rule4_x0 - rule5_x0 - rule10_x0 - rule13_x0 + rule13_x0 ==  locSE_y0 - locSE_x0)
s.add(0 + rule5_x0 - rule11_x0 - rule14_x0 + rule14_x0 ==  locCMT_y0 - locCMT_x0)
s.add(0 + rule2_x0 + rule3_x0 + rule4_x0 - rule12_x0 - rule15_x0 + rule15_x0 ==  locABR_y0 - locABR_x0)
s.add(0 + rule6_x0 + rule7_x0 + rule8_x0 + rule9_x0 + rule10_x0 + rule11_x0 + rule12_x0 ==  locCR_y0 - locCR_x0)






##################Step 3########################


#Flow equations for the shared variables

s.add(0 + rule0_x0 == nsntNoCF_y0 - nsntNoCF_x0)
s.add(0 + rule1_x0 == nsntYesCF_y0 - nsntYesCF_x0)






####################Step 4########################


#Rule is fired implies rule is enabled

s.add(Implies( (rule0_x0 > 0), And(True, ) ))
s.add(Implies( (rule1_x0 > 0), And(True, ) ))
s.add(Implies( (rule2_x0 > 0), And(True, ) ))
s.add(Implies( (rule3_x0 > 0), And(True, ) ))
s.add(Implies( (rule4_x0 > 0), And(nsntNoCF_x0>=1, ) ))
s.add(Implies( (rule5_x0 > 0), And(nsntNoCF_x0==0, nsntYesCF_x0>=N, ) ))
s.add(Implies( (rule6_x0 > 0), And(True, ) ))
s.add(Implies( (rule7_x0 > 0), And(True, ) ))
s.add(Implies( (rule8_x0 > 0), And(True, ) ))
s.add(Implies( (rule9_x0 > 0), And(True, ) ))
s.add(Implies( (rule10_x0 > 0), And(True, ) ))
s.add(Implies( (rule11_x0 > 0), And(True, ) ))
s.add(Implies( (rule12_x0 > 0), And(True, ) ))
s.add(Implies( (rule13_x0 > 0), And(True, ) ))
s.add(Implies( (rule14_x0 > 0), And(True, ) ))
s.add(Implies( (rule15_x0 > 0), And(True, ) ))

##################Step 5#########################


#Ensuring that configurations x0 and y0 have the same context

s.add((nsntNoCF_x0==0) == (nsntNoCF_y0==0))
s.add((nsntNoCF_x0>=1) == (nsntNoCF_y0>=1))
s.add((True) == (True))
s.add((nsntYesCF_x0>=N) == (nsntYesCF_y0>=N))

#############Additional step for the initial configuration#####################


#############Ensure that the first configuration only contains initial locations###########

s.add((locNO_x0 + locYES_x0 + locFDNO_x0 + locFDYES_x0) == N)
s.add(locSE_x0 == 0)
s.add(locCMT_x0 == 0)
s.add(locABR_x0 == 0)
s.add(locCR_x0 == 0)
s.add(nsntNoCF_x0 == 0)
s.add(nsntYesCF_x0 == 0)






###########Ensure that the first configuration satisfies the initial condition#############

s.add(And(locNO_x0 == 0, locFDNO_x0 == 0, locFDYES_x0 == 0))






####################################################################################

#Creating constraints for a run between the x1th and y1th configurations

################Step 1#################


#Creating many copies of location variables

locNO_x1 = Real('locNO_x1')
locNO_y1 = Real('locNO_y1')
s.add(locNO_x1 >= 0)
s.add(locNO_y1 >= 0)
locYES_x1 = Real('locYES_x1')
locYES_y1 = Real('locYES_y1')
s.add(locYES_x1 >= 0)
s.add(locYES_y1 >= 0)
locFDNO_x1 = Real('locFDNO_x1')
locFDNO_y1 = Real('locFDNO_y1')
s.add(locFDNO_x1 >= 0)
s.add(locFDNO_y1 >= 0)
locFDYES_x1 = Real('locFDYES_x1')
locFDYES_y1 = Real('locFDYES_y1')
s.add(locFDYES_x1 >= 0)
s.add(locFDYES_y1 >= 0)
locSE_x1 = Real('locSE_x1')
locSE_y1 = Real('locSE_y1')
s.add(locSE_x1 >= 0)
s.add(locSE_y1 >= 0)
locCMT_x1 = Real('locCMT_x1')
locCMT_y1 = Real('locCMT_y1')
s.add(locCMT_x1 >= 0)
s.add(locCMT_y1 >= 0)
locABR_x1 = Real('locABR_x1')
locABR_y1 = Real('locABR_y1')
s.add(locABR_x1 >= 0)
s.add(locABR_y1 >= 0)
locCR_x1 = Real('locCR_x1')
locCR_y1 = Real('locCR_y1')
s.add(locCR_x1 >= 0)
s.add(locCR_y1 >= 0)






#Creating many copies of shared variables

nsntNoCF_x1 = Real('nsntNoCF_x1')
nsntNoCF_y1 = Real('nsntNoCF_y1')
s.add(nsntNoCF_x1 >= 0)
s.add(nsntNoCF_y1 >= 0)
nsntYesCF_x1 = Real('nsntYesCF_x1')
nsntYesCF_y1 = Real('nsntYesCF_y1')
s.add(nsntYesCF_x1 >= 0)
s.add(nsntYesCF_y1 >= 0)






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






###################Step 2####################


#Flow equations for the locations

s.add(0 - rule0_x1 - rule6_x1 ==  locNO_y1 - locNO_x1)
s.add(0 - rule1_x1 - rule8_x1 ==  locYES_y1 - locYES_x1)
s.add(0 - rule2_x1 - rule7_x1 ==  locFDNO_y1 - locFDNO_x1)
s.add(0 - rule3_x1 - rule9_x1 ==  locFDYES_y1 - locFDYES_x1)
s.add(0 + rule0_x1 + rule1_x1 - rule4_x1 - rule5_x1 - rule10_x1 - rule13_x1 + rule13_x1 ==  locSE_y1 - locSE_x1)
s.add(0 + rule5_x1 - rule11_x1 - rule14_x1 + rule14_x1 ==  locCMT_y1 - locCMT_x1)
s.add(0 + rule2_x1 + rule3_x1 + rule4_x1 - rule12_x1 - rule15_x1 + rule15_x1 ==  locABR_y1 - locABR_x1)
s.add(0 + rule6_x1 + rule7_x1 + rule8_x1 + rule9_x1 + rule10_x1 + rule11_x1 + rule12_x1 ==  locCR_y1 - locCR_x1)






##################Step 3########################


#Flow equations for the shared variables

s.add(0 + rule0_x1 == nsntNoCF_y1 - nsntNoCF_x1)
s.add(0 + rule1_x1 == nsntYesCF_y1 - nsntYesCF_x1)






####################Step 4########################


#Rule is fired implies rule is enabled

s.add(Implies( (rule0_x1 > 0), And(True, ) ))
s.add(Implies( (rule1_x1 > 0), And(True, ) ))
s.add(Implies( (rule2_x1 > 0), And(True, ) ))
s.add(Implies( (rule3_x1 > 0), And(True, ) ))
s.add(Implies( (rule4_x1 > 0), And(nsntNoCF_x1>=1, ) ))
s.add(Implies( (rule5_x1 > 0), And(nsntNoCF_x1==0, nsntYesCF_x1>=N, ) ))
s.add(Implies( (rule6_x1 > 0), And(True, ) ))
s.add(Implies( (rule7_x1 > 0), And(True, ) ))
s.add(Implies( (rule8_x1 > 0), And(True, ) ))
s.add(Implies( (rule9_x1 > 0), And(True, ) ))
s.add(Implies( (rule10_x1 > 0), And(True, ) ))
s.add(Implies( (rule11_x1 > 0), And(True, ) ))
s.add(Implies( (rule12_x1 > 0), And(True, ) ))
s.add(Implies( (rule13_x1 > 0), And(True, ) ))
s.add(Implies( (rule14_x1 > 0), And(True, ) ))
s.add(Implies( (rule15_x1 > 0), And(True, ) ))

##################Step 5#########################


#Ensuring that configurations x1 and y1 have the same context

s.add((nsntNoCF_x1==0) == (nsntNoCF_y1==0))
s.add((nsntNoCF_x1>=1) == (nsntNoCF_y1>=1))
s.add((True) == (True))
s.add((nsntYesCF_x1>=N) == (nsntYesCF_y1>=N))

####################################################################################

#Creating constraints for a run between the x2th and y2th configurations

################Step 1#################


#Creating many copies of location variables

locNO_x2 = Real('locNO_x2')
locNO_y2 = Real('locNO_y2')
s.add(locNO_x2 >= 0)
s.add(locNO_y2 >= 0)
locYES_x2 = Real('locYES_x2')
locYES_y2 = Real('locYES_y2')
s.add(locYES_x2 >= 0)
s.add(locYES_y2 >= 0)
locFDNO_x2 = Real('locFDNO_x2')
locFDNO_y2 = Real('locFDNO_y2')
s.add(locFDNO_x2 >= 0)
s.add(locFDNO_y2 >= 0)
locFDYES_x2 = Real('locFDYES_x2')
locFDYES_y2 = Real('locFDYES_y2')
s.add(locFDYES_x2 >= 0)
s.add(locFDYES_y2 >= 0)
locSE_x2 = Real('locSE_x2')
locSE_y2 = Real('locSE_y2')
s.add(locSE_x2 >= 0)
s.add(locSE_y2 >= 0)
locCMT_x2 = Real('locCMT_x2')
locCMT_y2 = Real('locCMT_y2')
s.add(locCMT_x2 >= 0)
s.add(locCMT_y2 >= 0)
locABR_x2 = Real('locABR_x2')
locABR_y2 = Real('locABR_y2')
s.add(locABR_x2 >= 0)
s.add(locABR_y2 >= 0)
locCR_x2 = Real('locCR_x2')
locCR_y2 = Real('locCR_y2')
s.add(locCR_x2 >= 0)
s.add(locCR_y2 >= 0)






#Creating many copies of shared variables

nsntNoCF_x2 = Real('nsntNoCF_x2')
nsntNoCF_y2 = Real('nsntNoCF_y2')
s.add(nsntNoCF_x2 >= 0)
s.add(nsntNoCF_y2 >= 0)
nsntYesCF_x2 = Real('nsntYesCF_x2')
nsntYesCF_y2 = Real('nsntYesCF_y2')
s.add(nsntYesCF_x2 >= 0)
s.add(nsntYesCF_y2 >= 0)






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






###################Step 2####################


#Flow equations for the locations

s.add(0 - rule0_x2 - rule6_x2 ==  locNO_y2 - locNO_x2)
s.add(0 - rule1_x2 - rule8_x2 ==  locYES_y2 - locYES_x2)
s.add(0 - rule2_x2 - rule7_x2 ==  locFDNO_y2 - locFDNO_x2)
s.add(0 - rule3_x2 - rule9_x2 ==  locFDYES_y2 - locFDYES_x2)
s.add(0 + rule0_x2 + rule1_x2 - rule4_x2 - rule5_x2 - rule10_x2 - rule13_x2 + rule13_x2 ==  locSE_y2 - locSE_x2)
s.add(0 + rule5_x2 - rule11_x2 - rule14_x2 + rule14_x2 ==  locCMT_y2 - locCMT_x2)
s.add(0 + rule2_x2 + rule3_x2 + rule4_x2 - rule12_x2 - rule15_x2 + rule15_x2 ==  locABR_y2 - locABR_x2)
s.add(0 + rule6_x2 + rule7_x2 + rule8_x2 + rule9_x2 + rule10_x2 + rule11_x2 + rule12_x2 ==  locCR_y2 - locCR_x2)






##################Step 3########################


#Flow equations for the shared variables

s.add(0 + rule0_x2 == nsntNoCF_y2 - nsntNoCF_x2)
s.add(0 + rule1_x2 == nsntYesCF_y2 - nsntYesCF_x2)






####################Step 4########################


#Rule is fired implies rule is enabled

s.add(Implies( (rule0_x2 > 0), And(True, ) ))
s.add(Implies( (rule1_x2 > 0), And(True, ) ))
s.add(Implies( (rule2_x2 > 0), And(True, ) ))
s.add(Implies( (rule3_x2 > 0), And(True, ) ))
s.add(Implies( (rule4_x2 > 0), And(nsntNoCF_x2>=1, ) ))
s.add(Implies( (rule5_x2 > 0), And(nsntNoCF_x2==0, nsntYesCF_x2>=N, ) ))
s.add(Implies( (rule6_x2 > 0), And(True, ) ))
s.add(Implies( (rule7_x2 > 0), And(True, ) ))
s.add(Implies( (rule8_x2 > 0), And(True, ) ))
s.add(Implies( (rule9_x2 > 0), And(True, ) ))
s.add(Implies( (rule10_x2 > 0), And(True, ) ))
s.add(Implies( (rule11_x2 > 0), And(True, ) ))
s.add(Implies( (rule12_x2 > 0), And(True, ) ))
s.add(Implies( (rule13_x2 > 0), And(True, ) ))
s.add(Implies( (rule14_x2 > 0), And(True, ) ))
s.add(Implies( (rule15_x2 > 0), And(True, ) ))

##################Step 5#########################


#Ensuring that configurations x2 and y2 have the same context

s.add((nsntNoCF_x2==0) == (nsntNoCF_y2==0))
s.add((nsntNoCF_x2>=1) == (nsntNoCF_y2>=1))
s.add((True) == (True))
s.add((nsntYesCF_x2>=N) == (nsntYesCF_y2>=N))

####################################################################################

#Creating constraints for a run between the x3th and y3th configurations

################Step 1#################


#Creating many copies of location variables

locNO_x3 = Real('locNO_x3')
locNO_y3 = Real('locNO_y3')
s.add(locNO_x3 >= 0)
s.add(locNO_y3 >= 0)
locYES_x3 = Real('locYES_x3')
locYES_y3 = Real('locYES_y3')
s.add(locYES_x3 >= 0)
s.add(locYES_y3 >= 0)
locFDNO_x3 = Real('locFDNO_x3')
locFDNO_y3 = Real('locFDNO_y3')
s.add(locFDNO_x3 >= 0)
s.add(locFDNO_y3 >= 0)
locFDYES_x3 = Real('locFDYES_x3')
locFDYES_y3 = Real('locFDYES_y3')
s.add(locFDYES_x3 >= 0)
s.add(locFDYES_y3 >= 0)
locSE_x3 = Real('locSE_x3')
locSE_y3 = Real('locSE_y3')
s.add(locSE_x3 >= 0)
s.add(locSE_y3 >= 0)
locCMT_x3 = Real('locCMT_x3')
locCMT_y3 = Real('locCMT_y3')
s.add(locCMT_x3 >= 0)
s.add(locCMT_y3 >= 0)
locABR_x3 = Real('locABR_x3')
locABR_y3 = Real('locABR_y3')
s.add(locABR_x3 >= 0)
s.add(locABR_y3 >= 0)
locCR_x3 = Real('locCR_x3')
locCR_y3 = Real('locCR_y3')
s.add(locCR_x3 >= 0)
s.add(locCR_y3 >= 0)






#Creating many copies of shared variables

nsntNoCF_x3 = Real('nsntNoCF_x3')
nsntNoCF_y3 = Real('nsntNoCF_y3')
s.add(nsntNoCF_x3 >= 0)
s.add(nsntNoCF_y3 >= 0)
nsntYesCF_x3 = Real('nsntYesCF_x3')
nsntYesCF_y3 = Real('nsntYesCF_y3')
s.add(nsntYesCF_x3 >= 0)
s.add(nsntYesCF_y3 >= 0)






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






###################Step 2####################


#Flow equations for the locations

s.add(0 - rule0_x3 - rule6_x3 ==  locNO_y3 - locNO_x3)
s.add(0 - rule1_x3 - rule8_x3 ==  locYES_y3 - locYES_x3)
s.add(0 - rule2_x3 - rule7_x3 ==  locFDNO_y3 - locFDNO_x3)
s.add(0 - rule3_x3 - rule9_x3 ==  locFDYES_y3 - locFDYES_x3)
s.add(0 + rule0_x3 + rule1_x3 - rule4_x3 - rule5_x3 - rule10_x3 - rule13_x3 + rule13_x3 ==  locSE_y3 - locSE_x3)
s.add(0 + rule5_x3 - rule11_x3 - rule14_x3 + rule14_x3 ==  locCMT_y3 - locCMT_x3)
s.add(0 + rule2_x3 + rule3_x3 + rule4_x3 - rule12_x3 - rule15_x3 + rule15_x3 ==  locABR_y3 - locABR_x3)
s.add(0 + rule6_x3 + rule7_x3 + rule8_x3 + rule9_x3 + rule10_x3 + rule11_x3 + rule12_x3 ==  locCR_y3 - locCR_x3)






##################Step 3########################


#Flow equations for the shared variables

s.add(0 + rule0_x3 == nsntNoCF_y3 - nsntNoCF_x3)
s.add(0 + rule1_x3 == nsntYesCF_y3 - nsntYesCF_x3)






####################Step 4########################


#Rule is fired implies rule is enabled

s.add(Implies( (rule0_x3 > 0), And(True, ) ))
s.add(Implies( (rule1_x3 > 0), And(True, ) ))
s.add(Implies( (rule2_x3 > 0), And(True, ) ))
s.add(Implies( (rule3_x3 > 0), And(True, ) ))
s.add(Implies( (rule4_x3 > 0), And(nsntNoCF_x3>=1, ) ))
s.add(Implies( (rule5_x3 > 0), And(nsntNoCF_x3==0, nsntYesCF_x3>=N, ) ))
s.add(Implies( (rule6_x3 > 0), And(True, ) ))
s.add(Implies( (rule7_x3 > 0), And(True, ) ))
s.add(Implies( (rule8_x3 > 0), And(True, ) ))
s.add(Implies( (rule9_x3 > 0), And(True, ) ))
s.add(Implies( (rule10_x3 > 0), And(True, ) ))
s.add(Implies( (rule11_x3 > 0), And(True, ) ))
s.add(Implies( (rule12_x3 > 0), And(True, ) ))
s.add(Implies( (rule13_x3 > 0), And(True, ) ))
s.add(Implies( (rule14_x3 > 0), And(True, ) ))
s.add(Implies( (rule15_x3 > 0), And(True, ) ))

##################Step 5#########################


#Ensuring that configurations x3 and y3 have the same context

s.add((nsntNoCF_x3==0) == (nsntNoCF_y3==0))
s.add((nsntNoCF_x3>=1) == (nsntNoCF_y3>=1))
s.add((True) == (True))
s.add((nsntYesCF_x3>=N) == (nsntYesCF_y3>=N))

####################################################################################

#Creating constraints for a run between the x4th and y4th configurations

################Step 1#################


#Creating many copies of location variables

locNO_x4 = Real('locNO_x4')
locNO_y4 = Real('locNO_y4')
s.add(locNO_x4 >= 0)
s.add(locNO_y4 >= 0)
locYES_x4 = Real('locYES_x4')
locYES_y4 = Real('locYES_y4')
s.add(locYES_x4 >= 0)
s.add(locYES_y4 >= 0)
locFDNO_x4 = Real('locFDNO_x4')
locFDNO_y4 = Real('locFDNO_y4')
s.add(locFDNO_x4 >= 0)
s.add(locFDNO_y4 >= 0)
locFDYES_x4 = Real('locFDYES_x4')
locFDYES_y4 = Real('locFDYES_y4')
s.add(locFDYES_x4 >= 0)
s.add(locFDYES_y4 >= 0)
locSE_x4 = Real('locSE_x4')
locSE_y4 = Real('locSE_y4')
s.add(locSE_x4 >= 0)
s.add(locSE_y4 >= 0)
locCMT_x4 = Real('locCMT_x4')
locCMT_y4 = Real('locCMT_y4')
s.add(locCMT_x4 >= 0)
s.add(locCMT_y4 >= 0)
locABR_x4 = Real('locABR_x4')
locABR_y4 = Real('locABR_y4')
s.add(locABR_x4 >= 0)
s.add(locABR_y4 >= 0)
locCR_x4 = Real('locCR_x4')
locCR_y4 = Real('locCR_y4')
s.add(locCR_x4 >= 0)
s.add(locCR_y4 >= 0)






#Creating many copies of shared variables

nsntNoCF_x4 = Real('nsntNoCF_x4')
nsntNoCF_y4 = Real('nsntNoCF_y4')
s.add(nsntNoCF_x4 >= 0)
s.add(nsntNoCF_y4 >= 0)
nsntYesCF_x4 = Real('nsntYesCF_x4')
nsntYesCF_y4 = Real('nsntYesCF_y4')
s.add(nsntYesCF_x4 >= 0)
s.add(nsntYesCF_y4 >= 0)






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






###################Step 2####################


#Flow equations for the locations

s.add(0 - rule0_x4 - rule6_x4 ==  locNO_y4 - locNO_x4)
s.add(0 - rule1_x4 - rule8_x4 ==  locYES_y4 - locYES_x4)
s.add(0 - rule2_x4 - rule7_x4 ==  locFDNO_y4 - locFDNO_x4)
s.add(0 - rule3_x4 - rule9_x4 ==  locFDYES_y4 - locFDYES_x4)
s.add(0 + rule0_x4 + rule1_x4 - rule4_x4 - rule5_x4 - rule10_x4 - rule13_x4 + rule13_x4 ==  locSE_y4 - locSE_x4)
s.add(0 + rule5_x4 - rule11_x4 - rule14_x4 + rule14_x4 ==  locCMT_y4 - locCMT_x4)
s.add(0 + rule2_x4 + rule3_x4 + rule4_x4 - rule12_x4 - rule15_x4 + rule15_x4 ==  locABR_y4 - locABR_x4)
s.add(0 + rule6_x4 + rule7_x4 + rule8_x4 + rule9_x4 + rule10_x4 + rule11_x4 + rule12_x4 ==  locCR_y4 - locCR_x4)






##################Step 3########################


#Flow equations for the shared variables

s.add(0 + rule0_x4 == nsntNoCF_y4 - nsntNoCF_x4)
s.add(0 + rule1_x4 == nsntYesCF_y4 - nsntYesCF_x4)






####################Step 4########################


#Rule is fired implies rule is enabled

s.add(Implies( (rule0_x4 > 0), And(True, ) ))
s.add(Implies( (rule1_x4 > 0), And(True, ) ))
s.add(Implies( (rule2_x4 > 0), And(True, ) ))
s.add(Implies( (rule3_x4 > 0), And(True, ) ))
s.add(Implies( (rule4_x4 > 0), And(nsntNoCF_x4>=1, ) ))
s.add(Implies( (rule5_x4 > 0), And(nsntNoCF_x4==0, nsntYesCF_x4>=N, ) ))
s.add(Implies( (rule6_x4 > 0), And(True, ) ))
s.add(Implies( (rule7_x4 > 0), And(True, ) ))
s.add(Implies( (rule8_x4 > 0), And(True, ) ))
s.add(Implies( (rule9_x4 > 0), And(True, ) ))
s.add(Implies( (rule10_x4 > 0), And(True, ) ))
s.add(Implies( (rule11_x4 > 0), And(True, ) ))
s.add(Implies( (rule12_x4 > 0), And(True, ) ))
s.add(Implies( (rule13_x4 > 0), And(True, ) ))
s.add(Implies( (rule14_x4 > 0), And(True, ) ))
s.add(Implies( (rule15_x4 > 0), And(True, ) ))

##################Step 5#########################


#Ensuring that configurations x4 and y4 have the same context

s.add((nsntNoCF_x4==0) == (nsntNoCF_y4==0))
s.add((nsntNoCF_x4>=1) == (nsntNoCF_y4>=1))
s.add((True) == (True))
s.add((nsntYesCF_x4>=N) == (nsntYesCF_y4>=N))

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






###################Step 2####################


#Flow equations for the locations

s.add(0 - rule0_y0 - rule6_y0 ==  locNO_x1 - locNO_y0)
s.add(0 - rule1_y0 - rule8_y0 ==  locYES_x1 - locYES_y0)
s.add(0 - rule2_y0 - rule7_y0 ==  locFDNO_x1 - locFDNO_y0)
s.add(0 - rule3_y0 - rule9_y0 ==  locFDYES_x1 - locFDYES_y0)
s.add(0 + rule0_y0 + rule1_y0 - rule4_y0 - rule5_y0 - rule10_y0 - rule13_y0 + rule13_y0 ==  locSE_x1 - locSE_y0)
s.add(0 + rule5_y0 - rule11_y0 - rule14_y0 + rule14_y0 ==  locCMT_x1 - locCMT_y0)
s.add(0 + rule2_y0 + rule3_y0 + rule4_y0 - rule12_y0 - rule15_y0 + rule15_y0 ==  locABR_x1 - locABR_y0)
s.add(0 + rule6_y0 + rule7_y0 + rule8_y0 + rule9_y0 + rule10_y0 + rule11_y0 + rule12_y0 ==  locCR_x1 - locCR_y0)






##################Step 3########################


#Flow equations for the shared variables

s.add(0 + rule0_y0 == nsntNoCF_x1 - nsntNoCF_y0)
s.add(0 + rule1_y0 == nsntYesCF_x1 - nsntYesCF_y0)






####################Step 4########################


#Rule is fired implies rule is enabled

s.add(Implies( (rule0_y0 > 0), And(True, ) ))
s.add(Implies( (rule1_y0 > 0), And(True, ) ))
s.add(Implies( (rule2_y0 > 0), And(True, ) ))
s.add(Implies( (rule3_y0 > 0), And(True, ) ))
s.add(Implies( (rule4_y0 > 0), And(nsntNoCF_y0>=1, ) ))
s.add(Implies( (rule5_y0 > 0), And(nsntNoCF_y0==0, nsntYesCF_y0>=N, ) ))
s.add(Implies( (rule6_y0 > 0), And(True, ) ))
s.add(Implies( (rule7_y0 > 0), And(True, ) ))
s.add(Implies( (rule8_y0 > 0), And(True, ) ))
s.add(Implies( (rule9_y0 > 0), And(True, ) ))
s.add(Implies( (rule10_y0 > 0), And(True, ) ))
s.add(Implies( (rule11_y0 > 0), And(True, ) ))
s.add(Implies( (rule12_y0 > 0), And(True, ) ))
s.add(Implies( (rule13_y0 > 0), And(True, ) ))
s.add(Implies( (rule14_y0 > 0), And(True, ) ))
s.add(Implies( (rule15_y0 > 0), And(True, ) ))

##################Step 5########################


#Ensuring that at most one rule is fired alternating configurations y0 and x0, if a fall condition is present


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






###################Step 2####################


#Flow equations for the locations

s.add(0 - rule0_y1 - rule6_y1 ==  locNO_x2 - locNO_y1)
s.add(0 - rule1_y1 - rule8_y1 ==  locYES_x2 - locYES_y1)
s.add(0 - rule2_y1 - rule7_y1 ==  locFDNO_x2 - locFDNO_y1)
s.add(0 - rule3_y1 - rule9_y1 ==  locFDYES_x2 - locFDYES_y1)
s.add(0 + rule0_y1 + rule1_y1 - rule4_y1 - rule5_y1 - rule10_y1 - rule13_y1 + rule13_y1 ==  locSE_x2 - locSE_y1)
s.add(0 + rule5_y1 - rule11_y1 - rule14_y1 + rule14_y1 ==  locCMT_x2 - locCMT_y1)
s.add(0 + rule2_y1 + rule3_y1 + rule4_y1 - rule12_y1 - rule15_y1 + rule15_y1 ==  locABR_x2 - locABR_y1)
s.add(0 + rule6_y1 + rule7_y1 + rule8_y1 + rule9_y1 + rule10_y1 + rule11_y1 + rule12_y1 ==  locCR_x2 - locCR_y1)






##################Step 3########################


#Flow equations for the shared variables

s.add(0 + rule0_y1 == nsntNoCF_x2 - nsntNoCF_y1)
s.add(0 + rule1_y1 == nsntYesCF_x2 - nsntYesCF_y1)






####################Step 4########################


#Rule is fired implies rule is enabled

s.add(Implies( (rule0_y1 > 0), And(True, ) ))
s.add(Implies( (rule1_y1 > 0), And(True, ) ))
s.add(Implies( (rule2_y1 > 0), And(True, ) ))
s.add(Implies( (rule3_y1 > 0), And(True, ) ))
s.add(Implies( (rule4_y1 > 0), And(nsntNoCF_y1>=1, ) ))
s.add(Implies( (rule5_y1 > 0), And(nsntNoCF_y1==0, nsntYesCF_y1>=N, ) ))
s.add(Implies( (rule6_y1 > 0), And(True, ) ))
s.add(Implies( (rule7_y1 > 0), And(True, ) ))
s.add(Implies( (rule8_y1 > 0), And(True, ) ))
s.add(Implies( (rule9_y1 > 0), And(True, ) ))
s.add(Implies( (rule10_y1 > 0), And(True, ) ))
s.add(Implies( (rule11_y1 > 0), And(True, ) ))
s.add(Implies( (rule12_y1 > 0), And(True, ) ))
s.add(Implies( (rule13_y1 > 0), And(True, ) ))
s.add(Implies( (rule14_y1 > 0), And(True, ) ))
s.add(Implies( (rule15_y1 > 0), And(True, ) ))

##################Step 5########################


#Ensuring that at most one rule is fired alternating configurations y1 and x1, if a fall condition is present


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






###################Step 2####################


#Flow equations for the locations

s.add(0 - rule0_y2 - rule6_y2 ==  locNO_x3 - locNO_y2)
s.add(0 - rule1_y2 - rule8_y2 ==  locYES_x3 - locYES_y2)
s.add(0 - rule2_y2 - rule7_y2 ==  locFDNO_x3 - locFDNO_y2)
s.add(0 - rule3_y2 - rule9_y2 ==  locFDYES_x3 - locFDYES_y2)
s.add(0 + rule0_y2 + rule1_y2 - rule4_y2 - rule5_y2 - rule10_y2 - rule13_y2 + rule13_y2 ==  locSE_x3 - locSE_y2)
s.add(0 + rule5_y2 - rule11_y2 - rule14_y2 + rule14_y2 ==  locCMT_x3 - locCMT_y2)
s.add(0 + rule2_y2 + rule3_y2 + rule4_y2 - rule12_y2 - rule15_y2 + rule15_y2 ==  locABR_x3 - locABR_y2)
s.add(0 + rule6_y2 + rule7_y2 + rule8_y2 + rule9_y2 + rule10_y2 + rule11_y2 + rule12_y2 ==  locCR_x3 - locCR_y2)






##################Step 3########################


#Flow equations for the shared variables

s.add(0 + rule0_y2 == nsntNoCF_x3 - nsntNoCF_y2)
s.add(0 + rule1_y2 == nsntYesCF_x3 - nsntYesCF_y2)






####################Step 4########################


#Rule is fired implies rule is enabled

s.add(Implies( (rule0_y2 > 0), And(True, ) ))
s.add(Implies( (rule1_y2 > 0), And(True, ) ))
s.add(Implies( (rule2_y2 > 0), And(True, ) ))
s.add(Implies( (rule3_y2 > 0), And(True, ) ))
s.add(Implies( (rule4_y2 > 0), And(nsntNoCF_y2>=1, ) ))
s.add(Implies( (rule5_y2 > 0), And(nsntNoCF_y2==0, nsntYesCF_y2>=N, ) ))
s.add(Implies( (rule6_y2 > 0), And(True, ) ))
s.add(Implies( (rule7_y2 > 0), And(True, ) ))
s.add(Implies( (rule8_y2 > 0), And(True, ) ))
s.add(Implies( (rule9_y2 > 0), And(True, ) ))
s.add(Implies( (rule10_y2 > 0), And(True, ) ))
s.add(Implies( (rule11_y2 > 0), And(True, ) ))
s.add(Implies( (rule12_y2 > 0), And(True, ) ))
s.add(Implies( (rule13_y2 > 0), And(True, ) ))
s.add(Implies( (rule14_y2 > 0), And(True, ) ))
s.add(Implies( (rule15_y2 > 0), And(True, ) ))

##################Step 5########################


#Ensuring that at most one rule is fired alternating configurations y2 and x2, if a fall condition is present


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






###################Step 2####################


#Flow equations for the locations

s.add(0 - rule0_y3 - rule6_y3 ==  locNO_x4 - locNO_y3)
s.add(0 - rule1_y3 - rule8_y3 ==  locYES_x4 - locYES_y3)
s.add(0 - rule2_y3 - rule7_y3 ==  locFDNO_x4 - locFDNO_y3)
s.add(0 - rule3_y3 - rule9_y3 ==  locFDYES_x4 - locFDYES_y3)
s.add(0 + rule0_y3 + rule1_y3 - rule4_y3 - rule5_y3 - rule10_y3 - rule13_y3 + rule13_y3 ==  locSE_x4 - locSE_y3)
s.add(0 + rule5_y3 - rule11_y3 - rule14_y3 + rule14_y3 ==  locCMT_x4 - locCMT_y3)
s.add(0 + rule2_y3 + rule3_y3 + rule4_y3 - rule12_y3 - rule15_y3 + rule15_y3 ==  locABR_x4 - locABR_y3)
s.add(0 + rule6_y3 + rule7_y3 + rule8_y3 + rule9_y3 + rule10_y3 + rule11_y3 + rule12_y3 ==  locCR_x4 - locCR_y3)






##################Step 3########################


#Flow equations for the shared variables

s.add(0 + rule0_y3 == nsntNoCF_x4 - nsntNoCF_y3)
s.add(0 + rule1_y3 == nsntYesCF_x4 - nsntYesCF_y3)






####################Step 4########################


#Rule is fired implies rule is enabled

s.add(Implies( (rule0_y3 > 0), And(True, ) ))
s.add(Implies( (rule1_y3 > 0), And(True, ) ))
s.add(Implies( (rule2_y3 > 0), And(True, ) ))
s.add(Implies( (rule3_y3 > 0), And(True, ) ))
s.add(Implies( (rule4_y3 > 0), And(nsntNoCF_y3>=1, ) ))
s.add(Implies( (rule5_y3 > 0), And(nsntNoCF_y3==0, nsntYesCF_y3>=N, ) ))
s.add(Implies( (rule6_y3 > 0), And(True, ) ))
s.add(Implies( (rule7_y3 > 0), And(True, ) ))
s.add(Implies( (rule8_y3 > 0), And(True, ) ))
s.add(Implies( (rule9_y3 > 0), And(True, ) ))
s.add(Implies( (rule10_y3 > 0), And(True, ) ))
s.add(Implies( (rule11_y3 > 0), And(True, ) ))
s.add(Implies( (rule12_y3 > 0), And(True, ) ))
s.add(Implies( (rule13_y3 > 0), And(True, ) ))
s.add(Implies( (rule14_y3 > 0), And(True, ) ))
s.add(Implies( (rule15_y3 > 0), And(True, ) ))

##################Step 5########################


#Ensuring that at most one rule is fired alternating configurations y3 and x3, if a fall condition is present


#############Additional step for the final configuration#####################


###########Ensure that the last configuration satisfies the final condition#############

s.add(Or(locABR_y4 != 0, locABR_y4 != 0))






if s.check() == sat:

	print("Specification not satisfied")

else:

	print("Specification satisfied")
