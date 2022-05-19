
Script para recortar trozos sin perdida de videos. 

**machete**

    machete.py path [range]
- `path`: la ruta del video
- `range`: el rango de tiempo entre la hora de inicio y finalización a recortar, ejemplo: `00:30:40-00:35:43`. 



El siguiente comando recorda el video.mp4 desde el minuto 30 y 40 segundo hasta el minuto 35 y 43 segundos 

    >>> python machete.py video.mp4 00:30:40-00:35:43

range puede ser una lista de rangos sepadados por un espacio

    >>> python machete.py video.mp4 00:30:40-00:35:43 00:32:40-00:33:01

Si el script no recibe un rango de tiempo, se inicializa un bucle que pide el rango de tiempo.

    >>> python machete.py video.mp4
    range>>>

para salir del bucle se pasa el valor `exit`


----
## requisitos

Se requiere [ffmpeg]("https://www.ffmpeg.org/download.html") en las variable de entorno del sistema
```shell
ffmpeg -version
```