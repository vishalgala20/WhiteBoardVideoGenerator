import openai
from gtts import gTTS
import os
from moviepy.editor import VideoFileClip, AudioFileClip

# Set your OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")

# Define a function to generate AI response (e.g., poem or any text)
def generate_response(model, prompt, max_tokens=100):
    try:
        response = openai.Completion.create(
            model=model,
            prompt=prompt,
            max_tokens=max_tokens
        )
        return response.choices[0].text.strip()
    except openai.error.OpenAIError as e:
        return f"An error occurred: {str(e)}"

# Function to convert text to speech and save as an audio file
def text_to_speech(text, filename="output.mp3"):
    tts = gTTS(text)
    tts.save(filename)
    print(f"Audio saved as {filename}")

# Function to create a whiteboard animation (just an example placeholder)
# Here you will generate the animation based on the generated text
def create_whiteboard_animation(text, filename="whiteboard_animation.mp4"):
    # This is just a placeholder for where the animation generation logic would go
    # You can use Manim, PIL, or OpenCV to create an actual animation
    print("Creating whiteboard animation for the text...")
    
    # Create a blank whiteboard screen (for example)
    # For simplicity, we create a blank whiteboard video here, you can replace this with your actual animation
    # For advanced animations, refer to Manim or other animation tools

    # Example with MoviePy to create a simple whiteboard-like background
    from moviepy.editor import TextClip

    text_clip = TextClip(text, fontsize=30, color='black', bg_color='white', size=(1280, 720), method='caption')
    text_clip = text_clip.set_duration(5)  # Show for 5 seconds
    text_clip.write_videofile(filename, codec="libx264")

    print(f"Whiteboard animation saved as {filename}")

# Main function
if __name__ == "__main__":
    model_name = "gpt-3.5-turbo"
    prompt = "Write a poem about the stars."
    
    # Step 1: Generate AI response (e.g., a poem)
    response_text = generate_response(model_name, prompt)
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
