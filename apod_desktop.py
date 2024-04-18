"""
COMP 593 - Final Project

Description:
  Downloads NASA's Astronomy Picture of the Day (APOD) from a specified date
  and sets it as the desktop background image.

Usage:
  python apod_desktop.py [apod_date]

Parameters:
  apod_date = APOD date (format: YYYY-MM-DD)
"""

import os
import sys
import requests
import sqlite3
from datetime import date
from hashlib import sha256
from pathlib import Path
import ctypes
from image_lib import set_desktop_background_image


# Define the path for the image cache folder and database using pathlib for better handling
script_dir = Path(__file__).parent
image_cache_dir = script_dir / 'images'
image_cache_db = image_cache_dir / 'image_cache.db'

def main():
    apod_date = get_apod_date() # DO NOT CHANGE THIS FUNCTION #
                                # Get the APOD date from the command line

    # Initialize the image cache
    init_apod_cache()
    
    # Fetch APOD data
    apod_data = fetch_apod_data(apod_date)
    if apod_data:
        apod_id = add_apod_to_cache(apod_data)
        if apod_id:
            apod_info = get_apod_info(apod_id)
            if apod_info and 'file_path' in apod_info:
                set_desktop_background_image(apod_info['file_path'])

def get_apod_date():
    """Gets the APOD date
     
    The APOD date is taken from the first command line parameter.
    Validates that the command line parameter specifies a valid APOD date.
    Prints an error message and exits script if the date is invalid.
    Uses today's date if no date is provided on the command line.

    Returns:
        date: APOD date
    """
     # TODO: Complete function body
    try:
        return date.fromisoformat(sys.argv[1])
    except (IndexError, ValueError):
        return date.today()

def init_apod_cache():
     """Initializes the image cache by:
    - Creating the image cache directory if it does not already exist,
    - Creating the image cache database if it does not already exist.
    """
     image_cache_dir.mkdir(parents=True, exist_ok=True) # Create directory if it doesn't exist
     if not image_cache_db.exists():
        with sqlite3.connect(image_cache_db) as conn:
            conn.execute('''
                CREATE TABLE IF NOT EXISTS apod (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    date TEXT UNIQUE,
                    title TEXT,
                    explanation TEXT,
                    url TEXT,
                    hdurl TEXT,
                    media_type TEXT,
                    image_path TEXT,
                    image_hash TEXT UNIQUE
                );
            ''')
            conn.commit()
# TODO: Create the image cache directory if it does not already exist
# TODO: Create the DB if it does not already exist

def fetch_apod_data(apod_date):
    """Fetches APOD data from NASA API."""
    API_KEY = "MBY8qG63gsJ0imaKEIoT1B8r0vs7oBkbLJagPGYs"
    url = f"https://api.nasa.gov/planetary/apod?api_key={API_KEY}&date={apod_date.isoformat()}"
    response = requests.get(url)
    return response.json() if response.status_code == 200 else None

    # TODO: Download the APOD image
    # Hint: Use a function from image_lib.py 

def add_apod_to_cache(apod_data):
    """Adds the APOD image from a specified date to the image cache.
     
    The APOD information and image file is downloaded from the NASA API.
    If the APOD is not already in the DB, the image file is saved to the 
    image cache and the APOD information is added to the image cache DB.

    Args:
        apod_date (date): Date of the APOD image

    Returns:
        int: Record ID of the APOD in the image cache DB, if a new APOD is added to the
        cache successfully or if the APOD already exists in the cache. Zero, if unsuccessful.
    """
    image_url = apod_data['url']
    response = requests.get(image_url)
    if response.status_code == 200:
        image_path = image_cache_dir / f"{apod_data['date']}{Path(image_url).suffix}"
        with open(image_path, 'wb') as file:
            file.write(response.content)
        image_hash = sha256(response.content).hexdigest()
        with sqlite3.connect(image_cache_db) as conn:
            conn.execute('''
                INSERT OR IGNORE INTO apod (date, title, explanation, url, hdurl, media_type, image_path, image_hash)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?);
            ''', (apod_data['date'], apod_data['title'], apod_data['explanation'], 
                  apod_data['url'], apod_data.get('hdurl'), apod_data['media_type'], str(image_path), image_hash))
            conn.commit()
            return conn.execute('SELECT last_insert_rowid()').fetchone()[0]
    else:
        print('Failed to download the APOD image:', response.text)
        return None
    
    # TODO: Download the APOD information from the NASA API
    # Hint: Use a function from apod_api.py

    # TODO: Download the APOD image
    # Hint: Use a function from image_lib.py 

    # TODO: Check whether the APOD already exists in the image cache
    # Hint: Use the get_apod_id_from_db() function below

    # TODO: Save the APOD file to the image cache directory
    # Hint: Use the determine_apod_file_path() function below to determine the image file path
    # Hint: Use a function from image_lib.py to save the image file

    # TODO: Add the APOD information to the DB
    # Hint: Use the add_apod_to_db() function below



