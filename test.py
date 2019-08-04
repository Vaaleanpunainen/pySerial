import time
import serial

# configure the serial connections (the parameters differs on the device you are connecting to)
ser = serial.Serial(
	port='COM1',
	baudrate=9600,
	parity=serial.PARITY_ODD,
	stopbits=serial.STOPBITS_TWO,
	bytesize=serial.SEVENBITS
)
print("Port opened on " + ser.name)

if ser.isOpen() == False:
    ser.open()

print('Enter your commands below.\r\nInsert "exit" to leave the application.')

inputs=1
while 1:
	# get keyboard input
    inputs = input(">> ")
    if inputs == 'exit':
        ser.close()
        exit()
    else:
		# send the character to the device
        ser.write(str.encode(inputs))
        out = ''
		# let's wait one second before reading output (let's give device time to answer)
        time.sleep(1)
        while ser.redlines() > 0:
            out += ser.readlines()

        if out != '':
            print(">>" + out)
