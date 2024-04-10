from abc import ABC, abstractmethod
#Clase Padre Membresia
class Membresia(ABC):
    def __init__(self, correo:str, tarjeta:str):
        self.__correo = correo
        self.__tarjeta = tarjeta
    # Se definen los métodos getter correo y tarjeta utilizando decoradores @property, 
    # que permiten acceder a los atributos privados __correo y __tarjeta.
    @property
    def correo(self):
        return self.__correo
    
    @property
    def tarjeta(self):
        return self.__tarjeta
    # Se define un método abstracto cambiar_suscripcion, 
    @abstractmethod
    def cambiar_suscripcion(self, tipo_membresia):
        pass
    # Se define un método protegido _crear_nueva_membresia
    def _crear_nueva_membresia(self, nueva_membresia:int):
        if nueva_membresia == 1:
            return Basica(self.correo, self.tarjeta)
        elif nueva_membresia == 2:
            return Familiar(self.correo, self.tarjeta)
        elif nueva_membresia == 3:
            return SinConexion(self.correo, self.tarjeta)
        elif nueva_membresia == 4:
            return Pro(self.correo, self.tarjeta)        

#Membresía Gratis
class Gratis(Membresia):
    costo = 0
    max_dispositivos = 1
    # se sobreescribe método cambiar_suscripcion
    def cambiar_suscripcion(self, nueva_membresia:int):
        # Valida si el valor de la nueva_membresía es válido entre 1 y 4 inclusive
        if nueva_membresia not in [1, 2, 3, 4]:
            return self
        else:
            #si es válido el número, llama a la función _crear_nueva_membresia
            return self._crear_nueva_membresia(nueva_membresia)
#-----
# Membresia Básica
class Basica(Membresia):
    costo = 3000
    max_dispositivos = 2
    # Se sobrescribe el método __init__ para inicializar algunos atributos adicionales.   
    def __init__(self, correo:str, tarjeta:str):
        super().__init__(correo, tarjeta)

        if isinstance(self, Familiar) or isinstance(self, SinConexion):
            self.__dias_regalo = 7
        elif isinstance(self, Pro):
            self.__dias_regalo = 15
            
    def cancelar_suscripcion(self):
        return Gratis(self.correo, self.tarjeta)
    # se sobreescribe método cambiar_suscripcion
    def cambiar_suscripcion(self, nueva_membresia:int):
        # Valida si el valor de la nueva_membresía es menor que 1 o mayor que 4
        if nueva_membresia not in [2, 3, 4]:
            return self
        else:
            #si es válido el número, llama a la función _crear_nueva_membresia
            return self._crear_nueva_membresia(nueva_membresia)

#-----
# Membresia Familiar
class Familiar(Basica):
    costo = 5000
    max_dispositivos = 5
    # se sobreescribe método cambiar_suscripcion
    def cambiar_suscripcion(self, nueva_membresia:int):
        if nueva_membresia not in [1, 3, 4]:
            return self
        else:
            return self._crear_nueva_membresia(nueva_membresia)

    def modificar_control_parental(self):
        pass

#-----
# Membresia Sin Conexion
class SinConexion(Basica):
    costo = 3500
    max_dispositivos = 2
    # se sobreescribe método cambiar_suscripcion
    def cambiar_suscripcion(self, nueva_membresia:int):
        if nueva_membresia not in [1, 2, 4]:
            return self
        else:
            return self._crear_nueva_membresia(nueva_membresia)

    def incrementar_cantidad_maxima_offline(self):
        pass

#-----
# Membresia Pro
class Pro(Familiar, SinConexion):
    costo = 7000
    max_dispositivos = 6
    # se sobreescribe método cambiar_suscripcion
    def cambiar_suscripcion(self, nueva_membresia):
        if nueva_membresia not in [1, 2, 3]:
            return self._crear_nueva_membresia(nueva_membresia)
        else:
            return self
#------

#Verificacion de instancias
g = Gratis("correo@correo.cl", "123 123 123")
print(type(g))
b = g.cambiar_suscripcion(1)
print (type(b))
f = b.cambiar_suscripcion(2)
print (type(f))
sc = f.cambiar_suscripcion(3)
print (type(sc))
pro = sc.cambiar_suscripcion(4)
print (type(pro))