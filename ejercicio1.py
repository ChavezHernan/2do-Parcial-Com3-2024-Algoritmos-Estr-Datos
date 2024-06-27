import datetime

class Fecha:
    def _init_(self, dia=None, mes=None, anio=None):
        if dia is None or mes is None or anio is None:
            hoy = datetime.date.today()
            self.dia = hoy.day
            self.mes = hoy.month
            self.anio = hoy.year
        else:
            self.dia = dia
            self.mes = mes
            self.anio = anio

    def calcular_dif_fecha(self, otra_fecha):

        fecha1 = datetime.date(self.anio, self.mes, self.dia)
        fecha2 = datetime.date(otra_fecha.anio, otra_fecha.mes, otra_fecha.dia)
        diferencia = abs(fecha1 - fecha2)
        return diferencia.days

    def _str_(self):
        return (f"{self.dia:02d}/{self.mes:02d}/{self.anio}")

    def _add_(self, dias):
        nueva_fecha = datetime.date(self.anio, self.mes, self.dia) + datetime.timedelta(days=dias)
        return Fecha(nueva_fecha.day, nueva_fecha.month, nueva_fecha.year)

    def _eq_(self, otra_fecha):
        return self.dia == otra_fecha.dia and self.mes == otra_fecha.mes and self.anio == otra_fecha.anio

# Ejemplo de uso
fecha1 = Fecha(15, 3, 2023)
print(fecha1)  

fecha2 = Fecha()
print(fecha2)  

diferencia = fecha1.calcular_dif_fecha(fecha2)
print(f"La diferencia es de {diferencia} días")

nueva_fecha = fecha1 + 10
print(nueva_fecha) 

print(fecha1 == fecha2) 

# Ejercicio 2

from datetime import date

class Alumno(dict):
    def _init_(self, nombre, dni, fecha_ingreso, carrera):
        self["Nombre"] = nombre
        self["DNI"] = dni
        self["FechaIngreso"] = fecha_ingreso
        self["Carrera"] = carrera

    def cambiar_datos(self, **kwargs):
         for key, value in kwargs.items():
            if key in self:
                self[key] = value
            else:
                raise KeyError(f"El atributo '{key}' no existe en la clase Alumno.")

    def antiguedad(self):
        hoy = date.today()
        fecha_ingreso = self["FechaIngreso"]
        antiguedad = hoy.year - fecha_ingreso.year
        if hoy.month < fecha_ingreso.month or (hoy.month == fecha_ingreso.month and hoy.day < fecha_ingreso.day):
            antiguedad -= 1
        return antiguedad

    def _str_(self):
        return f"Nombre: {self['Nombre']}, DNI: {self['DNI']}, Fecha de Ingreso: {self['FechaIngreso']}, Carrera: {self['Carrera']}"

    def _eq_(self, otro_alumno):
        return self["DNI"] == otro_alumno["DNI"]

# Ejemplo de uso
fecha_ingreso = date(2020, 3, 15)
alumno1 = Alumno("Marcelo Diaz", 12345678, fecha_ingreso, "Ingeniería Informática")
print(alumno1)

alumno1.cambiar_datos(Nombre="Lucas Gomez", Carrera="Licenciatura en Sistemas")
print(alumno1) 

alumno2 = Alumno("María Perez", 87654321, date(2018, 8, 1), "Economía")
print(alumno2.antiguedad()) 
print(alumno1 == alumno2)  

#Ejercicio 3 

from datetime import date, timedelta
import random

class Nodo:
    def _init_(self, dato):
        self.dato = dato
        self.siguiente = None
        self.anterior = None

