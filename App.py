import streamlit as st
import whisper as wsp
import os

st.header("Transcription d'audios")

model_mapping = {
    "Base": "base",
    "Small": "small",
    "Medium": "medium",
    "Large": "large"
}

st.sidebar.title("Modèles")
model_choisi = st.sidebar.radio("Choisissez un modèle :", list(model_mapping.keys()))

st.subheader(f"{model_choisi}")

def convertir(fichier_a_convertir) :
    if file_uploaded:
        try:
            temp_file = "temp_audio.mp3"

            # Création d'un fichier temporaire pour la transcription
            with open(temp_file, "wb") as f:
                f.write(file_uploaded.getbuffer())
            
            model = wsp.load_model(model_mapping[model_choisi])
            result = model.transcribe("temp_audio.mp3")
            
            st.markdown("### Transcription :")
            st.write(result["text"])
            
            os.remove(temp_file) # Supprime le fichier temporaire de l'audio
        
        except Exception as e:
            st.write(f"Erreur lors de la transcription : {e}")
    
    elif file_uploaded is None:
        st.warning("Veuillez uploader un fichier.")

file_uploaded = st.file_uploader("Déposez un fichier audio ici :", type=["mp3", "wav", "m4a"])

if st.button("Transcrire"):
    convertir(file_uploaded)