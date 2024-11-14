import os
import requests
from dotenv import load_dotenv
from util.secret_resolver import resolve_secret
import openai

# Load environment variables from .env file
load_dotenv()

# Resolve secrets
openai_api_key = resolve_secret(os.getenv("OPENAI_API_KEY"))
openai_org = resolve_secret(os.getenv("OPENAI_ORG"))
openai_project = resolve_secret(os.getenv("OPENAI_PROJ"))

# Set OpenAI API credentials
openai.api_key = openai_api_key
openai.organization = openai_org
openai.project = openai_project

# Generate image using OpenAI's API
response = openai.images.generate(
    model="dall-e-3",
    prompt="A young, agile orange tabby kitten play fighting with an older, fat black cat.",
    size="1024x1024",
    quality="standard",
    n=1,
)

# Save the images to a file
with open(f"image.png", "wb") as f:
    f.write(requests.get(response.data[0].url).content)