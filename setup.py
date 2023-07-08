import setuptools

version = {}

with open("./metalmaps/__version__.py", "r") as fh:
    exec(fh.read(), version)

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="metalmaps",
    version=version["__version__"],
    description="Rock and Metal inspired Matplotlib colormaps.",
    url="https://github.com/mivkov/metalmaps",
    author="Mladen Ivkovic",
    author_email="mladen.ivkovic@hotmail.com",
    packages=setuptools.find_packages(),
    long_description=long_description,
    long_description_content_type="text/markdown",
    zip_safe=False,
    classifiers=[
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: GNU Lesser General Public License v3 or later (LGPLv3+)",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        "matplotlib",
    ],
)
