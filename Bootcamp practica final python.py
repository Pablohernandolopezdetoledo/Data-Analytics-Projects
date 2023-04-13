#practica final de fundamentos, la primera parte del ejercicio consiste en hacer un programa con 4 acciones diferentes, en la segunda parte
# hay que encriptar las contraseñas

lista_aplicaciones = ["Gmail", "Tinder", "Twitter", "Tiktok", "Instagram"]
lista_contraseñas = ["20051206Correo!", "qwerasdf1234#", "Tw2022+LMP", "Tik2022*VTP","Ins2022!MFR"]

#variables apartado encriptador
clave = 'MURCIELAGO'
clave_numerica = '0123456789'
lista_clave_encriptada = []
lista_clave_desencriptada = []
clave_encriptada = ''
clave_desencriptada = ''
nueva_clave_encriptada = ''


from random import SystemRandom # importamos SystemRandom para hacer el punto 1. Generar aleatoriamente una contraseña

contador = 0 #creo un contador para el punto 3, donde se pide eliminar la ultima contraseña creada al ejecutar. El contador empieza en cero y se le suma 1 cuando se ejecute este apartado, entonces cumplirá la condicion para borrar la ultima contraseña
contador_encript = 0 #creo un contador
accion = ''

while accion != 'NO':

    print('BIENVENIDO AL GENERADOR DE CONTRASEÑAS \n \n 1.Agregar nuevas contraseñas \n 2.Buscar una aplicación \n 3.Eliminar la última contraseña agregada \n 4.Modificar una contraseña')
    accion = int(input('\n Que acción quiere realizar: '))

    #Agregar nuevas contraseñas: reutilizo código de un ejercicio pasado.
    if accion == 1:

        aplicacion = input('Introduzca el nombre de la aplicación: ').title()

        if aplicacion in lista_aplicaciones:
            print('La aplicación ya está registrada')

        else:
            lista_aplicaciones.append(aplicacion)
            tipo_contraseña = int(input('¿Quiere introducir manualmente la contraseña(1) o que se genera automáticamente(2)?: '))

            if tipo_contraseña == 1:
                contraseña_manual = input('Introduzca la contraseña: ')
                while contraseña_manual in lista_contraseñas:  #no se puede utilizar la misma contraseña dos veces, creamos un bucle con while hasta que no coincidan las dos contraseñas
                    print('La contraseña ya ha sido usada, por favor introduzca otra diferente')
                    contraseña_manual = input('Introduzca la contraseña: ')

                encriptar = input('Quieres encriptar tu contraseña? (SI/NO): ').upper()

                if encriptar == 'SI':
                    encriptador = contraseña_manual.upper() #hacemos mayuscula para que coincidan con MURCIELAGO
                    for i in encriptador:
                        if i in clave:
                            posicion = (clave.find(i)) #busco la posicion de i en MURCIELAGO y la guardo en una variable
                            lista_clave_encriptada.append(posicion) #añado esta variable a la lista de claves encriptadas
                        else:
                            lista_clave_encriptada.append(i.lower()) #utilizo el else para añdir las variables que no coincidan con las letras de MURCIELAGO, le meto un lower para que me lo haga minuscula

                    for i in lista_clave_encriptada:
                        clave_encriptada = clave_encriptada + str(i) # con un for recorro lista_clave_encriptada y añado a una variable los diferentes valores que se han ido añadiendo en la lista encriptada

                    if clave_encriptada in lista_contraseñas:  # no se puede utilizar la misma contraseña dos veces, creamos un bucle con while hasta que no coincidan las dos contraseñas
                        print('La contraseña ya ha sido usada, por favor introduzca otra diferente')
                        print('Error en el sistema... REINICIANDO...')
                        print('BIENVENIDO AL GENERADOR DE CONTRASEÑAS \n \n 1.Agregar nuevas contraseñas \n 2.Buscar una aplicación \n 3.Eliminar la última contraseña agregada \n 4.Modificar una contraseña')
                        accion = int(input('\n Que acción quiere realizar: '))

                    else:
                        print('Tu contraseña es', clave_encriptada)
                        lista_contraseñas.append(clave_encriptada)
                        lista_clave_encriptada.clear() # vacio la lista de contraseñas para que no se dupliquen los valores si el usuario va a añadir mas contraseñas
                        clave_encriptada = '' #igual con la clave_encriptada
                        contador_encript +=1
                else:
                    lista_contraseñas.append(contraseña_manual)

            if tipo_contraseña == 2:
                valores_aleatorios = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ" #valores con los que va a crear la contraseña
                longitud_contrasenia = 12

                generador_contraseña = SystemRandom()
                contraseña_automatica = ''

                while longitud_contrasenia > 0: #para que tenga 12 caracteres la contraseña
                    contraseña_automatica = contraseña_automatica + generador_contraseña.choice(valores_aleatorios) #en cada vuelta del bucle while se añade un valor aleatorio
                    longitud_contrasenia = longitud_contrasenia - 1 #primera vuelta 11, segunda vuelta 10... en cada vuelta se añade una variable, cuando llegue a 0 dejará de cumplir las condiciones para que se ejecute el bucle while
                print('La contraseña es', contraseña_automatica)
                lista_contraseñas.append(contraseña_automatica)

        print('Las aplicaciones metidas en consola son: ',lista_aplicaciones)
        print('Las contraseñas metidas en consola son: ',lista_contraseñas)
        contador += 1 #creo un contador para el punto 3, donde se pide eliminar la ultima contraseña creada al ejecutar. El contador empieza en cero y se le suma 1 cuando se ejecute este apartado, entonces cumplirá la condicion para borrar la ultima contraseña
        accion = input('¿Quieres realizar otra acción? (SI/NO): ').upper()

    if accion == 2: #nos piden que introduzcamos el nombre de una aplicacion y que devolvamos su contraseña
        busqueda_app = input('Introduzca la aplicacion que quiere buscar: ').title()

        if busqueda_app not in lista_aplicaciones:
            print('La aplicación no se encuentra registrada')

        elif busqueda_app in lista_aplicaciones: #primero con el condicional le pido que compruebe que la app se encuentra en la lista
            if contador_encript != 0:
                posicion_app = lista_aplicaciones.index(busqueda_app)  # busco la posicion de app en la lista

                # en este apartado nos estan pidiendo que desencriptemos la contraseña cuando el usuario pido visualizar la contraseña de la app
                for i in lista_contraseñas[posicion_app]: #buscamos la contraseña de la app igualando su posicion: posicion_app(lista aplicaciones) == posicion_contraseña(en lista_contraseñas) y recorremos la contraseña para desencriptarla
                    if i in clave_numerica: #si la i se encuentra en clave numerica '0123456789', buscaremos su posicion
                        posicion_numerica = i #creamos una variable con la posicion de i
                        posicion = clave[int(posicion_numerica)] #creamos otra variable que nos va a buscar la 'posicion' en clave 'MURCIELAGO'
                        lista_clave_desencriptada.append(posicion) #añadimos este dato a lista desencriptada

                    else:
                        lista_clave_desencriptada.append(i.lower()) #si no coincide con ninguna letra de MURCIELAGO se añade a la lista

                for i in lista_clave_desencriptada:
                    clave_desencriptada = clave_desencriptada + str(i.lower())

                print('La contraseña de', busqueda_app, 'es',clave_desencriptada)
                lista_clave_desencriptada.clear() #vaciamos la lista
                clave_desencriptada = ''

            else:
                posicion_app = lista_aplicaciones.index(busqueda_app) #busco la posicion de app en la lista
                print('La contraseña de',busqueda_app,'es',lista_contraseñas[posicion_app]) #igualo esa posicion de la lista de aplicaciones con la lista de contraseñas ya que estan ordenadas a la par

        accion = input('¿Quieres realizar otra acción? (SI/NO): ').upper()

    if accion == 3: #Eliminar la ultima contraseña añadida. la gracia de este apartado es detectar que se ha añadido una contraseña ejecutando el programa, como ya explico arriba este lo hago con un contador
        if contador != 0:
            lista_contraseñas.pop() #.pop borra el ultimo valor de la lista
            print('Se ha eliminado la ultima contraseña')
            print(lista_contraseñas)
        else:
            print('No hay ninguna contraseña que eliminar')

        accion = input('¿Quieres realizar otra acción? (SI/NO): ').upper()

    if accion == 4: #Modificar una contraseña. al modificar vamos a borrar la contraseña solicitado y sustituirla en la misma posicion en la lista por la nueva
        app = input('Introduce el nombre de la aplicación de la que quieres modificar la contraseña: ').title()

        if app in lista_aplicaciones:
            posicion_aplicacion = lista_aplicaciones.index(app) #busco la posicion de la app en la lista
            contraseña_vieja = lista_contraseñas[posicion_aplicacion] #creo una nueva variable con la posicion de la app, ya que coincide con la posicion de la contraseña
            lista_contraseñas.remove(contraseña_vieja) #elimino de la lista de contraseñas la vieja contraseña
            nueva_contraseña = int(input('¿Quiere introducir manualmente la contraseña(1) o que se genera automáticamente(2)?: '))

            if nueva_contraseña == 1:
                if contador_encript!=0:
                    contraseña_manual = input('Introduzca la contraseña: ')
                    encriptador = contraseña_manual.upper()
                    for i in encriptador:
                        if i in clave:
                            posicion = (clave.find(i))
                            lista_clave_encriptada.append(posicion)
                        else:
                            lista_clave_encriptada.append(i.lower())
                    print(lista_clave_encriptada)
                    for i in lista_clave_encriptada:
                        nueva_clave_encriptada = nueva_clave_encriptada + str(i)
                    lista_contraseñas.insert(posicion_aplicacion,nueva_clave_encriptada)  # con el insert le digo en que posicion de la lista tiene que meter la contraseña

                else:
                  contraseña_manual = input('Introduzca la contraseña: ')

                while contraseña_manual in lista_contraseñas:
                    print('La contraseña ya ha sido usada, por favor introduzca otra diferente')
                    contraseña_manual = input('Introduzca la contraseña: ')

                lista_contraseñas.insert(posicion_aplicacion,contraseña_manual) #con el insert le digo en que posicion de la lista tiene que meter la contraseña

            if nueva_contraseña == 2:
                valores_aleatorios = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
                longitud_contrasenia = 12

                generador_contraseña = SystemRandom()
                contraseña_automatica = ''

                while longitud_contrasenia > 0:
                    contraseña_automatica = contraseña_automatica + generador_contraseña.choice(valores_aleatorios)
                    longitud_contrasenia = longitud_contrasenia - 1
                print('La contraseña es', contraseña_automatica)
                lista_contraseñas.insert(posicion_aplicacion,contraseña_automatica)
            print(lista_contraseñas)
        else:
            print('Lo siento, la aplicación no está registrada')
            print(lista_aplicaciones)

        accion = input('¿Quieres realizar otra acción? (SI/NO): ').upper()





