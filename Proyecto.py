class NodoLista:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

class ListaLigada:
    def __init__(self):
        self.cabeza = None
    
    def insertar(self, dato):
        nuevo = NodoLista(dato)
        if self.cabeza is None:
            self.cabeza = nuevo
        else:
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo
        print(f"Registrado: {dato}")

    def mostrar(self):
        actual = self.cabeza
        if actual is None:
            print("No hay elementos registrados.")
            return
        while actual:
            print(actual.dato)
            actual = actual.siguiente

    def buscar_por_nombre(self, nombre):
        actual = self.cabeza
        while actual:
            try:
                if nombre.lower() in actual.dato.lower():
                    return actual.dato
            except:
                pass
            actual = actual.siguiente
        return None

    def actualizar_por_nombre(self, nombre_buscar, nuevo_texto):
        actual = self.cabeza
        while actual:
            try:
                if nombre_buscar.lower() in actual.dato.lower():
                    actual.dato = nuevo_texto
                    return True
            except:
                pass
            actual = actual.siguiente
        return False

    def eliminar_por_nombre(self, nombre_buscar):
        prev = None
        actual = self.cabeza
        while actual:
            try:
                if nombre_buscar.lower() in actual.dato.lower():
                    if prev is None:
                        self.cabeza = actual.siguiente
                    else:
                        prev.siguiente = actual.siguiente
                    return True
            except:
                pass
            prev = actual
            actual = actual.siguiente
        return False


class NodoCola:
    def __init__(self, pedido):
        self.pedido = pedido
        self.siguiente = None

class ColaPedidos:
    def __init__(self):
        self.frente = None
        self.final = None

    def encolar(self, pedido):
        nuevo = NodoCola(pedido)
        if self.final is None:
            self.frente = self.final = nuevo
        else:
            self.final.siguiente = nuevo
            self.final = nuevo
        print(f"Pedido agregado: {pedido}")

    def desencolar(self):
        if self.frente is None:
            print("No hay pedidos en cola.")
            return None
        pedido = self.frente.pedido
        self.frente = self.frente.siguiente
        if self.frente is None:
            self.final = None
        print(f"Atendiendo pedido: {pedido}")
        return pedido

    def mostrar(self):
        actual = self.frente
        if actual is None:
            print("No hay pedidos en cola.")
            return
        i = 1
        while actual:
            print(f"{i}. {actual.pedido}")
            actual = actual.siguiente
            i += 1

    def eliminar_por_cliente(self, nombre_cliente):
        prev = None
        actual = self.frente
        while actual:
            try:
                if nombre_cliente.lower() in actual.pedido.lower():
                    if prev is None:
                        self.frente = actual.siguiente
                    else:
                        prev.siguiente = actual.siguiente
                    if self.frente is None:
                        self.final = None
                    print(f"Pedido cancelado: {actual.pedido}")
                    return True
            except:
                pass
            prev = actual
            actual = actual.siguiente
        return False

class NodoPila:
    def __init__(self, pedido):
        self.pedido = pedido
        self.siguiente = None

class PilaHistorial:
    def __init__(self):
        self.tope = None

    def apilar(self, pedido):
        nuevo = NodoPila(pedido)
        nuevo.siguiente = self.tope
        self.tope = nuevo
        print(f"Historial + {pedido}")

    def mostrar(self):
        actual = self.tope
        if actual is None:
            print("Historial vacío.")
            return
        i = 1
        while actual:
            print(f"{i}. {actual.pedido}")
            actual = actual.siguiente
            i += 1

    def filtrar_por_cliente(self, nombre_cliente):
        resultados = []
        actual = self.tope
        while actual:
            try:
                if nombre_cliente.lower() in actual.pedido.lower():
                    resultados.append(actual.pedido)
            except:
                pass
            actual = actual.siguiente
        return resultados

    def filtrar_por_zona(self, zona):
        resultados = []
        actual = self.tope
        while actual:
            try:
                if zona.lower() in actual.pedido.lower():
                    resultados.append(actual.pedido)
            except:
                pass
            actual = actual.siguiente
        return resultados


class ColaConPrioridad:
    def __init__(self):
        self.items = []

    def encolar(self, item):
        if self.esta_vacia():
            self.items.append(item)
        else:
            inserted = False
            for i in range(len(self.items)):
                if item[0] < self.items[i][0]:
                    self.items.insert(i, item)
                    inserted = True
                    break
            if not inserted:
                self.items.append(item)

    def desencolar(self):
        if not self.esta_vacia():
            return self.items.pop(0)
        return None

    def esta_vacia(self):
        return len(self.items) == 0



class Vertice:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None
        self.listaAdyacencia = ListaAdyacencia()

    def __str__(self):
        return self.dato

class Arista:
    def __init__(self, destino, peso):
        self.destino = destino
        self.peso = peso
        self.siguiente = None

