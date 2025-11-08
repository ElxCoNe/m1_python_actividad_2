animals = []

while True:

    print("1.Crear un nuevo animal \n2.Listar todos los animales \n3.Borrar un animal por ID(posicion \n4.Borrar un animal por nombre \n5.Borrar todos los animales \n6. Listar un animal por ID(posicion \n7.Salir")
    
    option = int(input("Por favor selecciona la opción que deseas: "))

    match option:

        case 1:
            animal = input("Que animal deseas agregar: ")
            animals.append(animal)
        
        case 2:
            if animals:
                print("Estos son los animales que tienes al momento..")
                for i, animal in enumerate(animals):
                    print(f"{i+1} - {animal}")
            else:
                print("No hay animales en la lista hasta el momento, por favor agregar alguno")

        case 3:
            idDelete = int(input("Por favor ingresar el ID del animal que deseas eliminar: "))
            delete = animals.pop(idDelete)
            print(f"Haz eliminado {delete} de la lista con exito")

        case 4:
            deleteName = input("Por favor ingresar el nombre del animal que deseas eliminar: ")
            animals.remove(deleteName)

        case 5:
            animals.clear()
            print("Haz eliminado los animlaes de la lista exitosamente")

        case 6:
            animalPrint = int(input("Por favor ingresar el id del animal que deseas listar"))
            print(f"El animal es: {animals[animalPrint]}")
        
        case 7:
            break

        case _:
            print("La opción seleccionada no existe, por favor volver a intentarlo")








            

        