class ListaDoblementeEnlazada:
    def _init_(self):
        self.cabeza = None
        self.cola = None
        self.longitud = 0

    def agregar_nodo(self, nuevo_nodo):
        if self.cabeza is None:
            self.cabeza = self.cola = nuevo_nodo
        else:
            self.cola.siguiente = nuevo_nodo
            nuevo_nodo.anterior = self.cola
            self.cola = nuevo_nodo
        self.longitud += 1

    def _iter_(self):
        self.nodo_actual = self.cabeza
        return self

    def _next_(self):
        if self.nodo_actual is None:
            raise StopIteration
        dato = self.nodo_actual.dato
        self.nodo_actual = self.nodo_actual.siguiente
        return dato

    def lista_ejemplo(self, cantidad_alumnos=10):
        nombres = ["Marcelo", "María", "Lucas", "Ana", "Carlos", "Sofía", "Luis", "Juana", "Ernesto", "Lucía"]
        carreras = ["Ingeniería Informática", "Medicina", "Derecho", "Economía", "Diseño Gráfico", "Psicología"]

        for _ in range(cantidad_alumnos):
            nombre = random.choice(nombres)
            dni = random.randint(10000000, 99999999)
            fecha_ingreso = date.today() - timedelta(days=random.randint(365, 3650))
            carrera = random.choice(carreras)
            alumno = Alumno(nombre, dni, fecha_ingreso, carrera)
            self.agregar_nodo(Nodo(alumno))

        return self

# Ejemplo de uso
lista_alumnos = ListaDoblementeEnlazada().lista_ejemplo()

for alumno in lista_alumnos:
    print(alumno)


#Ejercicio 4

    from datetime import date, timedelta
import random

class Nodo:
    def _init_(self, dato):
        self.dato = dato
        self.siguiente = None
        self.anterior = None

class ListaDoblementeEnlazada:
    def _init_(self):
        self.cabeza = None
        self.cola = None
        self.longitud = 0

    def agregar_nodo(self, nuevo_nodo):
        if self.cabeza is None:
            self.cabeza = self.cola = nuevo_nodo
        else:
            self.cola.siguiente = nuevo_nodo
            nuevo_nodo.anterior = self.cola
            self.cola = nuevo_nodo
        self.longitud += 1

    def _iter_(self):
        self.nodo_actual = self.cabeza
        return self

    def _next_(self):
        if self.nodo_actual is None:
            raise StopIteration
        dato = self.nodo_actual.dato
        self.nodo_actual = self.nodo_actual.siguiente
        return dato

    def lista_ejemplo(self, cantidad_alumnos=10):
        nombres = ["Marcelo", "María", "Lucas", "Ana", "Carlos", "Sofía", "Luis", "Juana", "Ernesto", "Lucía"]
        carreras = ["Ingeniería Informática", "Medicina", "Derecho", "Economía", "Diseño Gráfico", "Psicología"]

        for _ in range(cantidad_alumnos):
            nombre = random.choice(nombres)
            dni = random.randint(10000000, 99999999)
            fecha_ingreso = date.today() - timedelta(days=random.randint(365, 3650))
            carrera = random.choice(carreras)
            alumno = Alumno(nombre, dni, fecha_ingreso, carrera)
            self.agregar_nodo(Nodo(alumno))

        return self

    def ordenar_por_fecha_ingreso(self):
        if self.cabeza is None or self.cabeza.siguiente is None:
            return
        self.cabeza = self.quicksort(self.cabeza)

    def quicksort(self, nodo):
        if nodo is None or nodo.siguiente is None:
            return nodo

        pivote = nodo
        izquierda = nodo.siguiente
        derecha = nodo.siguiente

        while derecha is not None:
            if derecha.dato.fecha_ingreso < pivote.dato.fecha_ingreso:
                
                derecha.dato, izquierda.dato = izquierda.dato, derecha.dato
                izquierda = izquierda.siguiente
            derecha = derecha.siguiente

        pivote.dato, izquierda.dato = izquierda.dato, pivote.dato

        self.quicksort(nodo)
        self.quicksort(izquierda.siguiente)

        return nodo

# Ejemplo de uso
lista_alumnos = ListaDoblementeEnlazada().lista_ejemplo()
print("Lista original:")
for alumno in lista_alumnos:
    print(alumno)

lista_alumnos.ordenar_por_fecha_ingreso()
print("\nLista ordenada por fecha de ingreso:")
for alumno in lista_alumnos:
    print(alumno)


#Ejercicio 5

    import os
from datetime import date, timedelta
import random

