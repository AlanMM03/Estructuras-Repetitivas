class Coche():
    #Atributos
    estado=False
    marca = None
    modelo= None
    color= None
    velocidad=0
    #Constructor
    def __init__(self, marca,modelo,color,velocidad=0,estado=False):
        self.marca=marca
        self.modelo=modelo
        self.color=color
        self.velocidad=velocidad
        self.estado=estado
    #Metodo
    def acelerar(self):
        ace=int(input("Ingresa la velociada a la que deseas acelerar: "))
        i=0
        while self.velocidad<=ace:
            self.velocidad+=2
            print(f"{self.velocidad} km/h")
    #Metodo
    def frenar(self):
        if self.velocidad!=0:
            fre=int(input("¿Cuantos segundos desea frenar? "))
            i=1
            while i<=fre:
                if self.velocidad>0:
                    self.velocidad-=3
                    print(f"{self.velocidad} km/h")
                else:
                    print(f"\nNo puedes frenar más, la velocidad del coche es {self.velocidad} km/h\n")
                    break
                i+=1
        else:
            print("\nEl coche esta detenido\n")
    #Método    
    def mostrarInfo(self):
        print(f"\t\n.:Información del coche:.\nMarca: {self.marca}\nModelo: {self.modelo}\nColor: {self.color}\nVelocidad: {self.velocidad}km/h\n")
    #Método
    def apagar(self):
        if self.estado != False:
            self.estado=False
            print("\nAPAGADO\n")
        else:
            print("\nEl coche ya esta apagado...\n")
    #Método
    def encender(self):
        if self.estado !=True:
            self.estado=True
            print("\nENCENDIDO\n")
        else:
            print("El coche ya esta encendido...")
#Función
def infoCoche():
    ma=input("Marca del coche: ")
    mo=input("Modelo del coche: ")
    c=input("Color del coche: ")
    
    return ma,mo,c

ma,mo,c=infoCoche()
coche=Coche(ma,mo,c)
res=0
while res != 5:
    res=int(input("\tOpciones\n1.-Encender\n2.-Acelerar\n3.-Frenar\n4.-Información del coche \n5.-Apagar\nRespuesta: "))
    if res==1:
        coche.encender()
    elif res==2:
        coche.acelerar()
    elif res==3:
        coche.frenar()
    elif res==4:
        coche.mostrarInfo()
    elif res==5:
        coche.apagar()