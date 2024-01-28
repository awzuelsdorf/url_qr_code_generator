import qrcode
import sys
from urllib.request import urlopen, URLError

def is_valid_url(url):
    """
    Determines if a URL can be accessed (valid).
    
    Returns true if access succeeds, false if access fails.
    """
    try:
        urlopen(url)
        return True
    except URLError:
        return False

def main():
    if len(sys.argv) != 3:
        sys.stderr.write(f"Usage: {sys.argv[0]} <URL> <PNG image file name>\n\nNote: image file does not have to already exist.\nPlease surround URL with quotes (\" or \'), particularly if it contains ampersands (&).\nNote: this script assumes you are using a computer with Internet access.\n")

        sys.exit(1)

    if not sys.argv[2].lower().endswith(".png"):
        sys.stderr.write(f"Received file name \"{sys.argv[2]}\" . Please make sure file name ends with \".png\"\n")
        sys.exit(1)

    if is_valid_url(sys.argv[1]):
        sys.stderr.write(f"The URL \"{sys.argv[1]}\" cannot be accessed. Please check your internet connection and your URL spelling.\n")
        sys.exit(1)

    img = qrcode.make(sys.argv[1])

    img.save(sys.argv[2])

    print(f"QR code for {sys.argv[1]} saved to {sys.argv[2]}")

if __name__ == "__main__":
    main()
