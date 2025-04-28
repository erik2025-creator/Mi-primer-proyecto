import os
from funciones import (
    Carrito, 
    vaciar_carrito, 
    agregar_prod_carrito, 
    eliminar_prod_carrito, 
    finalizar_compra,  
    mostrar_menu, 
    mostrar_catalogo, 
    mostrar_carrito
)



#Limpia la consola
def limpiar_consola() -> None:
    os.system("cls" if os.name == "nt" else "clear")
    
#Función principal que ejecuta el programa
def main() -> None:
    carrito: Carrito = {}
    
    while True:
        limpiar_consola()
        mostrar_menu()
        
        try:
            opcion = input("\nEscoge una opcion a realizar -> ").strip()
            
            if opcion == "1":
                limpiar_consola()
                mostrar_catalogo()
                input("\nPresiona Enter para continuar...")
            
            elif opcion == "2":
                limpiar_consola()
                agregar_prod_carrito(carrito)
                input("\nPresiona Enter para continuar...")
            
            elif opcion == "3":
                limpiar_consola()
                eliminar_prod_carrito(carrito)
                input("\nPresiona Enter para continuar...")
            
            elif opcion == "4":
                limpiar_consola()
                vaciar_carrito(carrito)
                input("\nPresiona Enter para continuar...")
            
            elif opcion == "5":
                limpiar_consola()
                mostrar_carrito(carrito)
                input("\nPresiona Enter para continuar...")
            
            elif opcion == "6":
                limpiar_consola()
                finalizar_compra(carrito)
                input("\nPresiona Enter para continuar...")
            
            elif opcion == "7":
                print("\nHasta pronto 👋")
                break
            
            else:
                print("Opción no válida. Intente nuevamente.")
                input("\nPresiona Enter para continuar...")
        
        
        except Exception as e:
            print(f"\nOcurrió un error inesperado: {e}")
            input("\nPresiona Enter para continuar...")

if __name__ == "__main__":
    main()