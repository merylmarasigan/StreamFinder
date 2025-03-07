
import tkinter as tk
from tkinter import messagebox, scrolledtext
import requests
import json
from dotenv import load_dotenv
import os

# ✅ Load .env file
load_dotenv()

# ✅ Retrieve API key
API_KEY = os.getenv("API_KEY")

# ✅ Debugging: Print API Key to check if it's loaded
if not API_KEY:
    raise ValueError("Missing API_KEY! Make sure it's set in your environment or .env file.")

headers = {
    "accept": "application/json",
    "Authorization": f"Bearer {API_KEY}"
}

def search():

    # calling the API that will get the movies with the given name in its title
    result_label.delete("1.0", tk.END)
    url = "https://api.themoviedb.org/3/search/"


    name = entry.get()
    type = var.get()
    if type == "series":
        m = "tv?query="
        url += m
    else:
        m = "movie?query="
        url += m

    #replacing spaced with %20 to url-ify multi-word titles
    name = name.replace(" ", "%20")

    #eliminating any non alphanumeric characters that could end up in the middle of a word
    to_replace = ["'","-",":"]

    for char in to_replace:
        name = name.replace(char,"")

    url += name
    url += "&include_adult=true&language=en-US&page=1"

    print(f'generated url:{url}')
    response = requests.get(url, headers= headers)

    ids = [] 
    #ids will have (name, id) pairs for the movies that have the given in its title

    if response.status_code == 200:
        data = response.json()
        
        for e in data['results']:
            if type == "series":
                title = e['original_name']
            else:
                title = e['original_title']
                
            # doing some text cleaning and replacing the %20 with " " again for comparison with names in db
            unmodified_name = name.replace("%20", " ").lower()
            
            
            modified_title = title.replace("-", "").replace("'","").replace(":", "").lower()


            if unmodified_name in modified_title.lower():
                print(f'{unmodified_name} found in title:{modified_title}')
                id = e['id']
                ids.append((title,id))
            else:
                print(f'{unmodified_name} not found in title:{modified_title}')
    else:
        print('REQUEST FAILED')
    streamings = ""

    #going through the (name,id) pairs in ids and access the providers endpoint to see the providers of the movie/series
    for TI_combo in ids:

        if type == 'series':
            url = f'https://api.themoviedb.org/3/tv/{TI_combo[1]}/watch/providers'
        else:
            url = f'https://api.themoviedb.org/3/movie/{TI_combo[1]}/watch/providers'
        response = requests.get(url,headers=headers)

        if response.status_code == 200:
            data = response.json()
            

            for country in data['results']:
                #separating by country 
                keys = [k for k in data['results'][country].keys()]
                mod = keys[1]
                l = data['results'][country][str(mod)]             
                providers = ",".join([i['provider_name'] for i in l])
                media_title = TI_combo[0]
                
                streamings += f'You can watch {media_title} on {providers} in {country}\n'
        else:
            print(f'cannot get provider info for {TI_combo}')
    
    if streamings == "":
        streamings = "No results found"


    
    result_label.insert(tk.END, streamings)

def resize_widgets(event):
    """Ensure the result_label expands properly within the window."""
    result_label.pack_configure(fill=tk.BOTH, expand=True)  # Ensure it resizes properly

# UI Setup
root = tk.Tk()
root.title("Movie/TV Finder")
root.geometry("800x600")  # Set initial size

# Movie Title Entry
tk.Label(root, text="Enter Title:").pack()
entry = tk.Entry(root)
entry.pack()  # Expand horizontally

# Radio Buttons for Movie or TV Show
var = tk.StringVar(value="movie")
radio_movie = tk.Radiobutton(root, text="Movie", variable=var, value="movie")
radio_series = tk.Radiobutton(root, text="TV Show", variable=var, value="series")
radio_movie.pack()
radio_series.pack()

# Search Button
search_button = tk.Button(root, text="Search", command=search)
search_button.pack()

# Scrollable Text Widget
result_label = scrolledtext.ScrolledText(root, wrap=tk.WORD)
result_label.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

# Bind resize event
root.bind("<Configure>", resize_widgets)

root.mainloop()