def get_apod_id_from_db(image_sha256):
    """Gets the record ID of the APOD in the cache having a specified SHA-256 hash value
    
    This function can be used to determine whether a specific image exists in the cache.

    Args:
        image_sha256 (str): SHA-256 hash value of APOD image

    Returns:
        int: Record ID of the APOD in the image cache DB, if it exists. Zero, if it does not.
    """
    # TODO: Complete function body
    return 0

def determine_apod_file_path(image_title, image_url):
    """Determines the path at which a newly downloaded APOD image must be 
    saved in the image cache. 
    
    The image file name is constructed as follows:
    - The file extension is taken from the image URL
    - The file name is taken from the image title, where:
        - Leading and trailing spaces are removed
        - Inner spaces are replaced with underscores
        - Characters other than letters, numbers, and underscores are removed

    For example, suppose:
    - The image cache directory path is 'C:\\temp\\APOD'
    - The image URL is 'https://apod.nasa.gov/apod/image/2205/NGC3521LRGBHaAPOD-20.jpg'
    - The image title is ' NGC #3521: Galaxy in a Bubble '

    The image path will be 'C:\\temp\\APOD\\NGC_3521_Galaxy_in_a_Bubble.jpg'

    Args:
        image_title (str): APOD title
        image_url (str): APOD image URL
    
    Returns:
        str: Full path at which the APOD image file must be saved in the image cache directory
    """
    # TODO: Complete function body
    # Hint: Use regex and/or str class methods to determine the filename.
    return

def get_apod_info(image_id):
    """Gets the title, explanation, and full path of the APOD having a specified
    ID from the DB.

    Args:
        image_id (int): ID of APOD in the DB

    Returns:
        dict: Dictionary of APOD information
    """
    # TODO: Query DB for image info
    # TODO: Put information into a dictionary
    apod_info = {
        #'title': , 
        #'explanation': ,
        'file_path': 'TBD',
    }
    return apod_info

import sqlite3


def get_all_apod_titles():
    """Gets a list of the titles of all APODs in the image cache

    Returns:
        list: Titles of all images in the cache
    """
    # Connect to the SQLite database
    conn = sqlite3.connect(
        "path_to_image_cache.db"
    )  # Replace 'path_to_image_cache.db' with the actual path
    cursor = conn.cursor()

    # Query the database to fetch all titles
    cursor.execute("SELECT apod_title FROM apod_images")
    titles = cursor.fetchall()

    # Close the database connection
    conn.close()

    # Extract titles from the fetched data
    title_list = [title[0] for title in titles]

    return title_list


def set_desktop_background_image(image_path):
    """Sets the desktop background image to a specific image.

    Args:
        image_path (str): Path of image file

    Returns:
        bool: True, if successful. False, if unsuccessful.
    """
    print(f"Setting desktop background to {image_path}...", end="")
    try:
        # Use ctypes to set desktop background (Windows-specific)
        SPI_SETDESKWALLPAPER = 20
        if ctypes.windll.user32.SystemParametersInfoW(
            SPI_SETDESKWALLPAPER, 0, image_path, 3
        ):
            print("success")
            return True
        else:
            print("failure")
            return False
    except Exception as e:
        print("failure")
        print(f"Error: {e}")
        return False


if __name__ == '__main__':
    main()
