

#  declararcion de variables
# nombre=input()
# # ejemplo de contatenacion
# edad=input()
# print("hola", nombre, "y tu edad es", edad)

# print("ingrese 2 numeros")

# n1=int(input("ingrese un numero"))
# n2=int(input("ingrese un numero"))
# print("el resultado de la suma es", n1+n2)

# promedip

# print("ingrese 3 numeros para sacar su promedio")
# n1=int(input("ingrese un numero"))
# n2=int(input("ingrese un numero"))
# n3=int(input("ingrese un numero"))
# prom=(n1+n2+n3)/3
# print("el promedio es", prom)

# if prom>=40:
#     print("el alumno aprobo")
# else:
#     print("el alumno reprobo")


# verificacion de mayoria de edad

# edad=int(input("ingrese su edad"))

# if edad>=18:
#     print("usted es mayor de edad")
# else:
#     print("usted es menor de edad")

# niño menor de 12
# adolecente entre 12 y 17
# mayor de edad mas o igual a 18

# edad = int(input("ingrese su edad: "))

# if edad < 12:
#     print("tiene", edad, "es un niño")
# elif edad >= 12 and edad <= 17:
#     print("tiene", edad, "es adolecente")
# else:
#     print("tiene", edad, "es mayor de edad")




# n1=int(input("ingrese un numero"))
# n2=int(input("ingrese otro numero"))
# n3=int(input("ingrese otro numero"))

# if n1>n2 and n1<n3:
#     print("el numero", n1, "es el mayor")
# elif n2>n3:
#         print("el numero", n2, "es el mayor")
# else:
#     print("el numero", n3, "es el mayor")



c1="Kaiser"
c2="Billy"

cantvotos1=0
cantvotos2=0

cantV=int(input("ingrese la cantidad de votantes :"))

for i in range(cantV):
    print("por quien votara?: 1.-", c1, " , 2.-" ,c2 )
    voto=input()

if voto=="1":
    print(f"usted voto por {c1}")
    cantvotos1+=1
else:
    print(f"usted voto por {c2}")
    cantvotos2+=1

print(f"la cantidad de votos de {c1} es {cantvotos1}")
print(f"la cantidad de votos de {c2} es {cantvotos2}")

if cantvotos1>cantvotos2:
    print(f"gano {c1}")
elif cantvotos1<cantvotos2:
    print(f"gano {c2}")
else:
    print("votacion empatada")



# print("ingrese la cant de notas")
# suma=0
# notas_azules=0
# cantN=int(input())
# for i in range(cantN):
#     print("ingrese la nota ",i +1 )

#     nota=float(input())
#     if nota>=4:
#         # notas_azules=notas_azules+1
#         notas_azules+=1
#     # suma+=nota
#     suma=suma+nota

# prom=suma/cantN
# print("su promedio es ", round (prom, 1))
# print(f"obtuvo {notas_azules} nota sobre 4" )

# if prom>=4:
#     print("el alumno aprobo")
# else:
#     print("el alumno reprobo")

# frase=input("ingrese su nombre")
# cont=0
# for i in frase:
#     cont+=1
# print (f"la cantidad de caracteres es {cont}")

# cont=len(frase)
# print (f"la cantidad de caracteres es {cont}")