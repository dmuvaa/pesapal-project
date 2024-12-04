# def modify_pixel(pixel: tuple, iteration: int) -> tuple:
#     """
#     Modify a pixel slightly while maintaining visual similarity.
#     - Uses the iteration number to vary the least significant bit.
#     """
#     r, g, b = pixel
#     b = (b & 0xFE) | (iteration % 2)  # Adjust the blue channel
#     return (r, g, b)


import random

def modify_pixel(pixel, iteration):
    """
    Modify the pixel value in a way that introduces randomness.
    This function adjusts the RGB components based on iteration.
    """
    r, g, b = pixel
    
    # Modify RGB values with some random variation
    r = (r + random.randint(-10, 10)) % 256
    g = (g + random.randint(-10, 10)) % 256
    b = (b + random.randint(-10, 10)) % 256

    return (r, g, b)
