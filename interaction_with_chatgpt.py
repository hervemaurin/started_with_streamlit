"""import streamlit as st
import openai

# Setze deine OpenAI API Schlüssel
openai.api_key = "DEIN_API_SCHLÜSSEL_HIER_EINFÜGEN"

def chat_mit_gpt(prompt):
    # Sendet die Anfrage an ChatGPT und gibt die Antwort zurück
    response = openai.Completion.create(
        engine="text-davinci-002",  # Modell, das du verwenden möchtest
        prompt=prompt,
        max_tokens=50  # Maximale Anzahl von Tokens für die Antwort
    )
    return response.choices[0].text.strip()

# Streamlit App
st.title("Chat mit GPT-3.5")

# Eingabefeld für den Benutzer
user_input = st.text_input("Gib deine Nachricht ein:")

# Wenn der Benutzer eine Nachricht eingibt und auf Senden klickt
if st.button("Senden"):
    # Übergebe die Benutzereingabe an ChatGPT und erhalte die Antwort
    response = chat_mit_gpt(user_input)
    st.write("Antwort von GPT:", response)"""

# new approche
