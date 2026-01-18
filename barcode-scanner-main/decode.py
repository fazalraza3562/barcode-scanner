from PIL import Image
import string

def read_barcode(image_path):
    """read barcode image and convert back to text"""
    barcode_img = Image.open(image_path).convert("L")
    pixel_data = barcode_img.load()
    
    # scan middle row (200) to read the bars
    middle_row = 200
    decoded_text = ""
    bar_length = 0
    
    for x in range(barcode_img.width):
        if pixel_data[x, middle_row] < 128:  # black pixel
            bar_length += 1
        else:  # white pixel
            if bar_length > 0:
                if bar_length == 1:
                    decoded_text += " "  # space
                else:
                    # convert width back to letter
                    # A=2px -> letter_pos=2 -> A (index 0)
                    letter_position = bar_length
                    if 2 <= letter_position <= 27:
                        decoded_text += string.ascii_uppercase[letter_position - 2]
                    else:
                        decoded_text += "?"  # unknown character
                bar_length = 0
    
    # handle last bar if image ends with black
    if bar_length > 0:
        if bar_length == 1:
            decoded_text += " "
        else:
            letter_position = bar_length
            if 2 <= letter_position <= 27:
                decoded_text += string.ascii_uppercase[letter_position - 2]
    
    return decoded_text

if __name__ == "__main__":
    import sys
    file_to_decode = sys.argv[1] if len(sys.argv) > 1 else "Output.png"
    decoded_result = read_barcode(file_to_decode)
    print(f"Decoded text: {decoded_result}")
