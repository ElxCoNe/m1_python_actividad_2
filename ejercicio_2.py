animals = []

while True:

    print("\n1.Crear un nuevo animal \n2.Listar todos los animales \n3.Borrar un animal por ID(posicion \n4.Borrar un animal por nombre \n5.Borrar todos los animales \n6. Listar un animal por ID(posicion \n7.Salir \n")
    
    option = int(input("Por favor selecciona la opción que deseas: "))

    match option:

        case 1:
            animal = input("\nQue animal deseas agregar: ")
            animals.append(animal)
            print(f"Haz agregado {animal} exitosamente")
        
        case 2:
            if animals:
                print("\nEstos son los animales que tienes al momento..")
                for i, animal in enumerate(animals):
                    print(f"{i+1} - {animal}")
            else:
                print("\nNo hay animales en la lista hasta el momento, por favor agregar alguno")

        case 3:
            idDelete = int(input("\nPor favor ingresar el ID del animal que deseas eliminar: "))
            delete = animals.pop(idDelete)
            print(f"\nHaz eliminado {delete} de la lista con exito")

        case 4:
            deleteName = input("\nPor favor ingresar el nombre del animal que deseas eliminar: ")
            animals.remove(deleteName)

        case 5:
            animals.clear()
            print("\nHaz eliminado los animlaes de la lista exitosamente")

        case 6:
            animalPrint = int(input("\nPor favor ingresar el id del animal que deseas listar"))
            print(f"El animal es: {animals[animalPrint]}")
        
        case 7:
            break

        case _:
            print("\nLa opción seleccionada no existe, por favor volver a intentarlo")







            

        


