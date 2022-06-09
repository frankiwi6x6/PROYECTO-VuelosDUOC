#IMPORTANTE, AL MOMENTO DE INGRESAR UN DATO Y RETORNE 'VALUEERROR', SE ENVIA AL MENU PRINCIPAL, SIN AGREGAR LOS DATOS A LA LISTA.
#SI ESCRIBE 6 EN EL MENU PRINCIPAL, LE MUESTRA LA LISTA DE LOS USUARIOS, PARA VERIFICAR QUE ESTÉN AGREGANDOSE CORRECTAMENTE.

cAst=50                                             #CAMBIAR ESTO PARA LA CANTIDAD DE ASTERISKOS QUE HAYA EN EL MENU DE ASIENTOS
def asteriskos():                                   #FUNCION PARA CREAR UNA LINEA DE ASTERISKOS.
    print ("*"*cAst)
cG=50                                               #CANTIDAD DE GUIONES
def guiones():
    print("-"*cG)

#BANCOS
bancos=["bancoDUOC","Banco Credito e Inversiones (BCI)","Banco de Chile", "Banco Estado", "Banco Edwards", "Otro"]

#Registro de usuarios
rUser=[[None, None, None, None, None, None],        #DEBE SER UNA LISTA DE 6x42, SI ES UN
       [None, None, None, None, None, None],        #ARREGLO NO SE PUEDEN COLOCAR VARIABLES TIPO STRING
       [None, None, None, None, None, None],        #AL ALMACENAR DATOS, SE ORDENAN POR, (RUT, DV, NOMBRE, NUMERO TELEFONICO, NUMERO DE BANCO Y ASIENTO)
       [None, None, None, None, None, None],
       [None, None, None, None, None, None],
       [None, None, None, None, None, None],
       [None, None, None, None, None, None],
       [None, None, None, None, None, None],
       [None, None, None, None, None, None],
       [None, None, None, None, None, None],
       [None, None, None, None, None, None],
       [None, None, None, None, None, None],
       [None, None, None, None, None, None],
       [None, None, None, None, None, None],
       [None, None, None, None, None, None],       
       [None, None, None, None, None, None],
       [None, None, None, None, None, None],       
       [None, None, None, None, None, None],
       [None, None, None, None, None, None],
       [None, None, None, None, None, None],
       [None, None, None, None, None, None],
       [None, None, None, None, None, None],
       [None, None, None, None, None, None],
       [None, None, None, None, None, None],
       [None, None, None, None, None, None],
       [None, None, None, None, None, None],
       [None, None, None, None, None, None],
       [None, None, None, None, None, None],
       [None, None, None, None, None, None],
       [None, None, None, None, None, None],
       [None, None, None, None, None, None],
       [None, None, None, None, None, None],
       [None, None, None, None, None, None],
       [None, None, None, None, None, None],
       [None, None, None, None, None, None],
       [None, None, None, None, None, None],
       [None, None, None, None, None, None],
       [None, None, None, None, None, None],
       [None, None, None, None, None, None],
       [None, None, None, None, None, None],
       [None, None, None, None, None, None],
       [None, None, None, None, None, None],
]
#ASIENTOS
asientos=[[ 1,  2,  3,  4,  5,  6], #LISTA DE ASIENTOS, BIDIMENSIONAL DE MEDIDA 6x7
          [ 7,  8,  9, 10, 11, 12],
          [13, 14, 15, 16, 17, 18],
          [19, 20, 21, 22, 23, 24],
          [25, 26, 27, 28, 29, 30],
          [31, 32, 33, 34, 35, 36],
          [37, 38, 39, 40, 41, 42]]

