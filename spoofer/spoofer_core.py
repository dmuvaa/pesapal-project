# from PIL import Image
# from io import BytesIO
# from .pixel_modifier import modify_pixel
# from .hashing import calculate_hash
# from spoofer.logger import log_message
# import random


# class ImageHashSpoofer:
#     def __init__(self, target_prefix: str):
#         self.target_prefix = target_prefix.replace('0x', '').lower()
#         self.iterations = 0
#         self.max_iterations = 1000000

#     def create_image_with_target_hash(self, image_data: bytes) -> BytesIO:
#         """Create an image with a hash starting with the target prefix."""
#         img = Image.open(BytesIO(image_data)).convert('RGB')
#         width, height = img.size
#         pixels = img.load()

#         while self.iterations < self.max_iterations:
#             x = (self.iterations // height) % width
#             y = self.iterations % height
#             pixels[x, y] = modify_pixel(pixels[x, y], self.iterations)

#             buffer = BytesIO()
#             img.save(buffer, format='PNG')
#             current_hash = calculate_hash(buffer.getvalue())

#             if current_hash.startswith(self.target_prefix):
#                 buffer.seek(0)
#                 return buffer

#             self.iterations += 1

#         return None

from PIL import Image
from io import BytesIO
from .pixel_modifier import modify_pixel
from .hashing import calculate_hash
from spoofer.logger import log_message
import random

class ImageHashSpoofer:
    def __init__(self, target_prefix: str):
        self.target_prefix = target_prefix.replace('0x', '').lower()
        self.iterations = 0
        self.max_iterations = 1000000

    def create_image_with_target_hash(self, image_data: bytes) -> BytesIO:
        """Create an image with a hash starting with the target prefix."""
        img = Image.open(BytesIO(image_data)).convert('RGB')
        width, height = img.size
        pixels = img.load()

        while self.iterations < self.max_iterations:
            # Randomize pixel selection instead of sequentially
            x = random.randint(0, width - 1)
            y = random.randint(0, height - 1)
            pixels[x, y] = modify_pixel(pixels[x, y], self.iterations)

            # Save the modified image to a buffer
            buffer = BytesIO()
            img.save(buffer, format='PNG')
            current_hash = calculate_hash(buffer.getvalue())

            # Check if the hash starts with the target prefix
            if current_hash.startswith(self.target_prefix):
                buffer.seek(0)
                return buffer

            self.iterations += 1

        return None
