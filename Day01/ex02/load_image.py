import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from PIL import Image
import numpy as np
from os.path import exists


def ft_load(path: str) -> any:
    try:
        assert exists(path), "Error: file not found"
        assert Image.open(path)
        img = np.asarray(Image.open(path))
        print("The shape of image is:", img.shape)
        print(img)
        img = mpimg.imread(path)
        imgplot = plt.imshow(img)
        plt.show()
    except Image.UnidentifiedImageError as e:
        print("Bad file:", e)
        return (1)
    except AssertionError as e:
        print(e)
        return (1)
    return (0)