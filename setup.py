import setuptools

with open("README.md", "r") as fh:

    long_description = fh.read()

setuptools.setup(
    install_requires=[
        'confluent-kafka',
        'Pillow',
        'numpy'
    ],
    name="raymondpang365", # Replace with your username
    version="1.0.0",
    author="Raymond Pang",
    author_email="raymondpang365@gmail.com>",
    description="A helper that wraps your service with messaging protocols",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/raymondpang365/endpoint-wrapper",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)