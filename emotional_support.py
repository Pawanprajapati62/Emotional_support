import speech_recognition as sr
import pyttsx3
import requests
import google.generativeai as genai 
from text_to_speech import text_to_speech 

def generate_sarcastic_response(user_input):
    # Configure the Gemini API with your API key
    genai.configure(api_key='your api key ')

    model = genai.GenerativeModel('gemini-1.5-pro')  # Updated model name

    try:
        response = model.generate_content(
            f"Provide a simple, sarcastic, humanly, funny response to this input, the output should be 30 to 50 words long: {user_input}",
            generation_config=genai.types.GenerationConfig(
                temperature=0.7,
                top_p=1,
                top_k=1,
                max_output_tokens=50,
            )
        )

        sarcastic_response = response.text.strip()
        print(f"Generated sarcastic response: {sarcastic_response}")
        return sarcastic_response

    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return "Sorry, I'm having trouble being sarcastic right now. Must be my existential crisis acting up again."

def speech_to_text():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something!")
        audio = recognizer.listen(source)
        
    try:
        text = recognizer.recognize_google(audio)
        print("You said: " + text)
        return text
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
        
    return None

def main():
    while True:
        user_input = speech_to_text()
        if user_input:
            sarcastic_response = generate_sarcastic_response(user_input)
            print("Sarcastic response:", sarcastic_response)
            text_to_speech(sarcastic_response)
            
        choice = input("Continue? (y/n): ")
        if choice.lower() != 'y':
            break

if __name__ == "__main__":
    main()