from urllib.parse import urlparse

url = "https://www.w3school.com"

parsed_url = urlparse(url)

if parsed_url.query:
    print("f{url} is a valid url with a query String")
else:
    print(f"{url} is not a valid url with a query String")