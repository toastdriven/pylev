import os

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


setup(
    name="pylev",
    version="1.5.0-alpha",
    description="A pure Python Levenshtein implementation that's not freaking GPL'd.",
    author="Daniel Lindsley",
    author_email="daniel@toastdriven.com",
    long_description=open(
        os.path.join(os.path.dirname(__file__), "README.rst"), "r"
    ).read(),
    packages=["pylev"],
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        # That's right, works in Py3 (& PyPy) too!
        "Programming Language :: Python :: 3",
    ],
    url="http://github.com/toastdriven/pylev",
)
