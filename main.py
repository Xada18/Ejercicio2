from ClaseManejadorViajeros import ManejadorViajeros

if __name__ == '__main__':
    archivo = "viajeros.csv"
    ListaViajeros = ManejadorViajeros()
    ListaViajeros.carga(archivo)

    ban = True
    while ban:
        print("Menu")
        print("1 - Millas acumuladas")
        print("2 - Acumular millas")
        print("3 - Canjear millas")
        print("0 - Salir")
        op = input("Ingrese una opcion: ")

        
        if op == "1":
            numero = input("Ingrese numero de viajero: ")
            viajero = ListaViajeros.buscarViajero(numero)
            millas = viajero.cantidadTotalMillas()
            print(f"Millas acumuladas: {millas}")
            print("")

        elif op == "2":
            numero = input("Ingrese numero de viajero: ")
            viajero = ListaViajeros.buscarViajero(numero)
            millas_recorridas = input("Ingrese cantidad de millas recorridas: ")
            millas = viajero.acumularMillas(int(millas_recorridas))
            print(f"Millas acumuladas: {millas}")
            print("")

        elif op == "3":
            numero = input("Ingrese numero de viajero: ")
            viajero = ListaViajeros.buscarViajero(numero)
            millas_canje = input("Ingrese cantidad de millas a canjear: ")
            millas = viajero.canjearMillas(int(millas_canje))
            print(f"Millas acumuladas: {millas}")
            print("")

        elif op == "0":
            ban = False

        else:
            print("Opcion no valida")
            print("")

        
        
