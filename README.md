La programación estructurada es un paradigma de programación que se basa en dividir un programa en bloques o estructuras lógicas que facilitan su comprensión, desarrollo y mantenimiento. Se enfoca en el uso de estructuras de control bien definidas, como:
	•	Secuencia: instrucciones que se ejecutan en orden.
	•	Selección (condicionales): como if, else, switch, para tomar decisiones.
	•	Repetición (bucles): como while, for, para repetir acciones.

Características clave de la programación estructurada:
	1.	Código claro y legible: al organizarse en bloques lógicos, el código es más fácil de leer y entender.
	2.	Evita el uso excesivo de goto: que puede hacer que el código sea confuso (“código espagueti”).
	3.	Facilita la depuración y el mantenimiento: al tener una estructura ordenada.
	4.	Permite reutilizar código: usando funciones o procedimientos.
 La programación orientada a objetos (POO) es un paradigma de programación que se basa en el uso de objetos, los cuales representan elementos del mundo real dentro del programa. Cada objeto combina datos (atributos) y comportamientos (métodos o funciones).

Principales conceptos de la POO:
	1.	Clase: es el molde o plantilla para crear objetos. Define qué atributos y métodos tendrá un tipo de objeto.
	2.	Objeto: es una instancia de una clase. Tiene sus propios valores y puede ejecutar métodos.
	3.	Encapsulamiento: oculta los detalles internos de un objeto, permitiendo controlar el acceso a sus datos.
	4.	Herencia: permite crear nuevas clases a partir de otras, reutilizando código.
	5.	Polimorfismo: permite que un mismo método tenga diferentes comportamientos dependiendo del objeto que lo use.
 🔹 ¿Qué es una clase?

Una clase en Python es como un molde o plantilla que define cómo deben ser los objetos que se creen a partir de ella. En esa plantilla se indican:
	•	Qué datos tendrá el objeto (atributos)
	•	Qué acciones podrá realizar (métodos)
 class NombreDeLaClase:
    def _init_(self, parametro1, parametro2):
        self.atributo1 = parametro1
        self.atributo2 = parametro2

    def metodo(self):
        print("Esto es un método")
        🔸 _init_:
	•	Es el constructor. Se ejecuta automáticamente cuando se crea un objeto.
	•	El parámetro self representa al objeto actual (como decir “yo mismo”).

⸻

🔹 Crear objetos (instancias de la clase)
mi_objeto = NombreDeLaClase(valor1, valor2)
EJEMPLO FINAL 
class Persona:
    def _init_(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def saludar(self):
        print(f"Hola, soy {self.nombre} y tengo {self.edad} años.")

# Crear un objeto de la clase Persona
persona1 = Persona("Ana", 20)

# Usar un método del objeto
persona1.saludar()
