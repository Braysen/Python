#Importamos la libreria sqlLite
import sqlite3

#Creamos la funcion que permitira crear y conectarnos a la base de datos
#Python tiene incorporado por default la libreria de SqlLite
def conecta_db():
    #Creamos una variable que nos va a permitir crear la base de datos y conectarla
    #Nota: si la base de datos no esta creada y no se encuentra en la carpeta de destino
    #se crea la base de datos
    bd=sqlite3.connect("libros.db")
    #Mostramos un mensaje indicandole al usuario que la base de datos a sido creada correctamente y que la base de datos esta abierta
    print("\nBase de datos abierta")

#Creamos la funcion que permitira crear la tabla, en esta tabla se registraran los datos de los libros
def crea_tabla():
    try:
        #Creamos una variable que va a estar conectada a la base de datos de los libros
        bd=sqlite3.connect("libros.db")
        cursor=bd.cursor()
        #Creamos la sentencia sql que nos permitira crear la tabla libros
        tablas=["""create table if not exists libros(autor text not null, genero text not null, precio real not null,titulo text not null);"""]
        #Recorremos los datos
        for tabla in tablas:
            #Ejecutamos la sentencia
            cursor.execute(tabla);
        #Mostramos un mensaje al usuario indicandole que la tabla a sido creada correctamente
        print("\nTablas creadas correctamente")
    except sqlite3.OperationalError as error:
        print("Error al abrir: ",error) #Mostramos un error si las operaciones establecidas en el try no se ejecutan correctamente


#Creamos la funcion que permitira borrar la tabla libros
def borra_tabla():
    try:
        #Creamos una variable que va a estar conectada a la base de datos de los libros
        bd=sqlite3.connect("libros.db")
        cursor=bd.cursor()
        #Creamos la sentencia sql que nos permitira borrar la tabla libros
        tablas=["""drop table libros"""]
        #Recorremos los datos
        for tabla in tablas:
            #Ejecutamos la sentencia
            cursor.execute(tabla);
        #Mostramos un mensaje al usuario indicandole que la tabla a sido borrada correctamente
        print("\nTablas borradas correctamente")
    except sqlite3.OperationalError as error:
        print("Error al abrir: ",error) #Mostramos un error si las operaciones establecidas en el try no se ejecutan correctamente


#Creamos la funcion que permitira guardar los datos del libro
#Los datos que se registraran son los siguientes:
#-nombre de autor
#-genero del libro
#-precio del libro
#-titulo del libro
def inserta_tabla(aut,gen,pre,tit):
    try:
        #Creamos una variable que va a estar conectada a la base de datos de los libros
        bd=sqlite3.connect("libros.db")
        cursor=bd.cursor()
        #Creamos la sentencia sql que nos permitira registrar el libro
        libros=["""insert into libros (autor,genero,precio,titulo) values (?,?,?,?);"""]
        #Recorremos los datos
        for sentencia in libros:
            #Ejecutamos la sentencia y le enviamos como parametros los datos que se van a registrar
            cursor.execute(sentencia,[aut,gen,pre,tit]);
        #Mostramos un mensaje al usuario indicandole que los datos han sido registrados correctamente
        print("\nEl libro a sido registrado correctamente")
        bd.commit() #Guardamos los cambios
    except sqlite3.OperationalError as error:
        print("Error al abrir: ",error) #Mostramos un error si las operaciones establecidas en el try no se ejecutan correctamente


#Creamos la funcion que permitira mostrar los datos de los libros
def muestra_tabla():
    try:
        #Creamos una variable que va a estar conectada a la base de datos de los libros
        bd=sqlite3.connect("libros.db")
        cursor=bd.cursor()
        #Creamos la sentencia sql que nos permitira mostrar los datos de los libros
        sentencia="select * from libros;"
        #Ejecutamos la sentencia por medio de un cursor que nos permitira acceder a sus datos y poder recorrerlos
        cursor.execute(sentencia)
        libros=cursor.fetchall()
        #Creamos los bordes de la tabla y agregamos los campos que tiene la tabla libro
        print("+{:-<20}+{:-<20}+{:-<10}+{:-<50}".format("","","",""))
        print("|{:^20}+{:^20}+{:^10}+{:^50}".format("Autor","Genero","Precio","Titulo"))
        print("+{:-<20}+{:-<20}+{:-<10}+{:-<50}".format("","","",""))
        #Recorremos los datos
        for autor,genero,precio,titulo in libros:
            #Mostramos los datos de los libros
            print("|{:^20}+{:^20}+{:^10}+{:^50}".format(autor,genero,precio,titulo))

        #Cerramos el borde de la tabla
        print("+{:-<20}+{:-<20}+{:-<10}+{:-<50}".format("","","",""))
    except sqlite3.OperationalError as error:
        print("Error al abrir ",error) #Mostramos un error si las operaciones establecidas en el try no se ejecutan correctamente



