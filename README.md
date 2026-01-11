<h1>MaVM</h1>

## English:

## The MAVM format is a video container based on MKV and JSON, capable of holding menu files and multiple videos with their audio tracks and subtitles.

Player for the format: [SoPepo32/reproductormavm](https://github.com/SoPepo32/reproductormavm)

link for FMaVM: [SoPepo32/fmavm](https://github.com/SoPepo32/fmavm)

The default execution file is start.json, located within the file with the .mavm extension (Matroska Video Menu).

## .mavm file format:
```MaVM
-++<filename_including_extension>+--<file_contained_in_binary_format>
```
and repeats for each file

## The menu commands are (Every time you write a command, you must include all parameters unless it is specified that the parameter is optional):

"start": [
-commands-
]
where the commands are executed when the video starts.

Then there is:

"loop": [
-commands-
]
where the commands are executed in a continuous loop until the video closes or the menu changes.

{"menu": ["create", -menu_name-]}
This command creates the menu container.

{-menu_name-: [-command-]}
This indicates that the command inside the square brackets [] will be executed.

{"resolution": [-x_axis_resolution-,-y_axis_resolution-]}
This command defines the size of the coordinates. These are not pixels; they are coordinates that indicate the level of detail in the coordinates, avoiding decimals.

{"image": [-create/edit-,-id_of_the_image_to_create_or_edit-, "coordinates",-start_x_axis_coordinates-,-start_y_axis_coordinates-,-end_x_axis_coordinates-, -image_location_within_the_container-]}
This command is for setting Images

{"button": [-create/edit-,-id_of_the_button_to_create_or_edit-, "coordinates",-start_x_axis_coordinate-,-start_y_axis_coordinate-,-end_x_axis_coordinate-,-end_y_axis_coordinate-, "title",-button_title-, "color",[-red_rgb_color-,-green_rgb_color-,-blue_rgb_color-], "command_click",[-command_to_execute_on_click-], "command4selection",-command_to_execute_on_selection-, "command4no_selection",-command_to_execute_on_de-selection-]}
This command is for creating buttons that allow you to execute another command (or commands if they are between --> []) when clicked. When selected and when deselected. The parameters ""command_click",-command_to_execute_on_click-", ""command4selection",-command_to_execute_on_selection- and ""command4no_selection",-command_to_execute_on_deselection- are optional.

{"teleport":[-location_of_file_to_teleport]}
The teleport command teleports you to another menu or a video. If you want to teleport to more than one video, place the locations you want to teleport to inside the brackets, in order. The first item listed is the first item you teleport to, and the last item is the final item you teleport to. If you use it to teleport to a video, you can (optionally) specify the part of the video to which you teleport using ["-hour:minutes:seconds-","-hour:minutes:seconds-"], where the first value is the starting point and the second value is the ending point. For example... Usage: {"teleport":["video.mkv", ["00:00:05.5000","00:00:30.0000"]]} Here, only seconds 5.5 to 30 are played. Yes, you have to include all zeros and decimal places even if you're not using minutes and hours. If the hours are more than 99 (unlikely), just use "-100:minutes:seconds-" (replacing 100 with the hours). I hope this clarifies that hours can have as many digits as you need, but they can't be less than two. If it's one hour, use 01; if it's 10, use 10; and if it's 100, use 100. If you want to set a default video, audio, and/or subtitle track when entering the video, you have to add the following after the video you want to teleport to. [-video_track-,-audio_track-,-subtitle_track-] example [0,0,null] null if you don't want any subtitle track if you want one by 0 or the track number that is the subtitle track you want to put, if you also want to put a start and end point you have to put ["-hour:minutes:seconds-","-hour:minutes:seconds-", 0,0,null] in the same list.

{"video":[-create/edit-,-id_of_video_to_create_or_edit-, "coordinates", -start_x_coordinate-, -start_y_coordinate-, -end_x_coordinate-, -end_y_coordinate-, "video_path",-video_location_within_container-]}
This command allows you to place videos within a menu that will start automatically when the menu is accessed. It won't wait for the video to finish before executing the next command; it will execute both simultaneously.

{"video":[-create/edit-,-id_of_video_to_create_or_edit-, "coordinates",-start_x_axis_coordinate-,-start_y_axis_coordinate-,-end_x_axis_coordinate-,-end_y_axis_coordinate-, "video_path",-location_of_video_within_the_container-]}
This command allows you to place videos within a menu that will start automatically when you enter the menu. It won't wait for the video to finish before executing the next command; it will run simultaneously.

{"time": ["wait",-wait_time-,-seconds/minutes/hours-]}
This command is the only one (when I wrote this, it no longer is) that executes outside of a command like "{-menu_name-: [-command-]}" It is used to wait "x" time until the next command

{"button_default":[-button_id-]}
This command allows you to set a button as the default button selected when entering the menu.

{"sound":["create",-sound_id-, -sound_to_play-, "volume",-sound_volume_from_1_to_100-]}
This command allows you to play sounds when, for example, a button is pressed, and you can choose the volume.

{"sound":["edit",-sound_id-, "volume",-sound_volume_from_1_to_100-]}
This command allows you to edit the volume of a sound.

{"text":["create",-text_id- "coordinates", -start_x_axis_coordinates-, -start_y_axis_coordinates-, -end_x_axis_coordinates-, -end_y_axis_coordinates-, "text", -text-]}
This command is used to create text.

{"text":["edit", -id_of_text_to_edit- "coordinates", -start_x_axis_coordinates-, -start_y_axis_coordinates-, -end_x_axis_coordinates-, -end_y_axis_coordinates-, "text", -text-]}
This command is used to edit text.

{"ebook": ["create/edit", -page_id-, "epub_path", -epub_name_with_the_extension-, "page", -epub_page_to_import-, "coordinates", [ -start_x_coordinate-, -start_y_coordinate-, -end_x_coordinate-, -end_y_coordinate-]]}
This command allows you to import a page from an epub and place it as an image in the menu.

{"script": ["create", -script_name-]}
This command allows you to create a script within a menu and is written without {-menu_name-: [-command-]}, just like the time command.

## Let's move on to script commands (each time you write a command you must include all parameters unless it is specified that the parameter is optional):

(From here on, commands are written with {-script_name-: [{-command-}]})

{"variable": ["create", -variable_id-, "content", -variable_content-]}
With this command you can create a variable with its default value. Examples of possible variable contents: list, [0,1,3,1,-1,"hello:D"]; list of lists, [["hello:D",1],1,"hello:D"]; number, 137 and text, "hello:D"

{"variable:":["insert_value", -id_of_the_variable-]}
With this command you can insert the value of a variable as a parameter.
{"variable": ["edit", -id_de_la_variable-, "content", [{"script2":[{"variable:":["insert_value", "num"]}]}, "-", [-1, "+", 0, "*", 0]]]}
With this command you can edit the value of a variable and insert equations as shown there. The equation it's equivalent to is {"script2":[{"variable:":["insert_value", "num"]}]} - (-1 + 0*0), which is simply adding 1 since 0*0 is 0, -1 + 0 is -1, and - (-1) is +1. I only included that to give examples of many calculations, and yes, division is indicated with "/". The available symbols are "**"
for exponentiation,

for example, 3 squared "3**2"

or 3 cubed "3**3". For square root, use "//2", and for any other root, replace the 2 with its corresponding number. For example, cube root would be "//3". For square root, the square root of 9 would be 9//2. For division, use /, with the number being divided on the left and the divisor on the right. For multiplication, use *, using the same logic. For addition, use +. For subtraction, use -. And those are all the calculation symbols.

IMPORTANT! The number used and the symbol are not in the same string; they are separated. For example, [9, "//", 2], not ["9//2"]. The same applies to exponentiation, division, multiplication, addition, and subtraction; the numbers/variables are separated from the symbols.

IMPORTANT! If you want to create a list with predefined values, you must use double square brackets [[-values-]], otherwise it will be a calculation. Only if you initialize without predefined values ​​(i.e., an empty list) can you use brackets [], but [[]] is recommended for consistency in the menu code.

{"range": ["starting_value", -starting_value of the range-, "final_value", -final_value of the range-, "definition", -definition_value-, "output_variable", -output_variable-]}
This command allows you to store values ​​between two numbers in a variable. The definition is determined by the "definition" parameter, and the direction (whether to start with the highest or lowest value) is indicated with a negative number if it's from largest to smallest and with a positive number if it's from smallest to largest. "starting_value" should contain the starting value of the range, not the smallest.

{"folder_contents": ["folder", -folder_to_read_contents-, "output_variable", -output_variable-]}
This command allows you to obtain The contents of the project's main folder (using "/" for the "folder" parameter) or a folder within a .tar file (using the .tar logic defined later) are then placed into a previously defined variable as a list.

{"for": [["temporary_variable_for_output", "-variable_temporary", "content_list_variable", "-list_of_content_to_pass_through_the_temporary_variable-], [-commands_to_execute]]}
This command is the classic for loop. You define the name of the temporary variable (which doesn't need to be predefined), the variable containing the list to be passed, and the commands to execute.

{"if": [-variable_a-, "-type_of_comparison-", "variable_b-", "true", "-command_to_execute-", "false", "-command_to_execute-]}
This command is the conditional statement, allowing you to determine if a variable is true ("=="), false, or not. The `!="` operator determines whether a condition is greater than (>), less than (<), greater than or equal to (>=), or less than or equal to (<=") another variable. A command is executed if the condition is met (the `true` parameter) or false if it is not. If you don't want anything to be executed if the condition is met or not, use `["ignore"]` as the parameter for whether the condition is met or not (depending on your case). If you want more than one command to be executed if the condition is met or not, you must put all the commands inside square brackets.

## We finish with the commands

Images, buttons, and videos will be placed one on top of the other depending on which one was created first (editing is not taken into account for this). If command "x" is written before command "z" (as long as they are images, videos, buttons, text, ebooks, etc., otherwise, for example, if it's a teleport, the screen is cleared and the video/menu to which the teleport sends is displayed). The "z" command will be above the "x" command in the display.

The MaVM format does not support folders within its structure; instead, .tar files must be used.

To import a file from a .tar archive, you must type the .tar archive name followed by a colon (:) and the name of the internal file you want to access, for example, file.tar:file.png or file.tar:folder/file.mkv. Files can be placed inside folders within a .tar archive. What can be placed inside a .tar archive includes content folders, images, videos, audio, and menus.

## In the example file, the images, videos, and menus are organized within the same folder. You can do it differently, but it might complicate the teleport command.

File "metadata.json"

Example content:
```json
{
    "mavm_version": "v.4.0.0",
    "description": {
        "text": "example description"
        "duration": 3
    }
}
```

"mavm_version" is the MAVM version the file uses.
"description" is the file description, the data that will be displayed when the file is opened, along with the duration in seconds it will be displayed.

## Version naming:

v - version of large changes - version of small/medium changes - bug_corrections - corrections of the README.md. The example video (video_de_ejemplo.mavm) or the MAVM creator is not included in the "mavm_version" of the "metadata.json" file.

## License
All content in this repository is under GPL-3.0.

## Español:

## el formato mavm es un contenedor de video basado en mkv y json capaz de contener los archivos de menus y varios videos con sus pistas de audio y subtitulos

reproductor para el formato: [SoPepo32/reproductormavm](https://github.com/SoPepo32/reproductormavm)

Enlace para FMaVM: ​​[SoPepo32/fmavm](https://github.com/SoPepo32/fmavm)

El archivo de ejecución predeterminado es start.json, ubicado dentro del archivo con la extensión .mavm (Matroska Video Menu).

### Formato de archivo .mavm:
```MaVM
-++<nombre_de_archivo_incluida_la_extensión>+--<archivo_contenido_en_formato_binario>
```
y se repite para cada archivo

## los comandos de los menus son (cada que escribas un comando debes poner todos los parametros a no ser que se especifique que el parametro es opcional):

"start": [
-comandos-
]
donde se ejecutan los comandos al iniciar el video

despues esta

"loop":[
-comandos-
]
donde los comandos se ejecutan en bucle permanente hasta cerrar el video o cambiar el menu

{"menu": ["create", -nombre_del_menu-]}
este comando crea el contenedor del menu

{-nombre_del_menu-: [-comando-]}
esto indica que el comando se va a ejecutar que va dentro de los de los []

{"resolution": [-resolucion_eje_X-,-resolucion_eje_Y-]}
con este comando define el tamaño de las coordenadas, estas no son pixeles, solo son coordenadas que indican cuanta definicion en las coordendas hay, esto para evitar los decimales

{"image": [-create/edit-,-id_de_la_imagen_a_crear_o_editar-, "coordinates",-cordenada_eje_x_inicio-,-cordenada_eje_y_inicio-,-cordenada_eje_x_fin-,-cordenada_eje_y_fin-, -ubicacion_de_la_imagen_dentro_del_contenedor-]}
este comando es para poner imagenes

{"button": [-create/edit-,-id_of_the_button_to_create_or_edit-, "coordinates",-inicio_x_coordenada-,-inicio_y_coordenadas-,-final_x_coordenadas-,-final_y_coordenadas-, -title/image-,-title_del_boton/ubicacion_de_la_imagen_en_el_contenedor-, "color",[-red_rgb_color-,-green_rgb_color-,-blue_rgb_color-], "command_click",-command_to_execute_on_click-], "command4selection",-command_to_execute_on_selection-, "command4no_selection",-command_to_execute_on_deletion-}
Este comando permite crear botones que permiten ejecutar otro comando (o comandos si están entre --> []) al hacer clic, al seleccionar y al deseleccionar. Los parámetros "command_click", "command_to_execute_on_click", "command4selection", "command_to_execute_on_selection" y "command4no_selection", "command_to_execute_on_deselection" son opcionales.

{"teleport":[-ubicacion_del_archivo_a_teletransportar-]}
el comando teleport cumple la funcion de teletrasnportarte a otro menu o a un video, si quieres que te teletransporte a mas de un video por dentro de los corchetes los lugares a los que quieres que te teletransporte en orden siendo el primer objeto puesto es el primer objeto al que te teletransporta y el ultimo objeto es el ultimo al que teletransporta. si lo usas para teletransportarte a un video puede (opcional) establecer a que parte del video con ["-hora:minutos:segundos-","-hora:minutos:segundos-"] siendo el primer valor de donde empiezas y donde terminas el segundo valor ejemplo. de uso: {"teleport":["video.mkv", ["00:00:05.5000","00:00:30.0000"]]} aca solo se reproduce del segundo 5.5 al 30 y si, se tienen que poner los ceros y decimales completos aun que no se usen los minutos y horas, si las horas son mas de 99 (cosa poco probable) solo pones "-100:minutos:segundos-" (remplazas 100 por las horas) espero que con esta aclacion haya quedado claro que las horas pueden tener cuantos digitos necesites pero no puen ser menos de 2 si es una hora se pone 01 si son 10 se pone 10 y si son 100 se pone 100. si quieres establecer una pista de video, audio y/o subiutulo por defecto al entrar al video tienes que poner despues del video al que vas a teletransportarte [-pista_de_video-,-pista_de_audio-,-pista_de_subtitulo-] ejemplo [0,0,null] null si no quieres ninguna pista de subtitulo si quieres una por 0 o el numero de pista que sea la pista de subtitulo que quieres poner, si ademas quieres poner un punto de inicio y uno de final tienes que poner ["-hora:minutos:segundos-","-hora:minutos:segundos-", 0,0,null] en la misma lista.

{"video":[-create/edit-,-id_del_video_a_crear_o_editar-, "coordinates",-cordenada_eje_x_inicio-,-cordenada_eje_y_inicio-,-cordenada_eje_x_fin-,-cordenada_eje_y_fin-, "video_path",-ubicacion_del_video_dentro_del_contenedor-]}
este comando permite poner videos dentro de un menu que se iniciaran automaticamente al entrar al menu, no se esperara a que termine el video para ejecutar el siguiente comando, se hara a la vez

{"video":["edit",-id_del_video-, "restart"]}
este comando permite volver a iniciar el video, este comando no se puede volver a ejecutar con el mismo video hasta que el video haya terminado, porqué solo se puede resetear un video que ya haya terminado, no importa hace cuanto termino

{"time": ["wait",-tiempo_a_esperar-,-seconds/minutes/hours-]}
este comando es el unico (cuando escribi esto, ahora ya no) que se ejcuta fuera de un comando tipo "{-nombre_del_menu-: [-comando-]}" sirve para esperar "x" tiempo hasta el siguiente comando

{"button_default":[-id_del_boton-]}
este comando permite establecer un boton como el por defecto seleccionado al entrar al menu

{"sound":["create",-id_del_sonido-, -sonido_a_reproducir-, "volume",-volumen_del_sonido_del_1_al_100-]}
este comando permite ejecutar sonidos al, por ejemplo, presionar un boton pudiendo elegir el volumen

{"sound":["edit",-id_del_sonido-, "volume",-volumen_del_sonido_del_1_al_100-]}
este comando permite editar el volumen de un sonido

{"text":["create",-id_del_texto_a_crear- "coordinates",-cordenada_eje_x_inicio-,-cordenada_eje_y_inicio-,-cordenada_eje_x_fin-,-cordenada_eje_y_fin-, "text",-texto-]}
este comando sirve para crear un texto

{"text":["edit",-id_del_texto_a_editar- "coordinates",-cordenada_eje_x_inicio-,-cordenada_eje_y_inicio-,-cordenada_eje_x_fin-,-cordenada_eje_y_fin-, "text",-texto-]}
este comando sirve para editar un texto

{"ebook": ["create/edit",-id_de_la_pagina-, "epub_path",-nombre_del_epub_con_la_extencion-, "page",-pagina_del_epub_a_importar-, "coordinates",[-cordenada_eje_x_inicio-,-cordenada_eje_y_inicio-,-cordenada_eje_x_fin-,-cordenada_eje_y_fin-]]}
este comando permite importar una pagina de un epub y ponerla como una imagen en el menu

{"script": ["create", -nombre_del_script-]}
este comando permite crear un script dentro de un menu y se pone sin {-nombre_del_menu-: [-comando-]} al igual que el comando time

## pasamos a los comandos de los scripts (cada que escribas un comando debes poner todos los parametros a no ser que se especifique que el parametro es opcional):

(a partir de aqui los comandos se escriben con {-nombre_del_script-: [{-comando-}]})

{"variable": ["craate",-id_de_la_variable-, "content",-contenido_de_la_variable-]}
con este comando puedes crear una variable con su valor por defecto, ejemplos de contenidos que puede tener una variable; lista, [0,1,3,1,-1,"hola:D"]; lista de listas, [["hola:D",1],1,"hola:D"]; numero, 137 y texto, "hola:D"

{"variable:":["insert_value", -id_de_la_variable-]}
con este comando puedes insertar el valor de una variable como parametro

{"variable": ["edit", -id_de_la_variable-, "content", [{"script2":[{"variable:":["insert_value", "num"]}]}, "-", [-1, "+", 0, "*", 0]]]}
con este comando puedes editar el valor de una variable, y meter ecuaciones como se muestra ahi, la equacion a la que quivale es {"script2":[{"variable:":["insert_value", "num"]}]} - (-1 + 0*0) que es resumidamente sumarle 1 ya que el 0*0 es 0 -1 + 0 es -1 y - (-1) es +1 solo puse eso para poner ejemplos de muchos calculos, y si, la divicion se pone con "/". Ls simbolos disponibles son "**" para elevado,

siendo 3 al cuadrado "3**2" o

3 al cubo "3**3" para raiz cuadrada se usa "//2" y para cualquier otra raiz se cambia el 2 por su numero correspondiente ejemplo raiz cubica seria "//3" ejemplo de uso para raiz cuadrada raiz cuadrada de 9 se usaria 9//2
 para  division es con / siendo el numeor dividido a la izquierda y el divisor a la derecha
 para multiplicar se usa * misma logica
 para sumar +
 para restar -
 y esos son todos los simbolos de calculos

 IMPORTANTE! el numero que se usa y el simbolo no van en la misma cadena de texto, van separados, ejemplo [9, "//", 2], no ["9//2"]. igual con el elevado, division, multiplicacion, suma y resta; los numeros/variables van separadas de los simbolos

 IMPORTANTE! si quieres crear una lista con valores predefinidos hay que ponerla como [[-valores-]] doble corchete, porque si no lo pones asi seria un calculo, solo en caso de inicializar sin valores predefinidos o sea lista vacia puedes poner [] pero se recomienda [[]] para consistencia en el codigo del menu

{"range": ["starting_value",-valor_de_inicio_del_rango-, "final_value",-valor_de_final_del_rango-, "definition",-valor_de_la_definicion-, "output_variable",-variable_de_salida-]}
este comando permite poner los valor entre 2 numero en una variable, la definicion definida por el parametro "definition" y el sentido (si se emnpieza por el mas alto o el mas bajo) se indica con un numero negativo si es de mas grande a mas pequeño y con numero postivo si es de numero mas pequeño a mas grande ponidose en "starting_value" el valor con el que empieza el rango y no el mas pequeño

{"folder_contents": ["folder",-carpeta_a_leer_el_contenido-, "output_variable",-variable_de_salida-]}
este comando permite obtener el contenido de la carpeta principal del proyecto (poniendo "/" para el parametro "folder") o una carpeta dentro de un .tar (usando la logica de un .tar definida mas adelante) y ponerlo en una variable praviamente definida como lista

{"for": [["temporary_variable_for_output",-variable_temporal, "content_list_variable",-lista_del_contenido_a_pasar_por_la_variable_temporal-],[-comandos_a_ejecutar]]}
este comando es el clasico bucle for, estableces el nombre de la variable temporal (no que no hay que predefinir antes), la variable con la lista a pasar y los comandos a ejecutar

{"if": [-variable_a-,-tipo_de_comparacion-,-variable_b-, "true",-comando_a_ejecutar-, "false",-comando_a_ejecutar-]}
este comando es el condicional pudiendo determinar si una variable es ("==), no es "!=", o es mayor (">"), menor "(<"), mayor o igual (">=) o menor o igual ("<=") a otra variable y ejecutando un comando si se cumple (el parametro "true") o si no se cumple (el parametro "false") si no quieres que se ejcute nada en el caso de que se cumpla y/o no se cumpla la condicion pon un ["ignore"] como parametro de si se cumple o no se cumple (dependiendo tu caso) y si quieres que se ejcute mas de un comando si se cumple o no se cumple la condicion debes poner todos los comandos dentro de un []

## finalizamos con los comandos

las imagenes, botones y videos se pondran uno encima del otro dependiendo de cual este escrita su creacion primero (no se toma en cuenta la edicion para eso) si "x" comando se escribe antes que "z" comando (siempre y cuando sean imagenes, videos, botones, texto, ebook, etc, en caso contrario, por ejemplo sea un teleport se limpia la pantalla y se muestra el video/menu al que mando el teleport) "z" comando estara arriba de "x" comando en la visualizacion

El formato MaVM no admite carpetas dentro de su estructura; en su lugar, se deben utilizar archivos .tar.

Para importar un archivo desde un archivo .tar, debe escribir el nombre del archivo .tar seguido de dos puntos (:) y el nombre del archivo interno al que desea acceder, por ejemplo, file.tar:file.png o file.tar:folder/file.mkv. Los archivos se pueden colocar dentro de carpetas dentro de un archivo .tar. Entre los elementos que se pueden colocar dentro de un archivo .tar se incluyen carpetas de contenido, imágenes, vídeos, audio y menús.

## en el archivo de ejemplo las imagenes, videos y menus estan organizados dentro de una misma carpeta, puedes hacerlo distinto pero se te puede complicar el comando teleport


archivo "metadata.json"

contenido ejemplo:
```json
{
    "mavm_version": "v.4.0.0",
    "description": {
        "text": "example description"
        "duration": 3
    }
}
```

"mavm_version" es la version de mavm con la que trabaja el archivo
"descripcion" es la descripcion del archivo, datos que se mostraran al abrir el archivo junto al tiempo por el que se mostrara en segundos

## nombracion de versiones:

v.-version_de_cambios_grandes-.-version_de_cambios_pequeños/medianos-.-correccion_de_errores--correciones_del_README.md_el_video_de_ejemplo(video_de_ejemplo.mavm)_o_creador_mavm_no_se_incluye_en_"mavm_version"_de_"metadata.json-

## Licencia
Todo el contenido de este repositorio está bajo GPL-3.0.
