import serial
import json

ser = serial.Serial('COM1')
j = open('magnetic_data.json','wb')

data = {}
data['filed'] = []
data['distance'] = []

try:
    while True:
        line = str(ser.readline())
        data['distance'] += float(line.split(',')[0])
        data['field'] += int(line.split(',')[1])
except KeyboardInterrupt:
    pass

json.dump(data, j)
j.close()