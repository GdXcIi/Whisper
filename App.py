import streamlit as st
import whisper

st.header("Transcription d'audios")

st.sidebar.title("Modèles")
model_choisi = st.sidebar.radio("Choisissez un modèle :", ["Base", "Small", "Medium", "Large"])

# Chargement du modèle une seule fois
model = whisper.load_model(model_choisi.lower())

def convertir(fichier):
    if fichier is not None:
        # Sauvegarde temporaire du fichier uploadé
        with open("temp_audio.mp3", "wb") as f:
            f.write(fichier.getbuffer())

        result = model.transcribe("temp_audio.mp3")
        st.write(result["text"])
    else:
        st.warning("Veuillez uploader un fichier audio.")

fichier = st.file_uploader("Déposez un fichier audio ici", type=["mp3", "wav", "m4a"])

if st.button("Lancer la transcription"):
    convertir(fichier)
