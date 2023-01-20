from fastapi import FastAPI, File, UploadFile
from fastapi.responses import HTMLResponse, StreamingResponse
from deta import Deta
from data import df_total_final as df
import pandas as pd
import requests

app = FastAPI()
deta = Deta("e0a36kkj_7bL719ZNRuMKGyfZF46NCW1h3czf39fV")  # configure your Deta project 
drive = deta.Drive("images") # access to your drive

@app.get("/", response_class=HTMLResponse)
def render():
    return """
    <form action="/upload" enctype="multipart/form-data" method="post">
        <input name="file" type="file">
        <input type="submit">
    </form> """
    

@app.post("/upload")
def upload_img(file: UploadFile = File(...)):
    name = file.filename
    f = file.file
    res = drive.put(name, f)
    return res

    # Cantidad de veces que aparece una keyword en el título de peliculas/series, por plataforma

@app.get("/get_word_count/{plataforma}/{keyword}")
def get_word_count(plataforma,keyword): 
    df_plat = df[(df['plataforma'] == plataforma)]
    word = df_plat['title'].str.contains(keyword)
    words = df_plat[word]
    count = words['title'].value_counts().sum()
    contador= count
    
    
    return f'En la plataforma {plataforma} hay {contador} películas con la palabra {keyword} en el título'



# Cantidad de películas por plataforma con un puntaje mayor a XX en determinado año


@app.get('/score_by_year/{plataforma}/{year}/{puntaje}')
def score_by_year(plataforma, year, puntaje):
    
    anio = df[(df['release_year'] == year) & (df['plataforma']== plataforma) & (df['score']==puntaje) & (df['type'] == 'movie')]
    cantidad = anio['title'].value_counts().sum()
    amount = cantidad
    
    return f'En el año {year} hubo {amount} películas con un puntaje mayor a {puntaje} en {plataforma}'

# La segunda película con mayor score para una plataforma determinada, según el orden alfabético de los títulos.

@app.get('/second_score/{plataforma}')
def second_score(plataforma):
    segunda = df[(df['plataforma'] == plataforma)]
    orden = segunda.sort_values('title')
    titulo = orden[['score','title']].nlargest(2, 'score').iloc[1]
    respuesta = titulo['title']
    ultima_respuesta = respuesta
    
    
    return f'La segunda película con mayor score en {plataforma}, según el orden alfabético de los títulos es {ultima_respuesta}'


# Película que más duró según año, plataforma y tipo de duración

@app.get('/longest_movie/{year}/{plataforma}/{type}')
def longest_movie(year, plataforma, duration_type):
    longest = df[(df['plataforma'] == plataforma) & (df['release_year'] == year) & (df['duration_type'] == duration_type)]
    pelicula_larga = longest[['duration_int', 'title']].nlargest(1, 'duration_int').iloc[0]
    
    answer = pelicula_larga['title']
    respuesta_final = answer
    
    
    return f'La película de mayor duración del año {year} en la plataforma {plataforma} fue {respuesta_final}'

# Cantidad de series y películas por rating

@app.get('/amount_by_rating/{rating}')
def amount_by_rating(rating):
    cantidad = df[(df['rating'] == rating)]
    amount = cantidad['type'].value_counts().sum()
    total = amount
    
    return f'La cantidad de series y películas según el rating {rating} es {total}'
