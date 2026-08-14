def planear_viaje(vuelos:list) -> list:
    lista = []
    i = 0
    while i < len(vuelos):
        h = 0
        j = 1
        contador = 0
        while h < len(vuelos):
            inicio = vuelos[i][0]
            salida = vuelos[h][j]
            if inicio == salida:
                contador += 1
            h += 1
        if contador == 0:
            lista.append(vuelos[i])
        i += 1
    i = 0 
    j = 0 
    while i < len(vuelos) and j == len(lista)-1:
        if lista[j][1] == vuelos[i][0]:
            lista.append(vuelos[i])
            j += 1
            if len(lista) != len(vuelos):
                i = 0
            else:
                i += 1
        else:
            i += 1
        
    
    return lista 


print(planear_viaje([
[ "Berlin", "Beijing"],
[ "Amsterdam" , "Berlin"] ,
[ "Bogota", "Madrid"] ,
[ "Beijing", "Tokyo" ] ,
[ "Madrid", "Amsterdam"] 
]))