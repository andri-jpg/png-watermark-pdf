import fitz
from PIL import Image
import argparse

def add_image_to_pdf(pdf_path, image_path, output_path, coordinates):
    pdf_document = fitz.open(pdf_path)
    image = Image.open(image_path)
    
    temp_image_path = "temp_image.png"
    image.save(temp_image_path)

    for page_number in range(len(pdf_document)):
        page = pdf_document[page_number]
        x, y = coordinates
        image_rect = fitz.Rect(x, y, x + image.width, y + image.height)
        page.insert_image(image_rect, filename=temp_image_path)

    pdf_document.save(output_path)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Add an image to all pages of a PDF at specified coordinates.")
    
    parser.add_argument('--pdf', type=str, default="input.pdf", help='Path to the input PDF file')
    parser.add_argument('--image', type=str, default="image.png", help='Path to the image file')
    parser.add_argument('--output', type=str, default="output.pdf", help='Path to the output PDF file')
    parser.add_argument('--x', type=int, default=400, help='X coordinate for image placement')
    parser.add_argument('--y', type=int, default=750, help='Y coordinate for image placement')
    
    args = parser.parse_args()

    coordinates = (args.x, args.y)
    
    add_image_to_pdf(args.pdf, args.image, args.output, coordinates)
