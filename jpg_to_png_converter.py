"""
Simple script to convert JPEG files into PNG. It accepts two command line arrguments:
- First arg is a path to directory containing JPEG files
- Second arg is a path to save converted PNG files to
"""

import sys
import os
from pathlib import Path
from PIL import Image


# Grab the first and second argument
try:
    image_dir, output_dir = sys.argv[1], sys.argv[2]
except IndexError as err:
    raise Exception('Provide command line args: image dir and output dir') from err

# Check if the first argument points to existing directory
if not os.path.exists(image_dir):
    raise Exception('First arg must point to existing directory')

# Check if output folder exist, if not create it
if not os.path.exists(output_dir):
    os.mkdir(output_dir)

# Loop through image folder
for filename in os.listdir(image_dir):
    file = os.path.join(image_dir, filename)

    # Check if file is a jpeg
    if os.path.isfile(file) and os.path.splitext(
            file)[-1].lower() in ['.jpg', '.jpeg']:
        img = Image.open(os.path.join(image_dir, filename))
        
        # Convert file to png and save
        output_filename = Path(file).stem + '.png'
        save_dir = os.path.join(output_dir, output_filename)
        img.save(save_dir, 'png')
