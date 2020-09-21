class Descuento:
    def __init__(self, tipo, valor):
        if not isinstance(tipo, str):
            raise ValueError('TIPO debe ser string')
        if not isinstance(valor, int):
            raise ValueError('VALOR debe ser un entero')
        if valor<=0:
            raise ValueError('El descuento debe ser positivo')
        if valor>100 and tipo.lower == "porcentaje":
            raise ValueError('Descuento maximo permitido 100%')
        self.__tipo = tipo
        self.__valor = valor
    @property
    def tipo(self):
        return self.__tipo
    @tipo.setter
    def tipo(self, tipo):
        self.__tipo = tipo
    @property
    def valor(self):
         return self.__valor
    @valor.setter
    def valor(self, valor):
        self.__valor = valor
    def realizar_descuento(self, precio):
        if self.__tipo.lower() == 'fijo':
            if precio > self.__valor:
                return precio - self.__valor
            else:
                return 0
        if self.__tipo.lower() == "porcentaje":
            return precio - (precio*self.__valor/100) 
        else:
            raise Exception('Tipo incorrecto')

class Producto:
    def __init__(self, codigo, nombre, precio, descuento= None):
        self.__codigo = codigo
        self.__nombre = nombre
        self.__precio = precio
        self.__descuento = descuento
    @property
    def codigo(self):
        return self.__codigo
    @codigo.setter
    def codigo(self, valor):
        self.__codigo = valor
    @property
    def nombre(self):
        return self.__nombre
    @nombre.setter
    def nombre(self, valor):
        self.__nombre = valor   
    @property
    def precio(self):
        if self.__descuento == None:
            return self.__precio
        else:
            return self.__descuento.realizar_descuento(self.__precio)
    @precio.setter
    def precio(self, valor):
        self.__precio = valor
    def __str__(self):
        return f"Codigo: {self.__codigo}, Descripcion:{self.__nombre}, Precio: {self.__precio}"
    def calcular_precio(self, u):
        return self.precio * u
    def precio_por_unidades(self, u):
        return f"El precio por {u} unidades es: {self.calcular_precio(u)}"
class Pedido:
    def __init__(self):
        self.__productos = []
        self.__cantidades = []
    def aniadir_producto(self, producto, cantidad):
        if not isinstance(producto, Producto):
            raise Exception("Debe ingresar un producto valido.")
        if not isinstance(cantidad, int):
            raise Exception("Debe ingresar un numero")
        if cantidad<1:
            raise Exception("Debe ingresar al menos un producto.")
        if producto in self.__productos:
            bandera = self.__productos.index(producto)
            self.__cantidades[bandera] += cantidad
        else:
            self.__productos.append(producto)
            self.__cantidades.append(cantidad)

    def eliminar_producto(self, producto):
        if not isinstance(producto, Producto):
            raise Exception("Debe ingresar un producto valido.")
        if producto not in self.__productos:
            raise Exception("Producto no encontrado en el pedido")
        else:
            bandera = self.__productos.index(producto)
            del self.__productos[bandera]
            del self.__cantidades[bandera]

    def total_pedido(self):
        total = 0
        for (p,c) in zip(self.__productos, self.__cantidades):
            total += p.calcular_precio(c)
        return total  
    def mostrar_pedido(self):
        for p,c in zip(self.__productos, self.__cantidades):
            print(f"Descripcion: {p.nombre}\t ->Cant.: {c} ->\tP. total: {p.calcular_precio(c)}")
desc1 = Descuento("fijo", 150)
desc2 = Descuento("porcentaje", 50)
p1 = Producto(1015, "Chancla", 750, desc1)
p2 = Producto(1016, "Remera", 500, desc2 )
p3 = Producto(1017, "Pantalon", 2000)

try:
    pedido = Pedido()
    
    pedido.aniadir_producto(p1, 4)
    pedido.aniadir_producto(p2, 8)
    pedido.aniadir_producto(p3, 2)


    pedido.mostrar_pedido()
    print("------------------------------------------------------")
    print("\t\t\t\tTotal pedido: ", pedido.total_pedido())
    print()
    pedido.eliminar_producto(p1)#eliminamos un producto
    
    pedido.mostrar_pedido()
    print("------------------------------------------------------")
    print("\t\t\t\tTotal pedido: ", pedido.total_pedido())
except Exception as e:
    print(e) 