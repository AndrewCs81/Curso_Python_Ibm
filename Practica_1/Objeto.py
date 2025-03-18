garaje = []

class Coche:
    def __init__(self, marca, modelo):
        """Constructor: inicializa los atributos del coche."""
        self.marca = marca
        self.modelo = modelo
        self.encendido = False  # Estado inicial apagado
        

    def encender(self):
        """Método para encender el coche."""
        if not self.encendido:
            self.encendido = True
            print(f"El {self.marca} {self.modelo} está encendido.")
        else:
            print(f"El {self.marca} {self.modelo} ya estaba encendido.")

    def apagar(self):
        """Método para apagar el coche."""
        if self.encendido:
            self.encendido = False
            print(f"El {self.marca} {self.modelo} está apagado.")
        else:
            print(f"El {self.marca} {self.modelo} ya estaba apagado.")
            
    def agregar(self):
        nuevo_coche = Coche(self.marca, self.modelo) #Crear objeto de la clase Libro
        garaje.append(self) #Agregarlo a la biblioteca de libros
        print(f"coche '{self.marca}' agregado al garaje con exito.")
# Llamar a los métodos

# Crear un objeto de la clase Coche
mi_coche = Coche("Toyota", "Corolla")
mi_coche2 = Coche("Cittroen", "C4")
mi_coche3 = Coche("Ford", "Focus")
mi_coche.agregar()
mi_coche2.agregar()
mi_coche.encender()
mi_coche.apagar()
print(garaje)
