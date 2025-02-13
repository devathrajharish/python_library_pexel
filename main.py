
# pip install pexels_api_python

from pexels_api_python import PexelsAPI

# Initialize the API with your API key
api_key = "API_KEY"
pexels = PexelsAPI(api_key)

# Search for photos with a query string

search_results = pexels.search_photos("mountains")

# Download the first photo from the search results

if search_results.get("photos"):
    first_photo = search_results["photos"][0]
    photo_url = first_photo["src"]["original"]
    pexels.download_photo(photo_url, "mountains.jpg")