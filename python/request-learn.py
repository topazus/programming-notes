# curl -X "GET"
#  "https://api.spotify.com/v1/search?q=Muse&type=track&market=US&limit=5&offset=5"
#  -H "Accept: application/json"
#  -H "Content-Type: application/json"
#  -H "Authorization: Bearer BQCLWU4DU4lhIzsL7Wb4Bm4dTzV4d0iXdCzsl0fWELGUk-RkMatL50vLVIpU3CmeJBgHuk7DGGL8VqiJv-kaZ9XTVRc2qkSErPxbfQn0ak0raYdLDobIe-dnNrOPGYKQi072HsGdZVmVqw9qntB2Cocgq8V6GjFUAeP1Or9o7_I"
import json
from pprint import pprint
import requests

url = "https://api.spotify.com/v1/search?q={query}&type=track,artist".format(
    query="Little Simz"
)

header = {
    "content-type": "application/json",
    "accept": "application/json",
    "authorization": "Bearer BQB4_cpKdzpRGo8LNCieZuDBp8hDbxpI0wxGXSNJclfXRu1qRVez1mrpyI-h8tbCi1bbQiW4Co4pop0q6l98hPA9DE_dKEJ6CcmAyBCCRDvfnvZdlYRDGpH-GFYqb9OgyIyfG8q-2cXl-y97a-aek1zWfKr-nnR9LthIyFP22nk",
}
response = requests.get(url, headers=header)
pprint(response.json())
