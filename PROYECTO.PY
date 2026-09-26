"""
================================================================
  JUEGO DEL AHORCADO
  Videojuego educativo para niños de 8 a 12 años.
  Adivina la palabra secreta antes de que se complete el dibujo.
================================================================
"""
 
import random
 
# ------------------ CLASE PRINCIPAL: Ahorcado ------------------
class Ahorcado:
    """Contiene toda la lógica de una partida de Ahorcado."""
 
    # Máximo de intentos fallidos permitidos antes de perder
    MAX_INTENTOS = 6
 
    # Banco de palabras organizado por categoría, con una pista para cada una
    # (esto hace el juego educativo: el niño aprende mientras juega)
    BANCO_PALABRAS = {
        "Animales": [
            ("elefante", "Es un animal"),
            ("jirafa", "Es un animal"),
            ("delfin", "Es un animal"),
        ],
        "Frutas": [
            ("manzana", "Es una fruta"),
            ("sandia", "Es una fruta"),
            ("platano", "Es una fruta"),
        ],
        "Planetas": [
            ("marte", "Es un planeta"),
            ("jupiter", "Es un planeta"),
            ("tierra", "Es un planeta"),
        ],
    }
 
    # Dibujos del ahorcado según la cantidad de errores (0 a 6)
    DIBUJOS = [
        """
           ------
           |    |
           |
           |
           |
           |
        --------""",
        """
           ------
           |    |
           |    O
           |
           |
           |
        --------""",
        """
           ------
           |    |
           |    O
           |    |
           |
           |
        --------""",
        """
           ------
           |    |
           |    O
           |   /|
           |
           |
        --------""",
        """
           ------
           |    |
           |    O
           |   /|\\
           |
           |
        --------""",
        """
           ------
           |    |
           |    O
           |   /|\\
           |   /
           |
        --------""",
        """
           ------
           |    |
           |    O
           |   /|\\
           |   / \\
           |
        --------""",
    ]
 
    def __init__(self):
        self.palabra, self.pista = self._elegir_palabra()
        self.letras_correctas = set()
        self.letras_incorrectas = set()
        self.vidas = self.MAX_INTENTOS
 
    def _elegir_palabra(self):
        """Elige una categoría y palabra al azar del banco de palabras."""
        categoria = random.choice(list(self.BANCO_PALABRAS.keys()))
        palabra, pista = random.choice(self.BANCO_PALABRAS[categoria])
        return palabra.upper(), pista
 
    def _mostrar_palabra(self):
        """Devuelve la palabra con guiones bajos en las letras aún no adivinadas."""
        return " ".join(
            letra if letra in self.letras_correctas else "_" for letra in self.palabra
        )
 
    def _palabra_completa(self):
        """True si ya se adivinaron todas las letras de la palabra."""
        return all(letra in self.letras_correctas for letra in self.palabra)
 
    def _dibujar_ahorcado(self):
        errores = self.MAX_INTENTOS - self.vidas
        print(self.DIBUJOS[errores])
 
    def _pedir_letra(self):
        """Pide una letra al jugador y valida que sea correcta antes de aceptarla."""
        while True:
            entrada = input("Ingresa una letra: ").strip().upper()
 
            if len(entrada) != 1 or not entrada.isalpha():
                print("Debes ingresar UNA sola letra (sin números ni símbolos).\n")
                continue
 
            if entrada in self.letras_correctas or entrada in self.letras_incorrectas:
                print(" Ya intentaste esa letra, prueba con otra.\n")
                continue
 
            return entrada
 
    def _procesar_letra(self, letra):
        """Revisa si la letra está en la palabra y actualiza el estado del juego."""
        if letra in self.palabra:
            self.letras_correctas.add(letra)
            print(f"¡Bien hecho! La letra '{letra}' sí está en la palabra.\n")
        else:
            self.letras_incorrectas.add(letra)
            self.vidas -= 1
            print(f"La letra '{letra}' no está en la palabra.\n")
 
    def jugar(self):
        """Ejecuta una partida completa, desde la pista inicial hasta el final."""
        print(f"\nPista: {self.pista}")
 
        while self.vidas > 0 and not self._palabra_completa():
            self._dibujar_ahorcado()
            print(f"Palabra: {self._mostrar_palabra()}")
            print(f"Letras usadas: {', '.join(sorted(self.letras_incorrectas)) or '(ninguna)'}")
            print(f"Vidas restantes: {self.vidas}")
 
            letra = self._pedir_letra()
            self._procesar_letra(letra)
 
        self._dibujar_ahorcado()
 
        if self._palabra_completa():
            print(f"¡GANASTE! La palabra era: {self.palabra}\n")
        else:
            print(f"¡PERDISTE! La palabra era: {self.palabra}\n")
 
 
# ------------------ FUNCIONES DE PANTALLAS Y MENÚS ------------------
def mostrar_bienvenida():
    print("=" * 50)
    print("    BIENVENIDO AL JUEGO DEL AHORCADO  ")
    print("=" * 50)
 
 
def mostrar_instrucciones():
    print("\n--- INSTRUCCIONES ---")
    print("1. La computadora elige una palabra secreta.")
    print("2. Debes adivinarla ingresando una letra a la vez.")
    print("3. Si la letra está en la palabra, se mostrará en su lugar.")
    print("4. Si la letra NO está, pierdes una vida y avanza el dibujo.")
    print("5. Ganas si adivinas toda la palabra antes de quedarte sin vidas.\n")
 
 
def menu_principal():
    print("--- MENÚ PRINCIPAL ---")
    print("1. Jugar")
    print("2. Instrucciones")
    print("3. Salir")
    return input("Elige una opción: ").strip()
 
 
def jugar_partida():
    """Controla el ciclo de 'Nueva Partida' -> jugar -> '¿jugar otra vez?'."""
    while True:
        partida = Ahorcado()
        partida.jugar()
 
        de_nuevo = input("¿Quieres jugar otra vez? (s/n): ").strip().lower()
        if de_nuevo != "s":
            break
 
 
# ------------------ PROGRAMA PRINCIPAL ------------------
def main():
    mostrar_bienvenida()
 
    while True:
        opcion = menu_principal()
 
        if opcion == "1":
            jugar_partida()
        elif opcion == "2":
            mostrar_instrucciones()
        elif opcion == "3":
            print("\n¡Gracias por jugar! Hasta pronto. ")
            break
        else:
            print("Opción inválida, intenta de nuevo.\n")
 
 
if __name__ == "__main__":
    main()