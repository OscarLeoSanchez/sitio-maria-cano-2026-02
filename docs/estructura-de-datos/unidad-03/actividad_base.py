"""Actividad: ¿Cómo organizarías los datos?

Trabaja solo el caso que te asignaron (A, B, C o D) y completa los métodos que dicen TODO.
Lo demás ya está hecho: no lo cambies.

Para comprobar tu trabajo, ejecuta este archivo:  python actividad_base.py
La función probar() prueba tu código con varios ejemplos y escribe OK, o indica cuál ejemplo falló.
Cambia la letra de la última línea del archivo por la de tu caso.
"""
import threading
import time


class Nodo:
    """Pieza básica: guarda un dato y el enlace al siguiente nodo."""

    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None


class NodoDoble(Nodo):
    """Nodo con dos enlaces: siguiente y anterior."""

    def __init__(self, dato):
        super().__init__(dato)
        self.anterior = None


# ----------------------------------------------------------------------------
# Caso A. La lista de reproducción: lista doble con un cursor
# ----------------------------------------------------------------------------
class ListaDoble:
    """Canciones en una lista doble. _actual es el cursor: la canción que suena."""

    def __init__(self):
        self._cabeza = None
        self._ultimo = None
        self._actual = None

    def agregar_al_final(self, dato):
        nuevo = NodoDoble(dato)
        if self._cabeza is None:
            self._cabeza = nuevo
            self._actual = nuevo
        else:
            nuevo.anterior = self._ultimo
            self._ultimo.siguiente = nuevo
        self._ultimo = nuevo

    def actual(self):
        return None if self._actual is None else self._actual.dato

    def siguiente(self):
        """Pasa a la canción siguiente (si no hay, se queda) y devuelve su dato."""
        if self._actual is not None and self._actual.siguiente is not None:
            self._actual = self._actual.siguiente
        return self.actual()

    def anterior(self):
        """Pasa a la canción anterior (si no hay, se queda) y devuelve su dato."""
        if self._actual is not None and self._actual.anterior is not None:
            self._actual = self._actual.anterior
        return self.actual()

    def a_lista(self):
        """Los datos de cabeza a último, para probar."""
        datos, nodo = [], self._cabeza
        while nodo is not None:
            datos.append(nodo.dato)
            nodo = nodo.siguiente
        return datos

    def a_lista_inversa(self):
        """Los datos de último a cabeza, para probar."""
        datos, nodo = [], self._ultimo
        while nodo is not None:
            datos.append(nodo.dato)
            nodo = nodo.anterior
        return datos

    def insertar_despues_de_actual(self, dato):
        """TODO. Inserta una canción justo después de la que suena. El cursor no se mueve.
        Si la lista está vacía, la canción nueva queda como la que suena."""
        raise NotImplementedError("completa este método")

    def quitar_actual(self):
        """TODO. Quita la canción que suena y devuelve su dato. El cursor pasa a la siguiente;
        si era la última, pasa a la anterior. Si la lista está vacía, lanza IndexError."""
        raise NotImplementedError("completa este método")


# ----------------------------------------------------------------------------
# Caso B. El editor de texto: pila
# ----------------------------------------------------------------------------
class Pila:
    """Pila con nodos. _cabeza es el tope."""

    def __init__(self):
        self._cabeza = None

    def esta_vacia(self):
        return self._cabeza is None

    def tope(self):
        if self._cabeza is None:
            raise IndexError("pila vacia")
        return self._cabeza.dato

    def apilar(self, dato):
        """TODO. Agrega un dato. No recorras la pila."""
        raise NotImplementedError("completa este método")

    def desapilar(self):
        """TODO. Quita el dato del tope y lo devuelve. Si la pila está vacía, lanza IndexError."""
        raise NotImplementedError("completa este método")


# ----------------------------------------------------------------------------
# Caso C. El banco: cola
# ----------------------------------------------------------------------------
class Cola:
    """Cola con nodos. _cabeza es el frente y _ultimo es el final."""

    def __init__(self):
        self._cabeza = None
        self._ultimo = None

    def esta_vacia(self):
        return self._cabeza is None

    def frente(self):
        if self._cabeza is None:
            raise IndexError("cola vacia")
        return self._cabeza.dato

    def encolar(self, dato):
        """TODO. Agrega un dato al final. No recorras la cola."""
        raise NotImplementedError("completa este método")

    def desencolar(self):
        """TODO. Quita el dato del frente y lo devuelve. Si la cola está vacía, lanza IndexError.
        Piensa qué le pasa a _ultimo cuando la cola se vacía."""
        raise NotImplementedError("completa este método")


