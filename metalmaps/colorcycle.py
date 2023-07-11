"""
Stuff related to setting up the color cycle.
"""

from matplotlib.colors import LinearSegmentedColormap, to_hex
from matplotlib import rc, colormaps
from typing import List, Union
from cycler import cycler

from numpy import ndarray, linspace, array, zeros, argsort, sqrt, dot


def _scrabmle(arr: ndarray) -> ndarray:
    """
    scramble the order of a numpy array. Creates a copy of the array, does
    not scramble in-place.

    Parameters
    ----------
    arr: ndarray
        1D array to work on

    Returns
    -------
    scrambled: ndarray
        a new array with scrambled elements of input arr
    """

    copy = arr.copy()
    n = arr.shape[0]

    for i in range(0, n // 2, 2):
        copy[i] = arr[n - i - 1]
        copy[n - i - 1] = arr[i]

    return copy


def _get_cmap_from_namestring(
    name: Union[str, LinearSegmentedColormap]
) -> LinearSegmentedColormap:
    """
    Get the LinearSegmentedColormap colormap from the `name` string.
    If `name` is a LinearSegmentedColormap already, just return that.
    """

    if isinstance(name, str):
        if name.startswith("metalmaps."):
            cmap_use = colormaps[name]
        else:
            cmap_use = colormaps["metalmaps." + name]
        return cmap_use
    elif isinstance(name, LinearSegmentedColormap):
        return name
    else:
        raise TypeError(
            "cmap you provided is invalid data type",
            type(cmap),
            "needs to be string or LinearSegmentedColormap",
        )


def get_colorlist_from_colormap(cmap: Union[str, LinearSegmentedColormap]) -> List[str]:
    """
    Generate a list of 10 colors based on the provided colormap. This function
    will attempt to re-order the colors in the list in order to improve visibility
    and hopefully make the colors distinguishable on a line plot.

    Parameters
    ---------
    cmap: str or LinearSegmentedColormap
        Colormap to work with.

    Returns
    -------
    colorlist: list[str]
        A list of colors in hex format based on the colormap.
    """

    cmap = _get_cmap_from_namestring(cmap)

    cols = [cmap.__call__(x) for x in linspace(0.0, 1.0, 10, endpoint=True)]
    cols = array(cols)

    # add up "score" - things I made up to hopefully make
    # similar colors be far away from each other on the cycle

    score = zeros(cols.shape[0])

    score += argsort(cols[:, 0])
    score += argsort(cols[:, 1])
    score += argsort(cols[:, 2])

    score /= score.sum()

    # convert RGBA to perceived greyscale luminance
    # cf. http://alienryderflex.com/hsp.html
    # based on https://jakevdp.github.io/blog/2014/10/16/how-bad-is-your-colormap/
    rgb_weight = [0.299, 0.587, 0.114]
    luminance = sqrt(dot(cols[:, :3] ** 2, rgb_weight))

    luminance /= luminance.sum()
    score *= luminance

    cols = cols[argsort(score)]
    cols = _scrabmle(cols)

    colorlist = [to_hex(rgb) for rgb in cols]

    if cmap.name.endswith("_r"):
        # revert order for reverse colormaps
        colorlist = colorlist[::-1]

    return colorlist


def set_color_cycle(cmap: Union[str, LinearSegmentedColormap]) -> None:
    """
    Generate color cycler colors from the colormap, and
    make matplotlib use it.

    Note: This sets the global color cycle. If you change it
    multiple times throughout your plotting script, only the
    last call before the drawing of the figure will stick,
    since the translation from the color cycle color names
    "CN", N in [0,9], only occurs then.

    Parameters
    ----------

    cmap: str or LinearSegmentedColormap
        color map to use.

    """

    cmap_use = _get_cmap_from_namestring(cmap)
    colorlist = get_colorlist_from_colormap(cmap_use)
    rc("axes", prop_cycle=(cycler("color", colorlist)))

    return
