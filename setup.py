from setuptools import find_packages, setup

VERSION = "0.0.1"
DESCRIPTION = "A document generator"
LONG_DESCRIPTION = "A more detailed description about the document generator"

# Setting up
setup(
    # the name must match the folder name 'verysimplemodule'
    name="radu",
    version=VERSION,
    author="Radu Gafita",
    author_email="radugaf@email.com",
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    packages=find_packages(exclude=["*.tests", "*.tests.*", "tests.*", "tests"]),
    install_requires=[],  # add any additional packages that
    # needs to be installed along with your package. Eg: 'caer'
    keywords=["python", "first package"],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Education",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ],
    scripts=[],
)

