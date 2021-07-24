# Primero que todo buenos días/tarde/noche cuando estés viendo esto :D 
from io import open
import os,fnmatch,shutil,errno
extensiones = ['*.jpg', '*.png'] #Extensiones que quiero que encientre 
directorios = ['/home/paul/Escritorio/ejercicio_python/pseudo_tarea/A','/home/paul/Escritorio/ejercicio_python/pseudo_tarea/B'] #directorios en los que buscara

lista2=[]
for i in directorios: 

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


archivo_externo=open('externo.txt','w') 
for i in lista2:
    shutil.copy(i,newDir)
    archivo_externo.write(i)
    archivo_externo.write('\n')

archivo_externo.close()

