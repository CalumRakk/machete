import os
import argparse
import re

def isTime(value):
    if not re.match(r'^\d{2}:\d{2}:\d{2}$', value):
        raise argparse.ArgumentTypeError(
            'El argumento debe ser de tipo HH:MM:SS')
    return value
def isFile(value):
    if not os.path.isfile(value):
        raise argparse.ArgumentTypeError(
            'El argumento debe ser un archivo')
    return value
def getOutput(value):
    ext= os.path.splitext(value)[1]
    basename= os.path.basename(value).replace(ext, '')
    dirname= os.path.dirname(value)
    
    index=1
    while True:
        path= os.path.join(dirname, f'{basename}_{index}{ext}')
        if not os.path.exists(path):
            return path
        
parser = argparse.ArgumentParser(description='Recorta video')

parser.add_argument('input', type=isFile, help='Archivo de entrada')
parser.add_argument('time', type=isTime, help='Tiempo de inicio')
parser.add_argument('to', type=isTime, help='Tiempo de fin')
args = parser.parse_args()

input_=args.input
out=getOutput(input_)

time=args.time
to=args.to
os.system(fr'ffmpeg -ss {time} -to {to} -i "{input_}" -force_key_frames {time} -c copy {out}')