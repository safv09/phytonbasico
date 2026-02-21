#Tuplas
mi_tupla = (2,4)
print("Mi tupla: ", mi_tupla)

#Lista
mi_lista = [1,3.1416, "Samuel", mi_tupla]
print("El primer elemnto de mi lista: ", mi_lista[0])
print("El cuarto elemento de mi lista:", mi_lista[3])
print("el tercer elemento de mi lista:", mi_lista[2])

#Diccionarios
mi_direccionario = {
    "mi lista": mi_lista,
    "nombre": "samuel",
    "Pi":3.1416,
    "Tel": "663-6968731"

}
print("Llave para accesar a mi diccionario mi_lista", mi_direccionario("mi_lista"))
print("Llave para accesar a mi direccionario Pi", mi_direccionario("Pi"))
print("Llave para accesar a mi direccionario Tel", mi_direccionario("Tel"))

