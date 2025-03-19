#Crear biblioteca para guardar los libros
biblioteca = []  # Lista para almacenar los libros

#Crear la clase Libro
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
                print(f"El libro:{self.titulo} , del autor {self.autor} , NO se puede devolver,ya estába disponible.")    
                
    def mostrar(self):
        """ Recorre la lista de libros e imprime la informacion de cada uno de ellos"""       
        print(f"Lista de libros en la biblioteca:{biblioteca}")
        for libro in biblioteca:
            print(f"Titulo:{libro.titulo},Autor:{libro.autor},ISBN:{libro.isbn},Prestado:{libro.prestado}")
                

#Implementar el menú interactivo

while True:
     print("1.Agregar libro")
     print("2.Prestar libro")
     print("3.Devolver libro")
     print("4.Mostrar libros")
     print("5.Salir")
     option = input("Elige una opción: ")

     if option == "1":
            titulo = input("Introduce el título del libro: ")
            autor = input("Introduce el autor del libro: ")
            isbn = input("Introduce el ISBN del libro: ")
            libro = Libro(titulo, autor,isbn)
            libro.agregar_libro()

     elif option == "2":
          Libro_Buscado = input("Introduce el ISBN del libro que quieres prestar: ")
          Encontrado    = False

          for libro in biblioteca:
               if libro.isbn == Libro_Buscado:
                    libro.prestar()
                    Encontrado = True
                    for libro in biblioteca:
                       print(f"Título: {libro.titulo}, Autor: {libro.autor}, ISBN: {libro.isbn}, Prestado: {libro.prestado}")
      
                    break
          if not Encontrado:
                       print("Libro no encontrado en la biblioteca.")
 
     elif option == "3":
               Libro_devuelto = input("Introduce el ISBN del libro que quieres devolver: ")
               Encontrado = False
               for libro in biblioteca:
                    if libro.isbn == Libro_devuelto:
                         libro.devolver()
                         Encontrado = True
                         for libro in biblioteca:
                              print(f"Título: {libro.titulo}, Autor: {libro.autor}, ISBN: {libro.isbn}, Prestado: {libro.prestado}")
                         break   
               if not Encontrado:
                    print("Libro no existe en la biblioteca.")

     elif option == "4":   
          libro.mostrar()     

