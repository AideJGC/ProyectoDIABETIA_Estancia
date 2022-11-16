# ProyectoDIABETIA_Estancia
### Estancia de investigación Maestría Ciencia de Datos
##### Aide Jazmín González Cruz

## :large_blue_circle: Tabla de contenido

1. [Introducción](https://github.com/AideJGC/ProyectoDIABETIA_Estancia/blob/main/README.md#introducci%C3%B3n-clipboard) :clipboard:
2. [Información general](https://github.com/AideJGC/ProyectoDIABETIA_Estancia/blob/main/README.md#informaci%C3%B3n-general-bookmark_tabs) :bookmark_tabs:
3. [Requerimientos de infraestructura](https://github.com/AideJGC/ProyectoDIABETIA_Estancia/blob/main/README.md#requerimientos-de-infraestructura-computer) :computer:
4. [Instalación](https://github.com/AideJGC/ProyectoDIABETIA_Estancia/blob/main/README.md#instalaci%C3%B3n-minidisc) :minidisc:
5. [Organización del código](https://github.com/AideJGC/ProyectoDIABETIA_Estancia/blob/main/README.md#organizaci%C3%B3n-del-c%C3%B3digo-octocat) :octocat:
6. [Correr el programa](https://github.com/AideJGC/ProyectoDIABETIA_Estancia/blob/main/README.md#correr-el-programa-green_circle) :green_circle:

## Introducción :clipboard:

El IMSS es un organismo descentralizado del Gobierno Federal Mexicano sectorizado a la Secretaría de Salud, que tiene por objeto organizar y administrar el Seguro Social, cuya finalidad es garantizar el derecho a la salud, la asistencia médica, la protección de los medios de subsistencia y los servicios sociales necesarios para el bienestar individual y colectivo, la población que cuenta con afiliación al instituto se les denomina derechohabientes.

Entre algunas de las tareas que tiene el IMSS está el desarrollo de investigación en salud y dirigir los procesos de promoción a la salud, prevención y detección de enfermedades. Bajo este marcó el IMSS tiene diversos Centros o unidades de investigación en el país, uno de ellos es el Centro de Investigación Biomédica (CIB) de Michoacán que actualmente tiene el proyecto denominado “DiabetIA”, cuyo objetivo es hacer un estudio longitudinal para el desarrollo de modelos predictivos de complicaciones crónicas de la Diabetes Mellitus tipo 2 (DM2).

La diabetes mellitus y la hipertensión arterial se han posicionado como la principal causa de gasto médico para el IMSS desde hace más de una década. En 2021 el número de pacientes atendidos por diabetes mellitus fue de 3.1 millones, y de  hipertensión arterial de 4.8 millones.2 Además la diabetes mellitus se ha convertido en la principal causa de muerte seguido de las cardiopatías, enfermedades cerebrovascular e hipertensivas. Por los que es importante establecer mecanismos de prevención, poder minimizar a tiempo el daño orgánico del paciente y evitar así un deceso. 

El objetivo  en este proyecto fue crear un modelo para determinar que pacientes con DM2 tendrán hipertensión arterial (HTA) como complicación el siguiente año. 

## Información general :bookmark_tabs:

Se trabajo con 2 archivos que se unificaron para construir una base inicial a partir de los siguientes archivos:

1. **Muestra.csv**: conformada por los siguientes campos.

| Variable | Tipo  | Descripción |
| :------- | :----:| :---------: |
|newid |Number|Identificador de la consulta|
|cx_curp |Text|CURP anonimizada del paciente|
|nota_medica |Text|Nota médica del paciente|
|glucosa |Number| Glucosa separada por un pipe, donde la primera medición es antes de tomar alimentos y la segunda después de alimentos. |
|colesterol |Text|Dato de colesterol |
|trigliceridos|Text|Dato de trigliceridos|
|hdl|Text|Dato de hdl|
|ldl|Text|Dato de ldl|
|fecha|Text|Fecha recuperada por algoritmo NER|
|presion_arterial|Number|Presión arterial sistolica y diastolica|
|hba1c|Floating Timestamp|Dato de la hemoglobina glucosilada|
|hipertension|Text|Texto de hipertensión encontrado por NER|
|plaquetas|Text|Dato de plaquetas|
|creatinina|Text|Dato de creatinina|
|acido_urico|Number|Dato de ácido urico|
|urea|Number|Dato de urea|
|peso|Location|Peso del paciente|
|altura|Location|Altura del paciente|
|tfg|Number|Dato de tfg|
|imc|Number|Dato de IMC|
|año_de_diagnostico_diabetes|Number|Año de diagnóstico de diabetes|
|año_de_diagnostico_hipertensión|Number|Año de diagnóstico de hipertensión seún el algoritmo NER|
|fechas_procesadas|Number|Dato defecha encontrada por algorimo NER|
|bandera_fechas_procesadas|Number|Si la fecha procesada es correcta o esta sucia|
|fuente|Text|Fuente de datos|
|in_consulta|Number|Identificador de la consulta|
|fecha_nacimiento|Objeto|Fecha de nacimieno del paciente|
|sexo|Objeto|Sexo del paciente|
|medicamentos|Text|Medicamentos preescritos al paciente en la consulta|
|codigos_cie|Objeto|Diagnósticos en Código CIE asignados al paciente en su consulta|
|diagnosticos|Objeto|Diagnósticos en texto asignados al paciente en su consulta|
|fecha_consulta|Date|Fecha de la consulta|

2. [NewHypertensionList.csv](https://github.com/AideJGC/ProyectoDIABETIA_Estancia/blob/main/data/NewHypertensionList.csv): conformada por los siguientes campos.

| Variable | Tipo  | Descripción |
| :------- | :----:| :---------: |
|cx_curp |Text|CURP anonimizada del paciente|
|FechaNuevaHipertension|Date|Nueva fecha evaluando medicamento hipertensivo, diagnóstico o mediciones de presión arterial|
|MedicamentoCodigo |Text|Código del medicamento|
|MedicamentoNombre |Text| Nombre del medicamento |
|Presion |Text|*No especificado* |

de los cuales sólo se tomo *cx_curp* para cruzar con el archivo **Muestra.csv** y recuperar la *FechaNuevaHipertension*. El archivo **Muestra.csv** se dividio en [Muestra_TT.csv](https://github.com/AideJGC/ProyectoDIABETIA_Estancia/blob/main/data/Muestra_TT.csv) para entrenamiento y test,  y [Muestra_V.csv](https://github.com/AideJGC/ProyectoDIABETIA_Estancia/blob/main/data/Muestra_V.csv) para validación. Quedando con la siguiente estructura:

| Variable | Tipo  | Descripción |
| :------- | :----:| :---------: |
|newid |Number|Identificador de la consulta|
|cx_curp |Text|CURP anonimizada del paciente|
|nota_medica |Text|Nota médica del paciente|
|glucosa |Number| Glucosa separada por un pipe, donde la primera medición es antes de tomar alimentos y la segunda después de alimentos. |
|colesterol |Text|Dato de colesterol |
|trigliceridos|Text|Dato de trigliceridos|
|hdl|Text|Dato de hdl|
|ldl|Text|Dato de ldl|
|fecha|Text|Fecha recuperada por algoritmo NER|
|presion_arterial|Number|Presión arterial sistolica y diastolica|
|hba1c|Floating Timestamp|Dato de la hemoglobina glucosilada|
|hipertension|Text|Texto de hipertensión encontrado por NER|
|plaquetas|Text|Dato de plaquetas|
|creatinina|Text|Dato de creatinina|
|acido_urico|Number|Dato de ácido urico|
|urea|Number|Dato de urea|
|peso|Location|Peso del paciente|
|altura|Location|Altura del paciente|
|tfg|Number|Dato de tfg|
|imc|Number|Dato de IMC|
|año_de_diagnostico_diabetes|Number|Año de diagnóstico de diabetes|
|año_de_diagnostico_hipertensión|Number|Año de diagnóstico de hipertensión seún el algoritmo NER|
|fechas_procesadas|Number|Dato defecha encontrada por algorimo NER|
|bandera_fechas_procesadas|Number|Si la fecha procesada es correcta o esta sucia|
|fuente|Text|Fuente de datos|
|in_consulta|Number|Identificador de la consulta|
|fecha_nacimiento|Objeto|Fecha de nacimieno del paciente|
|sexo|Objeto|Sexo del paciente|
|medicamentos|Text|Medicamentos preescritos al paciente en la consulta|
|codigos_cie|Objeto|Diagnósticos en Código CIE asignados al paciente en su consulta|
|diagnosticos|Objeto|Diagnósticos en texto asignados al paciente en su consulta|
|fecha_consulta|Date|Fecha de la consulta|
|FechaNuevaHipertension|Date|Nueva fecha evaluando medicamento hipertensivo, diagnóstico o mediciones de presión arterial|

Dicha base de datos corresponde a una muestra de 55 pacientes con su historial médico, generando un total de 9315 registros, y 33 columnas.

El campo **fuente** tiene los siguientes valores:

- corhis_somatometria: datos de somatrometría
- exphis_hc_diabetes: datos provenientes de expediente histórico
- NER: datos recuperador con un modelo de aprendizaje automático denominado NER, que es una forma de procesamiento del lenguaje natural (NLP), donde se realiza la detección de entidades y categorización de las mismas. Esta tarea fue realizada por un alumno de la Licenciatura de Tecnologías para la Información en Ciencias en la Escuela Nacional de Estudios Superiores Unidad Morelia. 
   
   
#### Pregunta analítica a contestar con el modelo predictivo

Con este proyecto se piensa contestar la siguiente pregunta:

- ¿El paciente con DM2 el siguiente año tendrá o no hipertención arterial?

#### Frecuencia de actualización de los datos

- La frecuencia de datos fuente es diaria, sin embargo en en este proyecto se usó una muestra.

## Requerimientos de infraestructura. :computer:

El presente proyecto se elaboró en una laptop con sistema operativo ubuntu 20.04, 6GB en RAM y 750 GB en disco duro.

## Instalación :minidisc:

### Requerimientos

Para usar el modelo se puede hacer vía clonación de git hub o bien con el uso del Docker.

### Vía vía clonación de git hub

1. **Clonar el repositorio**

- Para comenzar deberá [instalar la librería de git](https://github.com/git-guides/install-git), para ello puede seguirlos pasos descritos en esta página.

- Clonar el repositorio https://github.com/AideJGC/ProyectoDIABETIA_Estancia en su máquina elegida.

```
git clone https://github.com/AideJGC/ProyectoDIABETIA_Estancia
```

2. **Ambiente virtual**

- Deberá instalar [pyenv](https://github.com/pyenv/pyenv), para configurar un ambiente virtual [pyenv-virtualenv](https://github.com/pyenv/pyenv-virtualenv) con python superior o igual a 3.7.4., al cual podra acceder con el siguiente comando como ejemplo: 

```
pyenv activate nombre_de_tu_ambiente
```

3. **Librerías**

- Una vez dentro del ambiente instalar los paquetes descritos en el archivo requirements.txt con el siguiente comando:

```
pip install -r requirements.txt
```

4. Moverse a la carpeta src/biabetia_hta

```
cd src/diabetia_hta/
```


### Docker

1. **Instalación**

- [Instale Docker](https://docs.docker.com/engine/install/ubuntu/) en su computadora, en este link encontrará como instalarse en ubuntu, pero vienen instrucciones para otras distribuciones.

2. **Bajar imagen y ejecutar**

- Ejecute el siguiente comando para bajar la imagen de Docker y correr desde línea de comandos:

```
docker run -it --rm --entrypoint /bin/bash 4id3jgc/docker_diabetia_hta:0.1
```


## Organización del código :octocat:


El repositorio se encuentra organizado de la siguiente manera:

```
├── README.md          <- The top-level README for developers using this project.
│
├── .github/workflows  <- Action for docker
│
├── notebooks          <- Jupyter notebooks.
│
├── data               <- Data and folder to save information.
│
├── dockerfiles        <- Code to create docker
│
├── output             <- Output from run code
│
├── requirements.txt   <- The requirements file
│
├── setup.py
│
└── src                <- Source code for use in this project.
    ├── __init__.py    <- Makes src a Python module
    │
    ├── utils          <- Functions used across the project
    │    
    ├── pipeline       <- Scripts to transform, modeling and predict data
    │
    ├── diabetia_hta   <- Main scripts to run app

```


## Correr el programa :green_circle:

Hay 2 opciones para correr el programa una vez instalado, ya sea vía Git hub o Docker. Este programa se corre vía línea de comendos, donde realiza tareas dependiendo de los parámetros que se le asignen:

- Primer parámetro corresponde a tarea a realizar: Entrenamiento (1) o predicción (2).
- Segundo parámetro corresponde al archivo de dato sobre el cuál ejecutará la cción.
- Tercer parámetro corresponde a la ventana a trabajar: 2 años (1) o 3 meses (2).

***EJEMPLOS***

1. **Entrenamiento**

Para entrenar ejecutar el comando:

```
python3 diabetia_hta.py 1 "../../data/Muestra_TT.csv" 1
```

Donde:

- El primer parámetro 1 (1) es la opción de la tarea,en este caso entrenamiento, el archivo *"../../data/Muestra_TT.csv"* son los datos con los que se sacará el modelo, con ventana a 2 años.

2. **Predicción**

```
python3 diabetia_hta.py 2 "../../data/Muestra_V.csv" 1
```

Donde el parámetro 3 (2) es la opción de la tarea,en este caso predicción, el archivo *"../../data/Muestra_V.csv"* son los datos a predecir, con con ventana a 2 años.