class ListaAdyacencia:
    def __init__(self):
        self.primera = None

    def agregar(self, destino, peso):
        nueva = Arista(destino, peso)
        nueva.siguiente = self.primera
        self.primera = nueva

class Grafo:
    def __init__(self):
        self.primero = None

    def agregarVertice(self, dato):
        if self.buscarVertice(dato):
            return
        nuevo = Vertice(dato)
        if self.primero is None:
            self.primero = nuevo
        else:
            temp = self.primero
            while temp.siguiente:
                temp = temp.siguiente
            temp.siguiente = nuevo

    def buscarVertice(self, dato):
        temp = self.primero
        while temp:
            if temp.dato == dato:
                return temp
            temp = temp.siguiente
        return None

    def agregarArista(self, origen, destino, peso):
        v1 = self.buscarVertice(origen)
        v2 = self.buscarVertice(destino)
        if v1 and v2:
            v1.listaAdyacencia.agregar(v2, peso)

    def Dijkstra(self, origen):
        inicio = self.buscarVertice(origen)
        if inicio is None:
            return None, None

        dist = {}
        prev = {}
        visitado = {}

        temp = self.primero
        while temp:
            dist[temp] = float("inf")
            prev[temp] = None
            visitado[temp] = False
            temp = temp.siguiente

        dist[inicio] = 0
        cola = ColaConPrioridad()
        cola.encolar((0, inicio))

        while not cola.esta_vacia():
            d_actual, actual = cola.desencolar()
            if visitado[actual]:
                continue
            visitado[actual] = True

            ar = actual.listaAdyacencia.primera
            while ar:
                nueva = dist[actual] + ar.peso
                if nueva < dist[ar.destino]:
                    dist[ar.destino] = nueva
                    prev[ar.destino] = actual
                    cola.encolar((nueva, ar.destino))
                ar = ar.siguiente

        return dist, prev

    def reconstruir_ruta(self, prev, origen, destino):
        ruta = []
        actual = self.buscarVertice(destino)
        if actual is None:
            return []
        while actual:
            ruta.insert(0, actual.dato)
            if actual.dato == origen:
                break
            actual = prev.get(actual)
        return ruta



mapa = Grafo()
zonas = ["Norte", "Sur", "Centro", "Oriente", "Occidente", "Industrial"]
for z in zonas:
    mapa.agregarVertice(z)

mapa.agregarArista("Norte", "Centro", 5)
mapa.agregarArista("Centro", "Norte", 5)
mapa.agregarArista("Sur", "Centro", 4)
mapa.agregarArista("Centro", "Sur", 4)
mapa.agregarArista("Centro", "Oriente", 3)
mapa.agregarArista("Oriente", "Centro", 3)
mapa.agregarArista("Centro", "Occidente", 3)
mapa.agregarArista("Occidente", "Centro", 3)
mapa.agregarArista("Occidente", "Industrial", 6)
mapa.agregarArista("Industrial", "Occidente", 6)
mapa.agregarArista("Oriente", "Industrial", 5)
mapa.agregarArista("Industrial", "Oriente", 5)



clientes = ListaLigada()
restaurantes = ListaLigada()
domiciliarios = ListaLigada()
pedidos = ColaPedidos()
historial = PilaHistorial()

restaurantes.insertar("Restaurante: La Parrilla, Zona Centro")
restaurantes.insertar("Restaurante: El Sabor, Zona Oriente")
restaurantes.insertar("Restaurante: Don Pepe, Zona Sur")
restaurantes.insertar("Restaurante: Sushi House, Zona Norte")

domiciliarios.insertar("Domiciliario: Carlos, Zona Occidente")
domiciliarios.insertar("Domiciliario: Ana, Zona Norte")
domiciliarios.insertar("Domiciliario: Pedro, Zona Sur")
domiciliarios.insertar("Domiciliario: Luisa, Zona Centro")


menus = {
    "La Parrilla": [
        "Carne Asada",
        "Pollo a la Plancha",
        "Costillas BBQ",
        "Chorizo Asado",
        "Ensalada Verde",
        "Limonada Natural"
    ],
    "El Sabor": [
        "Bandeja Paisa",
        "Sopa de Pollo",
        "Arroz con Pollo",
        "Arepa Rellena",
        "Jugo de Guayaba",
        "Chocolate Caliente"
    ],
    "Don Pepe": [
        "Hamburguesa Especial",
        "Perro Caliente",
        "Salchipapa",
        "Nuggets",
        "Gaseosa",
        "Malteada de Fresa"
    ],
    "Sushi House": [
        "Sushi Roll California",
        "Sushi Roll Tempura",
        "Nigiri de Salmón",
        "Ramen",
        "Té Verde",
        "Mochi"
    ]
}



def extraer_zona(texto):
    if not texto:
        return None
    lower = texto.lower()
    if "zona" not in lower:
        return None
    idx = lower.find("zona")
    zona = texto[idx+4:].replace(":", "").replace(",", "").strip()
    return zona

