#authorisation keys
consumer_key="NvxD4eOpqZdfRBZt7G5k5cGbv" #Consumer key from twitter app
consumer_secret="Xs8FtbrnGNpbGznJVW6WGd8ZWSte6fVm5pEQNFtG4QYXnhyctb" #Consumer secret from twitter app
access_token="1516638805759229957-xRf0hucDZ6kbGtXoS1DfDjy1Ahm1WO" #access token from twitter app
access_token_secret="XHQrlBLKdtAM6iptL6JPSscoNKb5qoc5aOpXbcdoqZkna" #access secret from twitter app

import tweepy
import re
import pandas as pd
import time
import numpy as np
import pickle
import urllib.request
import shutil
import speech_recognition as sr 
import subprocess
import os

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth,wait_on_rate_limit=True)
try:
    import Image
except ImportError:
    from PIL import Image
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r".\Tesseract-OCR\tesseract.exe"

class MediaIncharge:
    photocount = 0
    videocount = 0
    phototext = []
    videotext = []
    normaltext= []
    
    
    def __init__(self):
        pass
    
     
    
    def saveFile(self,url,file_name):
       ##### raise ValueError('A very specific bad thing happened.')
        with urllib.request.urlopen(url) as response, open(file_name, 'wb') as out_file:
            shutil.copyfileobj(response, out_file)
    
    
    def getPhoto(self,url,pre):
        filename = pre+str(MediaIncharge.photocount)+".jpg"
        print(filename)
        self.saveFile(url,filename)
        MediaIncharge.photocount += 1
    
      
    def getVideo(self,url,pre):
        filename = pre+str(MediaIncharge.videocount)+".mp4"
        self.saveFile(url,filename)
        MediaIncharge.videocount += 1
    
       
    def photoToText(self,name,pre):
        filename = pre+name+".jpg"
        print(filename)
        from PIL import Image
        
        img = Image.open(filename).convert('L')
        
        img.save(filename, dpi=(100,100))
        return (pytesseract.image_to_string(Image.open(filename)))

     
    def wait_timeout(self,proc, seconds):
        """Wait for a process to finish, or raise exception after timeout"""
        start = time.time()
        end = start + seconds
        interval = min(seconds / 1000.0, .25)
        
        while True:
            result = proc.poll()
            if result is not None:
                return result
            if time.time() >= end:
                proc.kill()
                return "process killed"
                
            time.sleep(interval)

    
    def mp4towav(self,filename,savedFilename):
        command = "ffmpeg -i "+str(filename)+" -ab 160k -ac 2 -ar 44100 -vn "+str(savedFilename)+" "        
        print(command)
        p = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True) 
        
        self.wait_timeout(p,120)     
     
    
    def wavToText(self,wavFilename):
        
        str=""
        
        AUDIO_FILE = (wavFilename) 
        
       
        r = sr.Recognizer() 
        
        with sr.AudioFile(AUDIO_FILE) as source: 
        	#reads the audio file. Here we use record instead of 
        	#listen 
        	audio = r.record(source) 
        
        try: 
        	str= r.recognize_sphinx(audio)
            
        
        except sr.UnknownValueError: 
        	print("Sphinx could not understand audio") 
            
        
        except sr.RequestError as e: 
        	print("Sphinx error; {0}".format(e))
        return str    
     
        
    def videoToText(self,filename,savedFilename):
        self.mp4towav(filename,savedFilename)
        str = self.wavToText(savedFilename)
        
        return str

    
    def emptyFolder(self,path):
        folder = path
        for the_file in os.listdir(folder):
            file_path = os.path.join(folder, the_file)
            try:
                if os.path.isfile(file_path):
                    os.unlink(file_path)
                
            except Exception as e:
                print(e)
    
    
    def getImgandVideoofUser(self,userhandle):
        MediaIncharge.photocount = 0
        MediaIncharge.videocount = 0
        MediaIncharge.normaltext=[]
        try:
                 
            for tweet in tweepy.Cursor(api.user_timeline,id=userhandle,tweet_mode="extended",include_entities=True, count=5).items(5):
                MediaIncharge.normaltext.append(tweet.full_text)
                try:
                    x=tweet.extended_entities.get("media",[{}])
                except:
                    x=tweet.entities.get("media",[{}])
                for media in x:
                                      
                    if media.get("type",None) == "photo":
                        
                        
                        photo_url=media["media_url"]
                       
                        try:
                            self.getPhoto(photo_url,"images/")
                            
                        except:
                            pass
                        
                        
                        
                    if media.get("type",None) == "video":
                        
                        
                        video_url=media["video_info"]["variants"][0]["url"]
                        try:
                            self.getVideo(video_url,"videos/")
                            
                        except:
                            pass
                            
            self.implement_photoToText_singleuser() 
            self.implement_videoToText_singleuser()
           
        except:
            print("wait ...")
            time.sleep(900)
            
        self.emptyFolder('./images')  
        self.emptyFolder('./videos')  
        return(MediaIncharge.phototext,MediaIncharge.videotext,MediaIncharge.normaltext)           
                    
    def implement_photoToText_singleuser(self):
        s=""
        MediaIncharge.phototext = []
        for i in range(MediaIncharge.photocount):
            try:
                s= self.photoToText(str(i),"images/")
            except:
                pass
            MediaIncharge.phototext.append(s)
        return MediaIncharge.phototext   
    
    def implement_videoToText_singleuser(self):
        s=""
        MediaIncharge.videotext = []
        for i in range(MediaIncharge.videocount):
            try:
                s=self.videoToText("videos/"+str(i)+".mp4","videos/"+str(i)+".wav")
            except:
                pass
            MediaIncharge.videotext.append(s)
        return MediaIncharge.videotext   
               

