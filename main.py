from google import genai
import os

# Read API key from environment variable
client = genai.Client(api_key=os.environ.get("GENAI_API_KEY"))

prompt = "You are a comedic music critic. Roast the user’s Spotify playlist in a playful, entertaining way. Be witty, sarcastic, and confident, but never mean-spirited. Make sharp jokes about the[...]"

print("*****PLAYLIST ROASTER*****")

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=input("Enter Your Spotify Playlist: ") + prompt
)
print(response.text)
