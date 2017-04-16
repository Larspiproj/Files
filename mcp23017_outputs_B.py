#!/usr/bin/python

import smbus
import time
import mcp23017_outputs_A

#bus = smbus.SMBus(0)  # Rev 1 Pi uses 0
bus = smbus.SMBus(1) # Rev 2 Pi uses 1

DEVICE = 0x20 # Device address (A0-A2)
IODIRB = 0x01 # Pin direction register
OLATB  = 0x15 # Output latch register
GPIOB  = 0x13 # GPIO port register

# Set all GPB pins as outputs by setting
# all bits of IODIRB register to 0
bus.write_byte_data(DEVICE,IODIRB,0x00)

# Set all 8 output bits to 0
bus.write_byte_data(DEVICE,GPIOB,0)

def Outputs_A():
  print("A0")
  for MyData in range(1,9):
    # Count from 1 to 9 which in binary will count 
    # from 001 to 1111
    bus.write_byte_data(DEVICE,GPIOA,MyData)
    print (MyData)
    time.sleep(2)


def Outputs_B():
  for MyData in range(1,9):
    # Count from 1 to 9 which in binary will count 
    # from 001 to 1111
    bus.write_byte_data(DEVICE,GPIOB,MyData)
    print (MyData)
    time.sleep(2)

print("A") 
Outputs_A()
print("B")
Outputs_B()
print("slut")
  
# Set all bits to zero
bus.write_byte_data(DEVICE,OLATB,0)
