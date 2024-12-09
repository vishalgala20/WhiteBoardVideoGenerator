import openai
import os

# Load the OpenAI API key from environment variables
openai.api_key = os.getenv("OPENAI_API_KEY")  # Set your API key in your environment variables

# Define a function to call the OpenAI API
def generate_response(model, prompt, max_tokens=100):
    try:
        # Test the API with the provided parameters using Completion.create
        response = openai.Completion.create(
            model=model,
            prompt=prompt,
            max_tokens=max_tokens
        )
        # Return the text from the response
        return response.choices[0].text.strip()
    except openai.error.OpenAIError as e:
        # Handle API errors
        return f"An error occurred: {str(e)}"

# Define the parameters for the API call
model_name = "gpt-3.5-turbo"  # Define the model to use
prompt = "Write a poem about the stars."

# Call the function and print the response
if __name__ == "__main__":
    response = generate_response(model_name, prompt)
    print(response)
