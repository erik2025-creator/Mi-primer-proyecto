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
    
print(mostrar_menu())