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
        gestion_clientes()
       
login()

def entrada():
    while True:
        boleto_normal=0
        boleto_VIP=0
        print("")
        print("Elija si quiere entrar a un partido o al concierto")
        opcion=("\n1 -concierto \n2 -partido de futbol \n3 salir")
        print(opcion)
        elegir=int(input("Ingrese la opcion: "))
        if elegir==1:
            print("\n1 -boleto normal \n2 boleto VIP")
            boleto=int(input("Ingrese el tipo de boleto: "))
            if boleto==1:
                cantidad=int(input("Ingrese la cantidad de boletos: "))
                murlti=cantidad*15000
                boleto_normal+=cantidad
            elif boleto==2:
                cantidad=int(input("Ingrese la cantidad de boletos: "))
                murlti=cantidad*60000
                boleto_VIP+=cantidad
        elif elegir==2:
            print("partidos \n1 -Cali vs America fecha: 20/04/2023 \n2 Once caldas vs Millonarios fecha:21/04/2023 \n3 Nacional vs Junior fecha: 22/04/2023 \n4 Santa Fe vs Huila fecha: 23/04/2023")
            partido=int("Elija el partido que quiere ver: ")
            print("n1 -boleto normal \n2 boleto VIP")
            boleto=int(input("Ingrese el tipo de boleto: "))
            if boleto==1:
                cantidad=int(input("Ingrese la cantidad de boletos: "))
                murlti=cantidad*10000
                boleto_normal+=cantidad
            elif boleto==2:
                cantidad=int(input("Ingrese la cantidad de boletos: "))
                murlti=cantidad*50000
                boleto_VIP+=cantidad
        elif elegir==3:
            def datos():
                print(f"su nombre es", datos["nombre"], "Tiene", datos["edad"], "identificado ", datos["CC"], "boletos normales ", boleto_normal, "y boletos VIP", boleto_VIP)
            datos()
            break
entrada()   
