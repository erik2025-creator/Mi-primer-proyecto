from typing import Dict, List, Tuple
import os

Carrito=Dict[str , int]
Producto = Dict[str, str | float ]
Catalogo = Dict[ str , Producto]

#Catalog inicial de productos 

CATALOGO : Catalogo = {
    "A001": {"nombre": "Pan", "precio": 1.50},
    "B203": {"nombre": "Leche", "precio": 3.80},
    "C456": {"nombre": "Huevos (docena)", "precio": 6.20},
    "D789": {"nombre": "Arroz (1kg)", "precio": 4.50},
    "E012": {"nombre": "Aceite (1L)", "precio": 8.30},
    "F345": {"nombre": "Azúcar (1kg)", "precio": 3.20},
}

def mostrar_menu() -> None:
    """Muestra el menú de opciones"""
    print("\nBienvenido a la tienda virtual 🛍️")
    print("¿Qué deseas hacer?\n")
    print("1. Ver catálogo")
    print("2. Agregar producto al carrito")
    print("3. Eliminar producto del carrito")
    print("4. Vaciar carrito")
    print("5. Mostrar carrito")
    print("6. Finalizar compra")
    print("7. Salir")

#Limpia la consola
def limpiar_consola() -> None :
    os.system(os.system("cls" if os.name == "nt" else "clear"))
    
    
#Muestra todos los productos disponibles en el catálogo
def mostrar_catalogo() -> None: 
    print("\n📋 Catálogo de Productos:")
    for codigo , producto in CATALOGO.items():
        print(f"Codigo: {codigo} | Producto : {producto['nombre']} | Precio : S/{producto['precio']}")
    print()

#Agrega un producto al carrito de compras
def agregar_prod_carrito(carrito : Carrito) -> None :
    mostrar_catalogo()
    codigo=input("Ingrese el Codigo de producto a agregar: ").strip().upper()
    
    if codigo not in CATALOGO:
        print("Error: El codigo no existe en el catalogo,")
        return
    try:
        cantidad=int(input("Inserte la cantidad agregar del producto: "))
        if cantidad >=0:
            carrito[codigo]=carrito.get(codigo,0)+cantidad
            print(f"Producto {CATALOGO[codigo]["nombre"]} agregado al carrito")
        else:
            print("Error: La cantidad debe ser mayor a cero.")
            return
    except ValueError:
        print("Error : Ingrese un numero valido")
        
carrito: Carrito = {}
agregar_prod_carrito(carrito)