# <h1 align=center> **`Proyecto de Machine Learning Operations (MLOps)`** </h1>

## **Breve descripción**
Este proyecto tiene como objetivo crear un sistema de recomendación de películas y llevarlo al mundo real a través de una API. Además, se realizará transformaciones, un análisis exploratorio de los datos y se entrenará un modelo de machine learning para armar el sistema de recomendación.

## **Contexto**
Imagina que trabajas como Data Scientist en una start-up que provee servicios de agregación de plataformas de streaming. Tu objetivo es crear un sistema de recomendación de películas que aún no ha sido puesto en marcha. Sin embargo, te das cuenta de que los datos están poco maduros y necesitas hacer un trabajo rápido de Data Engineer para tener un MVP en una semana.

## **Propuesta de trabajo**
Para este proyecto, deberás realizar las siguientes tareas:

## **Transformaciones** [link](https://github.com/LionelMc/PI_ML_OPS_Project/blob/main/Transformaciones.ipynb)
Realizar las siguientes transformaciones a los datos:
+ Desanidar algunos campos, como **`belongs_to_collection`**, **`production_companies`** y otros.
+ Rellenar los valores nulos de los campos **`revenue`** y **`budget`** con el número **`0`**.
+ Eliminar los valores nulos del campo **`release date`**.
+ Dar formato **`AAAA-mm-dd`** a las fechas y crear la columna **`release_year`**.
+ Crear la columna **`return`** con los campos **`revenue`** y **`budget`**, dividiendo estas dos últimas **`revenue / budget`**.
+ Eliminar las columnas que no serán utilizadas, **`video`**,**`imdb_id`**,**`adult`**,**`original_title`**,**`vote_count`**,**`poster_path`** y **`homepage`**.

## **Desarrollo API**
Disponibilizar los datos de la empresa usando el framework FastAPI. Las consultas que propones son las siguientes:
+ **`peliculas_mes(mes)`**: Retorna la cantidad de películas que se estrenaron en un mes históricamente.
+ **`peliculas_dia(dia)`**: Retorna la cantidad de películas que se estrenaron en un día de la semana históricamente.
+ **`franquicia(franquicia)`**: Retorna la cantidad de películas, ganancia total y promedio de una franquicia.
+ **`peliculas_pais(pais)`**: Retorna la cantidad de películas producidas en un país.
+ **`productoras(productora)`**: Retorna la ganancia total y la cantidad de películas que produjo una productora.
+ **`retorno(pelicula)`**: Retorna la ganancia total y la cantidad de peliculas que produjeron.
+ **`recomendacion(titulo)`**: Recomienda 5 películas similares a una película dada.

## **Deployment**
La API será deployada en el servicio de Render para que pueda ser consumida desde la web. 
Listamos los los siguientes endpoints:  peliculas_mes('enero')
+ Request 1: [peliculas_mes('enero')](https://pi-ml-ops-p8ot.onrender.com/peliculas_mes/enero)
+ Request 2: [peliculas_dia('lunes')](https://pi-ml-ops-p8ot.onrender.com/peliculas_dia/lunes)
+ Request 3: [franquicia('Toy Story Collection')](https://pi-ml-ops-p8ot.onrender.com/franquicia/Toy%20Story%20Collection)
+ Request 4: [peliculas_pais('Brazil')](https://pi-ml-ops-p8ot.onrender.com/peliculas_pais/Brazil)
+ Request 5: [productoras('Pixar Animation Studios')](https://pi-ml-ops-p8ot.onrender.com/productoras/Pixar%20Animation%20Studios)
+ Request 6: [retorno('Jumanji')](https://pi-ml-ops-p8ot.onrender.com/retorno/Jumanji)
+ Request 7: [recomendacion('Sabrina')](https://pi-ml-ops-p8ot.onrender.com/recomendacion/Sabrina)

## **Análisis exploratorio de los datos** [link] (https://github.com/LionelMc/PI_ML_OPS_Project/blob/main/EDA.ipynb)
Realizar un análisis exploratorio de los datos para investigar las relaciones entre las variables de los datasets, ver si hay outliers o anomalías, y ver si hay algún patrón interesante que valga la pena explorar en un análisis posterior.

## **Sistema de recomendación** [link](https://github.com/LionelMc/PI_ML_OPS_Project/blob/main/Modelo_ML.ipynb)
Entrenar un modelo de machine learning para armar un sistema de recomendación de películas. El sistema consiste en recomendar películas a los usuarios basándose en películas similares. Debe ser deployado como una función adicional de la API.

## **Video** [link]()
Realizar un video mostrando el resultado de las consultas propuestas y del modelo de machine learning entrenado.

## **Conclusión**
+ Mediante la implementación de la metodología MLOps, se logró desarrollar un sistema de recomendación de películas que ofrece consultas rápidas y precisas a través de una API basada en FastAPI.
+ El proceso de transformación de los datos, permitió resolver los desafíos de datos anidados, valores nulos y formato de fechas, generando un conjunto de datos limpios y coherentes.
+ El análisis exploratorio de los datos reveló relaciones interesantes entre las variables, identificó posibles patrones y proporcionó información valiosa para el sistema de recomendación.
+ La implementación de un modelo de machine learning para el sistema de recomendación permitió identificar películas similares y ofrecer recomendaciones personalizadas a los usuarios, basadas en la similitud de puntuación entre las películas.
+ El despliegue exitoso de la API en una plataforma como Render permitió que el sistema de recomendación fuera accesible y consumible desde la web, brindando una experiencia fluida y satisfactoria para los usuarios.
