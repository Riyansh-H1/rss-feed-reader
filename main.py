import feedparser

url="https://feeds.bbci.co.uk/news/rss.xml" #input("Enter The RSS Feed URL")

feed = feedparser.parse(url)
entries = feed.entries

print("-"*50)
#print("\nFeed Title:", feed.feed.title)
print("-"*50)

choice = "y"
i=1

while choice.lower()=="y":
    entry = entries[i-1]
    print("\n"+"-"*50+"\n")
    print("News"+str(i)+":")
    print()

    title=entry.get("title")
    summary = entry.get("summary", "no summary")
    link = entry.get("id", "no link")
    published = entry.get("published")

    print("Title: ", title)
    print("Summary: ", summary)
    print("link: ", link)
    print("published on: ", published)
    print("\n"+"-"*50+"\n")
    
    i+=1
    choice=input("Do you want to read more news? (y/n): ")
    if choice.lower()=="n":
        print("Thank you for using the RSS Feed Reader")
    else:
        continue
