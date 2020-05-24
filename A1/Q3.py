site = input("Enter url of a site: ").lower()

denied_urls = ["https://www.google.com", "https://www.facebook.com",
               "https://www.twitter.com", "https://www.amazon.com"]

for url in denied_urls:
    # with https: | with www. | just .com
    if site in [url, url[8:], url[12:]]:
        print("Access denied!")
