#Import necessary libraries
import spotipy
import spotipy.util as util
import tweepy

#Import credentials from files
from credentials_twt-copy import *
from credentials_spot-copy import *

#Authenticating using Twitter Developer Account
auth = tweepy.OAuthHandler(twt_api_key, twt_api_secret)
auth.set_access_token(twt_acc, twt_acc_secret)

client = tweepy.Client(consumer_key= twt_api_key,consumer_secret= twt_api_secret,access_token= twt_acc,access_token_secret= twt_acc_secret)

api = tweepy.API(auth)

#Authenticating Spotify
token = util.prompt_for_user_token(username,
                                   scope,
                                   client_id=spot_client_id,
                                   client_secret=spot_client_secret,
                                   redirect_uri=spot_redirect_uri)


spotify = spotipy.Spotify(auth=token)

#Loop to check for current track and getting details using spotipy library
while True:
    try:
        current_track = spotify.current_user_playing_track()
        current_track_id = current_track['item']['id']

        if current_track_id is not None:
            client.create_tweet(text="A is currently listening to:" + '\n' + current_track['item']['artists'][0]['name'] + " - " +
                                                            current_track['item']['name'] + '\n' + str(
                                                            current_track['item']['external_urls']['spotify']) + '\n' + "#" + str(
                                                            current_track['item']['artists'][0]['name']).replace(" ", ""))
            break
        else:
            continue
    except spotipy.client.SpotifyException:
        token = util.prompt_for_user_token(username,
                                           scope,
                                           client_id=spot_client_id,
                                           client_secret=spot_client_secret,
                                           redirect_uri=spot_redirect_uri)

        spotify = spotipy.Spotify(auth=token)
    except AttributeError:
        pass

#Second loop to check for new track
while True:
    try:
        new_track = spotify.current_user_playing_track()
        new_track_id = new_track['item']['id']

        if current_track_id is not None and new_track_id != current_track_id:
            client.create_tweet(text="A is currently listening to:" + '\n' + new_track['item']['artists'][0]['name'] + " - " + 
                                                            new_track['item']['name'] + '\n' + str(
                                                            new_track['item']['external_urls']['spotify']) + '\n' + "#" + str(
                                                            new_track['item']['artists'][0]['name']).replace(" ", ""))
            current_track_id = new_track_id
        else:
            continue
    except spotipy.client.SpotifyException:
        token = util.prompt_for_user_token(username,
                                           scope,
                                           client_id=spot_client_id,
                                           client_secret=spot_client_secret,
                                           redirect_uri=spot_redirect_uri)

        spotify = spotipy.Spotify(auth=token)
    except AttributeError:
        pass