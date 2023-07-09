"""
Heavy Metal and Classic Rock color map collection.

Includes color maps based on the following albums:

+ TODO
+ TODO 2
+ TODO 3


License: LGPLv3
Author: Mladen Ivkovic (mladen.ivkovic@hotmail.com), Josh Borrow

Usage
-----

To use these, you can import them and use them
with matplotlib as you would with any other color map.

TODO: CLEAN THIS UP
.. code-block:: python

    from metalmaps import red
    from matplotlib.pyplot import imshow
    from numpy import random

    imshow(random.rand(128, 128), cmap=red)

"""

import metalmaps.colors as colors
from metalmaps.make_cmap import make_custom_cmap
from metalmaps.__version__ import __version__

red, red_r = make_custom_cmap("red", colors.red)


