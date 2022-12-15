import serial 
import time


while True: #Valida a conexão com o arduino
    try:  
        arduino = serial.Serial('COM8', 9600)
        print('Arduino conectado')
        break
    except:
        pass



while True: #Inicia o looping menu
    
        def home() :

            print("Home")
            while True :

                dados = str(arduino.readline())
                print(dados[2:-5])
                dados1 = dados[2:-5]

                if dados1 == "button1" :
                    print("Botão 1")

                if dados1 == "button2" :
                    print("Botão 2")

                if dados1 == "button3" :
                    print("Botão 3")

                if dados1 == "button4" :
                    print("Home >> Functions")
                    return secundary()

        def secundary() : #Funções secundárias

            print("Functions")
            while True :

                dados = str(arduino.readline())
                print(dados[2:-5])
                dados1 = dados[2:-5]

                if dados1 == "button1" :
                    print("Botão 1, 2")

                if dados1 == "button2" :
                    print("Botão 2, 2")

                if dados1 == "button3" :
                    print("Botão 3, 2")

                if dados1 == "button4" :
                    print("Home >> Functions")
                    return home()









