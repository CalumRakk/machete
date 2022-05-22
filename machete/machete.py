import os
from datetime import datetime
from typing import List

# TODO: ¿que pasa si un video durá menos de una hora? o ¿menor de un minuto?

def get_times(ranges:List[str])->dict:
    """
    Devuelve diccionario que tiene una lista de rangos bien formateados y otra con rangos que no se pudieron formatear. 
    """
    document={"good":[],"bad":[]}
    for range in ranges:
        try:
            if range.casefold()=="exit":
                exit()
                
            start= range.split("-")[0]
            objeto= datetime.strptime(start,"%H:%M:%S")
            start= objeto.strftime("%H:%M:%S")
            
            end= range.split("-")[1]
            objeto= datetime.strptime(end,"%H:%M:%S")
            end= objeto.strftime("%H:%M:%S")
            
            
            document["good"].append(f"{start}-{end}")
        except ValueError:
            document["bad"].append(range)
            
    return document


class Machete:
    def __init__(self,path):
        self.path= self._open_file(path)
    
    def bucle(self)->None:

        while True:
            print("exit para salir.")
            range= input("range>>>")
            self.split(range.split())
    
    def split(self, ranges:list)->None: 
        """
        ranges: es una lista de rango de tiempos.
        rango de tiempo es un string que tiene la hora de inicio y finalización del trozo a recortar, ejemplo: 00:30:00-00:35:40
        """
        ranges= get_times(ranges)
        for range in ranges["good"]: 
            time= range    
            start=time.split("-")[0]
            end= time.split("-")[1]
            
            
            dirname= os.path.dirname(self.path)
            filename= os.path.basename(self.path)
            name= os.path.splitext(filename)[0]
            ext=os.path.splitext(filename)[1] 
            new_filename= name + " " + time.replace(":","")+ ext
            path= os.path.join(dirname,new_filename)
            os.system(fr'ffmpeg -ss {start} -to {end} -i "{self.path}" -force_key_frames {start} -c copy "{path}"')
        
        for bad in ranges["bad"]:
            print("\n")
            print(bad, "Tiene el formato de duración mal.")
            
    
    def _open_file(self,path):
        """
        Determina si el video existe.
        """
        if os.path.exists(path):
            return os.path.abspath(path)
        print("La ruta del video parece que no existe")
        exit()
        
    