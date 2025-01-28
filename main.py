from pexels_api_python.pexels_api import PexelsAPI

# Initialize the API with your API key
api_key = "API_KEY"
pexels = PexelsAPI(api_key)

# Search for photos
search_results = pexels.search_photos("nature")
print(search_results)

# Get details of a specific photo
#photo_details = pexels.get_photo(12345)  # Replace with a valid photo ID
#print(photo_details)

# Get popular photos
popular_photos = pexels.get_popular_photos()
print(popular_photos)