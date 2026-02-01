import feedparser

url = input("Enter RSS feed URL: ")

feed = feedparser.parse(url)

print("Feed title:", feed.feed.title)
