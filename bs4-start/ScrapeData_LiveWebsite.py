from bs4 import BeautifulSoup
import requests

# Fetch the Hacker News page
response = requests.get("https://news.ycombinator.com/news")
yc_web_page = response.text

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(yc_web_page, "html.parser")

# Find all span tags with the class "titleline"
span_tags = soup.find_all(name="span", class_="titleline")

# List to store article titles, links, and upvotes
article_texts = []

# Loop through each span tag and find the 'a' tag within it to get the title and link
for span_tag in span_tags:
    # Find the 'a' tag within the 'span' tag
    article_tag = span_tag.find(name="a")
    if article_tag:
        # Get the article title
        article_title = article_tag.getText()
        # Get the article link
        article_link = article_tag['href']

        # Print the title and link
        print(f"Title: {article_title}")
        print(f"Link: {article_link}")
        print()

        # Append title and link to article_texts list
        article_texts.append((article_title, article_link))

# Find all span tags with the class "score" and extract the upvote count
article_upvotes = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]

# Find the index of the article with the highest upvotes
if article_upvotes:
    largest_number = max(article_upvotes)
    largest_index = article_upvotes.index(largest_number)

    # Print the article with the highest upvotes
    print("Article with the most upvotes:")
    print(f"Title: {article_texts[largest_index][0]}")
    print(f"Link: {article_texts[largest_index][1]}")
    print(f"Upvotes: {largest_number}")
else:
    print("No articles found.")

# Optional: Print a message if no articles are found
if not span_tags:
    print("No articles found.")
