participantes =[]
while true:
    print("1. AGREGAR PARTICIPANTES")
    print("2. MOSTRAR PARTICIPANTES POR NOMBRE")
    print("3. MOSTRAR PARTICIPANTES POR EDAD")
    print("4.  SALIR")
    opcion=input("elija una opcion")
    if opcion =="1":
        while True:
            dorsal=input("ingrese numero dorsal")
            nombre=input("ingrese nombre completo")
            edad=int(input("ingrese edad"))
            categoria=input("ingrese categoria")

            participantes.append({
                "dorsal":dorsal,
                "nombre":nombre,
                "edad":edad,
                "categoria":categoria
            })
    elif opcion =="2":
        print("participantes ordenados por nombre")
        ordenados=
    elif opcion=="3":
        print("participantes ordenados por edad")
    elif opcion =="4":
        print("saliendo del programa")
        break

    else:
        print("opcion invalida")

