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

apostasy, apostasy_r = make_custom_cmap("apostasy", colors.apostasy)
blues_brothers, blues_brothers_r = make_custom_cmap("blues_brothers", colors.blues_brothers)
blues_pills, blues_pills_r = make_custom_cmap("blues_pills", colors.blues_pills)
black_sabbath, black_sabbath_r = make_custom_cmap("black_sabbath", colors.black_sabbath)
london_calling, london_calling_r = make_custom_cmap("london_calling", colors.london_calling)
master_of_puppets, master_of_puppets_r = make_custom_cmap("master_of_puppets", colors.master_of_puppets)
obzen, obzen_r = make_custom_cmap("obzen", colors.obzen)
paranoid, paranoid_r = make_custom_cmap("paranoid", colors.paranoid)
ride_the_lightning, ride_the_lightning  = make_custom_cmap("ride_the_lightning", colors.ride_the_lightning)
meteora, meteora_r  = make_custom_cmap("meteora", colors.meteora)


