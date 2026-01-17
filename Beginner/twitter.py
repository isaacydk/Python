import re
url = input("URL: ").strip()

if matches := re.search(r"^https?://(?:www\.)?twitter\.com/(\w+)$", url, re.IGNORECASE):
    print(f"Username: {matches.group(1)}")



# username = re.sub(r"(https?://)?(www\.)?twitter.com/", "", url)
# # username = url.removeprefix("https://twitter.com/")
# print(f"Username: {username}")
