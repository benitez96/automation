import tkinter as tk

class Calculadora:
    
    def __init__(self, win):
        self.win = win
        self.win.title("Calcular importe")
        self.win.geometry("300x250")
        self.win.config(bg="#105e91")
        contenedor = tk.Frame(root, bg="#105e91")
        contenedor.pack()
        self.cobropant = tk.StringVar()
        self.pointpant = tk.StringVar()
        tk.Label(contenedor, text="6%+IVA", bg="#105e91").grid(row=0)
        tk.Label(contenedor, text="MONTO A COBRAR", bg="#105e91", font="FranklinGothicHeavy").grid(row=1)
        cobro = tk.Entry(contenedor, textvariable=self.cobropant)
        cobro.focus()
        cobro.grid(row=2)
        boton = tk.Button(contenedor, text="CALCULAR", command=lambda:self.porc())
        # self.win.bind('<Return>', lambda:self.porc) # NO FUNCIONA NO SE POR QUE
        boton.grid(row=3, pady=20)
        tk.Label(contenedor, text="INGRESAR EN POINT", bg="#105e91", font="FranklinGothicHeavy").grid(row=4)
        tk.Entry(contenedor, textvariable=self.pointpant).grid(row=5)
        self.win.mainloop()
    def porc(self):
        p = 0.06 # porcentaje
        iva = 0.21 #iva
        x = float(self.cobropant.get())
        y = x/(1-1*p-1*p*iva)
        self.pointpant.set(round(y, 2))    
        
        
root = tk.Tk()
calculadora = Calculadora(root) 
calculadora
