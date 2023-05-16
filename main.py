from fastapi import FastAPI
import pandas as pd
import numpy as np


# Crear la aplicación FastAPI
app = FastAPI()
df = pd.read_csv('df_modificada.csv', low_memory=False)

# Definir los endpoints de la API

# Q1
@app.get('/peliculas_mes/{mes}')
async def peliculas_mes(mes: str):
    """
    Otener la cantidad de películas que se estrenaron en un determinado mes.\n
    Ejemplo  ===>  mes: enero
    """
    meses_dict = {
        'enero': '01',
        'febrero': '02',
        'marzo': '03',
        'abril': '04',
        'mayo': '05',
        'junio': '06',
        'julio': '07',
        'agosto': '08',
        'septiembre': '09',
        'octubre': '10',
        'noviembre': '11',
        'diciembre': '12'
    }
    mes_numerico = meses_dict.get(mes.lower())
    if mes_numerico is None:
        return {'error': 'Mes inválido'}
    
    cantidad = df[df['release_date'].str[5:7] == mes_numerico].shape[0]
    return {'mes': mes, 'cantidad': cantidad}
#peliculas_mes('enero')

# Q2
@app.get('/peliculas_dia/{dia}')
async def peliculas_dia(dia: str):
    """
    Obtener la cantidad de películas que se estrenaron en un determinado día.\n
    Ejemplo  ===>  dia: lunes
    """
    dias_dict = {
        'lunes': 0,
        'martes': 1,
        'miércoles': 2,
        'miercoles': 2,  # Añadida una opción adicional sin acento
        'jueves': 3,
        'viernes': 4,
        'sábado': 5,
        'sabado': 5,  # Añadida una opción adicional sin acento
        'domingo': 6
    }
    dia_numerico = dias_dict.get(dia.lower())
    if dia_numerico is None:
        return {'error': 'Día inválido'}
    
    df['release_date'] = pd.to_datetime(df['release_date'])
    cantidad = df[df['release_date'].dt.dayofweek == dia_numerico].shape[0]
    return {'dia': dia, 'cantidad': cantidad}
#peliculas_dia('lunes')

# Q3
@app.get('/franquicia/{franquicia}')
async def franquicia(franquicia: str):
    """
    Obtener la cantidad de películas, ganancia total y promedio de una franquicia.\n
    Ejemplo  ===>  franquicia: Toy Story Collection
    """
    franquicia_df = df[df['belongs_to_collection'].apply(lambda x: franquicia in x)]
    cantidad = franquicia_df.shape[0]
    ganancia_total = franquicia_df['revenue'].sum()
    ganancia_promedio = franquicia_df['revenue'].mean()
    return {'franquicia': franquicia, 'cantidad': cantidad, 'ganancia_total': ganancia_total, 'ganancia_promedio': ganancia_promedio}
#franquicia('Toy Story Collection')

# Q4
@app.get('/peliculas_pais/{pais}')
async def peliculas_pais(pais: str):
    """
    Obtener la cantidad de películas producidas en un determinado país.\n
    Ejemplo  ===>  pais: Brazil
    """
    cantidad = df[df['production_countries'].apply(lambda x: pais in x)].shape[0]
    return {'pais': pais, 'cantidad': cantidad}
#peliculas_pais('Brazil')

# Q5
@app.get('/productoras/{productora}')
async def productoras(productora: str):
    """
    Obtener la ganancia total y la cantidad de películas producidas por una determinada productora.\n
    Ejemplo  ===>  productora: Pixar Animation Studios
    """
    productora_df = df[df['production_companies'].apply(lambda x: productora in x)]
    ganancia_total = productora_df['revenue'].sum()
    cantidad = productora_df.shape[0]
    return {'productora': productora, 'ganancia_total': ganancia_total, 'cantidad': cantidad}
#productoras('Pixar Animation Studios')

# Q6
@app.get('/retorno/{pelicula}')
async def retorno(pelicula: str):
    """
    Obtener la inversión, ganancia, retorno y año de una determinada película.\n
    Ejemplo  ===>  pelicula: Jumanji
    """
    # Reemplazar los valores nulos por una cadena vacía en la columna "title"
    df_cleaned = df.fillna({'title': ''})

    pelicula_df = df_cleaned[df_cleaned['title'].str.contains(pelicula)]
    inversion = pelicula_df['budget'].iloc[0]
    ganancia = pelicula_df['revenue'].iloc[0]
    retorno = pelicula_df['return'].iloc[0]
    anio = pelicula_df['release_year'].iloc[0]
    return {'pelicula': pelicula, 'inversion': inversion, 'ganancia': ganancia, 'retorno': retorno, 'anio': anio}
#retorno('Jumanji')

#########
import pandas as pd
from sklearn.preprocessing import MultiLabelBinarizer
from sklearn.neighbors import NearestNeighbors
from sklearn.impute import SimpleImputer
import numpy as np

# Cargar los datos
data = pd.read_csv('df_modelo.csv')

# Seleccionar un subconjunto aleatorio de los datos
np.random.seed(42)
idx = np.random.choice(data.index, size=15000, replace=False)
data = data.loc[idx]

# Preprocesar los datos
mlb = MultiLabelBinarizer()
genres = pd.DataFrame(mlb.fit_transform(data['genres']), columns=mlb.classes_)
languages = pd.DataFrame(mlb.fit_transform(data['spoken_languages']), columns=mlb.classes_)
X = pd.concat([genres, languages, data['vote_average']], axis=1)

# Imputar los valores NaN en la matriz X
imputer = SimpleImputer(strategy='mean')
X = imputer.fit_transform(X)

# Entrenar el modelo
model = NearestNeighbors(n_neighbors=6, algorithm='ball_tree')
model.fit(X)

# Q7
@app.get('/recomendacion/{titulo}')
async def recomendacion(titulo: str):
    """
    Ingresar el nombre de pelicula y te recomienda las similares en una lista de 5 valores.\n
    Ejemplo  ===>  pelicula: Sabrina
    """
    # Encontrar el índice de la película
    idx = data[data['title'] == titulo].index[0]

    # Encontrar las películas más similares
    distances, indices = model.kneighbors(X[idx].reshape(1, -1))

    # Crear la lista de recomendaciones
    recomendaciones = []
    for i in range(1, len(distances.flatten())):
        recomendaciones.append(data.iloc[indices.flatten()[i]]['title'])

    return {'Lista recomendada': recomendaciones}

#recomendacion('Sabrina')


