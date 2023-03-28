from dataclasses import dataclass
import numpy as np

@dataclass
class PixelDataclass:
    r: int
    g: int
    b: int

class PixelManual:
    r: int
    g: int
    b: int

    def __init__(self, r, g, b):
        self.r = r
        self.g = g
        self.b = b
    
    def __str__(self) -> str:
        return f"Mes données de pixel r: {self.r}, g: {self.g}, b: {self.b}"

    def hello(self) -> None:
        print("hello")

    def compute_brightness(self) -> int:
        # luminance formula from Ignacio Vazquez-Abrams
        return (0.2126*self.r) + (0.7152*self.g) + (0.0722*self.b)

class ImgDataManual:
    list_of_pixels: list[PixelManual] = []
    row_size: int = 0

    def __init__(self, list_of_pixels: list[tuple[int]], row_size: int) -> None:
        self.list_of_pixels = [PixelManual(pixel[0], pixel[1], pixel[2]) for pixel in list_of_pixels]
        self.row_size = row_size

    # [][] operator to access the pixel at a given position
    # 1 2 3 4 5 6 7 8 9
    #
    # 1 2 3
    # 4 5 6
    # 7 8 9   matrix[1, 1] = 5
    def __getitem__(self, position: tuple[int, int]) -> PixelManual:
        position_in_list = position[0] * self.row_size + position[1]
        return self.list_of_pixels[position_in_list]
    
    def add_brightness_to_darkest_pixel(self, brightness: int) -> None:
        # get darkest pixel
        darkest_pixel = self.list_of_pixels[0]
        for pixel in self.list_of_pixels:
            if pixel.compute_brightness() < darkest_pixel.compute_brightness():
                darkest_pixel = pixel

        # add brightness to darkest pixel
        darkest_pixel.r += brightness
        darkest_pixel.g += brightness
        darkest_pixel.b += brightness

        print("darkest pixel", darkest_pixel)

class ImgDataNumPy:
    tensor: np.ndarray

    def __init__(self, list_of_pixels: list[list[list[int]]]) -> None:
        self.tensor = np.array(list_of_pixels).reshape((3, 3, 3) )
    
    def __str__(self) -> str:
        string = ""
        for row in self.tensor:
            for pixel in row:
                string += str(pixel) + ", "
            string += "\n"
        return string
    
    def transform_pixel_to_black_if_brightness_is_under(self, brightness: int) -> None:
        # self.tensor = np.where(
        #     np.sum(self.tensor * [0.2126, 0.7152, 0.0722], axis=2) < brightness,
        #     self.tensor * [0, 0, 0], self.tensor
        # )
        brightness_matrix = np.sum(self.tensor * [0.2126, 0.7152, 0.0722], axis=2)
        mask = (brightness_matrix < brightness)[:, :, np.newaxis]
        self.tensor = np.where(mask, [0, 0, 0], self.tensor)
    
    def save_to_png_file(self, filename: str) -> None:
        from PIL import Image
        saved_tensor = self.tensor.copy()
        img = Image.fromarray(saved_tensor.astype('uint8'), 'RGB')
        img.save(filename)