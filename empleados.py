class Empleado :
    def __init__(self,id_empleado, nombre, salario):
        self.id_empleado=id_empleado
        self.nombre=nombre
        self.salario=salario

    def calcular_bonificacion(self):
        bonificacion=self.salario * 0.1
        return bonificacion

    def mostrar_informacion(self):
        print(f"El empleado se llama {self.nombre} y"
              f" gana {self.salario}")

class Gerente(Empleado):
    def __init__(self,id_empleado,nombre,salario,departamento):
        super().__init__(id_empleado,nombre,salario)
        self.departamento=departamento
    def aprobar_proyecto(self):
        print(f"El Gerente {self.nombre} del "
              f"departamento{self.departamento},"
              f"aprueba el proyecto")
    def mostrar_informacion(self):
        info=super().mostrar_informacion()+f"del Departamento{self.departamento}"
        return info

class Departamento:
    def __init__(self,id_departamento,nombredepartamento):
            self.id_departamento=id_departamento
            self.nombredepartamento=nombredepartamento
            self.plantilla=[]
    def agregar_empleados(self,empleado):
            self.plantilla.append(empleado)
            print(f"El empleado {empleado.nombre} ha sido "
                  f"agregado a la plantilla")
    def eliminar_empleados(self,empleado):
            self.plantilla.remove(empleado)
            print(f"El empleado {empleado.nombre} ha sido"
                  f"eliminado de la plantilla")
    def listar_empleados(self,empleado):
            for empleado in self.plantilla:
                print(empleado.mostrar_informacion())

    def main(self):
            empleado1=Empleado(1,"Juan Perez",3000)
            gerente1=Gerente(2,"Maria Gómez",5000, "Ventas")
            depto=Departamento(121,"RRHH")
            empleado1.mostrar_informacion()
            print(empleado1.calcular_bonificacion())
            gerente1.mostrar_informacion()
            depto.agregar_empleados(empleado1)
            depto.agregar_empleados(gerente1)
            depto.listar_empleados()
    if __name__=="__main__":
        main()










