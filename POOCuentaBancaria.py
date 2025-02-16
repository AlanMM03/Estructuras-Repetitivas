class CuentaBancaria:
    titular=None
    saldo=0

    def __init__(self, titular, saldo=0):
        self.titular=titular
        self.saldo=saldo        

    def depositar(self):
        dep=float(input("\n¿Cuanto desea depositar? $"))
        self.saldo=dep
        print(f"Se ha depositado con exito ${dep:,.2f} pesos.\n")
    def retirar(self):
        re=float(input("\n¿Cuanto desea retirar? $"))
        if re>self.saldo:
            print(f"No cuenta con los fondos requeridos para retirar ${re:,.2f} pesos.")
        elif re<=self.saldo:
            print(f"Se ha retirado con exito ${re:,.2f} pesos.")
            self.saldo-=re

    def mostrarSaldo(self):
        print("\n\t.:Información de la cuenta:.\n")
        print(f"Nombre del titular: {self.titular}")
        print(f"Saldo de la cuenta: ${self.saldo:,.2f}")

ti=input("Ingresa tu nombre: ")
cliente=CuentaBancaria(ti)
des=0
while des!=4:
    des=int(input("\n\t.:Menú:.\n1.-Depositar\n2.-Retirar\n3.-Mostrar Cuenta\n4.-Salir\nOpción: "))
    if des==1:
        cliente.depositar()
    elif des==2:
        cliente.retirar()
    elif des==3:
        cliente.mostrarSaldo()
    