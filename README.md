# Add Image to All Pages of a PDF

This Python script allows you to add an image to all pages of a PDF at specified coordinates.

## Requirements

- Python 3.x
- `fitz` (PyMuPDF)
- `Pillow`

You can install the required packages using pip:

```sh
pip install pymupdf pillow
```

## Usage

You can run the script from the command line with the following arguments:

- `--pdf`: Path to the input PDF file (default: `input.pdf`)
- `--image`: Path to the image file (default: `image.png`)
- `--output`: Path to the output PDF file (default: `output.pdf`)
- `--x`: X coordinate for image placement (default: 400)
- `--y`: Y coordinate for image placement (default: 750)

### Example

```sh
python add_image_to_all_pages.py --pdf input.pdf --image image.png --output output.pdf --x 400 --y 750
```

If you want to use the default values, you can simply run:

```sh
python add_image_to_all_pages.py
```

# Add Image to the First Page of a PDF

This Python script allows you to add an image to the first page of a PDF at specified coordinates.

You can run the script from the command line with the following arguments:

- `--pdf`: Path to the input PDF file (default: `input.pdf`)
- `--image`: Path to the image file (default: `image.png`)
- `--output`: Path to the output PDF file (default: `output.pdf`)
- `--x`: X coordinate for image placement (default: 400)
- `--y`: Y coordinate for image placement (default: 750)

### Example

```sh
python add_image_to_first_page.py --pdf input.pdf --image image.png --output output.pdf --x 400 --y 750
```

If you want to use the default values, you can simply run:

```sh
python add_image_to_first_page.py
```
