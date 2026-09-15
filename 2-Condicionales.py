
edad:int = 18

if edad >= 18 and not False:
    print("Puedes pasar")
elif edad == 17:
    print("Casi pero no")
else:
    print("Al carrer!")

numeros:str = '0123456789'
for numero in numeros:
    if numero == '3': 
        continue
    print(numero, end=' - ')
    if numero == '7':
        break