# ----------------------------------------------------------------------------
# Caso D. El juego de mesa: lista circular
# ----------------------------------------------------------------------------
class ListaCircular:
    """Jugadores en una lista circular: el último nodo apunta a la cabeza.
    _actual es el jugador que tiene el turno."""

    def __init__(self):
        self._cabeza = None
        self._ultimo = None
        self._actual = None

    def agregar_al_final(self, dato):
        nuevo = Nodo(dato)
        if self._cabeza is None:
            self._cabeza = nuevo
            self._actual = nuevo
        else:
            self._ultimo.siguiente = nuevo
        self._ultimo = nuevo
        self._ultimo.siguiente = self._cabeza

    def actual(self):
        return None if self._actual is None else self._actual.dato

    def a_lista(self):
        """Los jugadores desde la cabeza, una sola vuelta, para probar."""
        datos = []
        if self._cabeza is not None:
            nodo = self._cabeza
            while True:
                datos.append(nodo.dato)
                nodo = nodo.siguiente
                if nodo is self._cabeza or len(datos) > 10_000:
                    break
        return datos

    def siguiente(self):
        """TODO. Pasa el turno al jugador siguiente y devuelve su dato.
        Después del último, el turno vuelve al primero."""
        raise NotImplementedError("completa este método")

    def quitar_actual(self):
        """TODO. Quita al jugador que tiene el turno y devuelve su dato. El turno pasa al siguiente
        y la lista sigue siendo circular. Si la lista está vacía, lanza IndexError."""
        raise NotImplementedError("completa este método")


# ----------------------------------------------------------------------------
# Pruebas: no hace falta leer ni cambiar nada de aquí hacia abajo
# ----------------------------------------------------------------------------
def _igual(obtenido, esperado, que):
    if obtenido != esperado:
        raise AssertionError(f"{que}: se esperaba {esperado} y se obtuvo {obtenido}")


def _lista_doble(*datos):
    lista = ListaDoble()
    for d in datos:
        lista.agregar_al_final(d)
    return lista


def _doble_coherente(lista, esperado, que):
    _igual(lista.a_lista(), esperado, f"{que} (hacia adelante)")
    _igual(lista.a_lista_inversa(), esperado[::-1], f"{que} (hacia atrás)")


def _a_inserta_en_el_medio():
    lista = _lista_doble("A", "B", "C", "D")
    lista.insertar_despues_de_actual("X")
    _doble_coherente(lista, ["A", "X", "B", "C", "D"], "después de insertar X tras A")
    _igual(lista.actual(), "A", "la canción que suena")


def _a_inserta_al_final():
    lista = _lista_doble("A", "B", "C")
    lista.siguiente()
    lista.siguiente()
    lista.insertar_despues_de_actual("X")
    _doble_coherente(lista, ["A", "B", "C", "X"], "después de insertar X tras la última")
    _igual(lista.siguiente(), "X", "al avanzar desde C")


def _a_inserta_en_vacia():
    lista = ListaDoble()
    lista.insertar_despues_de_actual("X")
    _doble_coherente(lista, ["X"], "lista con una canción")
    _igual(lista.actual(), "X", "la canción que suena")


def _a_quita_en_el_medio():
    lista = _lista_doble("A", "B", "C", "D")
    lista.siguiente()
    _igual(lista.quitar_actual(), "B", "dato devuelto")
    _doble_coherente(lista, ["A", "C", "D"], "después de quitar B")
    _igual(lista.actual(), "C", "la canción que suena")


def _a_quita_la_primera():
    lista = _lista_doble("A", "B", "C")
    _igual(lista.quitar_actual(), "A", "dato devuelto")
    _doble_coherente(lista, ["B", "C"], "después de quitar A")
    _igual(lista.actual(), "B", "la canción que suena")


def _a_quita_la_ultima():
    lista = _lista_doble("A", "B", "C")
    lista.siguiente()
    lista.siguiente()
    _igual(lista.quitar_actual(), "C", "dato devuelto")
    _doble_coherente(lista, ["A", "B"], "después de quitar C")
    _igual(lista.actual(), "B", "la canción que suena")


def _a_quita_hasta_vaciar():
    lista = _lista_doble("A", "B")
    _igual(lista.quitar_actual(), "A", "primer dato")
    _igual(lista.quitar_actual(), "B", "segundo dato")
    _doble_coherente(lista, [], "lista vacía")
    _igual(lista.actual(), None, "la canción que suena")
    try:
        lista.quitar_actual()
    except IndexError:
        return
    raise AssertionError("quitar de una lista vacía debe lanzar IndexError")


def _b_orden():
    pila = Pila()
    for d in (1, 2, 3):
        pila.apilar(d)
    _igual([pila.desapilar(), pila.desapilar(), pila.desapilar()], [3, 2, 1], "orden de salida")