#Creamos la funcion que permitira actualizar los datos de los libros
def actualiza_tabla():
    try:
        #Creamos una variable que va a estar conectada a la base de datos de los libros
        bd=sqlite3.connect("libros.db")
        cursor=bd.cursor()
        #Creamos la sentencia sql que nos permitira actualizar los datos de los libros
        sentencia=("select *,rowid from libros")
        #Ejecutamos la sentencia por medio de un cursor que nos permitira acceder a sus datos y poder recorrerlos
        cursor.execute(sentencia)
        libros=cursor.fetchall()
        #Creamos los bordes de la tabla y agregamos los campos que tiene la tabla libro
        print("+{:-<20}+{:-<20}+{:-<10}+{:-<50}+{:-<10}".format("","","","",""))
        print("|{:^20}+{:^20}+{:^10}+{:^50}+{:^10}".format("Autor","Genero","Precio","Titulo","RowId"))
        print("+{:-<20}+{:-<20}+{:-<10}+{:-<50}+{:-<10}".format("","","","",""))

        #Recorremos los datos
        for autor,genero,precio,titulo,rowid in libros:
            #Mostramos los datos de los libros
            print("|{:^20}+{:^20}+{:^10}+{:^50}+{:^10}".format(autor,genero,precio,titulo,rowid))

        #Cerramos el borde de la tabla
        print("+{:-<20}+{:-<20}+{:-<10}+{:-<50}+{:-<10}".format("","","","",""))
        #Pedir id  del libro a editar
        id_libro=input("\nEscribe el id del libro que quiere editar: ")
        #Validamos el dato proporcionado por el usuario
        if not id_libro:
            #Mostramos un mensaje indicandole al usuario que no ingreso el Id del libro que se va a actualizar
            print("No escribio nada")
            exit()
        #Pedimos los datos que se van a registrar
        autor=input("\nNuevo autor: ")
        genero=input("\nNuevo genero: ")
        precio=input("\nNuevo precio: ")
        titulo=input("\nNuevo titulo: ")

        #SEntencia para actualizar
        sentencia="Update libros set autor=?, genero=?, precio=?, titulo=? where rowid=?;"

        #Actualizar datos
        cursor.execute(sentencia,[autor,genero,precio,titulo,id_libro])
        bd.commit() #Guardamos los cambios
        print("\nDatos guardados")
    except sqlite3.OperationalError as error:
        print("Error al abrir ",error) #Mostramos un error si las operaciones establecidas en el try no se ejecutan correctamente



#Creamos la funcion que permitira eliminar los datos de los libros
def elimina_dato():
    try:
        #Creamos una variable que va a estar conectada a la base de datos de los libros
        bd=sqlite3.connect("libros.db")
        cursor=bd.cursor()
        #Creamos la sentencia sql que nos permitira actualizar los datos de los libros
        sentencia=("select *,rowid from libros")
        #Ejecutamos la sentencia por medio de un cursor que nos permitira acceder a sus datos y poder recorrerlos
        cursor.execute(sentencia)
        libros=cursor.fetchall()
        #Creamos los bordes de la tabla y agregamos los campos que tiene la tabla libro
        print("+{:-<20}+{:-<20}+{:-<10}+{:-<50}+{:-<10}".format("","","","",""))
        print("|{:^20}+{:^20}+{:^10}+{:^50}+{:^10}".format("Autor","Genero","Precio","Titulo","RowId"))
        print("+{:-<20}+{:-<20}+{:-<10}+{:-<50}+{:-<10}".format("","","","",""))

        #Recorremos los datos
        for autor,genero,precio,titulo,rowid in libros:
            #Mostramos los datos de los libros
            print("|{:^20}+{:^20}+{:^10}+{:^50}+{:^10}".format(autor,genero,precio,titulo,rowid))

        #Cerramos el borde de la tabla
        print("+{:-<20}+{:-<20}+{:-<10}+{:-<50}+{:-<10}".format("","","","",""))

        #Solicitamos al usuario el id del libro que desea eliminar
        id_libro=input("\nEscribe el id del libro que quiere eliminar: ")
        #Validamos el dato proporcionado por el usuario
        if not id_libro:
            #Mostramos un mensaje indicandole al usuario que no ingreso el Id del libro que se va a actualizar
            print("No escribio nada")
            exit()
        
        #Creamos la sentencia sql que nos permitira eliminar el libro seleccionado
        sentencia="delete from libros where rowid=?;"

        #Ejecutamos la sentencia con el id proporcionado por el usuario
        cursor.execute(sentencia,[id_libro])
        bd.commit() #guardamos los cambios
        #Mostramos un mensaje indicandole al usuario que el libro seleccionado a sido eliminado correctamente
        print("\nEl libro a sido eliminado correctamente")
    except sqlite3.OperationalError as error:
        print("Error al abrir ",error) #Mostramos un error si las operaciones establecidas en el try no se ejecutan correctamente


