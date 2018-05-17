import serial
print("Antes")
ser = serial.Serial('COM6',timeout=5)  # open serial port
print("Depois")
print(ser.name)         # check which port was really used
ser.write(b'hello')     # write a string
#ser.close()             # close port

