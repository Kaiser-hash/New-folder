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