def _b_tope():
    pila = Pila()
    pila.apilar("a")
    pila.apilar("b")
    _igual(pila.tope(), "b", "tope")
    _igual(pila.tope(), "b", "el tope no debe quitar nada")


def _b_intercalado():
    pila = Pila()
    pila.apilar(1)
    pila.apilar(2)
    _igual(pila.desapilar(), 2, "primer desapilar")
    pila.apilar(3)
    _igual([pila.desapilar(), pila.desapilar()], [3, 1], "el resto")
    _igual(pila.esta_vacia(), True, "esta_vacia al terminar")


def _b_vacia():
    pila = Pila()
    try:
        pila.desapilar()
    except IndexError:
        return
    raise AssertionError("desapilar de una pila vacía debe lanzar IndexError")


def _b_muchos():
    pila = Pila()
    for i in range(20_000):
        pila.apilar(i)
    _igual(pila.desapilar(), 19_999, "último apilado")


def _c_orden():
    cola = Cola()
    for d in (1, 2, 3):
        cola.encolar(d)
    _igual(cola.frente(), 1, "frente")
    _igual([cola.desencolar(), cola.desencolar(), cola.desencolar()], [1, 2, 3], "orden de salida")


def _c_vaciar_y_volver():
    cola = Cola()
    for ronda in range(3):
        cola.encolar(f"a{ronda}")
        cola.encolar(f"b{ronda}")
        _igual([cola.desencolar(), cola.desencolar()], [f"a{ronda}", f"b{ronda}"], f"ronda {ronda}")
        _igual(cola.esta_vacia(), True, "esta_vacia con la cola vacía")
        _igual(cola._ultimo, None, "_ultimo cuando la cola queda vacía")


def _c_vacia():
    cola = Cola()
    try:
        cola.desencolar()
    except IndexError:
        return
    raise AssertionError("desencolar de una cola vacía debe lanzar IndexError")


def _c_muchos():
    cola = Cola()
    for i in range(20_000):
        cola.encolar(i)
    _igual(cola.desencolar(), 0, "primero en entrar")


def _d_turnos():
    lista = ListaCircular()
    for d in ("Ana", "Beto", "Cami", "Dani"):
        lista.agregar_al_final(d)
    _igual([lista.siguiente() for _ in range(6)], ["Beto", "Cami", "Dani", "Ana", "Beto", "Cami"], "turnos")


def _d_anillo(lista, esperado, que):
    _igual(lista.a_lista(), esperado, que)
    if esperado:
        _igual(lista._ultimo.siguiente is lista._cabeza, True, f"{que}: el último nodo debe apuntar a la cabeza")
        _igual(lista._ultimo.dato, esperado[-1], f"{que}: _ultimo")
        _igual(lista._cabeza.dato, esperado[0], f"{que}: _cabeza")


def _d_circular(*datos):
    lista = ListaCircular()
    for d in datos:
        lista.agregar_al_final(d)
    return lista


def _d_quita_en_el_medio():
    lista = _d_circular("Ana", "Beto", "Cami", "Dani")
    lista.siguiente()
    _igual(lista.quitar_actual(), "Beto", "dato devuelto")
    _d_anillo(lista, ["Ana", "Cami", "Dani"], "después de quitar a Beto")
    _igual(lista.actual(), "Cami", "el turno")


def _d_quita_la_cabeza():
    lista = _d_circular("Ana", "Beto", "Cami")
    _igual(lista.quitar_actual(), "Ana", "dato devuelto")
    _d_anillo(lista, ["Beto", "Cami"], "después de quitar a Ana")
    _igual(lista.actual(), "Beto", "el turno")


def _d_quita_el_ultimo():
    lista = _d_circular("Ana", "Beto", "Cami")
    lista.siguiente()
    lista.siguiente()
    _igual(lista.quitar_actual(), "Cami", "dato devuelto")
    _d_anillo(lista, ["Ana", "Beto"], "después de quitar a Cami")
    _igual(lista.actual(), "Ana", "el turno vuelve al primero")


def _d_quita_hasta_vaciar():
    lista = _d_circular("Ana", "Beto")
    lista.quitar_actual()
    _d_anillo(lista, ["Beto"], "queda un jugador")
    _igual(lista.siguiente(), "Beto", "con un solo jugador el turno es suyo")
    lista.quitar_actual()
    _igual(lista.a_lista(), [], "lista vacía")
    _igual(lista.actual(), None, "el turno")
    try:
        lista.quitar_actual()
    except IndexError:
        return
    raise AssertionError("quitar de una lista vacía debe lanzar IndexError")


