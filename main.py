from google import genai

client = genai.Client(api_key="AIzaSyBoe5F7wRQKzn00Thp_67o872WnFzWPzeE")

prompt = "You are a comedic music critic. Roast the user’s Spotify playlist in a playful, entertaining way. Be witty, sarcastic, and confident, but never mean-spirited. Make sharp jokes about their song choices, genres, and overall music taste while keeping it light-hearted and fun."

print("*****PLAYLIST ROASTER*****")

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents= input("Enter Your Spotify Playlist: ") + prompt
)
print(response.text)