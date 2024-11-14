import nest_asyncio,os
nest_asyncio.apply()  
from llama_parse import LlamaParse
from dotenv import load_dotenv
from PIL import Image


load_dotenv()


parser = LlamaParse(
    result_type="markdown",  # or "markdown" based on your requirement
    api_key="llx-M4edU51pPjYTi1qTZiVqFfbXX8O4IpkGB2kQBx14kMW8sm7b",
    num_workers=4,
    verbose=True,
    language="en"
)


image_path = 'bill.png'
if not os.path.exists(image_path):
    print(f"Error: The image file at {image_path} does not exist.")
else:
    
    documents = parser.load_data(image_path)

    if not documents:
        print("Error: No documents were returned by Llama Parse. Please check the image and API key.")
    else:
        
        print(documents[0].__dict__)

        
        extracted_text = documents[0].text
        print(extracted_text)

        def replace_text(original_text, old_word, new_word):
            return original_text.replace(old_word, new_word)

        
        old_word = 'Fuel'
        new_word = 'Indore'
        modified_text = replace_text(extracted_text, old_word, new_word)
        print(modified_text)

        from PIL import ImageDraw, ImageFont

        def text_to_image(text, image_path="output_image.jpg"):
           
            original_image = Image.open("ticket.jpg")
            new_image = Image.new('RGB', original_image.size, color='white') 

            draw = ImageDraw.Draw(new_image)
            font_path = "arial.ttf" 
            font_size = 20  
            font = ImageFont.truetype(font_path, font_size)

           
            draw.text((10, 10), text, font=font, fill="black")  # Adjust position and color as needed

            
            new_image.save(image_path)

        
        text_to_image(modified_text)
