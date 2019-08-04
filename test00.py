import serial

ser1=serial.Serial(
port='COM1',
baudrate=9600,
parity=serial.PARITY_NONE,
stopbits=serial.STOPBITS_ONE,
bytesize=serial.EIGHTBITS,
timeout=1
)

ser2=serial.Serial(
port='COM2',
baudrate=9600,
parity=serial.PARITY_NONE,
stopbits=serial.STOPBITS_ONE,
bytesize=serial.EIGHTBITS,
timeout=1
)


if ser1.isOpen():
     print(ser1.name + ' is open...')

if ser2.isOpen():
     print(ser2.name + ' is open...')

print('Enter your message below.\r\nInsert "exit" to leave the application.')

value1 = ""
value2 = ""

while True:
    value1 = input(">> COM1 sends: ")
    value2 = input(">> COM2 sends: ")
    if value1 and value2 == 'exit':
        ser1.close()
        ser2.close()
        exit()
    else:
        ser1.write(str.encode(str(value1)))
        ser2.write(str.encode(str(value2)))

        output1 = ser1.readline().decode('ascii')
        output2 = ser2.readline().decode('ascii')

        print(">> COM 1 received:")
        print(output1)
        print(">> COM 2 received:")
        print(output2)
        print("Next session...")
        print('Enter your message below.\r\nInsert "exit" to leave the application.')
