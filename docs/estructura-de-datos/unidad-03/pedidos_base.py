"""Actividad: El registro de pedidos que se vuelve lento.

Este archivo NO se modifica. Guarda los pedidos de una tienda de dos formas que ya conoces
y cuenta cuánto trabajo cuesta cada operación:

  1. ListaPedidos: una lista enlazada simple, siempre ordenada por número de pedido.
  2. ArregloPedidos: un arreglo (list de Python) siempre ordenado, que busca saltando a la mitad.

Un "paso" es una de dos cosas: mirar un pedido para compararlo, o correr un pedido de lugar.

Para ejecutarlo:  python pedidos_base.py
Prueba también con N = 20_000 y compara cómo cambian los números.
Requiere solo la biblioteca estándar de Python.
"""

N = 2000          # cantidad de pedidos del registro
PRIMERO = 1001    # número del primer pedido
ULTIMO = PRIMERO + N        # número del último pedido
TARDE = PRIMERO + N // 2    # un pedido del medio que llega tarde: el registro ya tiene todos los demás


class Nodo:
    """Un pedido y el enlace al siguiente."""

    def __init__(self, numero):
        self.numero = numero
        self.siguiente = None


class ListaPedidos:
    """Lista enlazada simple ordenada de menor a mayor número de pedido."""

    def __init__(self, numeros_ordenados=()):
        self.cabeza = None
        self.pasos = 0
        ultimo = None
        for numero in numeros_ordenados:  # carga rápida, no cuenta pasos
            nodo = Nodo(numero)
            if ultimo is None:
                self.cabeza = nodo
            else:
                ultimo.siguiente = nodo
            ultimo = nodo

    def buscar(self, numero):
        actual = self.cabeza
        while actual is not None:
            self.pasos += 1
            if actual.numero == numero:
                return True
            if actual.numero > numero:
                return False
            actual = actual.siguiente
        return False

    def insertar(self, numero):
        anterior, actual = None, self.cabeza
        while actual is not None and actual.numero < numero:
            self.pasos += 1
            anterior, actual = actual, actual.siguiente
        nuevo = Nodo(numero)
        nuevo.siguiente = actual
        if anterior is None:
            self.cabeza = nuevo
        else:
            anterior.siguiente = nuevo

    def cancelar(self, numero):
        anterior, actual = None, self.cabeza
        while actual is not None and actual.numero < numero:
            self.pasos += 1
            anterior, actual = actual, actual.siguiente
        if actual is None or actual.numero != numero:
            return False
        if anterior is None:
            self.cabeza = actual.siguiente
        else:
            anterior.siguiente = actual.siguiente
        return True

    def listar(self):
        salida, actual = [], self.cabeza
        while actual is not None:
            self.pasos += 1
            salida.append(actual.numero)
            actual = actual.siguiente
        return salida

    def rango(self, desde, hasta):
        """Los pedidos con desde <= número <= hasta, en orden."""
        salida, actual = [], self.cabeza
        while actual is not None and actual.numero <= hasta:
            self.pasos += 1
            if actual.numero >= desde:
                salida.append(actual.numero)
            actual = actual.siguiente
        return salida


class ArregloPedidos:
    """Arreglo ordenado de menor a mayor. Busca saltando a la mitad."""

    def __init__(self, numeros_ordenados=()):
        self.datos = list(numeros_ordenados)
        self.pasos = 0

    def _donde(self, numero):
        """Posición donde está el pedido, o donde tendría que estar si no está."""
        bajo, alto = 0, len(self.datos)
        while bajo < alto:
            self.pasos += 1
            medio = (bajo + alto) // 2
            if self.datos[medio] < numero:
                bajo = medio + 1
            else:
                alto = medio
        return bajo

    def buscar(self, numero):
        i = self._donde(numero)
        return i < len(self.datos) and self.datos[i] == numero

    def insertar(self, numero):
        i = self._donde(numero)
        self.pasos += len(self.datos) - i  # los pedidos de la derecha corren un lugar
        self.datos.insert(i, numero)

    def cancelar(self, numero):
        i = self._donde(numero)
        if i >= len(self.datos) or self.datos[i] != numero:
            return False
        self.pasos += len(self.datos) - i - 1  # los pedidos de la derecha corren un lugar
        del self.datos[i]
        return True

    def listar(self):
        self.pasos += len(self.datos)
        return list(self.datos)

    def rango(self, desde, hasta):
        """Los pedidos con desde <= número <= hasta, en orden."""
        i, salida = self._donde(desde), []
        while i < len(self.datos) and self.datos[i] <= hasta:
            self.pasos += 1
            salida.append(self.datos[i])
            i += 1
        return salida


# ----------------------------------------------------------------------------
# Medición: no hace falta leer ni cambiar nada de aquí hacia abajo
# ----------------------------------------------------------------------------
OPERACIONES = [
    ("Buscar el primer pedido", "buscar", (PRIMERO,)),
    ("Buscar un pedido del medio", "buscar", (TARDE + 1,)),
    ("Buscar el último pedido", "buscar", (ULTIMO,)),
    ("Insertar el pedido que llegó tarde", "insertar", (TARDE,)),
    ("Cancelar el primer pedido", "cancelar", (PRIMERO,)),
    ("Cancelar un pedido del medio", "cancelar", (TARDE + 1,)),
    ("Listar todos, ordenados", "listar", ()),
    ("Listar un rango de 100 pedidos", "rango", (PRIMERO + 500, PRIMERO + 599)),
]


def registro():
    """Los N pedidos desde PRIMERO hasta ULTIMO, sin el que llega tarde."""
    return [n for n in range(PRIMERO, ULTIMO + 1) if n != TARDE]


def pasos_de(clase, operacion, argumentos):
    estructura = clase(registro())
    resultado = getattr(estructura, operacion)(*argumentos)
    return estructura.pasos, resultado


def comprobar():
    """Las dos estructuras deben dar las mismas respuestas; solo cambia el costo."""
    for nombre, operacion, argumentos in OPERACIONES:
        _, de_lista = pasos_de(ListaPedidos, operacion, argumentos)
        _, de_arreglo = pasos_de(ArregloPedidos, operacion, argumentos)
        assert de_lista == de_arreglo, f"{nombre}: las respuestas no coinciden"


def medicion():
    comprobar()
    print(f"Registro de {N} pedidos, del {PRIMERO} al {ULTIMO}. Pasos por operación:\n")
    print(f"{'Operación':<38}{'Lista enlazada':>16}{'Arreglo ordenado':>20}")
    for nombre, operacion, argumentos in OPERACIONES:
        de_lista, _ = pasos_de(ListaPedidos, operacion, argumentos)
        de_arreglo, _ = pasos_de(ArregloPedidos, operacion, argumentos)
        print(f"{nombre:<38}{de_lista:>16}{de_arreglo:>20}")


if __name__ == "__main__":
    medicion()
