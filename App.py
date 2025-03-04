import streamlit as st
import whisper as wsp
import os

st.header("Transcription d'audios")

# Mapping des modèles disponibles
model_mapping = {
    "Base": "base",
    "Small": "small",
    "Medium": "medium",
    "Large": "large"
}

st.sidebar.title("Modèles")
st.sidebar.markdown("Le chargement du modèle peut prendre du temps...")
model_choisi = st.sidebar.radio("Choisissez un modèle :", list(model_mapping.keys()))

st.subheader(f"Modèle sélectionné : {model_choisi}")

# Charger le modèle une seule fois
model = wsp.load_model(model_mapping[model_choisi])

def convertir(fichier_a_convertir):
    if fichier_a_convertir is not None:
        try:
            temp_file = "temp_audio.mp3"

            # Sauvegarde du fichier temporaire
            with open(temp_file, "wb") as f:
                f.write(fichier_a_convertir.getbuffer())

            # Transcription
            result = model.transcribe(temp_file)

            # Affichage du texte transcrit
            st.markdown("### Transcription :")
            st.write(result["text"])

            # Suppression du fichier temporaire
            os.remove(temp_file)

        except Exception as e:
            st.error(f"Erreur lors de la transcription : {e}")

file_uploaded = st.file_uploader("Déposez un fichier audio ici :", type=["mp3", "wav", "m4a"])

if file_uploaded is not None:
    if st.button("Transcrire"):
        convertir(file_uploaded)
else:
    st.warning("Veuillez uploader un fichier avant de lancer la transcription.")
