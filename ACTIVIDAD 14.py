participantes =[]
while True:
    print("1. AGREGAR PARTICIPANTES")
    print("2. MOSTRAR PARTICIPANTES POR NOMBRE")
    print("3. MOSTRAR PARTICIPANTES POR EDAD")
    print("4.  SALIR")
    opcion=input("elija una opcion")
    if opcion =="1":
        cantidad=int(input("ingrese el numero de participantes"))
        for _ in range(cantidad):
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
        lista=participantes[:]
        for i in range(len(lista)):
            for j in range(len(lista)):
                if lista[i]["nombre"]<lista[j]["nombre"]:
                    lista[i],lista[j]=lista[j],lista[i]
        for p in lista:
            print(f"{p["nombre"]}(dorsal{p["dorsal"]},edad{p["edad"]},categoria{p["categoria"]})")
    elif opcion=="3":
        print("participantes ordenados por edad")
        lista = participantes[:]
        for i in range(len(lista)):
            for j in range(i+1, len(lista)):
                if lista[i]["edad"]>lista[j]["edad"]:
                    lista[i],lista[j]=lista[j],lista[i]
        for p in lista:
            print(f"{p["nombre"]}(dorsal{p["dorsal"]},edad{p["edad"]},categoria{p["categoria"]})")
    elif opcion =="4":
        print("saliendo del programa")
        break

    else:
        print("opcion invalida")

