""" 
Code runs on: VS code 
 
Steps to run the code: 
1. Download the file
2. Go to terminal and type 
python -u "path_of_the_file"


Steps used in creating this model:

1. Import necessary libraries
2. Connect to the Hugging Face Nebius API using your API key
3. Define a function to scrape metadata (title, description, h1) from a webpage
4. Define a function to scrape and clean visible text content from a webpage
5. Define a function to send a question and context to the Mistral model
6. Define the main function that controls the chatbot interaction
7. Run the main function when the script is executed

"""

import subprocess
import sys

def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

# Try importing, install if not found
try:
    import requests
except ImportError:
    install("requests")
    import requests

try:
    from bs4 import BeautifulSoup
except ImportError:
    install("beautifulsoup4")
    from bs4 import BeautifulSoup

try:
    from huggingface_hub import InferenceClient
except ImportError:
    install("huggingface_hub")
    from huggingface_hub import InferenceClient
# Import required libraries for web scraping and model inference

import requests
from bs4 import BeautifulSoup
from huggingface_hub import InferenceClient

# Initialize the Hugging Face InferenceClient with Nebius provider
client = InferenceClient(
    provider="nebius",
    api_key="your_hugging_face_access_token",
)
# Function to scrape metadata (title, description, H1) from a given URL
def scrape_metadata(url):
    """Scrape title, meta description, and H1 from the website."""
    try:
        # Send a GET request to the URL
        response = requests.get(url)
        response.raise_for_status()

        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(response.text, "html.parser")

# Extract <title> tag text
        title = soup.title.string.strip() if soup.title else ""

        # Extract meta description content
        desc_tag = soup.find("meta", attrs={"name": "description"})
        description = desc_tag["content"].strip() if desc_tag else ""
        h1 = soup.find("h1")
        h1_text = h1.get_text(strip=True) if h1 else ""

        metadata = f"Title: {title}\nDescription: {description}\nH1: {h1_text}"
        return metadata
    except Exception as e:
        print(f"[ERROR] Failed to scrape metadata: {e}")
        return ""
# Function to scrape and clean the main text content of a webpage
def scrape_website(url):
    """Scrape and clean text from a website. Limit output to 3000 characters."""
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")

        for script in soup(["script", "style"]):
            script.extract()

        text = soup.get_text(separator=" ", strip=True)
        return text[:3000]  # Limit to 3000 characters
    except Exception as e:
        print(f"[ERROR] Failed to scrape content: {e}")
        return ""
# Function to ask a question to the model with the scraped website content as context
def ask_with_context(user_input, website_data):
    """Send chat message to the Mistral model."""
    messages = [
        {
            "role": "system",
            "content": "You are a helpful assistant that answers questions based on provided website data."
        },
        {
            "role": "user",
            "content": f"Here is the website data:\n\n{website_data}\n\nNow answer this question: {user_input}"
        }
    ]

    response = client.chat.completions.create(
        model="mistralai/Mistral-Small-3.1-24B-Instruct-2503",
        messages=messages,
    )

    return response.choices[0].message["content"]
# Main function to run the chatbot application
def main():
    print("Console Chatbot using Hugging Face Mistral")
    url = input(" Enter a website URL to extract information from: ").strip()

    print(" Scraping website metadata and content... Please wait.")
    metadata = scrape_metadata(url)
    content = scrape_website(url)
    website_data = metadata + "\n\n" + content

    if not website_data.strip():
        print(" Failed to extract website data. Exiting.")
        return

    print("\nWebsite content loaded! You can now ask questions. (Type 'exit' to quit)\n")

    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            print("Chatbot: Goodbye! ")
            break

        response = ask_with_context(user_input, website_data)
        print("Chatbot:", response)


# Run the main function when the script is executed directly
if __name__ == "__main__":
    main()