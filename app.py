from gtts import gTTS
import os
from moviepy import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

# Function to interact with the free web-based ChatGPT
def generate_response_web(prompt):
    # Path to your ChromeDriver
    chrome_driver_path = r"C:\Users\Appex\Downloads\chromedriver-win64\chromedriver-win64\chromedriver.exe"


    # Set up Chrome options
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")
    chrome_options.add_argument("--headless")  # Optional: Run in headless mode (no GUI)

    # Initialize WebDriver
    service = Service(chrome_driver_path)
    driver = webdriver.Chrome(service=service, options=chrome_options)

    try:
        # Open the ChatGPT website
        chatgpt_url = "https://chat.openai.com/"
        driver.get(chatgpt_url)

        # Wait for the page to load (adjust sleep time as needed)
        print("Waiting for ChatGPT website to load...")
        time.sleep(10)

        # Locate the input text area
        input_box = driver.find_element(By.TAG_NAME, "textarea")

        # Input the prompt
        input_box.send_keys(prompt)
        input_box.send_keys(Keys.RETURN)

        # Wait for the response to generate (adjust sleep time as necessary)
        print("Waiting for ChatGPT response...")
        time.sleep(15)

        # Locate the response area
        response_elements = driver.find_elements(By.CSS_SELECTOR, ".markdown")  # Adjust selector as needed
        response_text = "\n".join([element.text for element in response_elements])

        print("Response received from ChatGPT.")
        return response_text

    except Exception as e:
        return f"An error occurred: {str(e)}"

    finally:
        # Close the browser
        driver.quit()

# Function to convert text to speech and save as an audio file
def text_to_speech(text, filename="output.mp3"):
    tts = gTTS(text)
    tts.save(filename)
    print(f"Audio saved as {filename}")

# Function to create a whiteboard animation (just an example placeholder)
def create_whiteboard_animation(text, filename="whiteboard_animation.mp4"):
    from moviepy.editor import TextClip

    text_clip = TextClip(text, fontsize=30, color='black', bg_color='white', size=(1280, 720), method='caption')
    text_clip = text_clip.set_duration(5)  # Show for 5 seconds
    text_clip.write_videofile(filename, codec="libx264")

    print(f"Whiteboard animation saved as {filename}")

# Main function
if __name__ == "__main__":
    prompt = "Write a poem about the stars."
    
    # Step 1: Generate AI response from the web-based ChatGPT
    response_text = generate_response_web(prompt)
    print(f"Generated Text: {response_text}")
    
    # Step 2: Convert generated text to speech and save it as an audio file
    audio_filename = "poem_output.mp3"
    text_to_speech(response_text, audio_filename)
    
    # Step 3: Create the whiteboard animation for the generated poem
    animation_filename = "whiteboard_animation.mp4"
    create_whiteboard_animation(response_text, animation_filename)
    
    # Step 4: Combine the audio and animation into one final video
    video_clip = VideoFileClip(animation_filename)
    audio_clip = AudioFileClip(audio_filename)
    
    # Sync audio with video
    video_clip = video_clip.set_audio(audio_clip)

    # Export the final video
    final_video_filename = "final_video.mp4"
    video_clip.write_videofile(final_video_filename, codec="libx264")
    print(f"Final video saved as {final_video_filename}")
