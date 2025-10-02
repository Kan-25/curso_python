# ============================================================
# conjuntos_relaciones.py
# Trabajo práctico: Conjuntos, Relaciones, Funciones y Clausuras
# Autor: [Manuel Vargas, Olmedo Sanchez, Luis Dominguez]
# Universidad de Panamá
# ============================================================

# ============================================================
# 1. Notación de conjuntos por extensión
# ============================================================
"""
Definición teórica:
La notación por extensión consiste en listar explícitamente todos
los elementos de un conjunto.
Ejemplo matemático:
A = {1, 2, 3, 4}
"""

A = {1, 2, 3, 4}
print("Resultado de extensión:", A)

def verificar_extension(conjunto):
    esperado = {1, 2, 3, 4}
    print("Operación extensión implementada correctamente:",
          conjunto == esperado)

verificar_extension(A)


# ============================================================
# 2. Notación por comprensión
# ============================================================
"""
Definición teórica:
La notación por comprensión describe un conjunto indicando la
propiedad que cumplen sus elementos.
Ejemplo matemático:
Pares = {x ∈ N | x ≤ 20 y x es par}
"""

pares = {x for x in range(1, 21) if x % 2 == 0}
print("Resultado de comprensión:", pares)

def verificar_comprension(conjunto):
    esperado = set(range(2, 21, 2))
    print("Compresión implementada correctamente:", conjunto == esperado)

verificar_comprension(pares)


# ============================================================
# 3. Operaciones con conjuntos
# ============================================================
"""
Definición teórica:
- Unión: A ∪ B = {x | x ∈ A o x ∈ B}
- Intersección: A ∩ B = {x | x ∈ A y x ∈ B}
- Diferencia: A - B = {x | x ∈ A y x ∉ B}
- Diferencia simétrica: A △ B = (A - B) ∪ (B - A)
"""

A = {1, 2, 3}
B = {3, 4, 5}

union = A | B
interseccion = A & B
diferencia = A - B
simetrica = A ^ B

print("Unión:", union)
print("Intersección:", interseccion)
print("Diferencia A-B:", diferencia)
print("Diferencia simétrica:", simetrica)

def verificar_union(A, B, resultado):
    print("Unión implementada correctamente:", resultado == A.union(B))

def verificar_interseccion(A, B, resultado):
    print("Intersección implementada correctamente:", resultado == A.intersection(B))

def verificar_diferencia(A, B, resultado):
    print("Diferencia implementada correctamente:", resultado == A.difference(B))

def verificar_simetrica(A, B, resultado):
    print("Diferencia simétrica implementada correctamente:",
          resultado == A.symmetric_difference(B))

verificar_union(A, B, union)
verificar_interseccion(A, B, interseccion)
verificar_diferencia(A, B, diferencia)
verificar_simetrica(A, B, simetrica)


# ============================================================
# 4. Conjuntos infinitos
# ============================================================
"""
Definición teórica:
Un conjunto infinito no tiene un número finito de elementos.
Ejemplo: el conjunto de los números naturales N = {1, 2, 3, ...}.
En Python se simula con generadores.
"""

import itertools
naturales = itertools.count(1)  # generador infinito
primeros_10 = list(itertools.islice(naturales, 10))
print("Primeros 10 números naturales:", primeros_10)


# ============================================================
# 5. Producto cartesiano
# ============================================================
"""
Definición teórica:
El producto cartesiano A × B es el conjunto de todos los pares ordenados
(a, b) con a ∈ A y b ∈ B.
Ejemplo matemático:
A = {1,2}, B = {a,b}
A × B = {(1,a), (1,b), (2,a), (2,b)}
"""

A = {1, 2}
B = {"a", "b"}
producto = {(x, y) for x in A for y in B}
print("Producto cartesiano A x B:", producto)

