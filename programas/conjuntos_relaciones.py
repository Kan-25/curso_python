# Notación de conjuntos 

A = set({1, 2, 3, 4})  # Notación de Conjuntos

def verificar_extension(A): #verificacion del conjunto A
    if set(A) == {1,2,3,4}: 
        print(" A contine los valores esperados. ")
    else :
        print(" El conjunto A no contiene los valores esperados ")

verificar_extension(set(A)) # envia los valores a la funcion
print(" El conjunto de valoes de A son: ", A)

B = set ({i for i in range(1, 21) if i%2 == 0}) #comprension de valores

def verificar_conjuntos(conjunto,n): #verificacion del conjunto B
    if set(conjunto) == {2,4,6,8,10,12,14,16,18,20}: 
        print(f" El conjunto {n} contiene los valores esperados. ")
        print(" El conjunto de valores pares de B son: ", conjunto)
    else : 
        print(f" El conjunto {n} no contiene los valores esperados ")
        print(" El conjunto de valores pares de B son: ", conjunto)

verificar_conjuntos(list(B), "B") # envia los valores a la funcion

# Cardinalidad
cardinalidad_a = len(A) #longitud de A

def verificar_cardinalidad(A, esperado): #verificacion de la cardinalidad
    if len(A) == esperado:
        print(f" La cardinalidad del conjunto A es correcta, el valor esperado es {esperado} ")
    else:
        print(f" La cardinalidad del conjunto A es incorrecta, el valor esperado es {esperado} ")

verificar_cardinalidad(A, 4) # envia los valores a la funcion

#conjuntos infinitos(Simulacion con cortes finitos)
for n in range (1,101):
    print(n)

longitud = len(range (1,101))
def verificar_tamaño(longitud, tamaño): #verificacion del ciclo
    #verifica que la longitud del conjunto dea correcta
    if longitud == tamaño:
        print(f" La longitud del conjunto es la correcta {tamaño}")
    else:
        print(f" la longitud es incorrecta, la longitd esperada es{tamaño}")

verificar_tamaño(longitud, 100)

#operaciones con conjuntos
union = set(A).union(set(B))
interseccion = set(A).intersection(set(B))
diferencia = set(A).difference(set(B))
diferencia_simetrica = set(A).symmetric_difference(set(B))

print(" La Union de A y B es: ", union)
print(" La Interseccion de A y B es: ", interseccion)
print(" La Diferencia de A y B es: ", diferencia)
print(" La Diferencia Simetrica de A y B es: ", diferencia_simetrica)

def verificacion(A, B, resultado, n):
    if resultado == set(A).union(set(B)): #Verifica si el resultado de una operación es el esperado.
        print(f" La {n} es correcta: {resultado}")
    else:
        print(f" La {n} es incorrecta: {resultado}")
#Envia los valores a la funcion verificar
verificacion(set(A),set(B), union, "Union")
verificacion(set(A),set(B), interseccion, " Interseccion")
verificacion(set(A),set(B), diferencia, " Diferencia")
verificacion(set(A),set(B), diferencia_simetrica, "Diferencia Simetrica")

# Definición del conjunto universal
U = set(range(1, 21))
print("El conjunto universal U es:", U)

# Complemento de A
complemento_A = U.difference(A)
print("El complemento de A (U - A) es:", complemento_A)

# Función de verificación del complemento
def verificar_complemento(original, complemento, universal):
    union_complemento = original.union(complemento)# La unión de un conjunto y su complemento debe ser el conjunto universal
    interseccion_complemento = original.intersection(complemento)# La intersección de un conjunto y su complemento debe ser un conjunto vacío
    
    if union_complemento == universal and interseccion_complemento == set(): #verificacion del complemento
        print(" La verificacion del complemento de A es correcta.")
    else:
        print(" La verificacion del complemento de A es incorrecta.")

verificar_complemento(A, complemento_A, U)#Llamada a la función de verificaci0n

producto_cartesiano_AB = {(a, b) for a in A for b in B}# Producto cartesiano de A y B
print("El producto cartesiano de A y B es:", producto_cartesiano_AB)

# Función de verificación del producto cartesiano
def verificar_productocartesiano(conjunto1, conjunto2, resultado):
    tamaño = len(conjunto1) * len(conjunto2) #Tamaño del  producto cartesiano
    
    if len(resultado) == tamaño: #verificacion del producto cartesiano
        print(f" La verificacion del producto cartesiano es correcta. El tamaño es {len(resultado)}.")
    else:
        print(f" La verificacion del producto cartesiano es incorrecta. El tamaño esperado era {tamaño}, pero se obtuvo {len(resultado)}.")

# Llamada a la función de verificación
verificar_productocartesiano(A, B, producto_cartesiano_AB)
#RELACIONES
#conjuntos
C = {1, 2, 3}
R = {(1, 1), (2, 2), (3, 3), (1, 2), (2, 3)}

# Reflexiva
def reflexiva(relacion, conjunto):
    return all((x, x) in relacion for x in conjunto)

