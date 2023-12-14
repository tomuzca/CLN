import pandas as pd
import streamlit as st

archivo_csv = "../CLN/spotify_songs.csv"
df = pd.read_csv(archivo_csv)

st.title('Canciopedia')

# Entrada de usuario para el nombre de la canción
nombre_cancion = st.text_input('Nombre de la canción:', '')

# Botón para buscar y mostrar la información de la canción en el DataFrame
if st.button('Buscar Información de la Canción'):
    # Verificar si el usuario ingresó un nombre de canción
    if nombre_cancion:
        # Buscar la información correspondiente a la canción en el DataFrame
        cancion_info = df[df['track_name'] == nombre_cancion]

        if not cancion_info.empty:
            tono = cancion_info['key'].values[0]
            modo = cancion_info['mode'].values[0]
            tempo = cancion_info['tempo'].values[0]
            año = cancion_info['track_album_release_date'].values[0]
            artista = cancion_info['track_artist'].values[0]

            st.success(f'Información para la canción "{nombre_cancion}":')
            st.write(f'- Tono: {tono}')
            st.write(f'- Modo: {modo}')
            st.write(f'- Tempo: {tempo}')
            st.write(f'- Año: {año}')
            st.write(f'- Artista: {artista}')
        else:
            st.warning(f'No se encontró información para la canción "{nombre_cancion}".')

# Mostrar el DataFrame actualizado

