#!/usr/bin/python3

from DB import BaseDatos

Base_Datos_Pulpe = BaseDatos('base_pulpe.sqlite')

# -----------------------------Funciones------------------------ #


def revisar_venta(lista):

    string_insert = 'INSERT INTO ventas (nombre_cliente, producto, '\
                    'id_producto, cantidad, costo_por_producto, id_factura) '\
                    'VALUES '
    update_list = []

    no_inventory = False

    m1 = ''

    total_pagar = 0

    query3 = 'SELECT MAX(id) FROM facturas'
    ultima_factura = Base_Datos_Pulpe.execute_read_query(query3)[0][0]

    if ultima_factura is None:
        id_factura = 1
    else:
        id_factura = ultima_factura + 1

    for una_venta in lista:
        nombre_cliente = '\'' + una_venta[0] + '\''
        producto = '\'' + una_venta[1] + '\''
        cantidad_producto_compra = una_venta[2]

        query1 = 'Select id FROM inventario '\
                 'WHERE producto = {}'.format(producto)
        id_producto = Base_Datos_Pulpe.execute_read_query(query1)[0][0]

        query2 = 'Select costo_producto FROM inventario '\
                 'WHERE producto = {}'.format(producto)
        costo_por_producto = Base_Datos_Pulpe.execute_read_query(query2)[0][0]

        query = 'SELECT cantidad_producto FROM inventario WHERE '\
                'id = {}'.format(id_producto)
        dato = Base_Datos_Pulpe.execute_read_query(query)[0][0]

        if dato >= cantidad_producto_compra:
            can = cantidad_producto_compra
            total_pagar = total_pagar + costo_por_producto*can

            update_cantidad = dato - cantidad_producto_compra

            if update_cantidad == 0:
                update_cantidad = 'NULL'

            update_string = 'UPDATE inventario SET cantidad_producto = {} '\
                            'WHERE id = '\
                            '{}'.format(update_cantidad, id_producto)

            update_list.append(update_string)

            a = nombre_cliente
            b = producto
            c = id_producto
            d = cantidad_producto_compra
            e = costo_por_producto
            f = id_factura

            value = '({}, {}, {}, {}, {}, {}), '.format(a, b, c, d, e, f)

            string_insert = string_insert + value

        else:
            no_inventory = True
            m1 = m1 + producto + ', '

    factura = 'INSERT INTO facturas (id, nombre_cliente, monto_a_pagar) '\
              'VALUES '\
              '({}, {}, {})'.format(id_factura, nombre_cliente, total_pagar)

    if no_inventory is True:
        m0 = 'No hay suficiente cantidad en los siguientes productos: '
        m0 = m0 + m1
        message = m0[:-2]
    else:
        message = 'Existe suficiente cantidad en todos los productos'

    ventas = string_insert[:-2]
    actualizacion = update_list
    return (message, ventas, actualizacion, factura)


def hacer_venta(ventas, actualizacion, factura):

    Base_Datos_Pulpe.execute_query(factura)
    a = Base_Datos_Pulpe.execute_query(ventas)
    print(a)
    for elemento in actualizacion:
        Base_Datos_Pulpe.execute_query(elemento)

    return ('Ventas correctamente agregadas a la base de datos')


def ingresar_proveedor(list):
    string_insert = 'INSERT INTO proveedores (proveedor) '\
                    'VALUES '

    for element in list:
        string_insert = string_insert + '(\'' + str(element) + '\'), '

    string_insert = string_insert[:-2]
    ejecucion = Base_Datos_Pulpe.execute_query(string_insert)
    return ejecucion

# [id_producto, 'producto', cantidad, 'proveedor', id_proveedor]
def agregar_producto_proveedor(list):

    # ingresa articulo por articulo
    # Tiene que existir el producto en agregar_inventario
    # Tiene que existir el proveedor en la tabla 'proveedores'
    # list = [codigo_producto, producto, cantidad, proveedor, id_proveedor]
    # a = list[0]
    b = '\'' + str(list[0]) + '\''
    c = list[1]
    d = '\'' + str(list[2]) + '\''
    # e = list[4]

    query4 = 'Select id FROM inventario '\
             'WHERE producto = {}'.format(b)
    a = Base_Datos_Pulpe.execute_read_query(query4)[0][0]

    query5 = 'Select id FROM proveedores '\
             'WHERE proveedor = {}'.format(d)
    print(query5)
    e = Base_Datos_Pulpe.execute_read_query(query5)[0][0]

    query1 = 'INSERT INTO producto_proveedores (codigo_producto, producto, '\
             'cantidad, proveedor, id_proveedor) '\
             'VALUES ({}, {}, {}, {}, {})'.format(a, b, c, d, e)

    ejecuacion1 = Base_Datos_Pulpe.execute_query(query1)

    query2 = 'SELECT cantidad_producto FROM inventario WHERE '\
             'id = {}'.format(a)

    vieja_cantidad = Base_Datos_Pulpe.execute_read_query(query2)[0][0]

    if vieja_cantidad is None:
        vieja_cantidad = 0

    nueva_cantidad = c + vieja_cantidad

    query3 = 'UPDATE inventario SET cantidad_producto = {} '\
             'WHERE id = {}'.format(nueva_cantidad, a)
    ejecucion3 = Base_Datos_Pulpe.execute_query(query3)

    print(ejecuacion1)
    print()
    print(ejecucion3)


