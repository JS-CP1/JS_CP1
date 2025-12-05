from PIL import Image, ImageDraw, ImageFont
import numpy as np

# ---------------------------------------------------
# ORIGINAL ASCII ART
# ---------------------------------------------------
ascii_art = r"""
                                        ..                                                          
                    ...::---:..        =*.               ...          ........                      
          :-==:.                    :.-*#******************=  :*+++++++++++++++*++=     .:          
        -%=                      .#@@@@@%*-:==::::::::::::=- :##++++++**##*=:             .         
        *#.                      +@@%#%%@@@@@%*..:::::::::-  :----::.    .:-=*#%%%%%%+    -         
        #*                       %@%####@@@@@@#                       =%%%%##########*    -         
        %*.                     :@@%####@@@%@@+                       -%%%############.   :         
        %+                      +@%#####@@@%@@-                       -%%%#######**##%+   .         
        %+                      *%%#####@@@@@%:                       -%%%#####*****#%*   .         
       .%+                      %@%####%%@@@@%.                       -######*******###              
       .%+                      %@%#%%%@@@@@@#.                       -#####*********#*.            
       .%+                      %@%#%#*=@@@@%%.                       -#######******##+.            
       .%+                      #@%#%%%@@%%%%%:                       -#######******##=:  .         
       .%+                      +@%#%%%@%%%%%@-                       -%%######*****#*-:  .         
        %+                      -@@##%%%%%%%%@+                       -%%############*    :         
        %*                       %@%#%%%%%%%%@#                       =%%%%###%######*    :         
        #*                       +%@#%%%%%@@@%*  ....:...::  :-::::.    .:-=+*#%%%%%%+    -         
        =#:                      .#@@@@@%#=.-++=-========+*: :##+++++++++++-:             :         
         :=+=:                     :-::=*#***#####%%%%%%%%%+  -*++++++++++*******+-     .:          
                 ..:---===--::.       .*=.               .:.        .....::::.                      
                                   .....:......
"""

# ---------------------------------------------------
# ASCII DENSITY RAMP (dark → light)
# ---------------------------------------------------
chars = np.array(list(" .:-=+*#%@"))

def ascii_to_image(ascii_text, scale=10, font_size=12):
    """Convert block ASCII to a PIL image."""
    lines = ascii_text.splitlines()
    if not lines:
        return None

    # Use monospace font (PIL default fallback works)
    font = ImageFont.load_default()

    # Measure text
    width = max(font.getlength(line) for line in lines)
    height = len(lines) * font_size

    img = Image.new("L", (int(width), int(height)), 255)
    draw = ImageDraw.Draw(img)

    for i, line in enumerate(lines):
        draw.text((0, i * font_size), line, 0, font=font)

    return img


def image_to_ascii(img, width=None):
    """Convert a grayscale PIL image back to ASCII."""
    if width:
        ratio = width / img.width
        img = img.resize((width, int(img.height * ratio)))

    img_arr = np.asarray(img)
    img_arr = img_arr.astype(float)
    img_arr -= img_arr.min()
    img_arr /= (img_arr.max() + 1e-9)

    idx = (img_arr * (len(chars) - 1)).astype(int)
    lines = ["".join(chars[row]) for row in idx]

    return "\n".join(lines)


def rotate_ascii(ascii_text, angle, output_width=None):
    """Rotate ASCII art at an arbitrary angle."""
    img = ascii_to_image(ascii_text)
    rotated = img.rotate(angle, expand=True, fillcolor=255)
    return image_to_ascii(rotated, width=output_width)


# ---------------------------------------------------
# GENERATE ALL 360 ROTATIONS
# ---------------------------------------------------
ae86 = []

for angle in range(360):
    rotated_ascii = rotate_ascii(ascii_art, angle, output_width=200)
    ae86.append(rotated_ascii)

# ---------------------------------------------------
# Example: print the 90° rotation
# ---------------------------------------------------
print(ae86[90])