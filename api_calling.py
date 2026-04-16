from google import genai
from dotenv import load_dotenv
import os , io
from gtts import gTTS

#loading the environment variable
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

#initializing a client
client = genai.Client(api_key= api_key)

#note generator
def note_generator(images):

    prompt = """Summarize the picture in note formate at max 100 words,
    make sure to add necessary markdown to differentiate different section"""

    response = client.models.generate_content(
        model = "gemini-3-flash-preview",
        contents =[images,prompt]
    )
    return response.text

def audio_transcription(text):
    speech = gTTS(text,lang='en',slow = False)

    audio_buffer = io.BytesIO()
    speech.write_to_fp(audio_buffer)
    return audio_buffer

def quiz_generator(image,difficulty):
    prompt = f"Generate 3 quizzes based on the {difficulty}. make sure to add markdown to differentiate the options. also provide the Correct answer below."

    response = client.models.generate_content(
        model="gemini-3-flash-preview",
        contents=[prompt,image]
    )

    return response.text
