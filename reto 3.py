from os import system
system("cls")

contra={}
def wifi():
    while True:
        print("Bienvenido al sistema de ubicación para zonas públicas WIFI")
        usuario=int(input("Ingrese el usuario: "))
        if usuario == 74568:
            usu=usuario
        else:
            print("ERROR")
            exit()
        contraseña=int(input("Ingresa la contraseña: "))
        if contraseña == 86547:
            contra["contraseña"]=contraseña
        else:
            print("ERROR")
            exit()
        valor_capcha1=(7+5)/(8/4)
        valor_capcha2=(8-5)+(7-4)
        valor_capcha3=8-5+7-4
        if valor_capcha1 and valor_capcha2 and valor_capcha3 ==6:
            capcha=int(input("Ingrese la suma de este capcha 568 + 6 es :"))
            if capcha == 574:
                print("SESION INICIADA")
            else:
                print("ERROR")
                exit()
            return contra
        break  
wifi()

def opciones():
    while True:
        contar_menu=0
        contar_elegir=0 
        print("")
        print("Elija una opcion")
        opciones=("\n1 -cambiar contraseña \n2 -ingresar coordenadas actuales \n3 -Ubicar zona Wifi mas cercana \n4 -Guardar archivo con ubicación cercana \n5 -Actualizar registros de zonas wifi desde archivo \n6 -Elegir opción de menú favorita \n7 -cerrar sesion ")
        print(opciones)
        print("---------------------------------------------------------------------------------------------------------------------------------------")
        opcion=int(input("Ingrese la opcion: "))
        if opcion == 1:
                cambiar=int(input("ingrese la contraseña actual: "))
                if cambiar != contra["contraseña"]:
                        print("ERROR")
                        print(contra)
                        exit()
                elif cambiar==contra["contraseña"]:
                        con=input("Ingrese la nueva contraseña: ")
                    
                        contra["contraseña"]=con
                        print(contra)
        elif opcion == 2:
                opcion2()
        elif opcion == 3:
                    print("Ubique la zona wifi mas cercana ")
        elif opcion == 4:
                    print("Guardar archivo con ubicacion cercana")
        elif opcion == 5:
                    print("Actualizar registros de zona wifi desde archivo")
        elif opcion==6:
            opcion6()
        elif opcion==7:
                        print("Hasta pronto")
                        exit()
        else:
                    print("ERROR")
                    contar_menu+=1
                    if contar_menu==3:
                        exit()
                    else:
                        print("")            
        
opciones()       
  
def main():
    print("")
    print(opciones)
main()  

def opcion2():
      pass

