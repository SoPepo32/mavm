el formato mvam es un contenedor de video basado en mkv, 7zip y json capaz de contener los archivos de menus y vaios videos con sus pistas de audio y subtitulos

el archivo por defecto de ejecucion es el start.json ubicado dentro del archivo comprimido del contenedor que es un 7zip renombrado con la extencio .mavm (matroska video menu) los comandos de los menus son

"start": [
<comandos>
]
donde se ejecutan los comandos al iniciar el video

despues est

"loop":[
<comandos>
]
donde los comandos se ejecutan en bucle permanente hasta cerrar el video

{"menu": ["create", "menu1"]}
este comando crea el contenedor del menu
