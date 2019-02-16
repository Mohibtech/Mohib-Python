##########################################################
##########################################################
# Help
# Create a folder "output"
# Run me with a gaana.com url
#
# ./gaanascript.py "https://gaana.com/playlist/gaana-dj-bollywood-top-50-1"
#
# If all went good all the songs in url will be saved in mp3 format in output folder
##########################################################
##########################################################
from _future_ import unicode_literals
import sys
import argparse
import os
import random
import time
import shutil
import requests
import urllib
import string
import youtube_dl
from bs4 import BeautifulSoup
 
 
 
##########################################################
# this class uses youtube_dl to download mp3 version of youtube video
##########################################################
class YouTube:
    def _init_( self , url ):
        self.__save_youtube_mp3( url , "output")
 
    def __save_youtube_mp3 ( self , url , subfolder ):
        #get location
        outtmpl = "{}/%(title)s.%(ext)s".format( subfolder )
 
        #options for audio downloader
        ydl_opts = {
            'ignoreerrors':True,
            'outtmpl': outtmpl ,
            'noplaylist' : True ,    # we can set this to False if playlist
            'extract-audio' : True,  # only keep the audio
            'audio-format' : "mp3",  # convert to mp3
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
            }],
            'download_archive' : 'archive.txt',
        }
 
        #download video
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download( [ url ] )
 
 
 
 
##########################################################
# this class takes gaana.com info and searches youtube to find a valid url
##########################################################
class YouTubeSearch:
    def _init_(self , query ):
        query = self.__clean( query )
        self.result_url = ''
        self.url = "https://www.youtube.com/results?search_query={}".format(query)
        self.__parse_url()
        print "youtube result={}".format(self.result_url)
 
 
    def __clean(self , word):
        return ''.join(letter for letter in word.lower() if 'a' <= letter <= 'z' or letter == '+')
 
 
    def __parse_url ( self ):
        print "Parsing yt url : {}".format( self .url )
        #download web page
        page = requests.get( self.url )
        #check return status
        if page.status_code == 200 :
            soup = BeautifulSoup(page.content, 'html.parser')
            #print soup
            self.parse_soup ( soup )
        else :
            print "Failed in parsing url :{}".format(url)
 
 
    def parse_soup ( self , soup ):
        #sleep for random time
        #google sometimes notices scripted downloads and webpage hits
        #providing random sleep time bypasses this check
        #self.rand_sleep()
 
        #find all divs with id contents
        divs = soup.find_all('div', class_='yt-lockup yt-lockup-tile yt-lockup-video vve-check clearfix')
        for div in divs :
            video_id = div["data-context-item-id"]
            self.result_url = "https://www.youtube.com/watch?v={}".format(video_id)
            break
 
 
    def rand_sleep ( self ):
        #get random sleep secs
        secs = random.randint(0,30)
        #echo sleep time
        print "Sleeping for {} seconds".format(secs)
        #sleep for time
        time.sleep ( secs )
 
    def get_result_url( self ):
        return self.result_url
 
 
 
##########################################################
# a helper class to save individual gaana.com songs
##########################################################
class GaanaInfo:
    def _init_( self , title ):
        self.title = title
        self.singers = []
        self.result_url = ''
 
    def set_result_url ( self , result_url ):
        self.result_url = result_url
 
    def get_result_url ( self ):
        return self.result_url
 
    def is_result_url_valid ( self ):
        return len(self.result_url) > 0
 
    def add_singer ( self , singer ):
        self.singers.append ( singer )
 
    def get_url ( self ):
        url = self.title
        for singer in self.singers:
            url = url +" "+singer
        return url.replace(" ","+")
 
 
 
##########################################################
# this class parses the gaana webpage and extracts song information
# artists and title
##########################################################
class GaanaParser :
    def _init_( self , url ):
        print "Parsing gaana url :{}".format(url)
        self.url = url
        self.gaanainfos = []
        #start parsing the page
        self._parse_page()
 
 
    def _parse_page ( self ):
        #download web page
        page = requests.get( self.url )
        #check return status
        if page.status_code == 200 :
            print ("Parsing success")
            soup = BeautifulSoup(page.content, 'html.parser')
            self.parse_soup ( soup )
        else :
            print ("Failed in parsing")
 
 
    def parse_soup ( self ,  soup ):
        #find all divs with class link
        tags = soup.find_all('li', class_='draggable')
        #iterate over tags
        for tag in tags:
            self.__parse_draggable ( tag )
 
        #we have collected all gaanainfos parse them
        self.__parse_gaanainfos()
 
 
    def __parse_draggable ( self , ul_tag ):
        title = self.__get_song_title( ul_tag )
        singers = self.__get_song_singers ( ul_tag )
        #create gaana info
        gaanainfo = GaanaInfo ( title )
        for singer in singers :
            gaanainfo.add_singer (singer)
        #append to array
        self.gaanainfos.append ( gaanainfo )
 
 
    def __get_song_title ( self , ul_tag ):
        #get the li tag where song name is saved
        li_tag = self.get_child ( ul_tag , "li" , 2 )
        #get the div tag where name is saved
        div_tag = self.get_child ( li_tag.div , "div" , 1 )
        #get the a_tag where name is finally saved
        return div_tag.a.getText()
 
 
    def __get_song_singers ( self , ul_tag ):
        singers = []
        #get the li tag where singers is saved
        li_tag = self.get_child ( ul_tag , "li" , 3 )
        #get the a tags where name is saved
        a_tags = li_tag.div.find_all ("a")
        #each a_tag has a singer
        for a_tag in a_tags :
            singers.append (a_tag.getText())
 
        #return singers
        return singers
 
 
    def __parse_gaanainfos ( self ):
        for gaanainfo in self.gaanainfos :
            self.__parse_gaanainfo ( gaanainfo )
 
 
    def __parse_gaanainfo ( self , gaanainfo ):
        self.__set_gaanainfo_result( gaanainfo )
        self.__download_gaanainfo_result( gaanainfo )
 
 
    def __download_gaanainfo_result ( self , gaanainfo ):
        #check if result_url is valid
        if not gaanainfo.is_result_url_valid() : return
        #result valid save mp3
        youtube = YouTube ( gaanainfo.get_result_url() )
 
 
    def __set_gaanainfo_result ( self , gaanainfo ):
        #create ytsearch
        ytsearch = YouTubeSearch (gaanainfo.get_url())
        #get the result url
        result_url = ytsearch.get_result_url()
        #save to gaanainfo
        gaanainfo.set_result_url ( result_url )
 
 
    def get_child ( self , parent_tag , child_tag , index ):
        #get all child tags
        tags = parent_tag.find_all (child_tag)
        #find the correct index
        return tags[index]
 
 
 
##########################################################
# main
##########################################################
if __name__ == "__main__":
    if len (sys.argv) == 1 :
        print "Please pass the gaana.com url as parameter"
    else :
        url = sys.argv[1]
        gp = GaanaParser( url )