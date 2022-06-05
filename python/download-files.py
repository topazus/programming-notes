import requests

# for small files
def download_file(url: str) -> None:
    get_response = requests.get(url, allow_redirects=True)
    file_name = url.split("/")[-1]
    # wb means write binary
    with open(file_name, "wb") as out_file:
        out_file.write(get_response.content)


# for large files
def download_file_with_requests(url: str, file_name: str) -> None:
    get_response = requests.get(url, allow_redirects=True, stream=True)
    filename = file_name
    with open(filename, "wb") as out_file:
        for chunk in get_response.iter_content(chunk_size=1024):
            if chunk:
                out_file.write(chunk)
                out_file.flush()


if __name__ == "__main__":
    url = "https://www.python.org/static/community_logos/python-logo-master-v3-TM.png"
    download_file(url)
    download_file_with_requests(url, "python.png")
