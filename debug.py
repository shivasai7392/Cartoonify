import cv2
import easygui
import numpy
import imageio
import matplotlib.pyplot as plt
import os


def upload():
    """[summary]

    [extended_summary]
    """
    imagepath = easygui.fileopenbox()
    cartoonify(imagepath)
    return 0

def cartoonify(imagepath):
    """[summary]

    [extended_summary]

    Args:
        imagepath ([type]): [description]

    Returns:
        [type]: [description]
    """
    # image = cv2.imread(imagepath)
    # image = cv2.cvtColor(image, cv2.Color_BGR2RGB)

    image = cv2.imread(imagepath)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    ReSized1 = cv2.resize(image, (960,540))

    grayscale_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    ReSized2 = cv2.resize(grayscale_image, (960, 540))

    smoothed_image = cv2.medianBlur(grayscale_image, 5)
    ReSized3 = cv2.resize(smoothed_image, (960, 540))

    get_edge = cv2.adaptiveThreshold(smoothed_image, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 9)
    ReSized4 = cv2.resize(get_edge, (960, 540))

    colorImage = cv2.bilateralFilter(image, 9, 300, 300)
    ReSized5 = cv2.resize(colorImage, (960, 540))

    cartoonImage = cv2.bitwise_and(colorImage, colorImage, mask=get_edge)
    ReSized6 = cv2.resize(cartoonImage, (960, 540))

    images=[ReSized1, ReSized2, ReSized3, ReSized4, ReSized5, ReSized6]
    fig, axes = plt.subplots(3,2, figsize=(8,8), subplot_kw={'xticks':[], 'yticks':[]}, gridspec_kw=dict(hspace=0.1, wspace=0.1))

    for i, ax in enumerate(axes.flat):
        ax.imshow(images[i], cmap='gray')
    plt.show()
    return 0

if __name__ == "__main__":
    upload()