def verificar_producto_cartesiano(A, B, resultado):
    esperado = set((x, y) for x in A for y in B)
    print("Producto cartesiano implementado correctamente:",
          resultado == esperado)

verificar_producto_cartesiano(A, B, producto)


# ============================================================
# 6. Conjunto potencia
# ============================================================
"""
Definición teórica:
El conjunto potencia P(A) es el conjunto de todos los subconjuntos de A.
Ejemplo matemático:
A = {1,2}
P(A) = {∅, {1}, {2}, {1,2}}
"""

def conjunto_potencia(S):
    return [set(sub) for i in range(len(S)+1) for sub in itertools.combinations(S, i)]

S = {1, 2}
potencia = conjunto_potencia(S)
print("Conjunto potencia de", S, ":", potencia)


# ============================================================
# 7. Relaciones
# ============================================================
"""
Definición teórica:
Una relación R sobre A es un subconjunto de A × A.
Propiedades:
- Reflexiva: ∀a∈A, (a,a)∈R
- Simétrica: ∀a,b∈A, (a,b)∈R → (b,a)∈R
- Transitiva: ∀a,b,c∈A, (a,b),(b,c)∈R → (a,c)∈R
"""

A = {1, 2, 3}
R = {(1,1), (2,2), (3,3), (1,2), (2,3)}

def es_reflexiva(A, R):
    return all((a,a) in R for a in A)

def es_simetrica(R):
    return all((b,a) in R for (a,b) in R)

def es_transitiva(R):
    return all(((a,c) in R) for (a,b) in R for (x,c) in R if b == x)

print("Relación R:", R)
print("Es reflexiva:", es_reflexiva(A,R))
print("Es simétrica:", es_simetrica(R))
print("Es transitiva:", es_transitiva(R))


# ============================================================
# 8. Clausuras
# ============================================================
"""
Definición teórica:
La clausura de una relación consiste en extenderla para que cumpla
una propiedad.
- Clausura reflexiva: R ∪ {(a,a) | a∈A}
- Clausura simétrica: R ∪ {(b,a) | (a,b)∈R}
- Clausura transitiva: se añaden los pares necesarios para cumplir transitividad.
"""

def clausura_reflexiva(A, R):
    return R.union({(a,a) for a in A})

def clausura_simetrica(R):
    return R.union({(b,a) for (a,b) in R})

def clausura_transitiva(R):
    clausura = set(R)
    agregado = True
    while agregado:
        agregado = False
        for (a,b) in list(clausura):
            for (c,d) in list(clausura):
                if b == c and (a,d) not in clausura:
                    clausura.add((a,d))
                    agregado = True
    return clausura

print("Clausura reflexiva:", clausura_reflexiva(A,R))
print("Clausura simétrica:", clausura_simetrica(R))
print("Clausura transitiva:", clausura_transitiva(R))


# ============================================================
# 9. Funciones
# ============================================================
"""
Definición teórica:
Una función f: A → B es una relación que asigna a cada elemento de A
exactamente un elemento de B.
Propiedades:
- Inyectiva: diferentes elementos de A van a diferentes elementos de B.
- Sobreyectiva: la imagen de f cubre todo el codominio.
- Biyectiva: es inyectiva y sobreyectiva.
"""

A = {1,2,3}
B = {2,3,4}
f = {(x, x+1) for x in A}
print("Función f:", f)

def es_funcion(A,f):
    return len({a for (a,_) in f}) == len(A)

def es_inyectiva(f):
    imagen = [b for (_,b) in f]
    return len(imagen) == len(set(imagen))

def es_sobreyectiva(f, B):
    imagen = {b for (_,b) in f}
    return imagen == B

print("¿f es función?:", es_funcion(A,f))
print("¿f es inyectiva?:", es_inyectiva(f))
print("¿f es sobreyectiva?:", es_sobreyectiva(f,B))
print("¿f es biyectiva?:", es_inyectiva(f) and es_sobreyectiva(f,B))