# Spotify Public Playlist Data
Python script to get data from the Spotify API.

## Instructions

1. Add usernames to the array and set your desired filename. If you signed up for Spotify with Facebook, your username is a little tricky to find. On your profile page in the desktop application, click on the '...' menu next to your profile picture.  Select the 'Copy Spotify URI' and paste it somewhere. Your username is the series of numbers. 
``` Python
usernames = ['']
filename = "default.csv"
```

2. Follow instructions from Spotify to [create a developer application](https://developer.spotify.com/my-applications/#!/). After creating a develoepr application, add the client id and secret to the script.
``` Python
client_id = ''
client_secret = ''
```

3. In a terminal window, navigate to the folder containing the script file. Run the script. ([Download Python](https://www.anaconda.com/download/#macos) if you don't already have it.) 
``` Bash
python3 playlistDataToCsv.py
```
