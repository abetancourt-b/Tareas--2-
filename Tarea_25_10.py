#Autor: Antonio Betancourt

# Punto 1: Desarrollar un algoritmo que determine si una matriz es magica. Se dice que una matriz cuadrada es magica si la suma de cada una de sus filas, de cada una de sus columnas y de cada diagonal es igual.

print("\n--- Punto 1 ---")
n = int(input("\nIngrese el tamaño de la matriz: "))

matriz = []
for i in range(n):
    fila = []
    for j in range(n):
        valor = int(input(f"Ingrese el valor para la posición [{i+1},{j+1}]: "))
        fila.append(valor)
    matriz.append(fila)

suma_referencia = 0
for j in range(n):
    suma_referencia += matriz[0][j]

print("\nSuma de referencia =", suma_referencia)
print("Analizando filas y columnas...\n")

magica = True

for i in range(n):
    suma_fila = 0
    suma_columna = 0

    for j in range(n):
        suma_fila += matriz[i][j]
        suma_columna += matriz[j][i]

    print(f"Fila {i+1}: {suma_fila} | Columna {i+1}: {suma_columna}")

    if suma_fila != suma_referencia or suma_columna != suma_referencia:
        print(f"\nFila o columna {i+1} no coincide con la suma de referencia ({suma_referencia}).")
        magica = False
        print("Se usó el break y se detiene el ciclo.\n")
        break  

if magica:
    suma_diag1 = 0
    suma_diag2 = 0
    for i in range(n):
        suma_diag1 += matriz[i][i]
        suma_diag2 += matriz[i][n - 1 - i]

    print(f"\nPrimera Diagonal: {suma_diag1} | Segunda Diagonal: {suma_diag2}")

    if suma_diag1 != suma_referencia or suma_diag2 != suma_referencia:
        magica = False

print("\nRESULTADO:")
if magica:
    print("La matriz es mágica.\n")
else:
    print("La matriz no es mágica.\n")

# Punto 2: Desarrollar un algoritmo que imprima de manera ascendente los valores (todos del mismo tipo) de un diccionario.

print("\n--- Punto 2 ---\n")

datos = {"a": 8, "b": 3, "c": 10, "d": 1, "e": 5}

valores_ordenados = sorted(datos.values())

print(valores_ordenados)

# Punto 3: Desarrollar un algoritmo que verifique si todas las clave:valor de un diccionario se encuentran en otro diccionario.

print("\n--- Punto 3 ---\n")

dict1 = {"Hola": 1, "Adios": 9, "Hasta Luego": 5, "Hasta Mañana": 7, "Buenos Dias": 10}
dict2 = {"Hola": 2, "Adios": 9, "Hasta Luego": 11, "Hasta Mañana": 7, "Buenos Dias": 10}

for clave, valor in dict2.items():
    if clave in dict1 and dict1[clave] == valor:
        print(f"{clave}: {valor} está en ambos diccionarios.")
    else:
        print(f"{clave}: {valor} No está en el otro diccionario.")

# Punto 4: Desarrollar una funcion que reciba dos diccionarios como parametros y los mezcle, es decir, que se construya un nuevo diccionario con las llaves de los dos diccionarios; si hay una clave repetida en ambos diccionarios, se debe asignar el valor que tenga la clave en el primer diccionario.

print("\n--- Punto 4 ---\n")

def mezclar_diccionarios(dict1, dict2):
    combinado = dict2.copy()
    combinado.update(dict1)    
    return combinado

a = {"x": 1, "y": 2, "z": 3}
b = {"y": 9, "w": 5}

resultado = mezclar_diccionarios(a, b)
print(resultado)

# Punto 5: Desarrollar un programa que dada una listas de personas, cada persona representada como el siguiente ejemplo: {"nombres":"Pedro Julio", "apellidos":"Tristan Merchan", "edad":101}, imprima los nombres y apellidos de las personas que estan en un rango de edades.

print("\n--- Punto 5 ---\n")

personas = [{"nombres": "Pedro Julio", "apellidos": "Tristán Merchán", "edad": 101},
    {"nombres": "Ana María", "apellidos": "Lopez Rojas", "edad": 25},
    {"nombres": "Carlos", "apellidos": "Gomez Perez", "edad": 45},
    {"nombres": "Lucia", "apellidos": "Martinez Soto", "edad": 18}]


edad_min = int(input("Ingrese la edad mínima: "))
edad_max = int(input("Ingrese la edad máxima: "))

print(f"\nPersonas entre {edad_min} y {edad_max} años:\n")

for p in personas:
    if edad_min <= p["edad"] <= edad_max:
        print(f"{p['nombres']} {p['apellidos']} ({p['edad']} años)")
