import imageio
import numpy as np
imageio.imwrite('flip.jpg', np.fliplr(imageio.imread('img.png')))