print(f"Relacion R: {R}")
print(f"Conjunto C: {C}")

# Simétrica
def simetrica(relacion):
    return all((y, x) in relacion for x, y in relacion)

# Antisimétrica
def antisimetrica(relacion):
    for x, y in relacion:
        if (y, x) in relacion and x != y:
            return False
    return True

# Transitiva
def transitiva(relacion):
    for a, b in relacion:
        for c, d in relacion:
            if b == c and (a, d) not in relacion:
                return False
    return True

# Verificación de propiedades para R
print(f"Reflexiva: {reflexiva(R, C)}")
print(f"Simetrica: {simetrica(R)}")
print(f"Antisimetrica: {antisimetrica(R)}")
print(f"Transitiva: {transitiva(R)}")

# Relaciones de Equivalencia y de Orden
def verificar_relacion_equivalencia(relacion, conjunto):
    return reflexiva(relacion, conjunto) and simetrica(relacion) and transitiva(relacion)

def verificar_relacion_orden(relacion, conjunto):
    return reflexiva(relacion, conjunto) and antisimetrica(relacion) and transitiva(relacion)

#relacion de equivalencia
R_equivalencia = {(1, 1), (2, 2), (3, 3), (1, 2), (2, 1), (2, 3), (3, 2), (1, 3), (3, 1)}
print(f" Relacion : {R_equivalencia}")
print(f" Es una relacion de equivalencia: {verificar_relacion_equivalencia(R_equivalencia, C)}")

#relacion de orden
r_orden = {(1, 1), (2, 2), (3, 3), (1, 2), (1, 3), (2, 3)}
print(f" Relacion: {r_orden}")
print(f"Es una relacion de orden: {verificar_relacion_orden(r_orden, C)}")

# Funciones
dominio = {1, 2, 3, 4, 5}
codominio = {2, 4, 6, 8, 10}
f1 = { (x, 2 * x) for x in dominio } # f(x) = 2x

dominio2 = {1, 2, 3, 4, 5, 6, 7, 8, 9}
codominio2 = {0, 1, 2}
f2 = { (x, x % 3) for x in dominio2 } # f(x) = x mod 3

dominio3 = {1, 2, 3}
codominio3 = {2, 3, 4}
f3 = { (x, x + 1) for x in dominio3 } # f(x) = x + 1

# Inyectiva
def inyectiva(funcion):
    valores_imagen = [par[1] for par in funcion]
    return len(valores_imagen) == len(set(valores_imagen))

print(f"Funcion f(x) = 2x: {f1}")
print(f"Es inyectiva: {inyectiva(f1)}")

#Sobreyectiva
def sobreyectiva(funcion, codominio):
    valores_imagen = {par[1] for par in funcion}
    return valores_imagen == codominio

print(f"Funcion f(x) = x mod 3: {f2}")
print(f"Codominio: {codominio2}")
print(f"Es sobreyectiva: {sobreyectiva(f2, codominio2)}")

# Biyectiva: es inyectiva y sobreyectiva
def biyectiva(funcion, codominio):
    return inyectiva(funcion) and sobreyectiva(funcion, codominio)

print(f"Funcion f(x) = x + 1: {f3}")
print(f"Codominio: {codominio3}")
print(f"Es biyectiva: {biyectiva(f3, codominio3)}")

# clausuras
R_original = {(1, 2), (2, 3)} #relacion original
print(f"Relacion original: {R_original}")

#Clausura Reflexiva
def clausura_reflexiva(relacion, conjunto):
    return relacion.union({(x, x) for x in conjunto})

R_reflexiva = clausura_reflexiva(R_original, C)
print(f"Clausura Reflexiva: {R_reflexiva}")
print(f"Es Reflexiva: {reflexiva(R_reflexiva, C)}")

#Clausura Simétrica
def clausura_simetrica(relacion):
    return relacion.union({(y, x) for x, y in relacion})

R_sim = clausura_simetrica(R_original)
print(f"Clausura Simetrica: {R_sim}")
print(f"Es Simetrica: {simetrica(R_sim)}")

#Clausura Transitiva
def clausura_transitiva(relacion):
    clausura = set(relacion)
    while True:
        nueva_clausura = clausura.union({(a, c) for a, b in clausura for c, d in clausura if b == c})
        if nueva_clausura == clausura:
            return clausura
        clausura = nueva_clausura

R_transitiva = clausura_transitiva(R_original)
print(f"Clausura Transitiva: {R_transitiva}")
print(f"Es Transitiva: {transitiva(R_transitiva)}")

# Clausura de Equivalencia: aplicada a las 3 clausuras
def clausura_equivalencia(relacion, conjunto):
    paso1 = clausura_reflexiva(relacion, conjunto)
    paso2 = clausura_simetrica(paso1)
    return clausura_transitiva(paso2)

R_eq_clausura = clausura_equivalencia(R_original, C)
print(f"Clausura de Equivalencia: {R_eq_clausura}")
print(f"Es una relacion de equivalencia: {verificar_relacion_equivalencia(R_eq_clausura, C)}")