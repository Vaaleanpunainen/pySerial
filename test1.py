import serial

#open serial port
#bound rate on two ports must be the same

ser = serial.Serial('COM1', 9600)
print("Port opened on " + ser.name)

if ser.isOpen() == False:
    ser.open()

#send data via serial port
print('Enter your message below.\r\nInsert "exit" to leave the application.')

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

ser.close()
