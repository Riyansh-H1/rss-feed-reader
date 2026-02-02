import feedparser

url = "https://blog.google/intl/en-in/feed/"
#input("Enter RSS feed URL: ")

feed = feedparser.parse(url)

# print("No. of entries", len(feed.entries) if len(feed.entries)!=0 else "No entries")
print(feed.entries[0].keys())
# print(feed.entries[0])
print("-"*50)
print("\nFeed Title:", feed.feed.title)
print("-"*50)
latest_entries = feed.entries[:1]
for i, entry in enumerate(latest_entries):
    title=entry["title"]
    summary = entry.get("summary", "no summary")
    link = entry.get("link", "no link")
    thumbnail = entry.get("media_thumbnail","no thumbnail")
    print(f"News {i+1}:\n")
    print("Title: ", title)
    print("Summary: ", summary)
    print("link: ", entry.get("id"))
    print("published on: ", entry.get("published"))


    print("\n"+"-"*50+"\n" if i!=4 else "")