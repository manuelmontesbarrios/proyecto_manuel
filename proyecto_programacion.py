print("Bienvenido a la tienda virtual de boleteria")

datos={}
def login():
        usuario=input("Ingrese su usuario: ")
        clave=int(input("Ingrese su calve: "))
        if usuario=='manuel' and clave==12345:
            def gestion_clientes():
                nombre=input("Ingrese su nombre: ")
                edad=int(input("Ingrese su edad: "))
                CC=int(input("Ingrese su numero de identificacion: "))
                fecha_nacimiento=input("Ingrese su fecha de nacimiento: ")
                datos["nombre"]=nombre 
                datos["edad"]=edad 
                datos["CC"]=CC 
                datos["fecha de nacimiento"]=fecha_nacimiento
                print(datos)
            gestion_clientes()
login()
def pago_factura():
    print("\n1 -Targeta de credito \n2 -Efectivo ")
    pago =int(input("Ingrese el tipo de pago: "))
    if pago ==1:
        print("Tipo de targeta de credito \n1 -clásica \n2 -dorada \n3 -platinum \n4 -signature o black")
        credito=int(input("Ingrese el tipo de targeta de credito: "))
        if credito==1:
            num_trageta=int(input("Ingrese el numero de la targeta: "))
            cv=int(input("Ingrese el Cv de la targeta: "))
            fecha=int(input("Ingrese la fecha de vencimiento: "))
        if credito==2:
            num_trageta=int(input("Ingrese el numero de la targeta: "))
            cv=int(input("Ingrese el Cv de la targeta: "))
            fecha=int(input("Ingrese la fecha de vencimiento: "))
        if credito==3:
            num_trageta=int(input("Ingrese el numero de la targeta: "))
            cv=int(input("Ingrese el Cv de la targeta: "))
            fecha=int(input("Ingrese la fecha de vencimiento: "))
        if credito==4:
            num_trageta=int(input("Ingrese el numero de la targeta: "))
            cv=int(input("Ingrese el Cv de la targeta: "))
            fecha=int(input("Ingrese la fecha de vencimiento: "))
        else:
            pass
    elif pago ==3:
        pass
        efectivo=int(input("Ingrese la cantidad a pagar: "))
        pass
    else:
        pass

def entrada():
    boleto_normal=0
    boleto_VIP=0
    suma=0
    while True:
        print("")
        print("Elija al que quiere ingresar")
        opcion=("\n1 -concierto \n2 -partido de futbol \n3 -factura \n4 -salir")
        print(opcion)
        elegir=int(input("Ingrese la opcion: "))
        if elegir==1:
            print("\n1 -boleto normal $10.000 \n2 boleto VIP $50.000")
            boleto=int(input("Ingrese el tipo de boleto: "))
            if boleto==1:
                cantidad=int(input("Ingrese la cantidad de boletos: "))
                boleto_normal=boleto_normal+cantidad
                multi=cantidad*15000
                suma=suma+multi
            elif boleto==2:
                cantidad=int(input("Ingrese la cantidad de boletos: "))
                boleto_VIP=boleto_VIP+cantidad
                multi=cantidad*60000 
                suma=suma+multi
        elif elegir==2:
            print("partidos \n1 -Cali vs America fecha: 20/04/2023 \n2 Once caldas vs Millonarios fecha:21/04/2023 \n3 Nacional vs Junior fecha: 22/04/2023 \n4 Santa Fe vs Huila fecha: 23/04/2023")
            partido=int(input("Elija el partido que quiere ver: "))
            print("\n1 -boleto normal $10.000 \n2 boleto VIP $50.000")
            boleto=int(input("Ingrese el tipo de boleto: "))
            if boleto==1:
                cantidad=int(input("Ingrese la cantidad de boletos: "))
                boleto_normal=boleto_normal+cantidad
                multi=cantidad*10000
                suma=suma+multi
            elif boleto==2:
                cantidad=int(input("Ingrese la cantidad de boletos: "))
                boleto_VIP=boleto_VIP+cantidad
                multi=cantidad*50000
                suma=suma+multi
        elif elegir==3:
            print("su nombre es", datos["nombre"], 
                  "Tiene", datos["edad"], 
                  "identificado ", datos["CC"], 
                  "boletos normales", boleto_normal, 
                  "y boletos VIP", boleto_VIP,
                  "Total a pagar $", suma)
            pago_factura()
entrada()   

    
