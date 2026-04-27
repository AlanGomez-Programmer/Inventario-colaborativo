def listar_productos():

    productos = leer_archivo(ruta_inventario)

    if not productos:
        print("No hay productos.")
    
    else:
        for nombre in productos:
            precio = productos[nombre]["precio"]
            cantidad = productos[nombre]["cantidad"]
            print(f"Producto : {nombre}")
            print(f"Precio : {precio}")
            print(f"Cantidad : {cantidad}")
