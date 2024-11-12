from PIL import Image, ImageDraw, ImageFont
import re

def read_text_from_file(file_path):
    try:
        with open(file_path, 'r') as file:
            text = file.read()
        return text
    except Exception as e:
        print(f"Error reading file: {e}")
        return None

def replace_case_insensitive(text, old, new):
    def replace(match):
        matched_text = match.group()
        if matched_text.isupper():
            return new.upper()
        elif matched_text.islower():
            return new.lower()
        elif matched_text[0].isupper():
            return new.capitalize()
        else:
            return new

    return re.sub(old, replace, text, flags=re.IGNORECASE)

def create_image_with_text(text, output_path, font_path='arial.ttf', font_size=20):
    try:
        # Load the font and set the text size
        font = ImageFont.truetype(font_path, font_size)
        
        # Create a drawing context to calculate text size
        dummy_image = Image.new('RGB', (1, 1))
        draw = ImageDraw.Draw(dummy_image)
        
        # Calculate text size
        text_bbox = draw.textbbox((0, 0), text, font=font)
        text_width = text_bbox[2] - text_bbox[0]
        text_height = text_bbox[3] - text_bbox[1]

        # Define minimum image size for visual appeal
        min_width = 800
        min_height = 600
        padding = 50

        # Calculate image size based on text size or minimum size
        image_width = max(text_width + 2 * padding, min_width)
        image_height = max(text_height + 2 * padding, min_height)

        # Create an image with the calculated size and white background
        image = Image.new('RGB', (image_width, image_height), color='white')
        draw = ImageDraw.Draw(image)

        # Calculate the position to center the text
        text_x = (image_width - text_width) / 2
        text_y = (image_height - text_height) / 2

        # Draw the text on the image
        draw.text((text_x, text_y), text, fill="black", font=font)

        # Save the image
        image.save(output_path)
        
        print(f"\nImage saved as {output_path}")
    except Exception as e:
        print(f"Error creating image: {e}")

def display_image(image_path):
    try:
        img = Image.open(image_path)
        img.show()
    except Exception as e:
        print(f"Error displaying image: {e}")

if __name__ == "__main__":
    file_path = 'input.txt'  # Replace with your file path
    output_path = 'output_image.png'
    
    # Step 1: Read text from file
    original_text = read_text_from_file(file_path)
    if original_text:
        print(f"Original Text: {original_text}")
        
        # Step 2: Create and display the initial image with the original text
        create_image_with_text(original_text, output_path)
        display_image(output_path)
        
        updated_text = original_text  # Initialize updated_text with original_text
        
        while True:
            print(f"\nCurrent Text: {updated_text}")
            
            # Step 3: Get user input for the word to replace and the new word
            word_to_replace = input("\nEnter the word to replace (or '0' to exit): ")
            if word_to_replace == '0':
                print("Exiting.")
                break
            
            new_word = input("Enter the new word: ")
            
            # Perform case-insensitive check and replacement
            if word_to_replace.lower() not in updated_text.lower():
                print(f"\nNo such word '{word_to_replace}' found in the text.")
                continue
            
            # Replace the word in the updated text while preserving the original case
            updated_text = replace_case_insensitive(updated_text, word_to_replace, new_word)
            
            # Step 4: Create image with updated text
            create_image_with_text(updated_text, output_path)
            display_image(output_path)
