import streamlit as st
import whisper as wsp
import os
import time

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

# Charger le modèle avec un spinner puis message de succès
with st.spinner("Chargement du modèle..."):
    model = wsp.load_model(model_mapping[model_choisi])
message_placeholder = st.empty()
message_placeholder.succes("Modèle chargé avec succès !")
time.sleep(2)
message_placeholder.empty()


def transcrire_audio(fichier_a_transcrire):
    if fichier_a_transcrire is not None:
        try:
            temp_file = "temp_audio.mp3"

            # Sauvegarde du fichier temporaire
            with open(temp_file, "wb") as f:
                f.write(fichier_a_transcrire.getbuffer())

            # Transcription
            with st.spinner("Transcription en cours..."):
                result = model.transcribe(temp_file)

            # Affichage du texte transcrit
            st.markdown("#### Transcription :")
            st.write(result["text"])

        except Exception as e:
            st.error(f"Erreur lors de la transcription : {e}")
        
        finally:
            if os.path.exists(temp_file):
                os.remove(temp_file)

file_uploaded = st.file_uploader("Déposez un fichier audio ici :", type=["mp3", "wav", "m4a"])

bouton_transcrire = st.button("Transcrire")

if bouton_transcrire:
    if file_uploaded is not None:
        transcrire_audio(file_uploaded)
    else:
        st.warning("Veuillez uploader un fichier avant de lancer la transcription.")
