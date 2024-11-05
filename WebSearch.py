import webbrowser

def SearchQuery(text):
    if text:
        # Construct the search URL for the song
        search_url = f"https://www.google.com/search?q={text}"
        
        # Open the web browser with the search URL
        webbrowser.open(search_url)
        print(f"Searching for '{text}' on your web browser...")
    else:
        print("No query provided")

# Run the function
if __name__=='__main__':
    SearchQuery('how are transfromers used in the field of Ai')

