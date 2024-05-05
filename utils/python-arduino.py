import serial

porta = "COM4"
veloc = 9600

conecao = serial.Serial(porta, veloc)

while True:
    opcao = input("A para hello word")

    if opcao == "a":
        conecao.write(b'a')



conecao.close()
