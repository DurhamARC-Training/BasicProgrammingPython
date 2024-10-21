import zipfile
from urllib.request import urlopen
import io

if __name__ == '__main__':
    REPO = "https://github.com/DurhamARC-Training/BasicProgrammingPython"
    url = f"{REPO}/zipball/main"
    print(f"Downloading {url}...)")
    with urlopen(url) as url_obj:
        zip_content = io.BytesIO(url_obj.read())

    with zipfile.ZipFile(zip_content) as zfile:
        zfile.extractall(".")
