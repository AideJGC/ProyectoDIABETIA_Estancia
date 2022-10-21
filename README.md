# ProyectoDIABETIA_Estancia
### Estancia de investigación Maestría Ciencia de Datos
##### Aide Jazmín González Cruz

## :large_blue_circle: Tabla de contenido

1. [Introducción]() :clipboard:
2. [Información general]() :bookmark_tabs:
3. [Requerimientos de infraestructura]() :computer:
4. [Instalación]() :minidisc:
5. [Organización del código]( :octocat:
6. [Correr el pipeline]() :green_circle:
7. [Predicciones y visualización]() :bar_chart:

## Introducción :clipboard:

El presente proyecto esta enfocado a apoyar en la predicción temprana de los pacientes con Diabetes Mellitus del Instituto Méxicano del Seguro Social, en particular de la OOAD de Michoacán que tendran como comorblidad Hipertensión arterial el próximo año.

## Información general :bookmark_tabs:

Se trabajo con una base generada por 3 fuentes de datos:

Y los datos con los que se trabajó tienen las siguientes características:

- Número de registros: **55**
- Número de columnas: **33**
- Diccionario de datos:
 
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
|fecha|Text|  |
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
|bandera_fechas_procesadas||Si la fecha procesada es correcta o esta sucia|
|fuente||Fuente de datos|
|in_consulta||Identificador de la consulta|
|fecha_nacimiento||Fecha de nacimieno del paciente|
|sexo||Sexo del paciente|
|bandera_fechas_procesadas||Si la fecha procesada es correcta o esta sucia|
|medicamentos||Medicamentos preescritos al paciente en la consulta|
|codigos_cie||Diagnósticos en Código CIE asignados al paciente en su consulta|
|diagnosticos|Diagnósticos en texto asignados al paciente en su consulta|
|fecha_consulta||Fecha de la consulta|
|FechaNuevaHipertension||Nueva fecha evaluando medicamento hipertensivo, diagnóstico o mediciones de presión arterial|
    
   
#### Pregunta analítica a contestar con el modelo predictivo

Con este proyecto se piensa contestar la siguiente pregunta:

- ¿El paciente el siguiente año tendrá o no hipertención arterial?

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

- Instale Docker en su computadore usando la siguiente instrucción:

```
comandp
```

2. **Bajar imagen y ejecutar**

- Ejecute el comendo para bajar la imagen de Docker y correr en línea de comandos:

```
docker run -it --rm --entrypoint /bin/bash 4id3jgc/docker_diabetia_hta:0.1
```


El repositorio se encuentra organizado de la siguiente manera:

```
├── README.md          <- The top-level README for developers using this project.
│
├── docs               <- Space for Sphinx documentation
│
├── notebooks          <- Jupyter notebooks.
│
├── references         <- Data dictionaries, manuals, and all other explanatory materials.
│
├── results            <- Intermediate analysis as HTML, PDF, LaTeX, etc.
│
├── requirements.txt   <- The requirements file
│
├── .gitignore         <- Avoids uploading data, credentials, outputs, system files etc
│
├── infrastructure
│
├── setup.py
└── src                <- Source code for use in this project.
    ├── __init__.py    <- Makes src a Python module
    │
    ├── utils      <- Functions used across the project
    │
    │
    ├── etl       <- Scripts to transform data from raw to intermediate

```


## Correr el programa :green_circle:

Hay 2 opciones para correr el programa una vez instalado, ya sea vía Git hub o Docker:

1. **Entrenamiento**

Para entrenar ejecutar el comando

```
python3 diabetia_hta.py 1 "../../data/Muestra_TT.csv"
```

Donde el parpametro 3 (1) es la opción de la tarea,en este caso entrenamiento y el archivo "../../data/Muestra_TT.csv" son los datos con los que se sacará el modelo.

2. **Predicción**

```
python3 diabetia_hta.py 2 "../../data/Muestra_V.csv"
```

Donde el parpametro 3 (2) es la opción de la tarea,en este caso predicción y el archivo "../../data/Muestra_V.csv" son los datos a predecir.
