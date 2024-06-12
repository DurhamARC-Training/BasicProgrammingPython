import zipfile
from urllib.request import urlopen
import io

if __name__ == '__main__':
    REPO = "https://github.com/DurhamARC/BasicProgrammingPython"
    RELEASE = "June2024"
    url = f"{REPO}/archive/refs/tags/{RELEASE}.zip"
    print(f"Downloading {url}...)")
    with urlopen(url) as url_obj:
        zip_content = io.BytesIO(url_obj.read())

    with zipfile.ZipFile(zip_content) as zfile:
        zfile.extractall(".")
