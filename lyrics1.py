import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import lyricsgenius

def get_lyrics(artist_name, song_name):
    try:
        # Provide your Genius API token here
        genius = lyricsgenius.Genius("YOUR_GENIUS_API_TOKEN_HERE")

        # Search for songs by the specified artist and title
        song = genius.search_song(song_name, artist_name)

        if song:
            return song.lyrics
        else:
            return "Lyrics not found for the specified song and artist."
    except Exception as e:
        return "An error occurred: {}".format(e)

def show_lyrics():
    artist_name = artist_entry.get()
    song_name = song_entry.get()

    if not artist_name or not song_name:
        messagebox.showerror("Error", "Please enter both artist and song names.")
        return

    lyrics = get_lyrics(artist_name, song_name)
    lyrics_text.config(state="normal")
    lyrics_text.delete(1.0, tk.END)
    lyrics_text.insert(tk.END, lyrics)
    lyrics_text.config(state="disabled")

    # Enable download button
    download_button.config(state="normal")

def download_lyrics():
    lyrics = lyrics_text.get(1.0, tk.END)
    if lyrics.strip():
        with open("lyrics1.txt", "w", encoding="utf-8") as file:
            file.write(lyrics)
        messagebox.showinfo("Download", "Lyrics downloaded successfully as lyrics.txt")
    else:
        messagebox.showerror("Error", "No lyrics to download.")

# Create the main window
window = tk.Tk()
window.title("Song Lyrics Extractor")
window.geometry("400x450")
window.configure(bg="#c2e0ff")

# Create and place widgets
artist_label = tk.Label(window, text="Artist:", bg="#c2e0ff", fg="#134e6f")
artist_label.grid(row=0, column=0, padx=5, pady=5, sticky="e")

artist_entry = tk.Entry(window, width=30)
artist_entry.grid(row=0, column=1, padx=5, pady=5)

song_label = tk.Label(window, text="Song:", bg="#c2e0ff", fg="#134e6f")
song_label.grid(row=1, column=0, padx=5, pady=5, sticky="e")

song_entry = tk.Entry(window, width=30)
song_entry.grid(row=1, column=1, padx=5, pady=5)

get_lyrics_button = tk.Button(window, text="Get Lyrics", command=show_lyrics, bg="#0080ff", fg="#ffffff", relief=tk.FLAT)
get_lyrics_button.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

lyrics_text = tk.Text(window, wrap="word", width=40, height=15)
lyrics_text.grid(row=3, column=0, columnspan=2, padx=5, pady=5)
lyrics_text.config(state="disabled")

download_button = tk.Button(window, text="Download Lyrics", command=download_lyrics, bg="#ffffff", fg="#000000", relief=tk.FLAT, state="disabled")
download_button.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

# Start the GUI event loop
window.mainloop()
