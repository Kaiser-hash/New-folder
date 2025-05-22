# Lavado de autos
# Crear un menu para lavar autos
# 1.- Cursar pago del lavado 
# 2.- Ver ventas diarias
# 3.- salir
# El lavado tiene 3 niveles
# 1.- Full $ 15.000, 2- standard 10.000, 3.- Básico $7.000.
# al mostrar las ventas diarias, debe mostar la 
# cantidad de autos que han ingresado y el monto total 
# recaudado. Tambien debe mostrar el monto mas alto pagado  .
    
# def pagolavado():
#     global ventas, autos, full, standard, basico
#     tipodelavado=int(input('''elija su tipo de lavado:
#                            1. FUll $15.000
#                            2. STANDARD $10.000
#                            3. BASICO $7.000
#                            '''))
#     match tipodelavado:
#         case 1:
#             ventas+=15000
#             autos+=1
#             full+=1
#             print("selecciono lavado FULL")
#         case 2:
#             ventas+=10000
#             autos+=1
#             standard+=1
#             print("selecciono lavado STANDARD")
#         case 3:
#             ventas+=7000
#             autos+=1
#             basico+=1
#             print("selecciono lavado BASICO")
#         case _:
#             print("opcion invalida")
# def ventasdia():
#     print(f'''ventas totales ${ventas}
#     Num de autos {autos}''')
#     if full>=1:
#         print("el monto mas alto fue de $15.000")
#     elif standard>=1 and full==0:
#         print("el monto mas alto fue de $10.000")
#     elif basico>=1 and standard==0 and full==0:
#         print("el monto mas alto fue de $7.000")
# ventas=0
# autos=0
# full=0
# standard=0
# basico=0
# while True:
#     op=int(input(''''elija que quiere hacer:
#                 1.pago de lavado
#                 2.ver ventas
#                 3.salir
#                  '''))
#     match op:
#         case 1:
#             pagolavado()
#         case 2:
#             ventasdia()
#             if ventas==0:
#                 print("usted no ha tenido ningun cliente")
        
#         case 3:
#             print("hasta la vista")
#             break
#         case _:
#             print("ingrese una opcion valida")


# ejercicio de crafteo de espada de diamante
# crear espadas de diamante
# para crear una espada de diamante necesitas
# 2 diamantes y 1 palo
# para obtener recursos debes tener
# el sig menu
# 1.-minar, se buscan recursos, la posibilidad de encontrar
# diamante de 1 entre 7 y palo 1 entre 3, y la del carbon 1 entre 3
# minar toma 3 segundos
# 2.- consultar recursos, muestra los recursos acumulados
# 3.- crear espadas, va a crer tantas espadas como pueda
# con los recursos existentes
# 4.- sali, sale


tronco=0
madera=0
palos=0
piedra=0
carbon=0
hierro=0
diamantes=0

import time
# import random
time.sleep(3)

try:
    print("elija una opcion")
    print(''' menu
          1.- minar recursos
          2.- consultar recursos
          3.- crear espadas
          4.- salir ''')
    op=int(input())
    match op:
        case 1:
            print("minar recursos")
        case 2:
            print("consultar recursos")
        case 3:
            print("crar espadas")
        case 4:
            print("saliendo")






            
    if diamantes >=2 and palos>=1:
        print("espada creada")
except Exception:
    print("recursos insuficientes")

# recursos=random.choice("diamante","palo","carbon")

# while True:
#     op=int(input())
#     break
# for i in range():
#     print("jj")





















































