#Creamos la funcion que permitira crear un menu, en dicho menu el usuario podra seleccionar que tipo de accion desea realizar
#Las acciones que el usuario podra realizar son las siguientes
#Conectarse a la base de datos  (Opcion 1)
#Crear la tabla de libros  (Opcion 2)
#Borrar la tabla de libros   (Opcion 3)
#Registrar datos a la tabla libros con los campos requeridos  (Opcion 4)
#Mostramos los datos que han sido registrados en la tabla libros  (Opcion 5)
#Actualizamos los libros  (Opcion 6)
#Eliminamos el libro seleccionado por el usuario  (Opcion 7)
#Salimos del menu   (Opcion 0)
#Solicitamos al usuario que introduzca la accion que desea realizar
def menu():
    print("----------------------------------")
    print("              Menu                ")
    print("1. Conexion con BD")
    print("2. Creacion de tabla")
    print("3. Borrar tabla")
    print("4. Inserta datos en tabla (predefinidos)")
    print("5. Mostrar datos en tabla")
    print("6. Actualizar datos en tabla")
    print("7. Eliminar dato en tabla")
    print("0. Salir")
    print("Ingrese Opcion -------->")
    opciones()


#Creamos la funcion opciones para indicarle al usuario que acciones debe de realizar el programa
def opciones():
    #Solicitamos la opcion al usuario
    opcion=input()
    #Si la opcion es igual a 1, el usuario podra crear y conectarse a la base de datos
    if opcion=="1":
        #Nos conectamos a la base datos
        conecta_db()
        #Mostramos de nuevo el menu con las opciones establecidas
        menu()
        opciones()
    #Si la opcion es igual a 1, el usuario podra crear y conectarse a la base de datos
    elif opcion=="2":
        #Creamos la tabla
        crea_tabla()
        #Mostramos de nuevo el menu con las opciones establecidas
        menu()
        opciones()
    #Si la opcion es igual a 3, el usuario podra borrar la tabla de libros
    elif opcion=="3":
        #Funcion que borra la tabla libros
        borra_tabla()
        #Mostramos de nuevo el menu con las opciones establecidas
        menu()
        opciones()
    #Si la opcion es igual a 4, el usuario podra insertar datos en la tabla libros
    elif opcion=="4":
        au=input("\nEscribe el nombre del autor: ")
        ge=input("\nEscribe el genero del libro: ")
        pre=input("\nEscribe el precio del libro: ")
        ti=input("\nEscribe el titulo del libro: ")
        #Funcion que inserta datos a la tabla libros
        inserta_tabla(au,ge,pre,ti)
        #Mostramos de nuevo el menu con las opciones establecidas
        menu()
        opciones()
    #Si la opcion es igual a 5, el usuario podra mostrar la tabla libros
    elif opcion=="5":
        #Funcion que muestra las tablas
        muestra_tabla()
        #Mostramos de nuevo el menu con las opciones establecidas
        menu()
        opciones()
    #Si la opcion es igual a 6, el usuario podra actualizar la tabla libros
    elif opcion=="6":
        #Funcion que permitira actualizar la tabla libros
        actualiza_tabla()
        #Mostramos de nuevo el menu con las opciones establecidas
        menu()
        opciones()
    #Si la opcion es igual a 7, el usuario podra eliminar algun registro de la tabla libros
    elif opcion=="7":
        elimina_dato()
        #Mostramos de nuevo el menu con las opciones establecidas
        menu()
        opciones()
    #Si la opcion es igual a 0, el usuario podra salir de la aplicacion
    elif opcion=="0":
        #Comando que permitira salir de la aplicacion
        exit()

#Invocamos a la funcion menu, esta funcion permitira acceder a las funciones de la aplicacion
menu()
