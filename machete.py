import argparse
from machete import Machete

parser = argparse.ArgumentParser(description='Script para recortar trozos sin perdida de videos.')
parser.add_argument('path',help='La ruta del video')
parser.add_argument('range', nargs='*' ,help='El rango de donde inicia y termina el recorte, ejemplo, 00:30:40-00:35:43')
args = parser.parse_args()

if "__main__" == __name__:
    path= args.path
    range= args.range
    video= Machete(path)

    # True si range tiene varios rangos de tiempo.
    if bool(range)==True:        
        video.split(range)
    else:
        video.bucle()

        


 