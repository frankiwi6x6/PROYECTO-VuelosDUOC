#Franco Reyes
import ast
from re import X
import numpy as np
#
cAst=55                                                                     #CAMBIAR ESTO PARA LA CANTIDAD DE ASTERISKOS QUE HAYA EN EL MENU DE ASIENTOS
def asteriskos():                   #FUNCION PARA CREAR UNA LINEA DE ASTERISKOS.
    print ("*"*cAst)
cG=55                               #CANTIDAD DE GUIONES
def guiones():
    print("-"*cG)
#Registro de usuarios
rUser=[ [None,None,None,None,None,None],
        [None,None,None,None,None,None],
        [None,None,None,None,None,None],
        [None,None,None,None,None,None]]
#ASIENTOS
asientos=[[ 1,  2,  3,  4,  5,  6], #LISTA DE ASIENTOS, BIDIMENSIONAL DE MEDIDA 6x7
          [ 7,  8,  9, 10, 11, 12],
          [13, 14, 15, 16, 17, 18],
          [19, 20, 21, 22, 23, 24],
          [25, 26, 27, 28, 29, 30],
          [31, 32, 33, 34, 35, 36],
          [37, 38, 39, 40, 41, 42]]
#LISTA USUARIOS.
user1=[]
user2=[]
user3=[]
user4=[]
#CONTADOR
cDatos=0                            #CONTADOR PARA LA OPERACION 'COMPRAR ASIENTOS'
cDV=0                               #CONTADOR PARA LA VERIFICACION DE DIGITO VERIFICADOR
#INICIALIZAR
aNormal=78900                       #VALOR PRECIO ASIENTO NORMAL
aVIP=240000                         #VALOR PRECIO ASIENTO VIP (31-42)
exe=1                               #VARIABLE EJECUTADORA.
print ("***Bienvenido a Vuelos-Duoc.***")
while exe==1:
    op=int(input(f"\t\tMENU\n1. Ver asientos disponibles\n2. Comprar asiento\n3. Anular vuelo\n4. Modificar datos de pasajero\n5. Salir\nIngrese su respuesta: "))
    cDatos=0
    cDV=0
    while op!=6:
    
        if op==1:
            print("\t\tAsientos disponibles.")
            asteriskos()
            
            print("\t\t[ASIENTOS NORMALES]")
            guiones()
            for x in range(7):
                for y in range(6):
                    print (asientos[x][y],"\t",end="")
                    if asientos[x][y]==asientos[x][2]:
                        print("", end="\t")
                    if asientos[x][y]==asientos[4][5]:
                        print("")
                        guiones()
                        print ("\t\t[ASIENTOS VIP]")
                        guiones()
                print(" ")
            break
        elif op==2:
            if cDatos==0:  
                rutPasajero=int(input("Ingrese su rut sin digito verificador: "))
                if rutPasajero>99999999:
                    print("RUT no valido, intentelo nuevamente.")
                else:                    
                    dvPasajero=str(input("Ingrese su DV: "))
                    cDV=0
                    for i in dvPasajero:
                        cDV+=1
                    if cDV!=1:
                        print("DV incorrecto.")
                    else:
                        cDatos+=1
            elif cDatos==1:
                nombrePasajero=str(input("Ingrese su nombre completo: "))
                cNombre=0
                for i in nombrePasajero:
                    cNombre+=1
                if cNombre>0:
                    cDatos+=1
                else:
                    print("Campo vacio, ingrese nuevamente su nombre.")
            elif cDatos==2:
                fonoPasajero=str(input("Ingrese su numero telefónico: "))
                cFono=0
                for i in fonoPasajero:
                    cFono+=1
                if cFono>0:
                    cDatos+=1
                else:
                    print("Campo vacio, ingrese nuevamente su telefono.")
            elif cDatos==3:
                bancoPasajero=str(input("Ingrese su banco: "))
                cDatos+=1
            elif cDatos==4:
                print("\t\tAsientos disponibles.")
                asteriskos()
                print("\t\t[ASIENTOS NORMALES]")
                guiones()
                for x in range(7):
                    for y in range(6):
                        print (asientos[x][y],"\t",end="")
                        if asientos[x][y]==asientos[x][2]:
                            print("", end="\t")
                        if asientos[x][y]==asientos[4][5]:
                            print("")
                            guiones()
                            print ("\t\t[ASIENTOS VIP]")
                            guiones()
                    print(" ")
                cDatos+=1
            elif cDatos==5:
                asientoPasajero=int(input("Ingrese el asiento que desea ocupar: "))
                if asientoPasajero<=42 and asientoPasajero>0:
                    cDatos+=1
                else:
                    print("Usted indico un numero de asiento incorrecto.")
            elif cDatos==6:
                for x in range(7):
                    for y in range(6):
                        if asientoPasajero==asientos[x][y]:
                            asientos[x][y]="X"
                cDatos+=1
                        
            elif cDatos==7:
                if asientoPasajero<=30:
                    pAsiento=aNormal
                    print(f"El precio de este asiento es: ${pAsiento}.")
                elif asientoPasajero>30:
                    pAsiento=aVIP
                    print(f"El precio de este asiento es: ${pAsiento}.")
                cDatos+=1
                
            elif cDatos==8:
                if bancoPasajero=="bancoDuoc":
                    dcto=pAsiento*0.15
                    pFinal=pAsiento-dcto 
                    print (f"Por ser usuario del bancoDuoc, se le hizo un descuento de: ${dcto}")
                else:
                    dcto=0
                    pFinal=pAsiento-dcto 
                print (f"El precio final es: ${pFinal}.")
                if rUser[0][0]==None:
                    rUser[0][0]=(rutPasajero)
                    rUser[0][1]=(dvPasajero)
                    rUser[0][2]=(nombrePasajero)
                    rUser[0][3]=(fonoPasajero)
                    rUser[0][4]=(bancoPasajero)
                    rUser[0][5]=(asientoPasajero)
                    print ("Se han agregado los datos a la casilla de USUARIO [1].")
                elif rUser[0][0]!=None and rUser[1][0]==None:
                    rUser[1][0]=(rutPasajero)
                    rUser[1][1]=(dvPasajero)
                    rUser[1][2]=(nombrePasajero)
                    rUser[1][3]=(fonoPasajero)
                    rUser[1][4]=(bancoPasajero)
                    rUser[1][5]=(asientoPasajero)
                    print ("Se han agregado los datos a la casilla de USUARIO [2].")
                elif rUser[1][0]!=None and rUser[2][0]==None:
                    rUser[2][0]=(rutPasajero)
                    rUser[2][1]=(dvPasajero)
                    rUser[2][2]=(nombrePasajero)
                    rUser[2][3]=(fonoPasajero)
                    rUser[2][4]=(bancoPasajero)
                    rUser[2][5]=(asientoPasajero)
                    print ("Se han agregado los datos a la casilla de USUARIO [3].")
                elif rUser[2][0]!=None and rUser[3][0]==None:
                    rUser[3][0]=(rutPasajero)
                    rUser[3][1]=(dvPasajero)
                    rUser[3][2]=(nombrePasajero)
                    rUser[3][3]=(fonoPasajero)
                    rUser[3][4]=(bancoPasajero)
                    rUser[3][5]=(asientoPasajero)
                    print ("Se han agregado los datos a la casilla de USUARIO [4].")
                break
        elif op==3:
            print("Usted decidio anular el vuelo.")
            RUTanularAsiento=int(input("Ingrese su RUT sin digito verificador: "))
            #print(user)
            for x in range(2):
                for y in range(6):
                    if RUTanularAsiento==rUser[x][y]:
                        for i in range(6):
                            rUser[x][i]=None
                        guiones()
                        print(f"Se han eliminado los datos del usuario [{x+1}] correctamente, el asiento quedara libre.")
                        guiones()
            break
                    
        elif op==5:
            print("Cerrando...")
            exe=0
            break

            
          