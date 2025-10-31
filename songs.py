import streamlit as st
from pathlib import Path

# ---------------------------------------------------
# PAGE CONFIG
# ---------------------------------------------------
st.set_page_config(page_title="🎬 Telugu Movie Jukebox", layout="centered")

st.title("🎵 Telugu Movie Jukebox")
st.write("Enjoy songs from your favorite Telugu movies — Listen or Download!")

# ---------------------------------------------------
# MOVIE DATA CONFIGURATION
# ---------------------------------------------------
movies = {
    "Murari": {
        "poster": Path(r"C:\Users\amrut\Downloads\murari.jpg"),
        "songs": {
            "Ekkada Ekkada": Path(r"C:\Users\amrut\Downloads\Ekkada Ekkada-SenSongsMp3.Co.mp3"),
            "Bangaru Kalla": Path(r"C:\Users\amrut\Downloads\Bangaru Kalla-SenSongsMp3.Co.mp3"),
            "Cheppama Cheppama": Path(r"C:\Users\amrut\Downloads\Cheppamma Cheppamma-SenSongsMp3.Co.mp3"),
            "Andaanike Addanive": Path(r"C:\Users\amrut\Downloads\Andaanike Aadanive-SenSongsMp3.Co.mp3"),
            "Alanati Ramachandrudu": Path(r"C:\Users\amrut\Downloads\Alanati Ramachandrudu-SenSongsMp3.Co.mp3"),
        },
    },
    "Guntur Karam": {
        "poster": Path(r"C:\Users\amrut\Downloads\guntur karam.jpg"),
        "songs": {
            "Dum Masala": Path(r"C:\Users\amrut\Downloads\Dum Masala.mp3"),
            "Oh My Baby": Path(r"C:\Users\amrut\Downloads\Oh My Baby.mp3"),
            "Kurchi Madathapetti": Path(r"C:\Users\amrut\Downloads\Kurchi Madathapetti.mp3"),
            "Mawaa Enthaina": Path(r"C:\Users\amrut\Downloads\Mawaa Enthaina.mp3"),
            "Guntur Kaaram": Path(r"C:\Users\amrut\Downloads\Guntur Kaaram.mp3"),
        },
    },
    "Khaleja": {
        "poster": Path(r"C:\Users\amrut\Downloads\khaleja.jpg"),  # add a poster if available
        "songs": {
            "Sada Siva Sanyasi": Path(r"C:\Users\amrut\Downloads\Sada Siva-SenSongsMp3.Co.mp3"),
            "Piliche": Path(r"C:\Users\amrut\Downloads\Pileche-SenSongsMp3.Co.mp3"),
            "Bhoom Shakenaka": Path(r"C:\Users\amrut\Downloads\Bhoom Shakenaka-SenSongsMp3.Co.mp3"),
            "Makathika": Path(r"C:\Users\amrut\Downloads\Makathika-SenSongsMp3.Co.mp3"),
            "Sunday Monday": Path(r"C:\Users\amrut\Downloads\Sunday Monday-SenSongsMp3.Co.mp3"),
        },
    },
    "Seethamma Vaakitlo Sirimalle Chettu": {
        "poster": Path(r"C:\Users\amrut\Downloads\seethamma.jpg"),  # add poster file if you have
        "songs": {
            "Yem Cheddam": Path(r"C:\Users\amrut\Downloads\Yem Cheddaam-SenSongsMp3.Co.mp3"),
            "Seethamma Vaakitlo Sirimalle Chettu": Path(r"C:\Users\amrut\Downloads\Seethamma Vakitlo Sirimalle Chettu-SenSongsMp3.Co.mp3"),
            "Aaraduguluntada": Path(r"C:\Users\amrut\Downloads\Aaraduguluntada-SenSongsMp3.Co.mp3"),
            "Inka Cheppaale": Path(r"C:\Users\amrut\Downloads\Inka Cheppaale-SenSongsMp3.Co.mp3"),
            "Mari Antaga": Path(r"C:\Users\amrut\Downloads\Mari Antaga-SenSongsMp3.Co.mp3"),
            "Vaana Chinukulu": Path(r"C:\Users\amrut\Downloads\Vaana Chinukulu-SenSongsMp3.Co.mp3"),
            "Meghaallo": Path(r"C:\Users\amrut\Downloads\Meghaallo-SenSongsMp3.Co.mp3"),
        },
    },
}

# ---------------------------------------------------
# SIDEBAR FOR MOVIE SELECTION
# ---------------------------------------------------
st.sidebar.title("🎬 Select Movie")
selected_movie = st.sidebar.selectbox("Choose a movie:", list(movies.keys()), index=0)

# Get selected movie data
movie_data = movies[selected_movie]
poster_path = movie_data["poster"]
songs = movie_data["songs"]

# ---------------------------------------------------
# DISPLAY POSTER
# ---------------------------------------------------
st.header(f"🎥 {selected_movie}")
if poster_path.exists():
    st.image(poster_path, use_container_width=True, caption=f"{selected_movie} Poster")
else:
    st.warning("Poster not found for this movie. Check the path.")

st.markdown("---")

# ---------------------------------------------------
# DISPLAY SONGS
# ---------------------------------------------------
st.subheader("🎵 Songs List")

for song_name, song_path in songs.items():
    st.markdown(f"### {song_name}")

    if song_path.exists():
        # Read the song file bytes
        with open(song_path, "rb") as f:
            audio_bytes = f.read()

        # Play song in-app
        st.audio(audio_bytes, format="audio/mp3")

        # Download button
        st.download_button(
            label="⬇️ Download & Play",
            data=audio_bytes,
            file_name=song_path.name,
            mime="audio/mpeg",
            key=f"{selected_movie}_{song_name}"
        )

        st.markdown("---")

    else:
        st.error(f"❌ File not found: {song_path}")

