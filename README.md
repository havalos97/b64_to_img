# Base64 to image converter

## Description
Convert array of strings in Base64 to PNG images \
\
**Usage:** main.py [-h] file {'file' | 'base64'} output \
\
Positional arguments:\
**FILE**\
Path to the JSON file that contains the images using the format included in this repo.\
\
**'file' | 'base64'**\
Choose an output type between images or JSON file.\
\
**OUTPUT**\
If **output-type=file** was chosen this will be used as the suffix for each one of the images inside the **./output_images** folder.\
If **output-type='base64'** this will be the filename used for the output JSON file.

## Author
@havalos97\
hg.avalosc97@gmail.com