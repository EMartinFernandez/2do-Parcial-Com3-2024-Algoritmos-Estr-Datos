import datetime
import random
import os

class Fecha:
    def __init__(self, dd=None, mm=None, aaaa=None):
        if dd is None or mm is None or aaaa is None:
            today = datetime.date.today()
            self.dd = today.day
            self.mm = today.month
            self.aaaa = today.year
        else:
            self.dd = dd
            self.mm = mm
            self.aaaa = aaaa

    def __str__(self):
        return f"({self.dd}, {self.mm}, {self.aaaa})"
    
    def a_datetime(self):
        return datetime.date(self.aaaa, self.mm, self.dd)

    def __add__(self, dias):
        dias_totales = self.dd + self.mm * 30 + self.aaaa * 365
        dias_totales += dias
        aaaa = dias_totales // 365
        dias_restantes = dias_totales % 365
        mm = dias_restantes // 30
        dd = dias_restantes % 30
        return Fecha(dd, mm, aaaa)

    def __eq__(self, otra_fecha):
        return (self.dd == otra_fecha.dd and
                self.mm == otra_fecha.mm and
                self.aaaa == otra_fecha.aaaa)    

    def calcular_dif_fecha(self, otra_fecha):
        dias_self = self.dd + self.mm * 30 + self.aaaa * 365
        dias_otra = otra_fecha.dd + otra_fecha.mm * 30 + otra_fecha.aaaa * 365
        diferencia_dias = (dias_self - dias_otra)
        return diferencia_dias

class alumno(dict):
    def __init__(self, nombre, dni, fecha_ingreso, carrera):
        self.nombre = nombre
        self.dni = dni
        self.fecha_ingreso = fecha_ingreso
        self.carrera = carrera

    def __str__(self):
        return f"Nombre: {self['Nombre']}, dni: {self['dni']}, Fecha de Ingreso: {self['FechaIngreso']}, Carrera: {self['Carrera']}"

    def __eq__(self, otro):
        if not isinstance(otro, alumno):
            return False
        return (self.nombre == otro.nombre and
                self.dni == otro.dni and
                self.fecha_ingreso == otro.fecha_ingreso and
                self.carrera == otro.carrera)

    def actualizar_datos(self, nombre=None, dni=None, fecha_ingreso=None, carrera=None):
        if nombre is not None:
            self.nombre = nombre
        if dni is not None:
            self.dni = dni
        if fecha_ingreso is not None:
            self.fecha_ingreso = fecha_ingreso
        if carrera is not None:
            self.carrera = carrera
        
    def tiempo_inscripcion(self):
        fecha_actual = datetime.date.today()
        fecha_ingreso = self["FechaIngreso"].a_datetime()
        diferencia = fecha_actual - fecha_ingreso
        return diferencia.days // 365

class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None
        self.anterior = None

class ListaDoblementeEnlazada:
    def __init__(self):
        self.primero = None
        self.ultimo = None
        self.len=0
    
    def esta_vacia(self):
        return self.primero is None

    def agregar(self, valor): 
        nuevo_nodo = Nodo(valor)
        if self.primero is None:
            self.primero = self.ultimo = nuevo_nodo
        else:
            self.ultimo.siguiente = nuevo_nodo
            nuevo_nodo.anterior = self.ultimo
            self.ultimo = nuevo_nodo
        self.len +=1

    def remover_prim(self):
        if self.primero is None:
            return None
        valor = self.primero.valor
        if self.primero == self.ultimo:
            self.primero = self.ultimo = None
        else:
            self.primero = self.primero.siguiente
            self.primero.anterior = None
        self.len =self.len -1
        return valor

    def __str__(self):
        valores = []
        actual = self.primero
        while actual:
            valores.append(str(actual.valor))
            actual = actual.siguiente
        return "->".join(valores)

    def __iter__(self):
       return SecuenciaIteradormax(self)

class SecuenciaIteradormax:
    def __init__(self, secuencia):
        self.secuencia = secuencia
        self.nodo_actual = secuencia.elementos.primero
    def __iter__(self):
        return self
    def __next__(self):
        if self.nodo_actual is None:
            raise StopIteration
        valor = self.nodo_actual.valor
        self.nodo_actual = self.nodo_actual.siguiente
        return valor

    def lista_ejemplo(self, cantidad):
        nombres = ["Martin", "María", "Marta", "Mariana", "Ana"]
        carreras = ["Ciencias", "Filosofia", "Economía"]

        for _ in range(cantidad):
            nombre = random.choice(nombres)
            dni = random.randint(10000000, 99999999)
            fecha_ingreso = Fecha(random.randint(1, 28), random.randint(1, 12), random.randint(2000, 2023))
            carrera = random.choice(carreras)
            alumno = alumno(nombre, dni, fecha_ingreso, carrera)
            self.insertar_al_final(alumno)

    def lista_alumnos(lista_de_alumnos):
        nombres = ["Martin", "María", "Marta", "Mariana", "Ana"]
        carreras = ["Ciencias", "Filosofia", "Economía"]
        lista_alumnos = []

        for _ in range(lista_de_alumnos):
            nombre = random.choice(nombres)
            dni = random.randint(10000000, 99999999)
            fecha_ingreso = Fecha(random.randint(1, 28), random.randint(1, 12), random.randint(2000, 2023))
            carrera = random.choice(carreras)
            alumno = alumno(nombre, dni, fecha_ingreso, carrera)
            lista_alumnos.append(alumno)

        return lista_alumnos

    def crear_directorio_y_guardar_lista(lista_alumnos, directorio, archivo):
        try:
            os.mkdir(directorio, exist_ok=True)
            ruta_archivo = os.path.join(directorio, archivo)
            with open(ruta_archivo, 'w') as f:
                for alumno in lista_alumnos:
                    f.write(str(alumno) + '\n')
            return directorio, ruta_archivo
        except OSError as e:
            raise
    
    def mover_directorio(origen, destino):
        try:
            os.rename(origen, destino)
        except OSError as e:
            raise

    def borrar_archivo_y_directorio(directorio, archivo):
        try:
            ruta_archivo = os.path.join(directorio, archivo)
            os.remove(ruta_archivo)
            os.rmdir(directorio)
        except OSError as e:
            raise


    
