 
class menu():
    nombre = ""
    apellido = ""
    edad=""
    listaUsuarios = []

    #crear
    def create(self):
        self.nombre=input(f"Digite su nombre: ")
        self.apellido=input(f"Digite su apellido: ")
        self.edad=input("Digite su edad: ")
        self.datos={
            "Nombre:"+ self.nombre,
            "Apellido:"+ self.apellido,
            "Edad:"+ self.edad
        }

        self.listaUsuarios.append(self.datos)


    def show(self):
        for x in self.listaUsuarios:
            print(x)
        

    def delete(self):
        delete=int(input("ingrese la posicion en digito que desea eliminar: "))
        #self.datos.clear()
        self.listaUsuarios.pop(delete)
        input("usuario eleiminado correctamente: ")

p1 = menu()

ciclo = True



while ciclo:
    opcion = int(input('''
    Por favor eliga una opcion
    
    1) > seleccione esta opcion para añadir a un usario:
    2) > seleccione esta opcion para eliminar un usuario
    3) > Mostrar los usarios de esta lista
    0) > Salir   
     :  '''))

    if opcion == 1:
       
        p1.create()
        


    elif opcion == 2:
        print('Eliminar  elementos')

        p1.delete()

    elif opcion == 3:
        print('Mostrar todos los elementos')
        p1.show()

    elif opcion == 0:
        print('Saliendo del programa...')
        ciclo = False

    else:
        print('Por favor seleccionar una opcion valida')