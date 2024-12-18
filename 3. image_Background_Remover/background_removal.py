from rembg import remove
from PIL import Image

def remove_background(input_path, output_path):
    # Open the input image
    input_image = Image.open(input_path)
    
    # Remove the background using rembg
    output_image = remove(input_image)
    
    # Save the output image
    output_image.save(output_path)

    print(f"Background removed and saved as {output_path}")

# Main function to run the background removal
if __name__ == "__main__":
    input_path = 'input_image.jpg'  # Path to input image
    output_path = 'output_image.png'  # Path to save output image

    remove_background(input_path, output_path)
