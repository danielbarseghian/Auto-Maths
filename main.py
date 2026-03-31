from PIL import Image
import moondream as md # Switch to gemini

def main():
    ex = input("Quel exercice? (Format exact: ex --> 9p90) ").strip().lower()
    exercice, page = ex.split("p")


    # Initialize with Moondream Cloud
    model = md.vl(api_key="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJrZXlfaWQiOiJjZWIwNmQyMS01OTU3LTRiZDItYjMzMi04MGM1OGZiMjcyOWQiLCJvcmdfaWQiOiJTb2dRVTZhZ0g0WTltT3lITWhrRVNkYXk0ZVFJYThZYSIsImlhdCI6MTc3NDkwMzc2NiwidmVyIjoxfQ.2XNgq2rii_f0wgouUQhIJ5OKJf-Ax71aGDBwaa39SlM")

    # Load an image
    image = Image.open(f"./files/{page}.jpg")

    # Generate a caption
    caption = model.caption(image)["caption"]
    print("Caption:", caption)

    # Ask a question
    answer = model.query(image, f"Please do the exercice {exercice} and give an awser. If the exercice is none existante please say None?")["answer"]
    print("Answer:", answer)

    # Stream the response
    for chunk in model.caption(image, stream=True)["caption"]:
        print(chunk, end="", flush=True)

main()