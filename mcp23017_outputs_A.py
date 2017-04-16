import smbus
import time

#bus = smbus.SMBus(0)  # Rev 1 Pi uses 0
bus = smbus.SMBus(1) # Rev 2 Pi uses 1

DEVICE = 0x20 # Device address (A0-A2)
IODIRA = 0x00 # Pin direction register
OLATA  = 0x14 # Output latch register
GPIOA  = 0x12 # GPIO port register

# Set all GPA pins as outputs by setting
# all bits of IODIRA register to 0
bus.write_byte_data(DEVICE,IODIRA,0x00)

# Set all 8 output bits to 0
bus.write_byte_data(DEVICE,GPIOA,0)


# Outputs_A()
  
# Set all bits to zero
bus.write_byte_data(DEVICE,OLATA,0)
