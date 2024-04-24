import streamlit as st

# Titre de l'application
st.title("Ma première application Streamlit")

# Ajouter un widget de texte
st.write("Bonjour, c'est une application de démonstration Streamlit!")

# Ajouter un widget pour saisir du texte
user_input = st.text_input("Veuillez saisir votre nom", "John Doe")

# Afficher le texte saisi
st.write("Bonjour", user_input, "!")

