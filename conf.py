# GEN TILES CONFS

# number of divisions per channel (R, G and B)
# DEPTH = 4 -> 4 * 4 * 4 = 64 colors
DEPTH = 4
# list of rotations, in degrees, to apply over the original image
ROTATIONS = [0]


#############################


# TILER CONFS

# number of divisions per channel
# (COLOR_DEPTH = 32 -> 32 * 32 * 32 = 32768 colors)
COLOR_DEPTH = 32
# Scale of the image to be tiled (1 = default resolution)
IMAGE_SCALE = 1
# tiles scales (1 = default resolution)
RESIZING_SCALES = [0.5, 0.4, 0.3, 0.2, 0.1]
# number of pixels shifted to create each box (tuple with (x,y))
# if value is None, shift will be done accordingly to tiles dimensions
PIXEL_SHIFT = (5, 5)
# if tiles can overlap
OVERLAP_TILES = False
# render image as its being built
RENDER = False
# multiprocessing pool size
POOL_SIZE = 8

# image to tile (ignored if passed as the 1st arg)
IMAGE_TO_TILE = 'D:\\Code_new\\tiler\\origin\\cat.png'
# folder with tiles (ignored if passed as the 2nd arg)
TILES_FOLDER = 'D:\\Code_new\\tiler\\tiles\\circles\\gen_circle_100'
# out file name
import os
image_base = os.path.splitext(os.path.basename(IMAGE_TO_TILE))[0]
tile_base = os.path.basename(TILES_FOLDER.rstrip('\\/'))
output_dir = 'D:\\Code_new\\tiler\\output'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)
OUT = os.path.join(output_dir, f'{image_base}_{tile_base}.png')