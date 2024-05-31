print('01 - OPERADORES Y ESTRUCTURAS DE CONTROL\n\n')
#Variables
x = 5; y = 3

#Aritméticos
print(" 1. Operadores aritméticos\n")
#Suma
print("Suma: ","x+y =", x+y)   #8
#Resta
print("Resta: ","x-y =", x-y)   #2
#Multiplicación
print("Multiplicación: ", "x*y =", x*y)   #15
#Division
print("División:", "x/y =", x/y)   #1.6666666666666666
#Módulo
print("Módulo: ", "x%y =", x%y)   #2
#Potencia
print("Potencia: ", "x**y =", x**y) #125
#Division_entera
print("División_Entera", "x//y =", x//y) #1

#Relacionales o Comparación
print("\n 2. Operadores Relacionales o Comparación\n")
#Igualdad
print("Igualdad: ","x==y =", x==y) # False
#Desigualdad
print("Desigualdad: ", "x!=y =", x!=y) # True
#MayorQue
print("MayorQue: ", "x>y  =", x>y)  # False
#MenorQue
print("MenorQue: ", "x<y  =", x<y)  # True
#MayorIgualQue
print("MayorIgualQue: ", "x>=y =", x>=y) # False
#MenorIgualQue
print("MenorIgualQue: ", "x<=y =", x<=y) # True

#Asignación
print("\n 3. Operadores de asignación:\n")
x =5
print(f"Asignación simple  x= {x}") #5
x +=5
print(f"Suma y asignación (x+=5) = {x}") #10
x -=y
print(f"Restar y asiganación (x-=y) = {x}") #7
x *= y
print(f"Multiplicación y asignación (x*=y) = {x}") #21
x /= y
print(f"División y asignación (x*=y) = {x}") #7.0
x %= y
print(f"Módulo y asignación (x%=y) = {x}") #1.0
x **= y
print(f"Potencia y asignación (x**=y) = {x}") #1.0
x //= y
print(f"División_Entera y asignación (x//=y) = {x}") #0.0

#Lógicos
print("\n 4. Operadores Lógicos:\n")
x = True; y = False
a = x and y
print(f"Opera_logic_AND (x and y) = {a}") #False
a = x or y
print(f"Opera_logic_OR (x and y) = {a}") #True
x = not x
print(f"Opera_logic_OR (x and y) = {x}") #False

#Identidad
print("\n 5. Operadores de identidad: \n")
x = ['a', 'b', 'c']
z = ['a', 'b']
y = x
c = x is z
print(f"OperadorIdentidad  (is) = {c}")
d = x is not z
print(f"OperadorIdentidad  (is not) = {d}")

#Pertenencia
print("\n 6. Operadores de Pertenencia: \n")

q = [1,2,3,4,5]
Nombre = 'Arturo De La Paz'

n = 'Paz' in Nombre
print(f"OperadorIdentidad  (in) = {n}") #True
o = 5 not in q
print(f"OperadorIdentidad  (in) = {o}") #False
#Operadores bit a bit
print("\n 7. Operadores bit a bit: \n")

a = 3 
b = 5
print(f"a = 3  binario =  {bin(3)}")
print(f"a = 5  binario =  {bin(5)}")
bit = a | b
print(f"Or: {bit}") #7
bit = a & b
print(f"And: {bit}") #1
bit = a ^ b
print(f"XOR: {bit}") #6
bit = ~a
print(f"NOT {bit}") #-4
bit = a >> b
print(f"Desplazamiento a la derecha : {bit}") #0
bit = a << b
print(f"Desplazamiento a la izquierda : {bit} \n") #96


print(' 8. DIFICULTAD EXTRA\n')
""" Programa que imprime por consola todos los números comprendidos entre 10 y 55 (incluidos), 
    pares, y que no son ni el 16 ni múltiplos de 3
    Lista para almacenar los números pares que cumplen las condiciones
"""
numeros_pares = []
# Bucle for que recorre los números entre 10 y 55 (incluidos)
for numero in range(10, 56):
  # Se evalúan las condiciones para agregar el número a la lista
    if numero != 16 and numero % 2 == 0 and numero % 3 != 0 or numero ==55:
        numeros_pares.append(numero)

print(numeros_pares)