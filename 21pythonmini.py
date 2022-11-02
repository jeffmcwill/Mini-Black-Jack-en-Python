import random
import time

lista=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21]
puntajeGanador=[]
puntajePerdedor=[]
cantidadPartidas=[]

def sumarPuntajes(lista):
    suma=0
    for elem in lista:
        suma+=elem
    return suma

def Juego():
    print("--------------------------------")
    print("- Mini BlackJack en Python v.1 -")
    print("--------------------------------")
    print("Codificado por Jeff McWill.")
    time.sleep(1)
    print("Cargando")
    time.sleep(1)
    print("Preparando baraja...")
    time.sleep(1)
    print("Mezclando cartas")
    time.sleep(1)
    print("Ordenando mesa...")
    time.sleep(1)
    print("¡Comienza!")
    
    user=0

    while user != 2:
        try:
            print("---------------------------")
            usuario=int(input("presione 1 para jugar: "))
            if usuario <= 21:
                bot=random.choice(lista)
                usuario=random.choice(lista)

                if usuario > bot:
                    print("------------------")
                    print(">Tu: ",usuario)
                    print(">Bot: ",bot)
                    print("------------------")                    
                    ganar=1
                    juego=1
                    puntajeGanador.append(ganar)
                    cantidadPartidas.append(juego)
                    print("Usuario gana :3")
                    print(f"Partidas ganadas: {sumarPuntajes(puntajeGanador)}")
                    print("------------------")

                    user=int(input("2 para salir: "))
                    if user == 2:
                        print("Ok hasta luego.")
                        print("-------------------------")
                        print(f"Partidas Ganadas: {sumarPuntajes(puntajeGanador)}")
                        print(f"Partidas Perdidas: {sumarPuntajes(puntajePerdedor)}")
                        print(f"Total partidas: {sumarPuntajes(cantidadPartidas)}")
                        print("-------------------------")

                        if sumarPuntajes(puntajeGanador) > sumarPuntajes(puntajePerdedor):
                            print("¡GANASTE :D!")
                            time.sleep(5)

                        else:
                            print("Perdiste... :c")
                            time.sleep(5)
                    
                    elif user != 2:
                        print("Ok sigamos jugando")


                elif usuario < bot:
                    print("------------------")
                    print(">Tu: ",usuario)
                    print(">Bot: ",bot)
                    print("------------------")
                    perder=1
                    juego=1
                    puntajePerdedor.append(perder)
                    cantidadPartidas.append(juego)
                    print("Bot gana :c")
                    print(f"Puntaje Perdedor: {sumarPuntajes(puntajePerdedor)}")
                    print("------------------")

                    user=int(input("2 para salir: "))
                    if user == 2:
                        print("Ok, hasta luego.")
                        print("-------------------------")
                        print(f"Partidas Ganadas: {sumarPuntajes(puntajeGanador)}")
                        print(f"Partidas Perdidas: {sumarPuntajes(puntajePerdedor)}")
                        print(f"Total partidas: {sumarPuntajes(cantidadPartidas)}")
                        print("-------------------------")

                        if sumarPuntajes(puntajeGanador) > sumarPuntajes(puntajePerdedor):
                            print("¡GANASTE :D!")
                            time.sleep(5)

                        else:
                            print("Perdiste... :c")
                            time.sleep(5)

                    elif user != 2:
                        print("Ok, sigamos jugando.")
                    
                elif usuario == bot:
                    print("------------------")
                    print(">Tu: ",usuario)
                    print(">Bot: ",bot)
                    print("------------------")
                    juego=1
                    cantidadPartidas.append(juego)
                    print("Empate.")
                    print(f"Cantidad de partidas hasta ahora: {sumarPuntajes(cantidadPartidas)}")
                    print("--------------------------------------")
                    

                    user=int(input("2 para salir: "))
                    if user == 2:
                        print("Ok hasta luego.")
                        print("-------------------------")
                        print(f"Partidas Ganadas: {sumarPuntajes(puntajeGanador)}")
                        print(f"Partidas Perdidas: {sumarPuntajes(puntajePerdedor)}")
                        print(f"Total partidas: {sumarPuntajes(cantidadPartidas)}")
                        print("-------------------------")

                        if sumarPuntajes(puntajeGanador) > sumarPuntajes(puntajePerdedor):
                            print("¡GANASTE :D!")
                            time.sleep(5)

                        else:
                            print("Perdiste... :c")
                            time.sleep(5)

                    elif user != 2:
                        print("Ok sigamos jugando.")
            else:
                print("Algun error o comando mal implementado.")
                continue
        except:
            print("Presione solo numero 1.")

if __name__ == "__main__":
    Juego()

    