class Alumno:
    def _init_(self, nombre, dni, fecha_ingreso, carrera):
        self.nombre = nombre
        self.dni = dni
        self.fecha_ingreso = fecha_ingreso
        self.carrera = carrera

    def _str_(self):
        return f"{self.nombre}, DNI: {self.dni}, Fecha de Ingreso: {self.fecha_ingreso.strftime('%Y-%m-%d')}, Carrera: {self.carrera}"

class ListaDoblementeEnlazada:
    def _init_(self):
        self.cabeza = None
        self.cola = None
        self.longitud = 0
    def agregar_nodo(self, nuevo_nodo):
        if self.cabeza is None:
            self.cabeza = self.cola = nuevo_nodo
        else:
            self.cola.siguiente = nuevo_nodo
            nuevo_nodo.anterior = self.cola
            self.cola = nuevo_nodo
        self.longitud += 1

    def _iter_(self):
        self.nodo_actual = self.cabeza
        return self

    def _next_(self):
        if self.nodo_actual is None:
            raise StopIteration
        dato = self.nodo_actual.dato
        self.nodo_actual = self.nodo_actual.siguiente
        return dato

    def lista_ejemplo(self, cantidad_alumnos=10):
        nombres = ["Marcelo", "María", "Lucas", "Ana", "Carlos", "Sofía", "Luis", "Juana", "Ernesto", "Lucía"]
        carreras = ["Ingeniería Informática", "Medicina", "Derecho", "Economía", "Diseño Gráfico", "Psicología"]

        for _ in range(cantidad_alumnos):
            nombre = random.choice(nombres)
            dni = random.randint(10000000, 99999999)
            fecha_ingreso = date.today() - timedelta(days=random.randint(365, 3650))
            carrera = random.choice(carreras)
            alumno = Alumno(nombre, dni, fecha_ingreso, carrera)
            self.agregar_nodo(Nodo(alumno))

        return self

    def crear_directorio(directorio):
        try: os.mkdir(directorio)
        
        print(f"Directorio '{directorio}' creado exitosamente.")
        except OSError as e:
        print(f"Error al crear el directorio '{directorio}': {e}")

    def guardar_lista_alumnos(directorio, nombre_archivo, lista_alumnos):
    try:
        archivo_path = os.path.join(directorio, nombre_archivo)
        with open(archivo_path, "w") as archivo:
            for alumno in lista_alumnos:
                archivo.write(str(alumno) + "\n")
        print(f"Archivo '{nombre_archivo}' guardado en el directorio '{directorio}'.")
        except OSError as e:
        print(f"Error al guardar el archivo '{nombre_archivo}' en el directorio '{directorio}': {e}")

    def mover_directorio(directorio_origen, directorio_destino):
    try:
        os.rename(directorio_origen, directorio_destino)
        print(f"Directorio '{directorio_origen}' movido a '{directorio_destino}'.")
    except OSError as e:
        print(f"Error al mover el directorio '{directorio_origen}' a '{directorio_destino}': {e}")

    def borrar_archivo_y_directorio(directorio, nombre_archivo):
    try:
        archivo_path = os.path.join(directorio, nombre_archivo)
        os.remove(archivo_path)
        print(f"Archivo '{nombre_archivo}' eliminado.")
        os.rmdir(directorio)
        print(f"Directorio '{directorio}' eliminado.")
    except OSError as e:
        print(f"Error al eliminar el archivo '{nombre_archivo}' o el directorio '{directorio}': {e}")

# Ejemplo de uso
directorio_origen = "alumnos"
directorio_destino = "alumnos_movido"
nombre_archivo = "lista_alumnos.txt"

# Crear directorio
crear_directorio(directorio_origen)

# Guardar lista de alumnos en el archivo
lista_alumnos = ListaDoblementeEnlazada().lista_ejemplo()
guardar_lista_alumnos(directorio_origen, nombre_archivo, lista_alumnos)

# Mover el directorio
mover_directorio(directorio_origen, directorio_destino)

# Borrar archivo y directorio
borrar_archivo_y_directorio(directorio_destino, nombre_archivo)
