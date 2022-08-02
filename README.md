# spotify-twitter-bot
A twitter (music) bot which will tweet out the song currently being listened to on Spotify.

First things first, go on to https://developer.twitter.com/en and create our application (which will be using the Twitter API) under a Project (and not as a stand-alone app). Now within the Twitter developer portal navigate to Project and change the application's permissions to 'Read and write'. Generate the Keys and Tokens required and store them in a sperate file like, credentials_twt.py .

Move on to https://developer.spotify.com/dashboard/login and get your Client ID and Client Secret. Again, store these in a separate file like, credentials_spot.py .

Import required libraries, [Tweepy](https://www.tweepy.org/) and [Spotipy](https://spotipy.readthedocs.io/en/latest/#installation) .

Have your necessary files like requirements.txt and Procfile for deployment on Heroku.

Run spotify+twitter_bot.py

Code has been updated upon from https://github.com/haranlakha/spotify-tweet-bot
