class Rectangulo:
    ancho=0
    alto=0

    def __init__(self, ancho=0,alto=0):
        self.ancho=ancho
        self.alto=alto

    def calArea(self):
        return  self.ancho*self.alto
    def calPerimetro(self):
        return (2*(self.ancho+self.alto))
    def mostrarInfo(self,area,perimetro):
        print(f"\n\t.:Dotos del rectangulo:.\nAncho: {self.ancho}\nAlto: {self.alto}\nÁrea: {area}\nPerimetro: {perimetro}")

def datosRectangulo():
    ancho=float(input("Ingresa el ancho del Rectangulo: "))
    alto=float(input("Ingresa la altura del Rectangulo: "))
    return ancho,alto

an,al=datosRectangulo()
rectangulo=Rectangulo(an,al)
des=0
a=0
p=0
while des!=4:
    des=int(input("\n\t.:Opciones:.\n1.-Calcular Áraea\n2.-Calcular Perimetro\n3.-Mostrar datos del rectangulo\n4.-Salir\nOpción: "))
    if des==1:
        a=rectangulo.calArea()
    elif des==2:
        p=rectangulo.calPerimetro()
    elif des==3:
        rectangulo.mostrarInfo(a,p)
    
