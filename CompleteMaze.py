from PIL import Image
from random import randint

def checkPixels(pixels,list_coord):
    for coord in list_coord:
        if not pixels[coord[0],coord[1]]:
            return True
    return False

def availablePaths(img, pixels, x, y):
    width, height = img.size
    pixels_to_check = [(x - 2, y), (x + 2, y), (x, y - 2), (x, y + 2)]
    if x == 1:
        pixels_to_check.remove((x - 2, y))
    if x == width - 2:
        pixels_to_check.remove((x + 2, y))
    if y == 1:
        pixels_to_check.remove((x, y - 2))
    if y == height - 2:
        pixels_to_check.remove((x, y + 2))
    return [coord for coord in pixels_to_check if not pixels[coord[0],coord[1]]]


def checkIfOpenPath(img, pixels, x, y):
    width, height = img.size
    if x < 0 or x >= width or y < 0 or y >= height:
        return False
    if not pixels[x,y]:
        return False
    pixels_to_check = [(x - 2, y), (x + 2, y), (x, y - 2), (x, y + 2)]
    if x == 1:
        pixels_to_check.remove((x - 2, y))
    if x == width - 2:
        pixels_to_check.remove((x + 2, y))
    if y == 1:
        pixels_to_check.remove((x, y - 2))
    if y == height - 2:
        pixels_to_check.remove((x, y + 2))
    return checkPixels(pixels, pixels_to_check)


def detectOpenPaths(img):
    # Get the size of the image
    width, height = img.size
    # Get the pixels of the image
    pixels = img.load()
    # Create a list to store the open paths
    openPaths = []
    # Iterate through the pixels in the image
    for x in range(1,width,2):
        for y in range(1,height,2):
            # Check if the pixel is white
            if checkIfOpenPath(img, pixels, x, y):
                # Add the pixel to the open paths list
                openPaths.append((x, y))
    # Return the open paths list
    return openPaths

img = Image.open("psyduck.png")
pixels = img.load()
openPaths = detectOpenPaths(img)
while openPaths:
    print(len(openPaths))
    index = randint(0, len(openPaths) - 1)
    x, y = openPaths[index]
    print(availablePaths(img, pixels, x, y))
    newPaths = availablePaths(img, pixels, x, y)
    if newPaths:
        index_new = randint(0, len(newPaths) - 1)
        new_x, new_y = newPaths[index_new]
        pixels[(new_x + x) // 2, (new_y + y) // 2] = 1
        pixels[new_x, new_y] = 1
        if checkIfOpenPath(img, pixels, new_x, new_y):
            openPaths.append((new_x, new_y))
        if not checkIfOpenPath(img, pixels, x, y):
            openPaths.remove((x, y))
    else:
        openPaths.remove((x, y))
img.save("complete_maze.png")