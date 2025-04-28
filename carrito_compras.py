from typing import Dict, List, Tuple
import os
from datetime import datetime

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
            print(f"Producto {CATALOGO[codigo]["nombre"]} (x{carrito[codigo]}) agregado al carrito")
        else:
            print("Error: La cantidad debe ser mayor a cero.")
            return
    except ValueError:
        print("Error : Ingrese un numero valido")
        
#Mostrar el contenido del carrito de compras
def mostrar_carrito(carrito : Carrito) -> None:
    if not carrito:
        print("Tu carrito se encuentra vacio")
        return
        
    print(f"\nContenido de mi carrito: \n")
    total =0.0
    
    for codigo, cantidad in carrito.items():
        total_producto= CATALOGO[codigo]["precio"]*cantidad
        total += total_producto
        print(f" Producto : {CATALOGO[codigo]["nombre"]} (x{cantidad}) -> S/{total_producto:.2f}")
    print()    
    print(f"Tu total a pagar : S/{total:.2f}")

def vaciar_carrito(carrito : Carrito) -> None:
    if not carrito:
        print("Tu carrito se encuentra vacio")
        return
    carrito.clear()
    print("El contenido de tu carrito fue eliminado exitosamente.")
    
#Quita un producto al carrito de compras
def eliminar_prod_carrito(carrito : Carrito)-> None:
    if not carrito:
        mostrar_carrito()
        return
    mostrar_carrito(carrito)
    codigo=input("Introduce el Codigo del Producto a Eliminar : ").strip().upper()
    
    if codigo not in carrito:
        print("El codigo : {codigo} introducido no se encuentra en el carrito")
        return
    try:
        cantidad= int(input(f"Cantidad a eliminar (actualmente : {carrito[codigo]}): "))
        if cantidad <=0 :
            print("La cantidad debe ser mayor a cero ")
            return
        if cantidad > carrito[codigo]:
            print("Error La cantidad debe ser menor o igual a la que tienes ")
            return
    except ValueError:
        print("Error Debes Ingresar un numero para la cantidad a eliminar ")
        return
    #Actualiza al carrito de compras
    if cantidad==carrito[codigo]:
        del carrito[codigo]
        print(f" Producto : {CATALOGO[codigo]["nombre"]} eliminado del carrito")
    else :
        carrito[codigo] -= cantidad 
        print(f" Se eliminaron del carrito (x{cantidad}) cantidad(es) del producto: {CATALOGO[codigo]["nombre"]} ")
    
 #Finaliza la compra
def finalizar_compra(carrito : Carrito ) -> None :
    if not carrito:
        print("No se pudo procesar, el carrito se encuenta vacio")
        return
    mostrar_carrito(carrito)
    print("\nResumen de tu compra: ")
    
    total=0
    productos_comprados =[]
    
    for codigo , cantidad in carrito.items() :
        producto= CATALOGO[codigo]
        total_producto= producto["precio"]*cantidad
        total += total_producto
        productos_comprados.append(f"{producto["nombre"]} (x{cantidad}) - S/{total_producto:.2f}")
        print(f"- {producto["nombre"]} (x{cantidad}) - S/{total_producto:.2f}")
    print(f"\nTotal a pagar: S/{total:.2f}")
    print("Procesando pago...")
    print("Pago realizado con éxito. ¡Gracias por tu compra! ")
    
    #Reto Guardar en un .txt 
    registrar_compra(productos_comprados,total)
    
    #Limpiar el carrito
    #vaciar_carrito(carrito)
    carrito.clear()

#Registra la compra en un archivo .txt
def registrar_compra(productos_comprados : List[str],total : float) -> None:
    try:
        with open("historial_compras.txt" , "a" , encoding= "utf-8") as archivo :
            fecha=datetime.now().strftime("%Y/%m/%d, %H:%M:%S")
            archivo.write(f"\n Resumen de Compra del {fecha}\n")
            archivo.write("------------------\n")
            for producto in productos_comprados:
                archivo.write(f"✔ {producto}\n")
            archivo.write(f"Total pagado: S/{total:.2f}\n")
    except Exception as error:
        print(f"No se pudo registrar el Historial : {error}")
    
      
      
carrito: Carrito = {}
agregar_prod_carrito(carrito)
mostrar_carrito(carrito)
eliminar_prod_carrito(carrito)
mostrar_carrito(carrito)
finalizar_compra(carrito)
agregar_prod_carrito(carrito)
finalizar_compra(carrito)