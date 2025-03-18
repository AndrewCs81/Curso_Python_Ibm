biblioteca = []  # Lista para almacenar los libros


class Libro:
    def __init__(self, titulo, autor,isbn):
         """Constructor: inicializa los atributos del libro.
         Explicación:
__init__ → Es el constructor que inicializa la titulo, autor... y estado (No prestado) .

         """
         self.titulo = titulo
         self.autor = autor
         self.isbn = isbn
         self.prestado = False  # Estado inicial no prestado
      
    def agregar_libro(self):
        """Método para agregar un libro a la biblioteca."""
        nuevo_libro = Libro(self.titulo, self.autor,self.isbn) #Crear objeto de la clase Libro
        biblioteca.append(self) #Agregarlo a la biblioteca de libros
        print(f"Libro '{self.titulo}' agregado a la biblioteca con exito.")
      
      
      
            
    def prestar(self):
            """Método para prestar un libro,comprueba si esta disponble , si lo está, lo presta y pone a False la disponibilidad."""
            if not self.prestado:
                self.prestado = True
                print(f"El {self.titulo} {self.autor} Prestamo concedido.")
            else:
                print(f"El {self.titulo} {self.autor} Denegado,ya está prestado.")
                
    def devolver(self):
            """Método para devolver un libro,comprueba si esta prestado , si lo está, lo devuelve y pone a True la disponibilidad."""
            if self.prestado:
                self.prestado = False
                print(f"El libro:{self.titulo} , del autor {self.autor} ha sido devuelto.")
            else:
                print(f"El libro:{self.titulo} , del autor {self.autor} ya estába disponible.")    
                
    def mostrar(self):
        """ Recorre la lista de libros e imprime la informacion de cada uno de ellos"""       
        
                
                