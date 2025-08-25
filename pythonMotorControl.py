import pyfirmata
import time
board = pyfirmata.Arduino('/dev/cu.usbmodem22301')

def run(pin, n):
  for i in range(n):
    board.digital[pin].write(1)  # set to 1, not rotate
    time.sleep(0.5)
    board.digital[pin].write(0)  # set to 0 to rotate
    time.sleep(0.5)

run(12,1)
commands = [(i) for i in input().split()]
for i in commands:
    #if commands
    if i == 'R1':   "Right 1 time clockwise"
    run(3, 1)
    if i == 'R2':
      run(3, 2)
    if i == 'R3':
      run(2, 1)
    if i == 'L1':
      run(9, 1)
    if i == 'L2':
      run(9, 2)
    if i == 'L3':
      run(8, 1)
    if i == 'U1':
      run(11, 1)
    if i == 'U2':
      run(11, 2)
    if i == 'U3':
      run(10, 1)
    if i == 'D1':
      run(12, 1)
    if i == 'D2':
      run(12, 2)  
    if i == 'D3':
      run(13, 1)
    if i == 'F1':
      run(7, 1)
    if i == 'F2':
      run(7, 2)
    if i == 'F3':
      run(6, 1)
    if i == 'B1':
      run(5, 1)
    if i == 'B2':
      run(5, 2)
    if i == 'B3':
      run(4, 1)








