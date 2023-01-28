import serial
arduino = serial.Serial('COM6', 9600)
while True:
    leitura = str(arduino.readline())
    a = [leitura[2:-3]]
    print(a)
    arq = open('leitura.txt', 'a')
    arq.write('{}.'.format(a))
    arq.close()
arduino.close()