CASOS = {
    "A": ("A. La lista de reproducción", [
        ("insertar después de la que suena, en el medio", _a_inserta_en_el_medio),
        ("insertar después de la última", _a_inserta_al_final),
        ("insertar en una lista vacía", _a_inserta_en_vacia),
        ("quitar la que suena, en el medio", _a_quita_en_el_medio),
        ("quitar la primera", _a_quita_la_primera),
        ("quitar la última", _a_quita_la_ultima),
        ("quitar hasta vaciar la lista", _a_quita_hasta_vaciar),
    ]),
    "B": ("B. El editor de texto", [
        ("el último que entra es el primero que sale", _b_orden),
        ("consultar el tope sin quitarlo", _b_tope),
        ("apilar y desapilar intercalados", _b_intercalado),
        ("desapilar con la pila vacía", _b_vacia),
        ("apilar 20.000 datos sin recorrer la pila", _b_muchos),
    ]),
    "C": ("C. El banco", [
        ("el primero que entra es el primero que sale", _c_orden),
        ("vaciar la cola y volver a usarla", _c_vaciar_y_volver),
        ("desencolar con la cola vacía", _c_vacia),
        ("encolar 20.000 datos sin recorrer la cola", _c_muchos),
    ]),
    "D": ("D. El juego de mesa", [
        ("los turnos dan la vuelta", _d_turnos),
        ("quitar a un jugador del medio", _d_quita_en_el_medio),
        ("quitar al jugador de la cabeza", _d_quita_la_cabeza),
        ("quitar al último jugador", _d_quita_el_ultimo),
        ("quitar hasta vaciar la lista", _d_quita_hasta_vaciar),
    ]),
}


def probar(caso):
    """Prueba el caso ("A", "B", "C" o "D") con varios ejemplos. Escribe OK o indica cuál falló."""
    titulo, comprobaciones = CASOS[caso]
    print(f"Caso {titulo}")
    buenas = pendientes = 0
    for descripcion, funcion in comprobaciones:
        resultado = {}

        def correr():
            try:
                funcion()
                resultado["ok"] = True
            except NotImplementedError:
                resultado["pendiente"] = True
            except AssertionError as error:
                resultado["falla"] = str(error) or "el resultado no es el esperado"
            except Exception as error:
                resultado["falla"] = f"{type(error).__name__}: {error}"

        hilo = threading.Thread(target=correr, daemon=True)
        hilo.start()
        hilo.join(3)
        if hilo.is_alive():
            print(f"  FALLA      {descripcion}: tarda demasiado (¿un ciclo que no termina, o recorres toda la estructura?)")
            print("Se detienen las pruebas aquí.")
            return
        if resultado.get("ok"):
            buenas += 1
            print(f"  OK         {descripcion}")
        elif resultado.get("pendiente"):
            pendientes += 1
            print(f"  PENDIENTE  {descripcion}")
        else:
            print(f"  FALLA      {descripcion}: {resultado['falla']}")
    total = len(comprobaciones)
    if buenas == total:
        print(f"Las {total} pruebas salieron OK.")
    else:
        print(f"{buenas} de {total} pruebas OK, {pendientes} pendientes.")


def medicion(n=100_000):
    """Compara un arreglo (list) con una lista enlazada. Mide dos operaciones y escribe los tiempos."""
    inicio = time.perf_counter()
    arreglo = []
    for i in range(n):
        arreglo.insert(0, i)
    t_arreglo_insertar = time.perf_counter() - inicio

    inicio = time.perf_counter()
    cabeza = None
    for i in range(n):
        nuevo = Nodo(i)
        nuevo.siguiente = cabeza
        cabeza = nuevo
    t_nodos_insertar = time.perf_counter() - inicio

    repeticiones = 200
    inicio = time.perf_counter()
    for _ in range(repeticiones):
        arreglo[n // 2]
    t_arreglo_ir = (time.perf_counter() - inicio) / repeticiones

    inicio = time.perf_counter()
    for _ in range(repeticiones):
        nodo = cabeza
        for _ in range(n // 2):
            nodo = nodo.siguiente
    t_nodos_ir = (time.perf_counter() - inicio) / repeticiones

    print(f"Con {n:,} datos:".replace(",", "."))
    print(f"  Insertar {n:,} veces al inicio:".replace(",", "."))
    print(f"    list.insert(0, x):  {t_arreglo_insertar:.3f} s")
    print(f"    nodos enlazados:    {t_nodos_insertar:.3f} s")
    print("  Llegar al dato del medio (una vez):")
    print(f"    list[n // 2]:       {t_arreglo_ir * 1e6:.2f} microsegundos")
    print(f"    recorrer nodos:     {t_nodos_ir * 1e6:.0f} microsegundos")
    print("Los tiempos cambian de un computador a otro; compara las proporciones.")


if __name__ == "__main__":
    probar("A")      # cambia la letra por la de tu caso: "A", "B", "C" o "D"
    # medicion()     # al terminar tu caso, quita el # de esta línea y ejecuta de nuevo
