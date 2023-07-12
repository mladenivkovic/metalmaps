#!/usr/bin/env python3

"""
Generate the gallery plots for a colormap as shown on
https://mladenivkovic.github.io/metalmaps/metalmaps.html

- a colorbar plot, including the lightness of the colormap
- a Kelvin Helmholtz instability
- a galaxy (NGC7496)
- a mass projection of a cosmological simulation (EAGLE 25)

This creates the plot for both the colormap and the reversed
colormap (suffix '_r')

usage:

    python3 generate_plots.py <colormap_name>

    <colormap_name> : name of the colormap to plot for.
    E.g. black_sabbath, NOT metalmaps.black_sabbath
"""

import matplotlib as mpl
from matplotlib import pyplot as plt
from matplotlib.colors import LinearSegmentedColormap
from mpl_toolkits.axes_grid1 import make_axes_locatable

import h5py
import numpy as np
import os, sys

import metalmaps


try:
    cmap = sys.argv[1]
except IndexError:
    print("Error: You need to provide the colormap to plot for as a cmdline arg.")
    print("E.g. python3 generate_plots.py black_sabbath")
    quit(1)


# Plot parameters
params = {
    "axes.labelsize": 9,
    "axes.titlesize": 9,
    "font.size": 9,
    "font.family": "serif",
    "figure.figsize": (5, 5),
    "figure.dpi": 100,
}
mpl.rcParams.update(params)


def add_colorbar(im, ax, fig):
    """
    add a nice colorbar to the plot which has the same size
    as the plot. Remove all ticks and labels from the colorbar.

    im: the image

    ax: the axis object you plotted on

    fig: the pyplot figure to work on
    """
    divider = make_axes_locatable(ax)
    cax = divider.append_axes("right", size="5%", pad=0.05)
    cbar = fig.colorbar(im, cax=cax)
    cbar.set_ticks([])
    cbar.set_ticklabels([])
    return


def savefig(cmap, plot, ax):
    """
    Save figure.

    cmap: which colormap this is. String.
    plot: which data we're plotting. E.g. "EAGLE", or "KH", or "NGC". String.
    ax: which axis we're working with.
    """

    filename = plot + "-" + cmap + ".png"
    plt.sca(ax)
    plt.savefig(filename, dpi=300)
    print("Saved", filename)
    plt.close()


def grayify_cmap(cmap):
    """Return a grayscale version of the colormap"""
    cmap = mpl.colormaps.get_cmap(cmap)

    colors = cmap(np.arange(cmap.N))

    # convert RGBA to perceived greyscale luminance
    # cf. http://alienryderflex.com/hsp.html
    RGB_weight = [0.299, 0.587, 0.114]
    luminance = np.sqrt(np.dot(colors[:, :3] ** 2, RGB_weight))
    colors[:, :3] = luminance[:, np.newaxis]

    return LinearSegmentedColormap.from_list(cmap.name + "_grayscale", colors, cmap.N)


def make_colorbar_plot(cmap):
    """
    Make a plot of the colormap as a colorbar, along with the
    lightness
    """

    fig = plt.figure(figsize=(8, 0.9))
    im = np.outer(np.ones(50), np.arange(512))

    color_ax = fig.add_subplot(2, 2, 1)
    color_ax_r = fig.add_subplot(2, 2, 2)
    gray_ax = fig.add_subplot(2, 2, 3)
    gray_ax_r = fig.add_subplot(2, 2, 4)

    fig.subplots_adjust(
        left=0.01, right=0.99, bottom=0.01, top=0.75, hspace=0.01, wspace=0.08
    )

    for ax in fig.axes:
        ax.axis("off")

    title_font = {"fontname": "monospace", "fontsize": 10}
    artist_font = {"fontname": "DejaVu Sans", "fontsize": 12}

    color_ax.imshow(im, cmap=cmap)
    color_ax.set_title(cmap, **title_font)

    color_ax_r.imshow(im, cmap=cmap + "_r")
    color_ax_r.set_title(cmap + "_r", **title_font)

    gray_ax.imshow(im, cmap=grayify_cmap(cmap))
    gray_ax_r.imshow(im, cmap=grayify_cmap(cmap + "_r"))

    figname = "colormap-" + cmap + ".png"
    plt.savefig(figname, dpi=150)
    print("Saved", figname)
    plt.close()

    return


