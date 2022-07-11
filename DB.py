#!/usr/bin/python3

import sqlite3
from sqlite3 import Error


class BaseDatos:

    def __init__(self, path):
        connection = None
        try:
            self.connection = sqlite3.connect(path)
            print("Connection to SQLite DB successful")
        except Error as e:
            print(f"The error '{e}' occurred")

        crear_tabla_facturas = """
        CREATE TABLE IF NOT EXISTS facturas (
          id INTEGER PRIMARY KEY,
          nombre_cliente TEXT NOT NULL,
          monto_a_pagar INTEGER NOT NULL,
          Timestamp Fecha DEFAULT CURRENT_TIMESTAMP
        );
        """

        crear_tabla_inventario = """
        CREATE TABLE IF NOT EXISTS inventario (
          id INTEGER PRIMARY KEY AUTOINCREMENT,
          producto TEXT UNIQUE NOT NULL,
          costo_producto INTEGER NOT NULL,
          cantidad_producto INTEGER
        );
        """

        crear_tabla_ventas = """
        CREATE TABLE IF NOT EXISTS ventas (
          id INTEGER PRIMARY KEY AUTOINCREMENT,
          nombre_cliente TEXT NOT NULL,
          producto TEXT NOT NULL,
          id_producto INTEGER NOT NULL,
          cantidad INTEGER NOT NULL,
          costo_por_producto INTEGER NOT NULL,
          Timestamp Fecha DEFAULT CURRENT_TIMESTAMP,
          id_factura INTEGER NOT NULL,
          FOREIGN KEY (id_factura) REFERENCES facturas (id),
          FOREIGN KEY (id_producto) REFERENCES inventario(id)
        );
        """

        crear_tabla_proveedores = """
        CREATE TABLE IF NOT EXISTS proveedores (
          id INTEGER PRIMARY KEY AUTOINCREMENT,
          proveedor TEXT UNIQUE NOT NULL
        );
        """

        # Falta arreglar
        crear_tabla_producto_proveedores = """
        CREATE TABLE IF NOT EXISTS producto_proveedores (
          id INTEGER PRIMARY KEY AUTOINCREMENT,
          codigo_producto TEXT NOT NULL,
          producto TEXT NOT NULL,
          cantidad INTEGER NOT NULL,
          proveedor TEXT NOT NULL,
          id_proveedor INTEGER NOT NULL,
          Timestamp Fecha DEFAULT CURRENT_TIMESTAMP,
          FOREIGN KEY (codigo_producto) REFERENCES inventario (id),
          FOREIGN KEY(id_proveedor) REFERENCES proveedores(id)
        );
        """

        self.cursor = self.connection.cursor()
        self.cursor.execute("PRAGMA foreign_keys = ON")
        self.cursor.execute(crear_tabla_inventario)
        self.cursor.execute(crear_tabla_facturas)
        self.cursor.execute(crear_tabla_ventas)
        self.cursor.execute(crear_tabla_proveedores)
        self.cursor.execute(crear_tabla_producto_proveedores)

        return connection

    def execute_query(self, query):
        self.cursor = self.connection.cursor()
        self.cursor.execute("PRAGMA foreign_keys = ON")
        try:
            self.cursor.execute(query)
            self.connection.commit()
            message = "Query executed successfully"
        except Error as e:
            message = f"The error '{e}' occurred"
        return message

    def execute_read_query(self, query):
        result = None
        self.cursor = self.connection.cursor()
        try:
            self.cursor.execute(query)
            result = self.cursor.fetchall()
            return result
        except Error as e:
            print(f"The error '{e}' occurred")
