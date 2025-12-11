# Spotify Playlist Roaster 🎵🔥

This project is a fun, interactive Python script that uses **Google's Gemini API** to roast a user's Spotify playlist in a comedic and playful way. It’s designed to give users a humorous critique of their music taste — without ever being mean.

---

## 📌 What This Project Does

* Takes the user’s Spotify playlist (as text input)
* Sends it to the Gemini API along with a comedic prompt
* The AI then **roasts** the playlist in a witty, light-hearted, and entertaining style
* Returns a funny critique right in the terminal

It’s basically an AI-powered stand-up comedian for your questionable music taste.

---

## 🧠 Why I Built This

* To practice working with APIs in Python.
* To explore prompt engineering.
* And because roasting playlists is fun. 😎

---

## 🏗️ How It Works

### 1. Import the Gemini API

```python
from google import genai
```

This gives access to the Gemini client.

### 2. Authenticate the Client

```python
client = genai.Client(api_key="API_KEY")
```

Replace `API_KEY` with your actual Gemini API key.

### 3. Create a Prompt

The prompt tells the AI **how** to behave:

* comedic
* sarcastic
* playful
* NOT offensive

### 4. Ask the User for Their Playlist

The script waits for the user to paste or type their playlist.

### 5. Send the Request

```python
response = client.models.generate_content(...)
```

The playlist + prompt are sent to Gemini.

---

The AI responds with the roast.

---

## 🔧 Requirements

* Python 3.x
* Google Gemini API access
* `google-genai` Python package

Install using:

```bash
pip install google-genai
```

---

## 💡 Future Improvements

* Connect directly to Spotify API
* Auto-fetch user’s actual playlist
* Add roast intensity levels
* Add GUI version

---

If you want a more advanced or stylish README format for GitHub, I can improve this anytime!
