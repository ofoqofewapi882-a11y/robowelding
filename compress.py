import os
import glob
from PIL import Image
import re

tinified_dir = "tinified"
html_file = "report.html"

# Convert images
for filepath in glob.glob(os.path.join(tinified_dir, "*.png")):
    img = Image.open(filepath)
    if img.mode != "RGB":
        img = img.convert("RGB")
    
    # Scale down if very large (e.g. max width 1200)
    MAX_SIZE = (1200, 1200)
    img.thumbnail(MAX_SIZE, Image.Resampling.LANCZOS)
    
    new_filepath = filepath.rsplit('.', 1)[0] + '.webp'
    img.save(new_filepath, "webp", quality=80)
    os.remove(filepath)
    print(f"Converted and compressed: {os.path.basename(filepath)} -> {os.path.basename(new_filepath)}")

# Update html
with open(html_file, 'r', encoding='utf-8') as f:
    content = f.read()

# Replace .png extensions for files in tinified
# The src in HTML is like src="tinified/Аудит цеха.png"
def replace_ext(match):
    return match.group(1) + ".webp"

# Find paths that start with tinified/ and end with .png
new_content = re.sub(r'(tinified/[^"]+)\.png', replace_ext, content)

with open(html_file, 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Updated report.html with .webp extensions")
