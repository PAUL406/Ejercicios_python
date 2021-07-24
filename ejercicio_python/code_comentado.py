from io import open
import os,fnmatch,shutil,errno
# Primero que todo buenos días/tarde/noche cuando estés viendo esto :D 
extensiones = ['*.jpg', '*.png'] #Solo quiero los archivos con extension '.jpg' nad '.png'
directorios = ['/home/paul/Escritorio/ejercicio_python/pseudo_tarea/A','/home/paul/Escritorio/ejercicio_python/pseudo_tarea/B'] #Quiero que mire en 2 directorios diferentes.

lista2=[]
for i in directorios: 
    ''' Quiero simplificar esto ¿es posible? o ¿existe otro opción mas eficiente?....tengo que buscar mas...
    Utilizó 'os.path.join' para unir dos partes y conformar una ruta, 
    'os.walk' crea una un arbol de directorios, el valor retornado del objeto iterable es una tupla con tres elementos
    por ultimo utilizo 'fnmatch.filter' para filtrar entre el árbol de directorios generado por 'os.walk' 
    y extraer y añadir a una lista estos estos strings con la terminación especificada 
    se que podría utilizar la funcion 'open de la librería os' para escribir y leer información directamente
    pero no quiero que se complique 'todavía' por lo cual lo realizó con listas '''

    lista = [os.path.join(raiz, archivos)
        for raiz, _, archivos in os.walk(i)
            for ext in extensiones
                for archivos in fnmatch.filter(archivos, ext)]
    lista2.extend(lista)

newDir='lo_que_copio'
try:
    os.mkdir(newDir)
except OSError as e:
    if e.errno != errno.EEXIST:
        raise


archivo_externo=open('externo.txt','w') #Quiero que me guarde en un archivo con extensión '.txt' las rutas de los archivos 
for i in lista2:
    shutil.copy(i,newDir)
    archivo_externo.write(i)
    archivo_externo.write('\n')

archivo_externo.close()

