import requests as rq
from bs4 import BeautifulSoup as bs

def get_album_info(album_name: str, artist_name: str=None) -> dict:
    response = rq.get(f"https://en.wikipedia.org/wiki/{album_name}")
    parsed_html = bs(response.content, 'html.parser') if response.status_code == 200 else None
    
    if parsed_html is None:
        return {
            "status_code": response.status_code,
            "content": None,
            "album_name": album_name,
            "artist_name": artist_name
        }
    else:
        # Attempt to extract the following details:
        # 1. Release Year
        # 2. Genre Tags (if possible)
        # 3. Label
        # 4. Producer(s)
        # 5. Track number
        # 6. Length (if version is available)
        
        return {
            "status_code": response.status_code,
            "content": parsed_html,
            "album_name": album_name,
            "artist_name": artist_name
        }


def main():
    album_name = "Good_Kid,_M.A.A.D_City"
    print(f"Fetching information for album: {album_name}")
    print(get_album_info(album_name)['content'].prettify())


if __name__ == "__main__":
    main()