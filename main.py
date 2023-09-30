import argparse

def main(filename: str, output_type: str, output: str):
  import base64
  from PIL import Image
  from io import BytesIO
  import json
  import os

  json_file = open(filename)
  json_content = json.load(json_file)
  output_dir = 'output_images'

  output_json = []
  if output_type == 'file':
    os.mkdir(output_dir)
  for idx, image in enumerate(json_content):
    file_type, file_content = image.split(',')
    file_extension = file_type.split('/')[1].split(';')[0]
    decodedData = base64.b64decode(file_content)

    # I WAS USING THE FOLLOWING CODE TO CHANGE
    # A COLOR ON EACH ONE OF THE IMAGES
    # old_colors = [
    #   (204, 224, 139, 255),
    #   (204, 224, 139, 12)
    # ]
    # new_color = 16, 131, 206, 255
    im = Image.open(BytesIO(decodedData))
    # width, height = im.size
    # pix = im.load()
    # for x in range(0, width):
    #   for y in range(0, height):
    #     if pix[x,y] in old_colors:
    #       im.putpixel((x, y), new_color)
    if output_type == 'file':
      im.save(f'./{output_dir}/{idx + 1}{output}.{file_extension}')
    elif output_type == 'base64':
      buffered = BytesIO()
      im.save(buffered, format=file_extension)
      b64_str = base64.b64encode(buffered.getvalue()).decode('ascii')
      output_json.append(file_type + ',' + b64_str)

  if output_type == 'base64':
    output_filename = output if '.json' in output else f'{output}.json'
    output_file = open(output_filename, 'w+')
    output_file.write(json.dumps(output_json, indent=2))
    output_file.close()


if __name__ == "__main__":
  parser = argparse.ArgumentParser(
    description='Convert array of strings in Base64 to PNG images.'
  )
  parser.add_argument(
    'file',
    help='Path to the JSON file that contains the images with the following format: [ \'Base64Str_1\',\'Base64Str_2\',\'Base64Str_3\',\'Base64Str_N\'...  ]',
  )
  parser.add_argument(
    'output_type',
    choices=['file', 'base64'],
    help='Choose an output type between images or JSON file'
  )
  parser.add_argument(
    'output',
    help='If output-type=\'file\' was chosen this will be used as the suffix for each one of the images inside the \'output_images\' folder. If output-type=\'base64\' this will be the filename used for the output JSON file.',
  )
  args = parser.parse_args()

  main(args.file, args.output_type, args.output)
