from Proyecto import (
    clientes,
    restaurantes,
    domiciliarios,
    pedidos,
    historial,
    crear_pedido_con_carrito,
    atender_pedido_auto,
    cancelar_pedido_por_cliente

)

print("=========================================================")
print("     SISTEMA DE GESTIÓN Y SIMULACIÓN DE PEDIDOS          ")
print("=========================================================")

def mostrar_menu():
    print("\nMenú principal:")
    print("1. Crear pedido")
    print("2. Atender primer pedido")
    print("3. Mostrar restaurantes disponibles")
    print("4. Mostrar domiciliarios disponibles")
    print("5. Mostrar pedidos pendientes")
    print("6. Mostrar historial de entregas")
    print("7. Cancelar pedido por cliente")
    print("8. Salir")

def opcion_crear_pedido():
    print("\n--- Crear pedido con carrito ---")
    crear_pedido_con_carrito()

def opcion_atender():
    print("\n--- Atender pedido ---")
    atender_pedido_auto()

def opcion_restaurantes():
    print("\n--- Restaurantes predefinidos ---")
    restaurantes.mostrar()

def opcion_domiciliarios():
    print("\n--- Domiciliarios predefinidos (con ubicación actual) ---")
    domiciliarios.mostrar()

def opcion_pedidos():
    print("\n--- Pedidos en cola ---")
    pedidos.mostrar()

def opcion_historial():
    print("\n--- Historial de entregas ---")
    historial.mostrar()


while True:
    try:
        mostrar_menu()
        opcion = int(input("Seleccione una opción: "))
    except ValueError:
        print("Entrada inválida. Intente nuevamente.")
        continue

    if opcion == 1:
        opcion_crear_pedido()
    elif opcion == 2:
        opcion_atender()
    elif opcion == 3:
        opcion_restaurantes()
    elif opcion == 4:
        opcion_domiciliarios()
    elif opcion == 5:
        opcion_pedidos()
    elif opcion == 6:
        opcion_historial()
    elif opcion == 7:
        cancelar_pedido_por_cliente()
    elif opcion == 8:
        print("\nSaliendo... ¡Hasta luego!")
        break
    else:
        print("Opción no válida. Intente nuevamente.")
