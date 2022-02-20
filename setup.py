import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="alexscherba",
    version="1.0",
    author="Alex Schebrakov",
    author_email="alexscherba29@gmail.com",
    description="Alex home assignment",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url= "https://alexscherba.jfrog.io/artifactory/api/pypi/alex_assignment_local",
    packages=setuptools.find_packages(),
    install_requires=[
        'requests'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
    python_requires='>=3.6',
)
