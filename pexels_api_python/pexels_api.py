import requests

class PexelsAPI:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "https://api.pexels.com/v1"

    def search_photos(self, query, per_page=15, page=1):
        """
        Search for photos on Pexels.

        :param query: Search query string.
        :param per_page: Number of results per page (default is 15).
        :param page: Page number to fetch (default is 1).
        :return: JSON response containing the search results.
        """
        headers = {
            "Authorization": self.api_key
        }
        params = {
            "query": query,
            "per_page": per_page,
            "page": page
        }
        response = requests.get(f"{self.base_url}/search", headers=headers, params=params)
        response.raise_for_status()  # Raise an exception for HTTP errors
        return response.json()

    def get_photo(self, photo_id):
        """
        Get details of a specific photo by its ID.

        :param photo_id: The ID of the photo.
        :return: JSON response containing the photo details.
        """
        headers = {
            "Authorization": self.api_key
        }
        response = requests.get(f"{self.base_url}/photos/{photo_id}", headers=headers)
        response.raise_for_status()
        return response.json()

    def get_popular_photos(self, per_page=15, page=1):
        """
        Get popular photos from Pexels.

        :param per_page: Number of results per page (default is 15).
        :param page: Page number to fetch (default is 1).
        :return: JSON response containing the popular photos.
        """
        headers = {
            "Authorization": self.api_key
        }
        params = {
            "per_page": per_page,
            "page": page
        }
        response = requests.get(f"{self.base_url}/popular", headers=headers, params=params)
        response.raise_for_status()
        return response.json()

# Example usage:
if __name__ == "__main__":
    # Replace 'your_api_key' with your actual Pexels API key
    api_key = "your_api_key"
    pexels = PexelsAPI(api_key)

    # Search for photos
    search_results = pexels.search_photos("nature")
    print(search_results)

    # Get a specific photo by ID
    photo_details = pexels.get_photo(12345)  # Replace with a valid photo ID
    print(photo_details)

    # Get popular photos
    popular_photos = pexels.get_popular_photos()
    print(popular_photos)