import serial
import json

ser = serial.Serial('/dev/tty.usbserial-0001')
j = open('magnetic_data_parking2.json','w')

data = {}
data['field'] = []
data['distance'] = []

try:
    while True:
        line = str(ser.readline())
        print(line)
        line = line[2:-5]
        data['distance'] += [float(line.split(',')[0])]
        data['field'] += [int(line.split(',')[1])]
except KeyboardInterrupt:
    pass

json.dump(data, j)
j.close()
ser.close()