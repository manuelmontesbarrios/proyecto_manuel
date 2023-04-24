from os import system
system("cls")
import time

datos={}
def entrada():
    boleto_normal=0
    boleto_VIP=0
    suma=0
    while True:
        try:
            print("")
            print("Elija una opcion\n\t 1 -concierto \n\t 2 -partido de futbol \n\t 3 -factura ")
            elegir=int(input("Ingrese la opcion: "))
            if elegir==1:
                while True:
                    print("\n\t 1 -boleto normal $10.000 \n\t 2 -boleto VIP $50.000")
                    boleto=int(input("Ingrese el tipo de boleto: "))
                    if boleto==1:
                        cantidad=int(input("Ingrese la cantidad de boletos: "))
                        boleto_normal=boleto_normal+cantidad
                        multi=cantidad*15000
                        suma=suma+multi
                        break
                    elif boleto==2:
                        cantidad=int(input("Ingrese la cantidad de boletos: "))
                        boleto_VIP=boleto_VIP+cantidad
                        multi=cantidad*60000 
                        suma=suma+multi
                        break
                    else:
                        print("ERROR, la opcion no existe")
                        print("")
            elif elegir==2:
                while True:
                    print("partidos\n\t 1 -Cali vs America fecha: 20/04/2023 \n\t 2 Once caldas vs Millonarios fecha:21/04/2023 \n\t 3 Nacional vs Junior fecha: 22/04/2023 \n\t 4 Santa Fe vs Huila fecha: 23/04/2023")
                    partido=int(input("Elija el partido que quiere ver: "))
                    if partido <=4:
                        print("Tipo de boleto \n\t 1  -boleto normal $10.000 \n\t 2 -boleto VIP $50.000")
                        boleto=int(input("Ingrese el tipo de boleto: "))
                        if boleto==1:
                            cantidad=int(input("Ingrese la cantidad de boletos: "))
                            boleto_normal=boleto_normal+cantidad
                            multi=cantidad*10000
                            suma=suma+multi
                            break
                        elif boleto==2:
                            cantidad=int(input("Ingrese la cantidad de boletos: "))
                            boleto_VIP=boleto_VIP+cantidad
                            multi=cantidad*50000
                            suma=suma+multi
                            break
                        else:
                            print("ERROR, la opcion no existe")
                    else: 
                        print("ERROR, la opcion no existe")
                        print("")
            elif elegir==3:
                if suma >=1:
                    print("Su nombre es", datos["nombre"], 
                        "Tiene", datos["edad"], 
                        "identificado", datos["CC"], 
                        "boletos normales", boleto_normal, 
                        "y boletos VIP", boleto_VIP,
                        "Total a pagar $", suma)
                    print("")
                    while True:
                        print("--------------------------------------------------------------------------------------------------------------------------")
                        print("Tipo de pago\n\t 1 -Targeta de credito \n\t 2 -Efectivo ")
                        pago =int(input("Ingrese el tipo de pago: "))
                        if pago ==1:
                            print("")
                            while True:
                                print("Tipo de targeta de credito \n\t 1  -clásica \n\t 2 -dorada \n\t 3 -platinum \n\t 4 -signature o black")
                                credito=int(input("Ingrese el tipo de targeta de credito: "))
                                if credito<=4:
                                    num_trageta=int(input("Ingrese el numero de la targeta: "))
                                    cv=int(input("Ingrese el Cv de la targeta: "))
                                    fecha=int(input("Ingrese la fecha de vencimiento: "))
                                    print("PAGO EXITOSO!")
                                    exit()
                                else:
                                    print("ERROR, la opcion no existe")
                        elif pago ==2:
                            while True:
                                efectivo=int(input("Ingrese la cantidad a pagar: "))
                                if efectivo >= suma:
                                    print("este es su cambio", efectivo-suma)
                                    print("Gracias por la compra, que tenga un buen dia")
                                    exit()
                                else:
                                    print("No tiene dinero suficiente")
                        else:
                            print("ERROR")
                else:
                    print("ERROR, debe hacer un compra y para el total sea mayor a $0")
            else:
                print("ERROR, la opcion no existe")
        except ValueError:
            print("ERROR, no son datos numericos")
def login():
    while True:
        try:
            print("BIENVENIDO A LA TIENDA VIRTUAL DE BOLETERIA ^^LA ATAJADA & ROCK^^")
            usuario=input("Ingrese su usuario: ")
            usu=usuario.upper()
            if usu.isalpha()== True:
                if usu=="MANUEL":
                    clave=int(input("Ingrese su calve: "))
                    if usu=='MANUEL' and clave==12345:
                        time.sleep(1)
                        system("cls")
                        while True:
                            nombre=input("Ingrese su nombre: ")
                            if nombre.isalpha()==True:
                                edad=int(input("Ingrese su edad: "))
                                if edad>=18:
                                    CC=int(input("Ingrese su numero de identificacion: "))
                                    fecha_nacimiento=input("Ingrese su fecha de nacimiento separadas DD/MM/AA: ")
                                    datos["nombre"]=nombre 
                                    datos["edad"]=edad 
                                    datos["CC"]=CC 
                                    datos["fecha de nacimiento"]=fecha_nacimiento
                                    entrada()
                                else:
                                    print("Lo sentimos usted es menor de edad, por lo tanto no podra comprar boletos ")
                                    time.sleep(1)
                                    system("cls")
                                    break
                            else:
                                print("ERROR, no es un nombre")
                                time.sleep(1)
                                system("cls")
                    else:
                        print("ERROR de clave")
                        time.sleep(1)
                        system("cls")
                else:
                    print("ERROR los datos no son letras")
                    time.sleep(1)
                    system("cls")
            else:
                print("ERROR de usuario")
                time.sleep(1)
                system("cls")
        except ValueError:
            print("ERROR, los datos ingresados no son numeros")
            time.sleep(1)
            system("cls")
login()