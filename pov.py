#!/usr/bin/python 
# programme PorteOcculaireVma
#
# USAGE :
#   pov.py {c|a} countstep
#

debug = 1

import RPi.GPIO as GPIO
import time
import sys

if int(len(sys.argv)) < 3:
  print("USAGE : pov.py {c|a} countstep")
  exit()

sens = sys.argv[1]
if debug: print('sens=', sens)

countstep = int(sys.argv[2])
if debug: print('countstep=', countstep)

motorpin1 = 24	# GPIOO8
motorpin2 = 21	# GPIOO9
motorpin3 = 19	# GPIO10
motorpin4 = 23	# GPIO11

lookupav = ['1000','1100','0100','0110','0010','0011','0001','1001']
lookupar = ['1001','0001','0011','0010','0110','0100','1100','1000']

motorspeed = 2000
count = 0
#countstep = 1024

GPIO.setmode(GPIO.BOARD)

GPIO.setup(motorpin1, GPIO.OUT)
GPIO.setup(motorpin2, GPIO.OUT)
GPIO.setup(motorpin3, GPIO.OUT)
GPIO.setup(motorpin4, GPIO.OUT)

def clock():
  for av in lookupav:
     setoutput(av)
     time.sleep(motorspeed/1000000)
  if debug : print("clock")

def anticlock():
  for ar in lookupar:
     setoutput(ar)
     time.sleep(motorspeed/1000000)
  if debug : print("anticlock")

def setoutput(phase):
  print( phase[0], phase[1], phase[2], phase[3] )	# Print obligatoire
  GPIO.output(motorpin1,int(phase[0]))
  GPIO.output(motorpin2,int(phase[1]))
  GPIO.output(motorpin3,int(phase[2]))
  GPIO.output(motorpin4,int(phase[3]))

while count < countstep:
   if debug : print( count )
   if sens == 'c': clock()
   else: anticlock()
   time.sleep(motorspeed/1000000)
   count = count + 1

GPIO.cleanup()
