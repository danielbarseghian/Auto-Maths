from dotenv import load_dotenv
load_dotenv()
from PIL import Image
from groq import Groq
import base64
import os

def main():
    ex = input("Quel exercice? (Format exact: ex --> 9p90) ").strip().lower()
    exercice, page = ex.split("p")
    
    api_key = os.environ.get("key") 
    client = Groq(api_key=api_key)

    # Offset the page index by -2 to match the document numbering.
    page = int(page)
    page += 2
    page = str(page)

    with open(f"./files/{page}.jpg", "rb") as f:
        image_b64 = base64.b64encode(f.read()).decode()

    response = client.chat.completions.create(
    model="meta-llama/llama-4-scout-17b-16e-instruct",
    messages=[
        {
            "role": "user",
            "content": [
                {"type": "image_url", "image_url": {"url": f"data:image/jpeg;base64,{image_b64}"}},
                {"type": "text", "text": f"Repond a la l'exercice {exercice}, donne just les reponse et n'utilise pas le LaTeX complexe si possible."}
            ]
        }
    ]
    )
    print(response.choices[0].message.content)
    

main()