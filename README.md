# Image Processor 

## Project Overview
Image Processor is a Python-based project that provides two powerful image manipulation modules:

### Module 1: Text Extraction and Image Modification
This module enables users to:
- Read text from an input image
- Replace a specific word in the extracted text
- Paste the modified text back onto the original image

#### Key Features
- Image text extraction
- Word replacement
- Text overlay on images

### Module 2: Text to Image Conversion
This module allows users to:
- Read text from a text file
- Convert the text into an image
- Generate the image with a white background

#### Key Features
- Text file reading
- Text-to-image generation
- Customizable image creation

## Technologies and Libraries
The project leverages the following Python libraries and technologies:

- **OpenCV (cv2)**: For image processing and manipulation
- **Pillow**: Image handling and creation
- **NumPy**: Numerical computing and array operations
- **Lama Parser API**: Text extraction and parsing

## Prerequisites
- Python 3.8+
- pip package manager

## Installation
1. Clone the repository
```bash
git clone https://github.com/YASH-Prakhar/image-processor.git
```

2. Install required dependencies
```bash
pip install -r requirements.txt
```

## Usage

### Module 1: Text Replacement in Image
```python
from image_processor import TextReplacementModule

# Initialize the module
processor = TextReplacementModule()

# Process image
result_image = processor.replace_word('input_image.jpg', 'old_word', 'new_word')
result_image.save('output_image.jpg')
```

### Module 2: Text to Image Conversion
```python
from image_processor import TextToImageModule

# Initialize the module
converter = TextToImageModule()

# Convert text file to image
converter.text_to_image('input_text.txt', 'output_image.png')
```

## Contributing
1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## Contact
Your Name - Prakhar Kabra
Contributors - Sanika Patade, Ishita Porwal
Project Link: [https://github.com/YASH-Prakhar/ImageProcessor](https://github.com/YASH-Prakhar/ImageProcessor)
