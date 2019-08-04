import serial

#open serial port
ser = serial.Serial('COM2', 9600, timeout=1)
print("Port opened on " + ser.name)


while True:
    serOutputs = ser.readline().decode('ascii')
    if len(serOutputs) >= 1:
        print(serOutputs)
