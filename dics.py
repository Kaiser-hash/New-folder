
# personas={
#     1:{"nombre": " Diego Rivera",
#        "numeros":[7565434,97834231],
#        "estadoCivil": "Casado",
#        "trabajando": True,
#        "edad": 64},
#     2:{"nombre": " Diego Rivera",
#        "numeros":[7565434,97834231],
#        "estadoCivil": "Casado",
#        "trabajando": True,
#        "edad": 64},
#     3:{"nombre": " Diego Rivera",
#        "numeros":[7565434,97834231],
#        "estadoCivil": "Casado",
#        "trabajando": True,
#        "edad": 64}
# }

# list_prod=[]
# while True:
#     try:
       
#         op=int(input('''Seleccione una opcion 
#                     1.- Ingresar persona
#                     2.- Mostrar listado
#                     3.- Actualizar persona
#                     4.- Borrar persona
#                     5.- Salir'''))
#         match op:
#                 case 1:
#                     nom=input("Ingrese el nombre del producto: ")
#                     pre=int(input("Ingrese el precio: "))
#                     list_prod.insert(0,{"nombre":nom, "precio":pre})
#                     nombre=input("Ingrese el nombre: ")
#                     numero=int(input("Ingrese el numero: "))
#                     est=int(input("estado Civil 1.- Casado, 2.- Soltero: "))
#                     if est==1:
#                         estCivil="Casado"
#                     else:
#                         estCivil="Soltero"
#                     edad=int(input("Ingrese la edad: "))
#                     nextkey=len(personas)
#                     personas[nextkey+1]={"nombre": nombre,
#                     "numeros":[numero],
#                     "estadoCivil": estCivil,
#                     "trabajando": True,
#                     "edad": edad}
#                     print("Persona ingresada con exito")
#                 case 2:
#                     for p in list_prod:
#                         print(p)        
#                 case 3:
#                     # for n, p in enumerate(list_prod):
#                     #     print(n+1, ".- ", p)
#                     for i in range(len(list_prod)):
#                         print(i+1, ".-", list_prod[i])
#                     opc=int(input("Seleccione el producto a actualizar"))
#                     print(list_prod[opc-1])
#                     nn=input("Ingrese nuevo Nombre")
#                     np=int(input("Ingrese nuevo Precio"))
#                     list_prod[opc-1]["nombre"]=nn
#                     list_prod[opc-1]["precio"]=np
#                     print("Articulo actualizado!")
#                     for persona, val in personas.items():
#                         print(persona, val)
#                 case 4:
#                     for persona, val in personas.items():
#                         print(persona, val)
#                     dell=int(input("Seleccione cual desea borrar"))
#                     del personas[dell]
#                 case 5:
#                     break
#                 case _:
#                     print("Opcion invalida")
#     except Exception:
#         print("Solo numeros enteros")


personas={
    1:{"nombre": " Michael Kaiser",
       "numeros":[97838841],
       "estadoCivil": "soltero",
       "ciudadano": True,
       "edad": 19},
    2:{"nombre": " Charles",
       "numeros":[97832381],
       "estadoCivil": "soltero",
       "ciudadano": True,
       "edad": 15},
    3:{"nombre": " Don Lorenzo",
       "numeros":[97835778],
       "estadoCivil": "soltero",
       "ciudadano": True,
       "edad": 19}
}
while True:
    try:
        print('''
        1.- ingresar persona
        2.- mostrar listado
        3.- actualizar persona
        4.- borrar persona
        5.- salir
        ''')
        op=int(input("seleccione una opcion: "))
        match op:
            case 1:
                nom=input("ingrese el nombre: ")
                tel=int(input("ingrese numero telefonico: "))
                ed=int(input("inggrese la edad: "))
                est=int(input("estado civil 1.- casado, 2.- soltero: "))
                if est == 1:
                    estCivil = "casado"
                else:
                    estCivil = "soltero"
                ciu=int(input("es ciudadano 1.- si, 2.- no: "))
                if ciu == 1:
                    ciudadano = True
                else:
                    ciudadano = False
                ld=len(personas)+1
                personas[ld]={"nombre": nom,
                             "numeros": tel,
                             "estadoCivil": est,
                             "ciudadano": ciu,
                             "edad": ed}
            case 2:
                for n, persona in personas.items():
                    print(n, persona)
            
            case 5:
                break
            case _:
                print("opcion invalida")
    except Exception as e:
        print("el error es: ", e)
        













