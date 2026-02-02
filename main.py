import feedparser

def fetch_entries(url):
    feed = feedparser.parse(url)
    entries = feed.entries
    if len(entries)==0:
        return "No entries found"
    return entries, feed


def display_entries(entries, feed):
    print("-"*50)
    print("Feed Title:", feed.feed.title)
    print("-"*50+"\n")

    choice = "y"
    i=1

    while choice.lower()=="y":
        entry = entries[i-1]
        print("News "+str(i)+":")
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
        print("\n"+"-"*50+"\n")
        if choice.lower()=="n":
            print("Thank you for using the RSS Feed Reader")
            print("\n"+"-"*50+"\n")
            exit()
        else:
            continue

def main():
    url="https://feeds.bbci.co.uk/news/rss.xml" #input("Enter The RSS Feed URL")
    if fetch_entries(url)=="No entries found":
        print(fetch_entries(url))
    else:
        entries, feed = fetch_entries(url)
        display_entries(entries, feed)

if __name__=="__main__":
    main()