import os
from PIL import Image

def syn_1_jpg(image_folder,output_image):
    #input 64 img
    #output synthesis 1 imge
    #image_folder = './result/attention/first/img/CC(C)(C)c1cc(O)c(O)c(C(C)(C)C)c1'
    #output_image = 'final_image.jpg'

    image_files = [os.path.join(image_folder, f) for f in os.listdir(image_folder) if f.endswith('.jpg')]
    image_files.sort()  # Ensure the order is consistent.

    # Assume all images have the same dimensions.
    image_width, image_height = Image.open(image_files[0]).size
    grid_size = 8  # 8x8 Grid

    # Create a blank canvas.
    final_image = Image.new('RGB', (grid_size * image_width, grid_size * image_height))

    # Paste each image onto the canvas.
    for index, image_file in enumerate(image_files):
        image = Image.open(image_file)
        x = (index % grid_size) * image_width
        y = (index // grid_size) * image_height
        final_image.paste(image, (x, y))

    # Save the final concatenated image.
    final_image.save(output_image)
    #print(f'Final image saved as {output_image}')
    return final_image

def syn_1_png(image_folder,output_image):
    #input 64 img
    #output synthesis 1 imge
    #image_folder = './result/attention/first/img/CC(C)(C)c1cc(O)c(O)c(C(C)(C)C)c1'
    #output_image = 'final_image.jpg'

    image_files = [os.path.join(image_folder, f) for f in os.listdir(image_folder) if f.endswith('.png')]
    image_files.sort()  # Ensure the order is consistent.

    # Assume all images have the same dimensions.
    image_width, image_height = Image.open(image_files[0]).size
    grid_size = 8  # 8x8 Grid.

    # Create a blank canvas.
    final_image = Image.new('RGB', (grid_size * image_width, grid_size * image_height))

    # Paste each image onto the canvas.
    for index, image_file in enumerate(image_files):
        image = Image.open(image_file)
        x = (index % grid_size) * image_width
        y = (index // grid_size) * image_height
        final_image.paste(image, (x, y))

    # Save the final concatenated image.
    final_image.save(output_image)
    #print(f'Final image saved as {output_image}')
    return final_image

def syn_1_jpeg(image_folder,output_image):
    #input 64 img
    #output synthesis 1 imge
    #image_folder = './result/attention/first/img/CC(C)(C)c1cc(O)c(O)c(C(C)(C)C)c1'
    #output_image = 'final_image.jpg'

    image_files = [os.path.join(image_folder, f) for f in os.listdir(image_folder) if f.endswith('.jpeg')]
    image_files.sort()  # Ensure the order is consistent.

    # Assume all images have the same dimensions.
    image_width, image_height = Image.open(image_files[0]).size
    grid_size = 8  # 8x8 Grid

    # Create a blank canvas.
    final_image = Image.new('RGB', (grid_size * image_width, grid_size * image_height))

    # Paste each image onto the canvas.
    for index, image_file in enumerate(image_files):
        image = Image.open(image_file)
        x = (index % grid_size) * image_width
        y = (index // grid_size) * image_height
        final_image.paste(image, (x, y))

    # Save the final stitched image.
    final_image.save(output_image)
    #print(f'Final image saved as {output_image}')
    return final_image

if __name__ == "__main__":

    image_folder = './result/attention/first/img/CC(C)(C)c1cc(O)c(O)c(C(C)(C)C)c1'
    output_image = 'final_image.jpg'
