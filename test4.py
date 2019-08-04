import serial

ser=serial.Serial(
port='COM4',
baudrate=9600,
parity=serial.PARITY_NONE,
stopbits=serial.STOPBITS_ONE,
bytesize=serial.EIGHTBITS,
timeout=1
)

#time.sleep(1);

if ser.isOpen():
     print(ser.name + ' is open...')

print('Enter your message below.\r\nInsert "exit" to leave the application.')

value = ""

while True:
    value = input(">> ")
    if value == 'exit':
        ser.close()
        exit()
    else:
        ser.write(str.encode(str(value)))
        outputs = ser.readline().decode('ascii')
        print(outputs)