#from mc import MediaIncharge
import pandas as pd


# Using our classifier
import pickle
with open('tfidfmodel.pickle','rb') as f:
    vectorizer = pickle.load(f)
    
with open('logis.pkl','rb') as f:
    classifier = pickle.load(f)    
    



class implement_arch:
    
    def listToString(self,list1):
        str1 = ' '.join(list1)
        return str1
    
    def calculate_indiv_score(self,sample):
        sample = vectorizer.transform([sample]).toarray()
        sentiment = classifier.predict(sample)
        return sentiment[0]
    
    def getTextscore(self,handle):
        if handle.strip() == "":
            return -1
            
        m1 = MediaIncharge()
        df = pd.DataFrame(data = {'handle': [handle],})
        df[['phototext', 'videotext','normaltext']] = df.apply(
                lambda row: pd.Series(m1.getImgandVideoofUser(row['handle'])), axis=1)
        strin0=self.listToString(df['normaltext'][0])
        strin1=self.listToString(df['phototext'][0])
        strin2=self.listToString(df['videotext'][0])
       
        score0=1-self.calculate_indiv_score(strin0)
        score1=1-self.calculate_indiv_score(strin1)
        score2=1-self.calculate_indiv_score(strin2)
        
        print(strin0)
        print(strin1)
        print(strin2)
        
        ma=0
        mb=0
        mc=0
        
        if strin0.strip() == "":
            print("empty")
            ma=1
            
        if strin1.strip() == "":
            print("empty")
            mb=1
            
        if strin2.strip() =="":
            print("empty")
            mc=1
        
        final_score=0
        if ma==0 and mb==0 and mc==0:
            final_score=0.50*score0 + 0.25*score1 +0.25*score2
        elif ma==0 and mb==0 and mc==1:
            final_score=0.75*score0 + 0.25*score1 
        elif ma==0 and mb==1 and mc==0:
            final_score=0.75*score0 + 0.25*score2 
        elif ma==0 and mb==1 and mc==1:
            final_score=score0 
        elif ma==1:
            final_score=-1 
    
        print([ma,mb,mc,score0,score1,score2])
        return (final_score)
            
        
#s=implement_arch()

#s.getTextscore("prin_temp")



from flask import Flask, render_template,request,url_for
from flask_bootstrap import Bootstrap 
#from arch import implement_arch

#s=implement_arch()

#s.getTextscore("prin_temp")

import random 
import time

app = Flask(__name__)
Bootstrap(app)

@app.route('/')
def index():
    
    return render_template('def_index.html')


@app.route('/analyse',methods=['POST'])
def analyse():
    start = time.time()
    
    if request.method == 'POST':
        rawtext = request.form['rawtext']
        
        #NLP Stuff
        s=implement_arch()
        final_score=s.getTextscore(rawtext)
        end = time.time()
        final_time = round(end-start,3)
        
        
        if rawtext.strip()=="":
            return render_template('def_index.html')
            
        
        
    return render_template('index.html',received_text = rawtext,final_score=final_score,final_time=final_time)








if __name__ == '__main__':
    app.run(debug=False)