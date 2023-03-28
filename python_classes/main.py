from img_representation import *

# trouver le maximum dans une matrice de pixels
def hello_world():
    print("hello world")

# create main function
if __name__ == '__main__':

    manual_pixel = PixelManual(0xddd, 0xade, 0xa23)
    pixel_dataclass = PixelDataclass(0xddd, 0xade, 0xa23)

    print(manual_pixel)
    print(pixel_dataclass)

    manual_pixel.hello()

    hello_world()

    # work with matrix of pixels
    img_data = ImgDataManual(
        [
            (0xddd, 0xade, 0xa23), (0xddd, 0xade, 0xa23), (0xddd, 0xade, 0xa23),
            (0xded, 0xade, 0xa23), (0x444, 0x444, 0x444), (0xd0d, 0xade, 0xa23),
            (0x34d, 0xade, 0xa23), (0x11d, 0xade, 0xa23), (0xddd, 0xade, 0xa23)
        ],
        3
    )

    print(img_data[1, 1])
    
    img_data.add_brightness_to_darkest_pixel(0x001)

    # work with numpy
    img_data_numpy = ImgDataNumPy(
        [
            [[0xdd, 0xad, 0xa2], [0xdd, 0xad, 0xa2], [0x00, 0xad, 0xa2]],
            [[0x00, 0xad, 0xa2], [0x44, 0x44, 0x44], [0xd0, 0xad, 0xa2]],
            [[0x34, 0xad, 0xa2], [0x11, 0xad, 0xa2], [0xdd, 0xad, 0x00]],
        ]
    )
    print(img_data_numpy)
    print()
    img_data_numpy.save_to_png_file("test_before_mask.png")

    img_data_numpy.transform_pixel_to_black_if_brightness_is_under(0xb2)
    print(img_data_numpy)
    img_data_numpy.save_to_png_file("test_after_mask.png")
