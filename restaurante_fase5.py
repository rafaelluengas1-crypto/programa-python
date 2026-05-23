# ==============================================================================
# Autor: Rafael Andrés Luengas Rondón
# Curso: Fundamentos de Programación (213022) - UNAD
# Fase 5 - Evaluación Final
# Descripción: Solución al Problema 2 (Promoción de menú de restaurante)
# ==============================================================================

def calcular_precio_final(categoria, precio_base, categoria_objetivo, umbral):
    """
    Módulo para calcular el precio final de un producto.
    Aplica un 15% de descuento si el producto cumple con la categoría objetivo
    y su precio base es mayor al umbral definido.
    """
    # Lógica de negocio: validación de categoría y umbral de precio
    if categoria.lower() == categoria_objetivo.lower() and precio_base > umbral:
        descuento = precio_base * 0.15
        return precio_base - descuento
    else:
        # Mantiene el precio base si no se cumplen las condiciones
        return precio_base

def main():
    # Matriz con 6 productos de diversas categorías [Nombre, Categoría, Precio Base]
    menu = [
        ["Hamburguesa Sencilla", "Comidas Rápidas", 18000.0],
        ["Hamburguesa Doble", "Comidas Rápidas", 25000.0],
        ["Limonada Cerezada", "Bebidas", 7000.0],
        ["Cerveza Artesanal", "Bebidas", 12000.0],
        ["Ensalada César", "Saludable", 22000.0],
        ["Pizza Familiar", "Comidas Rápidas", 45000.0]
    ]

    # Parámetros de la promoción
    categoria_objetivo = "Comidas Rápidas"
    umbral_precio = 20000.0

    print("=== REPORTE DE PRECIOS DEL MENÚ ===")
    print(f"Promoción: 15% de descuento para '{categoria_objetivo}' en compras mayores a ${umbral_precio:,.0f}\n")

    # Ciclo iterativo para procesar e imprimir la salida de cada producto
    for producto in menu:
        nombre = producto[0]
        categoria = producto[1]
        precio_base = producto[2]

        # Llamado al módulo (función) para calcular el precio
        precio_final = calcular_precio_final(categoria, precio_base, categoria_objetivo, umbral_precio)

        # Salida de resultados
        print(f"Producto: {nombre} ({categoria})")
        print(f"Precio Base:  ${precio_base:,.2f}")
        print(f"Precio Final: ${precio_final:,.2f}")
        print("-" * 40)

if __name__ == "__main__":
    main()
