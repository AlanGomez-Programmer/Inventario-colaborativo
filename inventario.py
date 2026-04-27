from json import load, dumps

ruta_inventario = "inventario.json"

def leer_archivo(ruta):
    with open(ruta, "r") as archivo:
        datos = load(archivo)
        return datos
   

def guardar_datos(ruta, datos):
    with open(ruta, "w") as archivo:
        archivo.write(dumps(datos, indent=4))
   


def agregar_productos():

    productos = leer_archivo(ruta_inventario)

    nombre = input("PRODUCTO: ").strip()
    precio = float(input("PRECIO: ").strip())
    cantidad = int(input("CANTIDAD: ").strip())

    producto = {
        "precio": precio,
        "cantidad": cantidad
    }

    productos[nombre] = producto

    guardar_datos(ruta_inventario, productos)
    print("Producto agregado correctamente...")

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
