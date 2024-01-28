# QR Code Generator #

## Overview ##
This script saves a QR code of a URL to a PNG file. It validates the URL and the file name beforehand.

## Installation ##

This script assumes that the machine where it is installed has access to the Internet.

Install the requirements first using this command:

`pip install -r requirements.txt`

It is recommended to install and use this software using a virtual environment:

```
python -m venv .env
source .env/bin/activate # source .env/Scripts/activate on Windows
pip install -r requirements.txt
```

## Usage ##

The script can be ran using the following:

`python make_qr.py <URL> <output file name>

The image file does not have to already exist. Please surround URL with quotes (" or '), particularly if it contains ampersands (&).

Examples:

```
python make_qr.py 'https://www.google.com' google_qr.png

python make_qr.py 'https://en.wikipedia.org/wiki/Ingenious_(board_game)' wikipedia_ingenious_qr.png
```
