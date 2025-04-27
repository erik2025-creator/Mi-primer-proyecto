from typing import Dict

# Definición de tipos para mejorar la legibilidad
Producto = Dict[str, str | float]
Catalogo = Dict[str, Producto]

# Catálogo inicial de productos
CATALOGO: Catalogo = {
    "A001": {"nombre": "Pan", "precio": 1.50},
    "B203": {"nombre": "Leche", "precio": 3.80},
    "C456": {"nombre": "Huevos (docena)", "precio": 6.20},
    "D789": {"nombre": "Arroz (1kg)", "precio": 4.50},
    "E012": {"nombre": "Aceite (1L)", "precio": 8.30},
    "F345": {"nombre": "Azúcar (1kg)", "precio": 3.20},
}