#CONTADOR
cDatos=0                            #CONTADOR PARA LA OPERACION 'COMPRAR ASIENTOS'
cDV=0                               #CONTADOR PARA LA VERIFICACION DE DIGITO VERIFICADOR
cPasaj=0
#INICIALIZAR
aNormal=78900                       #VALOR PRECIO ASIENTO NORMAL
aVIP=240000                         #VALOR PRECIO ASIENTO VIP (31-42)
exe=1                               #VARIABLE EJECUTADORA.
print ("***Bienvenido a Vuelos-Duoc.***")
try:
    while exe==1:
        try: 
            op=int(input(f"\t\tMENU\n1. Ver asientos disponibles\n2. Comprar asiento\n3. Anular vuelo\n4. Modificar datos de pasajero\n5. Mostrar a los usuarios registrados.\n6. Salir\nIngrese su respuesta: "))
            cDatos=0
            cDV=0
        
            if op>=1 and op<=6:
                while op!=7:
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
                        print(" ")
                        print(" ")
                        break
                    elif op==2:
                        if cDatos==0:  
                            try:
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
                            except ValueError:
                                print("Ingrese un valor numerico cuando se le pida.")
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
                            fonoPasajero=str(input("Ingrese su numero telefónico (8 digitos): +56 9"))
                            cFono=0
                            for i in fonoPasajero:
                                cFono+=1
                            if cFono==8:
                                cDatos+=1
                            elif cFono!=8 and cFono!=0:
                                print("Error, número fuera de rango.\nInténtelo nuevamente.\n")
                            else:
                                print("Campo vacio, ingrese nuevamente su telefono.")
                        elif cDatos==3:
                                        #menu bancos
                            print("\t\tMENU BANCOS")
                            c=1
                            for e in bancos:
                                print(f"{c}. {e}.")
                                c+=1
                            bancoPasajero=int(input("Ingrese su respuesta: "))
                            if bancoPasajero==6:
                                otroBanco=str(input("Ingrese el nombre del banco: "))
                                bancos.append(otroBanco)
                            if bancoPasajero>=1 and bancoPasajero<c:
                                cDatos+=1
                            else:
                                print("Numero fuera de rango, intentelo nuevamente.")
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
                            print(" ")
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
                            if bancoPasajero==1:
                                dcto=pAsiento*0.15
                                pFinal=pAsiento-dcto 
                                print (f"Por ser usuario del bancoDuoc, se le hizo un descuento de: ${dcto}")
                                
                            else:
                                dcto=0
                                pFinal=pAsiento-dcto 
                            print (f"El precio final es: ${pFinal}.")
                            cDatos+=1

                        elif cDatos==9:
                            while cPasaj<42:
                                if rUser[cPasaj][0]!=rutPasajero:
                                    for i in range(6):
                                        if i==0:
                                            rUser[cPasaj][i]=(rutPasajero)
                                        elif i==1:
                                            rUser[cPasaj][i]=(dvPasajero)
                                        elif i==2:
                                            rUser[cPasaj][i]=(nombrePasajero)
                                        elif i==3:
                                            rUser[cPasaj][i]=(fonoPasajero)
                                        elif i==4:
                                            rUser[cPasaj][i]=(bancoPasajero)
                                        elif i==5:
                                            rUser[cPasaj][i]=(asientoPasajero)
                                break
                            print(f"La informacion se ha añadido correctamente a la casilla [{cPasaj+1}]")
                            cPasaj+=1
                            break
                            
                        
                        
                        
                    if op==3:
                        print("***Usted decidio anular el vuelo.***")
                        try:
                            RUTanularAsiento=int(input("Ingrese su RUT sin digito verificador: "))
                            #print(user)
                            solved=0
                        except ValueError:
                            print("Ingrese el RUT (Valor Entero)")
                        
                        try:
                            for x in range(42):
                                for y in range(6):
                                    if RUTanularAsiento==rUser[x][y]:
                                        eAsiento=rUser[x][-1]
                                        print(f"Asiento a eliminar {eAsiento}")
                                        for j in range(7):
                                            for l in range(6):
                                                if asientos[j][l]=="X" and (asientos[j][l-1]==eAsiento-1 or asientos[j-1][-1]==eAsiento-1 or asientos[j][l+1]==eAsiento+1):
                                                    asientos[j][l]=eAsiento
                                        for i in range(6):
                                            rUser[x][i]=None
                                        guiones()
                                        print(f"Se han eliminado los datos del usuario [{x+1}] correctamente, el asiento quedará libre.")
                                        guiones()
                                        solved=1
                            if solved==0:
                                print(" ")
                                asteriskos()
                                print("No se ha encontrado ningún asiento asociado a ese RUT.\n")
                                asteriskos()
                            
                                        
                            break
                        
                        
                        except NameError:
                            print("No existe información asociada a ese RUT.")

                    if op==4:       #OPCION MODIFICAR DATOS.
                        try:
                            modSolved=0
                            print("Usted seleccionó la opcion MODIFICAR\n*Escriba \"(-13)\", sin los paréntesis para volver al menu principal*")
                            guiones()
                            mRUT=int(input("Ingrese su RUT: "))
                            if mRUT!=-13:
                                mASIENTO=int(input("Ingrese su ASIENTO: "))
                                for x in range(42):
                                    cMOD=0
                                    if mRUT==rUser[x][0] and mASIENTO==rUser[x][-1]:
                                        print("\t\tSUBMENÚ MODIFICACIONES.\n1. NOMBRE.\n2. NÚMERO TELEFÓNICO.\n3. VOLVER AL MENU PRINCIPAL.")
                                        modif=int(input("Ingrese su respuesta: "))
                                        cMOD+=1
                                        while cMOD==1:
                                            if modif>=1 and modif<=3:
                                                if modif==1:
                                                    print(f"El nombre registrado anteriormente era: {(rUser[x][2])}.")
                                                    mNombre=str(input("Ingrese su nuevo nombre: "))
                                                    cMNOMBRE=0
                                                    for letras in mNombre:
                                                        cMNOMBRE+=1
                                                    if cMNOMBRE>=1:
                                                        cMOD+=1
                                                        rUser[x][2]=mNombre
                                                        modSolved=1
                                                        break
                                                    else:
                                                        print("Campo vacío intente nuevamente.")
                                                elif modif==2:
                                                    print(f"El número telefónico registrado anteriormente era: {(rUser[x][3])}.")
                                                    mFono=str(input("Ingrese su nuevo número telefónico: "))
                                                    cMFONO=0
                                                    for letras in mFono:
                                                        cMFONO+=1
                                                    if cMFONO>=1:
                                                        cMOD+=1
                                                        rUser[x][3]=mFono
                                                        modSolved=1
                                                        break
                                            else:
                                                print("VALOR SELECCIONADO FUERA DE RANGO OFRECIDO, INTÉNTELO NUEVAMENTE")
                                        break    
                                if modSolved==0:
                                    asteriskos()
                                    print ("No se han encontrado informacion asociada a ese RUT y/o ASIENTO")
                                    asteriskos()
                                    
                            else:
                                print(" ")
                                
                            break
                        except ValueError:
                            print("Error de valor, intentelo de nuevo.")
                    if op==5:
                        uMostrados=0
                        print("\tUSUARIOS REGISTRADOS")
                        guiones()
                        for x in range(42):
                            for y in range(6):
                                if rUser[x][y]!=None:
                                    print (f"{rUser[x][y]}, ",end="")
                                    print("",end="")
                                    
                                    uMostrados+=1
                        
                        if uMostrados==0:
                            print("No hay usuarios para mostrar")
                        print("")
                        guiones()    
                        print(" ")
                        print(" ")
                        break
                    if op==6:
                        exe=0
                        break
            else:
                print("[Opción fuera de rango.]\nIntente nuevamente.")
        except ValueError:
            guiones()
            print("***ERROR***\nCampo vacío, o Error de Valor.")
            guiones()
finally:
    print("Cerrando Sesión...")
    