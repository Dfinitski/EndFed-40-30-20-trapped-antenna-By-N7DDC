#!/usr/bin/env python3
#                      C_ser         L_trap                     lower freq side
#        --------------||---o---/\/\/\/\/\/\/\----o------------------------------
#                           |                     |
#                           |----------||---------|
#                                     C_trap
# Compensation capacitance calculation
# N7DDC

pi = 3.1415926535

# Enter trap parameters
L_trap = 3.86  # in microHenry
C_trap = 33    # in picoFarads 
Freq = 7.1     # in MHz
omega = 2*pi*Freq*1000000
C1 = C_trap/1000/1000/1000/1000
L1 = L_trap/1000/1000
ZC1 = 1/(1j*omega*C1)
ZL1 = 1j*omega*L1
Z_trap = ZC1*ZL1/(ZC1+ZL1)

C_ser = 1/(1j*omega*Z_trap)*1000*1000*1000*1000


print("X_C_trap = ", ZC1)
print("X_L_trap = ", ZL1)
print("Z_trap = ", Z_trap)
print("C_ser = ", round(C_ser.real, 1)*-1, " pF")

