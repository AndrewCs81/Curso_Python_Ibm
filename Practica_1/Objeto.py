"""
### **¿Por qué usamos `self`?
Cuando creamos un objeto de la clase, `self` nos permite:
1. **Acceder a los atributos** de ese objeto.
2. **Modificar su estado** dentro de los métodos.
3. **Diferenciar cada instancia** de la clase.

### **Ejemplo sin `self` (Incorrecto)**
Si no usamos `self`, el código no funcionará correctamente:

```python
class Coche:
    def __init__(marca, modelo):  # Falta self aquí
        marca = marca
        modelo = modelo  # Estas asignaciones no funcionan correctamente

    def mostrar_info():
        print(f"Marca: {marca}, Modelo: {modelo}")  # Error: No reconoce marca y modelo

mi_coche = Coche("Toyota", "Corolla")
mi_coche.mostrar_info()  # Esto dará un error
```
🔴 **Error:** La clase no almacena correctamente los valores porque `marca` y `modelo` solo existen dentro del constructor, pero no están asociados al objeto.

"""

"""### **Ejemplo correcto con `self`**"""
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

# Crear un objeto de la clase Coche
mi_coche = Coche("Toyota", "Corolla")

# Llamar a los métodos
mi_coche.encender()
mi_coche.apagar()
"""Explicación clara:
Clase Coche → Representa un coche con sus atributos (marca, modelo, encendido).
Constructor __init__() → Inicializa los atributos del coche.
Método encender() → Cambia encendido a True si estaba apagado.
Método apagar() → Cambia encendido a False si estaba encendido.
Se crea un objeto mi_coche y se ejecutan los métodos.
Así ya tienes una clase completa con atributos y métodos funcionales. 🚗💨
"""