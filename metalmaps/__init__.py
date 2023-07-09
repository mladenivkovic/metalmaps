"""
Heavy Metal and Classic Rock color map collection.

Includes color maps based on the following albums:

+ Apostasy
+ TODO 2
+ TODO 3


License: LGPLv3
Authors: Mladen Ivkovic (mladen.ivkovic@hotmail.com), Josh Borrow

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
ashes_of_the_wake, ashes_of_the_wake_r = make_custom_cmap("ashes_of_the_wake", colors.ashes_of_the_wake)
blues_brothers, blues_brothers_r = make_custom_cmap(
    "blues_brothers", colors.blues_brothers
)
blues_pills, blues_pills_r = make_custom_cmap("blues_pills", colors.blues_pills)
black_sabbath, black_sabbath_r = make_custom_cmap("black_sabbath", colors.black_sabbath)
cosmos_factory, cosmos_factory_r = make_custom_cmap(
    "cosmos_factory", colors.cosmos_factory
)
deep_purple_in_rock, deep_purple_in_rock_r = make_custom_cmap(
    "deep_purple_in_rock", colors.deep_purple_in_rock
)
dethalbum, dethalbum_r = make_custom_cmap("dethalbum", colors.dethalbum)
fear_of_the_dark, fear_of_the_dark_r = make_custom_cmap("fear_of_the_dark", colors.fear_of_the_dark)
from_mars_to_sirius, from_mars_to_sirius_r = make_custom_cmap(
    "from_mars_to_sirius", colors.from_mars_to_sirius
)
hypnotize, hypnotize_r = make_custom_cmap("hypnotize", colors.hypnotize)
in_utero, in_utero_r = make_custom_cmap("in_utero", colors.in_utero)
la_woman, la_woman_r = make_custom_cmap("la_woman", colors.la_woman)
lenfant_sauvage, lenfant_sauvage_r = make_custom_cmap("lenfant_sauvage", colors.lenfant_sauvage)
london_calling, london_calling_r = make_custom_cmap(
    "london_calling", colors.london_calling
)
master_of_puppets, master_of_puppets_r = make_custom_cmap(
    "master_of_puppets", colors.master_of_puppets
)
made_in_japan, made_in_japan_r = make_custom_cmap("made_in_japan", colors.made_in_japan)
meteora, meteora_r = make_custom_cmap("meteora", colors.meteora)
number_of_the_beast, number_of_the_beast_r = make_custom_cmap("number_of_the_beast", colors.number_of_the_beast)
obzen, obzen_r = make_custom_cmap("obzen", colors.obzen)
overkill, overkill_r = make_custom_cmap("overkill", colors.overkill)
paranoid, paranoid_r = make_custom_cmap("paranoid", colors.paranoid)
painkiller, painkiller_r = make_custom_cmap("painkiller", colors.painkiller)
powerslave, powerslave_r = make_custom_cmap("powerslave", colors.powerslave)
reign_in_blood, reign_in_blood_r = make_custom_cmap("reign_in_blood", colors.reign_in_blood)
ride_the_lightning, ride_the_lightning = make_custom_cmap(
    "ride_the_lightning", colors.ride_the_lightning
)
rock_n_roll, rock_n_roll_r = make_custom_cmap("rock_n_roll", colors.rock_n_roll)
screaming_for_vengeance, screaming_for_vengeance_r = make_custom_cmap("screaming_for_vengeance", colors.screaming_for_vengeance)
south_of_heaven, south_of_heaven_r = make_custom_cmap("south_of_heaven", colors.south_of_heaven)
the_hunter, the_hunter_r = make_custom_cmap("the_hunter", colors.the_hunter)
ziggy_stardust, ziggy_stardust_r = make_custom_cmap(
    "ziggy_stardust", colors.ziggy_stardust
)
