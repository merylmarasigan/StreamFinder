# StreamFinder

Movie/TV Finder

## 📌 Overview

Movie/TV Finder is a Python-based application that allows users to search for movies and TV shows and retrieve real-time streaming availability across multiple countries. The application integrates with TheMovieDB (TMDB) API and features a user-friendly GUI built with Tkinter.

## 🚀 Features

- Search for movies and TV shows by title

- Retrieve real-time streaming availability from TheMovieDB API

- Supports searching for both movies and TV series

- Interactive user interface using Tkinter

- Scrollable results display

- Error handling for failed API requests

## 🛠️ Technologies Used

Python (Core Programming Language)

Tkinter (GUI Framework)

Requests (Handling API Calls)

JSON (Data Handling)

Dotenv (Environment Variable Management)

## ⚙️ Setup and Installation

1️⃣ Clone the Repository

git clone https://github.com/merylmarasigan/movie-tv-finder.git
cd movie-tv-finder

2️⃣ Create and Activate a Virtual Environment

Windows (PowerShell)

python -m venv env
env\Scripts\Activate

Mac/Linux (Bash)

python3 -m venv env
source env/bin/activate

3️⃣ Install Dependencies

pip install -r requirements.txt

4️⃣ Set Up Environment Variables

Create a .env file in the root directory and add the following line:

API_KEY=your_tmdb_api_key_here

Note: Replace your_tmdb_api_key_here with your actual API key from TheMovieDB.

5️⃣ Run the Application

python app.py

## 🖥️ Usage

1. Enter a movie or TV show title in the input field.

2. Select whether it is a Movie or TV Show using radio buttons.

3. Click the Search button.

4. View streaming availability in the scrollable results box.
