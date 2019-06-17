# #  STEPS NEEDED:
# #  * 1) Open file.
# #  * 2) Read file.
# #  * 3) Get data from file.
# #  * 4) Clean it up, making into lines of line.
# #  * 5) Play with a solid color block.
# #   6) Make a square grid x/y then y/x.
# #   7) Color the pixels with info from data files.
# #   8) Make a colored line based on the easiest path.

# from PIL import image

# file = "elevation_small.txt"

# with open(file) as my_file:
#     clean_lines = []
#     my_file = my_file.readlines()
#     for line in my_file:
#         clean_line = line.strip().split()
#         clean_lines.append(clean_line)
# print(clean_lines)


# class ElevationMap:
#     """
#     Elevation map is a class that takes a matrix (lists of lists, 2D)
#     of integers and can be used to generate an image of those elevations
#     like a standard elevation map.
#     """

#     def __init__(self, elevations):
#         self.elevations = elevations

#     def elevation_at_coordinate(self, x, y):
#         return self.elevations[y][x]

#     def min_elevation(self):
#         return min([min(row) for row in self.elevations])

#     def max_elevation(self):
#         return max([max(row) for row in self.elevations])

#     def intenstity_at_coordinate(self, x, y):
#         elevation = self.elevation_at_coordinate(x, y)
#         min_eleivation = self.min_elevation()
#         max_eleivation = self.max_elevation()
#         return (elevation - min_elevation) / (max_elevation - min_elevation)


# def draw_grayscale_gradient(self, filename, width, height):
#     image = PIL.Image.new(mode='L', size=(width, height))
#     for x in range(width):
#         for y in range(height):
#             image.putpixel((x, y), (int(x / width) * (y / height) * 255))
#     image.save.(filename)


"""Was able to play around with size/shape and color"""

from PIL import Image

def draw_square():
  im = Image.new('RGBA', (600, 600))
  im.getpixel ((0, 0))
  for x in range(600):
      for y in range(600):
          im.putpixel((x, y), (10, 189, 209))
  im.save('putPixel.png')

draw_square()


# NOTES
# pipenv shell
    # python3 elevation1.py
# L ((=(8-bit pixil)))
# git examples, pathfinder scratch.py