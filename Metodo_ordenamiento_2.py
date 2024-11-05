# Lista de palabras
palabras = ["manzana", "naranja", "banana", "pera", "uva", "kiwi"]
print("Lista original:", palabras)

# 1. Método de Burbuja con proceso visible
def burbuja(arr):
    n = len(arr)
    print("\nProceso de ordenamiento por Burbuja:")
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
            print(f"Paso {i}-{j}: {arr}")
    return arr

# 2. Método de Inserción con proceso visible
def insercion(arr):
    print("\nProceso de ordenamiento por Inserción:")
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
            print(f"Paso {i}-{j}: {arr}")
        arr[j + 1] = key
    return arr

# 3. Método de Selección con proceso visible
def seleccion(arr):
    print("\nProceso de ordenamiento por Selección:")
    for i in range(len(arr)):
        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        print(f"Paso {i}: {arr}")
    return arr

# Copias de la lista original
palabras_burbuja = palabras[:]
palabras_insercion = palabras[:]
palabras_seleccion = palabras[:]

# Ordenar usando cada método
print("\nLista original:", palabras)
print("Resultado final por Burbuja:", burbuja(palabras_burbuja))
print("Resultado final por Inserción:", insercion(palabras_insercion))
print("Resultado final por Selección:", seleccion(palabras_seleccion))
