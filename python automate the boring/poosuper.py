class Producto:
    def __init__(self, nombre, precio, pn=None, pc=False):
        self.nombre = nombre
        self.precio = precio
        self.pc = pc
        self.pn = float(pn)
        self.__descuento()
    
    def __repr__(self):
        return f'Nombre: {self.nombre}, Precio: {self.precio}, P_Cuidado: {self.pc}, Descuento: {self.pn}'
    
    def __descuento(self):
        self.precio = self.precio - self.precio*self.pn/100
        
class Catalogo:
    def __init__(self):
        self.catalogo = dict()

    def añadir(self):
        print('-'*25)
        seccion = input('Seccion: ')
        nombre = input('Nombre del producto: ')
        precio = float(input('Precio del producto: '))
        pn = input('Descuento: ')
        self.catalogo.setdefault(seccion, [])
        self.catalogo[seccion].append(Producto(nombre, precio, pn))