def agregar_producto(producto, costo):
    # Agregar articulo por articulo
    producto = '\'' + producto + '\''
    query = 'INSERT INTO inventario (producto, costo_producto) '\
            'VALUES ({}, {})'.format(producto, costo)

    print(Base_Datos_Pulpe.execute_query(query))


def buscar_productos():
    lista_productos = []
    query = 'SELECT producto FROM inventario '\
            'WHERE cantidad_producto IS NOT NULL'
    busqueda = Base_Datos_Pulpe.execute_read_query(query)
    for producto in busqueda:
        lista_productos.append(producto[0])
    return lista_productos


def buscar_todos_productos():
    lista_productos = []
    query = 'SELECT producto FROM inventario '
    busqueda = Base_Datos_Pulpe.execute_read_query(query)
    for producto in busqueda:
        lista_productos.append(producto[0])
    return lista_productos


def buscar_proveedores():
    lista_proveedores = []
    query = 'SELECT proveedor FROM proveedores'
    busqueda = Base_Datos_Pulpe.execute_read_query(query)
    for proveedor in busqueda:
        lista_proveedores.append(proveedor[0])
    return lista_proveedores


def buscar_cantidad(producto):
    producto = '\'' + producto + '\''
    query = 'SELECT cantidad_producto FROM inventario WHERE '\
            'producto = {}'.format(producto)
    busqueda = Base_Datos_Pulpe.execute_read_query(query)[0][0]
    if busqueda is None:
        print(':)')
        busqueda = 0
        lista = [[0]]
    else:
        print(':(')
        a = 1
        lista = []
        for i in range(0, busqueda):
            b = str(a)
            lista.append(b)
            a = a + 1
        return (busqueda, lista)


def buscar_precio(producto):
    producto = '\'' + producto + '\''
    query = 'SELECT costo_producto FROM inventario WHERE '\
            'producto = {}'.format(producto)
    busqueda = Base_Datos_Pulpe.execute_read_query(query)[0][0]
    return busqueda


def mostrar_inventario():
    query = 'SELECT producto, cantidad_producto, costo_producto FROM '\
            'inventario'
    busqueda = Base_Datos_Pulpe.execute_read_query(query)
    return busqueda

# -----------------------Variables de Prueba------------------------#


proveedores = ['Verduras SA',
               'Agricultorse SA',
               'Bimbo',
               'Frutas SA'
               ]

lista_venta_Carlos = [
                ['Carlos', 'Pera', 20],
                ['Carlos', 'Manzana', 1],
                ['Carlos', 'Arroz', 1]
]

lista_venta_Juan = [
                ['Juan', 'Frijoles', 1],
                ['Juan', 'Pan', 3],
                ['Juan', 'Cebolla', 2]
]


producto_proveedor1 = ['Pera', 20, 'Verduras SA']
producto_proveedor2 = ['Manzana', 25, 'Verduras SA']
producto_proveedor3 = ['Arroz', 15, 'Agricultorse SA']
producto_proveedor4 = ['Frijoles', 20, 'Agricultores SA']
producto_proveedor5 = ['Pan', 20, 'Bimbo']
producto_proveedor6 = ['Cebolla', 20, 'Verduras SA']

# ---------------Ejemplos de cómo usar  las funciones-------------------#
# des-silenciando estos bloques se llena la base de datos:

# Agragar inventario:
# agregar_producto('Pera', 500)
# agregar_producto('Manzana', 400)
# agregar_producto('Arroz', 1000)
# agregar_producto('Frijoles', 950)
# agregar_producto('Pan', 600)
# agregar_producto('Cebolla', 200)

# Agragar proveedores:
# ingresar_proveedores = ingresar_proveedor(proveedores)

# Agregar inventario:
# agregar_producto_proveedor(producto_proveedor1)
# agregar_producto_proveedor(producto_proveedor2)
# agregar_producto_proveedor(producto_proveedor3)
# agregar_producto_proveedor(producto_proveedor4)
# agregar_producto_proveedor(producto_proveedor5)
# agregar_producto_proveedor(producto_proveedor6)

# Hacer una venta:
#revision = revisar_venta(lista_venta_Carlos)
# print(type(revision))
#venta = hacer_venta(revision[1], revision[2], revision[3])
# revision2 = revisar_venta(lista_venta_Juan)
# venta2 = hacer_venta(revision2[1], revision2[2], revision2[3])


# print()
# print('BUSQUEDAS')
# print()

# Obtener Productos

#print(buscar_productos())

# Obtener proveedores
# print(buscar_proveedores())

# Obtener cantidades seleccionables:
# print(buscar_cantidad('Pera'))