def make_EAGLE_plot(cmap):
    """
    Make a plot using the EAGLE data.
    """

    srcfile = "mass_plots_eagle25.hdf5"

    hfile = h5py.File(srcfile, "r")

    rhoDM = hfile["dm_mass_map"][:]
    rhoDM = rhoDM / rhoDM.max()  # scale down to [0,1]
    rho = hfile["mass_map"][:]
    rho = rho / rho.max()  # scale down to [0,1]

    # make halt plot DM, half plot baryon
    rhoPlot = rhoDM[:]
    rhoPlot[:, rho.shape[0] // 2 :] = rho[:, rho.shape[0] // 2 :]

    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    im = ax.imshow(
        np.log10(rhoPlot),
        origin="lower",
        extent=(0, 1, 0, 1),
        #  norm = LogNorm(), # LogNorm fucks with the colorbar ticks?!?! So skip it.
        cmap=cmap,
    )

    add_colorbar(im, ax, fig)
    title = r"EAGLE 25"

    ax.set_title(title)
    ax.set_xlabel(r"x", usetex=True)
    ax.set_xticks([])
    ax.set_xticklabels([])
    ax.set_ylabel(r"y", usetex=True)
    ax.set_yticks([])
    ax.set_yticklabels([])
    plt.tight_layout()


def make_KH_plot(cmap):
    """
    Make a plot using the Kelvin-Helmholtz data.
    """

    srcfile = "kelvin-helmholtz.hdf5"

    hfile = h5py.File(srcfile, "r")
    data = hfile["data"]
    rho = data["density"]

    metadata = hfile["metadata"]
    time = metadata.attrs["time"]

    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    im = ax.imshow(
        np.log10(rho),
        origin="lower",
        extent=(0, 1, 0, 1),
        #  norm = LogNorm(), # LogNorm fucks with the colorbar ticks?!?! So skip it.
        cmap=cmap,
    )

    add_colorbar(im, ax, fig)
    title = r"$t = {0:.3f}$".format(time)

    ax.set_title(title)
    ax.set_xlabel(r"x", usetex=True)
    ax.set_ylabel(r"y", usetex=True)
    plt.tight_layout()
    savefig(cmap, "KH", ax)

    return


def make_NGC_plot(cmap):
    """
    Make a plot using the NGC image.
    """

    srcfile = "NGC7496.hdf5"

    hfile = h5py.File(srcfile, "r")

    rho = hfile["image"][:]
    rho = rho / rho.max()  # scale down to [0,1]

    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    im = ax.imshow(
        rho,
        extent=(0, 1, 0, 1),
        #  norm = LogNorm(), # LogNorm fucks with the colorbar ticks?!?! So skip it.
        cmap=cmap,
    )

    add_colorbar(im, ax, fig)
    title = r"NGC7496"

    ax.set_title(title)
    ax.set_xlabel(r"x", usetex=True)
    ax.set_xticks([])
    ax.set_xticklabels([])
    ax.set_ylabel(r"y", usetex=True)
    ax.set_yticks([])
    ax.set_yticklabels([])
    plt.tight_layout()
    savefig(cmap, "NGC", ax)

    return


# for line plots
x = np.linspace(0, 1.4, 200)


# for line plots
def y(x, phi):
    return np.sin(1.2 * np.pi * (x + 0.25) - 0.1 * phi)


def make_lineplot(cmap):
    """
    Make a line plot.
    """

    metalmaps.set_color_cycle(cmap)

    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)

    for i in range(10):
        col = "C" + str(i)
        cmap_colnames = metalmaps.colorcycle.get_colorlist_from_colormap(cmap)
        #  cmap_colnames = "#000000"
        plt.plot(x, y(x, i), lw=3, c=col, label=col + " - " + cmap_colnames[i])

    ax.set_xlabel(r"x", usetex=True)
    ax.set_xticks([])
    ax.set_xticklabels([])
    ax.set_ylabel(r"y", usetex=True)
    ax.set_yticks([])
    ax.set_yticklabels([])

    plt.legend(ncols=2, fontsize="small", loc="upper right")
    plt.tight_layout()
    savefig(cmap, "lineplot", ax)


if __name__ == "__main__":
    if not cmap.startswith("metalmaps."):
        cmap = "metalmaps." + cmap

    make_colorbar_plot(cmap)

    for suffix in ["", "_r"]:
        c = cmap + suffix
        make_KH_plot(c)
        make_EAGLE_plot(c)
        make_NGC_plot(c)
        make_lineplot(c)
