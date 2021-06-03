print("################# Cajero Automatico ###############")

dinero = 1000

menu_principal = {
    "1": "Ingresar",
    "2": "Nuevo Usuario"
}

for contador in menu_principal:
    print(menu_principal)
    contador = int(input("Escriba el numero de la opcion que desea"))
    if contador == 1:
        clave = int(input("Ingrese la clave del Usuario"))
        if clave == 1234:
            print("Clave correcta")
            opciones = {
                "1": "Retirar",
                "2": "Depositar",
                "3": "Verificar Monto",
                "4": "Salir"
            }
            print("################# MENU ###################")
            print(opciones)
        else:
            print("Escribio una clave incorrecta")
    elif contador == 2:
        print("Aqui puedes ingresar un cliente(Aun no esta disponible")
        contador += 1
    for valor in opciones:
        valor = int(input("Elija cual opcion desea efectuar"))
        if valor == 1:
            print("A escogido Retirar dinero")
            retirar = int(input("Dijite el monto que desea retirar"))
            dinero = dinero - retirar
            resp = (f"El retiro fue exitoso el monto actual es de {dinero} y el retiro fue de {retirar}")
            print(resp)

        elif valor == 2:
            print("A escogido Depositar dinero")
            depositar = int(input("Dijte el monto que desea depositar"))
            dinero = depositar + dinero
            resp = (f"El deposito fue exitoso, el monto actual es {dinero} el deposito fue de {depositar}")
            print(resp)

        elif valor == 3:
            print("A escogido Verificar Monto")
            dinero = (f"El dinero en la cuenta es: {dinero}")
            print(dinero)

        elif valor == 4:
            print("A salido del menu")
            break
        else:
            print("A ingresado un numero que NO esta en la lista")




