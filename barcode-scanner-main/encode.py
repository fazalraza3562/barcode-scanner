from PIL import Image, ImageDraw
import string

def find_width(character):
    """figure out how wide the bar should be for this letter"""
    character = character.upper()
    if character in string.ascii_uppercase:
        position = string.ascii_uppercase.index(character)
        return position + 2  # A=0 -> 2px, B=1 -> 3px, etc
    return None

def create_barcode(input_text, output_file="Output.png"):
    """make a barcode image from text"""
    canvas_width, canvas_height = 400, 800
    image = Image.new("L", (canvas_width, canvas_height), 255)  # white background
    drawer = ImageDraw.Draw(image)
    
    current_x = 15  # where to start drawing
    gap_size = 9  # space between bars
    
    for letter in input_text:
        if letter == ' ':
            # drawing short bar for space
            drawer.rectangle([current_x, 150, current_x, 250], fill=0)
            current_x += 1 + gap_size
        else:
            width = find_width(letter)
            if width:
                # draw full height bar for letter
                drawer.rectangle([current_x, 10, current_x + width - 1, 350], fill=0)
                current_x += width + gap_size
        
        # stop if we run out of space
        if current_x > canvas_width - 20:
            break
    
    image.save(output_file)
    return output_file

if __name__ == "__main__":
    # Testing the code with sample text(my name)
    sample_text = "Muhammad Fazal Raza"
    result = create_barcode(sample_text)
    print(f"Encoded '{sample_text}' -> {result}")