def extraer_nombre_restaurante(dato):
    try:
        start = dato.index(":") + 1
        mid = dato.index(",", start)
        return dato[start:mid].strip()
    except:
        return None

def restaurante_mas_cercano(zona_cli):
    dist, _ = mapa.Dijkstra(zona_cli)
    mejor = None
    menor = float("inf")

    actual = restaurantes.cabeza
    while actual:
        zona_r = extraer_zona(actual.dato)
        v = mapa.buscarVertice(zona_r)
        if v and dist.get(v, float("inf")) < menor:
            menor = dist[v]
            mejor = actual.dato
        actual = actual.siguiente
    return mejor

def domiciliario_mas_cercano(zona_rest):
    mejor = None
    menor = float("inf")

    actual = domiciliarios.cabeza
    while actual:
        zona_d = extraer_zona(actual.dato)
        dist, _ = mapa.Dijkstra(zona_d)
        v = mapa.buscarVertice(zona_rest)

        if v and v in dist and dist[v] < menor:
            menor = dist[v]
            mejor = actual.dato

        actual = actual.siguiente
    return mejor

def calcular_ruta_textual(z1, z2):
    if z1 == z2:
        return f"{z1} (recorrido local)", 1

    dist, prev = mapa.Dijkstra(z1)
    destino = mapa.buscarVertice(z2)

    if destino is None or dist.get(destino, float("inf")) == float("inf"):
        return "Ruta no encontrada", float("inf")

    ruta = mapa.reconstruir_ruta(prev, z1, z2)
    return " → ".join(ruta), dist[destino]




def crear_pedido_con_carrito():
    nombre = input("Nombre cliente: ").strip()
    zona = input("Zona cliente: ").strip()
    if not nombre or not zona:
        print("Datos incompletos.")
        return

    cliente_txt = f"Cliente: {nombre}, Zona {zona}"
    existe = clientes.buscar_por_nombre(nombre)
    if not existe:
        clientes.insertar(cliente_txt)

    rest = restaurante_mas_cercano(zona)
    if rest is None:
        print("No hay restaurantes.")
        return

    nom_rest = extraer_nombre_restaurante(rest)
    menu = menus.get(nom_rest, [])

    carrito = []
    print(f"\nRestaurante asignado: {rest}")

    while True:
        print("\n--- Menú ---")
        for i,item in enumerate(menu,1):
            print(f"{i}. {item}")

        op = input("(número) / v / f / c: ").lower().strip()

        if op == "v":
            print("\nCarrito:")
            for i, c in enumerate(carrito,1):
                print(f"{i}. {c}")
            continue
        if op == "c":
            print("Pedido cancelado.")
            return
        if op == "f":
            if not carrito:
                print("Carrito vacío.")
                continue
            pedido = f"Pedido - {nombre} - {rest} - Items: {'; '.join(carrito)}"
            pedidos.encolar(pedido)
            print("\nPedido registrado:")
            print(pedido)
            return

        try:
            idx = int(op)
            if 1 <= idx <= len(menu):
                carrito.append(menu[idx-1])
                print(f"Agregado: {menu[idx-1]}")
            else:
                print("Número fuera de rango.")
        except:
            print("Entrada inválida.")



def atender_pedido_auto():
    pedido = pedidos.desencolar()
    if pedido is None:
        return

    partes = pedido.split(" - ")
    cliente = partes[1]
    restaurante_txt = partes[2]

    rc = clientes.buscar_por_nombre(cliente)
    zona_cli = extraer_zona(rc)

    zona_rest = extraer_zona(restaurante_txt)

    dom = domiciliario_mas_cercano(zona_rest)
    if dom is None:
        print("No hay domiciliarios.")
        historial.apilar("CANCELADO: " + pedido)
        return

    zona_dom = extraer_zona(dom)
    print(f"\nDomiciliario asignado: {dom}")

    ruta1, c1 = calcular_ruta_textual(zona_dom, zona_rest)
    ruta2, c2 = calcular_ruta_textual(zona_rest, zona_cli)

    print("\nEl domiciliario pasó por:")
    if ruta1 == ruta2:
        print(ruta1)
    else:
        print(ruta1 + " → " + ruta2)

    historial.apilar("ENTREGADO: " + pedido)

    nombre_dom = dom.split(",")[0].replace("Domiciliario:", "").strip()
    domiciliarios.actualizar_por_nombre(nombre_dom, f"Domiciliario: {nombre_dom}, Zona {zona_cli}")

def cancelar_pedido_por_cliente():
    nombre = input("Cliente: ").strip()
    if not nombre:
        print("Vacío.")
        return
    ok = pedidos.eliminar_por_cliente(nombre)
    if ok:
        historial.apilar(f"CANCELADO: Pedido de {nombre}")
    else:
        print("No se encontró pedido.")