def opcion6():
                favorita=int(input("Seleccione opcion favorita del 1 al 5: "))
                if favorita==1:
                        def elegir1():
                            elegir1=0
                            print("Usted ha elegido la opcion ",favorita )
                            adivinanza1=int(input("Si le sumas su hermano gemelo al tres, ya sabes cuál es: "))
                            adivinanza2=int(input("¿Qué número se convierte en cero si le quitas la mitad?: "))
                            if adivinanza1==6 and adivinanza2==8:
                                from os import system
                                system ("cls")
                                print("\n1 -cambiar contraseña* \n2 -ingresar coordenadas actuales \n3 -Ubicar zona Wifi mas cercana \n4 -Guardar archivo con ubicación cercana \n5 -Actualizar registros de zonas wifi desde archivo ")                                             
                                print("-----------------------------------------------------------------------------------------------------------------------")
                                opcion=int(input("Ingrese la opcion: "))
                                if opcion == 1:
                                    del usu
                                    contra=int(input("Ingrese su nueva contraseña: "))
                                    contraseña=contra
                                elif opcion == 2:
                                        print("Ingrese las coordenadas actuales ")
                                elif opcion == 3:
                                        print("Ubique la zona wifi mas cercana ")
                                elif opcion == 4:
                                        print("Guardar archivo con ubicacion cercana")
                                elif opcion == 5:
                                        print("Actualizar registros de zona wifi desde archivo")
                            else:
                                print("ERROR")
                                elegir1=+1
                                if elegir1==3:
                                    exit()
                                else:
                                    print("")
                        elegir1()
                elif favorita==2:
                        def elegir2():
                            elegir2=0
                            print("Usted ha elegido la opcion " ,favorita )
                            adivinanza1=int(input("Si le sumas su hermano gemelo al tres, ya sabes cuál es: "))
                            adivinanza2=int(input("¿Qué número se convierte en cero si le quitas la mitad?: "))
                            if adivinanza1==6 and adivinanza2==8:
                                            from os import system
                                            system ("cls")
                                            print("\n1 -ingresar coordenadas actuales* \n2 -cambiar contraseña \n3 -Ubicar zona Wifi mas cercana \n4 -Guardar archivo con ubicación cercana \n5 -Actualizar registros de zonas wifi desde archivo ")
                                            print("---------------------------------------------------------------------------------------------------------------")
                                            opcion=int(input("Ingrese la opcion: "))
                                            if opcion == 2:
                                                del contra
                                                contra=int(input("Ingrese su nueva contraseña: "))
                                                contraseña=contra
                                            elif opcion == 1:
                                                    print("Ingrese las coordenadas actuales ")
                                            elif opcion == 3:
                                                    print("Ubique la zona wifi mas cercana ")
                                            elif opcion == 4:
                                                    print("Guardar archivo con ubicacion cercana")
                                            elif opcion == 5:
                                                    print("Actualizar registros de zona wifi desde archivo")
                            else:
                                print("ERROR") 
                                elegir2+=1
                                if elegir2==3:
                                    exit()
                                else:
                                    print("")
                        elegir2()
                elif favorita==3:
                        def elegir3():
                            elegir3=0
                            print("Usted ha elegido la opcion " ,favorita )
                            adivinanza1=int(input("Si le sumas su hermano gemelo al tres, ya sabes cuál es: "))
                            adivinanza2=int(input("¿Qué número se convierte en cero si le quitas la mitad?: "))
                            if adivinanza1==6 and adivinanza2==8:
                                from os import system
                                system ("cls")
                                print("\n1 -Ubicar zona Wifi mas cercana* \n2 -cambiar contraseña \n3 -ingresar coordenadas actuales \n4 -Guardar archivo con ubicación cercana \n5 -Actualizar registros de zonas wifi desde archivo ")       
                                print("-----------------------------------------------------------------------------------------------------------------------")
                                opcion=int(input("Ingrese la opcion: "))
                                if opcion == 2:
                                    del usu
                                    contra=int(input("Ingrese su nueva contraseña: "))
                                    contraseña=contra
                                elif opcion == 2:
                                        print("Ingrese las coordenadas actuales ")
                                elif opcion == 3:
                                        print("Ubique la zona wifi mas cercana ")
                                elif opcion == 4:
                                        print("Guardar archivo con ubicacion cercana")
                                elif opcion == 5:
                                        print("Actualizar registros de zona wifi desde archivo")
                            else:
                                print("ERROR")
                                elegir3+=1
                                if elegir3==3:
                                    exit()
                                else:
                                    print("")
                        elegir3()
                elif favorita==4:
                        def elegir4():
                            elegir4=0
                            print("Usted ha elegido la opcion ",favorita )
                            adivinanza1=int(input("Si le sumas su hermano gemelo al tres, ya sabes cuál es: "))
                            adivinanza2=int(input("¿Qué número se convierte en cero si le quitas la mitad?: "))
                            if adivinanza1==6 and adivinanza2==8:
                                from os import system
                                system ("cls")
                                print("\n1 -Guardar archivo con ubicación cercana* \n2 -cambiar contraseña \n3 -ingresar coordenadas actuales \n4 -Ubicar zona Wifi mas cercana \n5 -Actualizar registros de zonas wifi desde archivo ")       
                                print("-----------------------------------------------------------------------------------------------------------------------")
                                opcion=int(input("Ingrese la opcion: "))
                                if opcion == 4:
                                    del usu
                                    contra=int(input("Ingrese su nueva contraseña: "))
                                    contraseña=contra
                                elif opcion == 2:
                                        print("Ingrese las coordenadas actuales ")
                                elif opcion == 3:
                                        print("Ubique la zona wifi mas cercana ")
                                elif opcion == 1:
                                        print("Guardar archivo con ubicacion cercana")
                                elif opcion == 5:
                                        print("Actualizar registros de zona wifi desde archivo")
                            else:
                                print("ERROR")
                                elegir4+=1
                                if elegir4==3:
                                    exit()
                                else:
                                    print("")
                        elegir4()
                elif favorita==5:
                        def elegir5():
                            elegir5=0
                            print("Usted ha elegido la opcion ",favorita )
                            adivinanza1=int(input("Si le sumas su hermano gemelo al tres, ya sabes cuál es: "))
                            adivinanza2=int(input("¿Qué número se convierte en cero si le quitas la mitad?: "))
                            if adivinanza1==6 and adivinanza2==8:
                                from os import system
                                system ("cls")
                                print("\n1 -Actualizar registros de zonas wifi desde archivo* \n2 -cambiar contraseña \n3 -ingresar coordenadas actuales \n4 -Guardar archivo con ubicación cercana \n5 -Ubicar zona Wifi mas cercana ")       
                                print("-----------------------------------------------------------------------------------------------------------------------")
                                opcion=int(input("Ingrese la opcion: "))
                                if opcion == 5:
                                    del usu
                                    contra=int(input("Ingrese su nueva contraseña: "))
                                    contraseña=contra
                                elif opcion == 2:
                                        print("Ingrese las coordenadas actuales ")
                                elif opcion == 3:
                                        print("Ubique la zona wifi mas cercana ")
                                elif opcion == 4:
                                        print("Guardar archivo con ubicacion cercana")
                                elif opcion == 1:
                                        print("Actualizar registros de zona wifi desde archivo")
                            else:
                                print("ERROR")
                                elegir5+=1
                                if elegir5==3:
                                    exit()
                                else:
                                    print("")
                        elegir5()