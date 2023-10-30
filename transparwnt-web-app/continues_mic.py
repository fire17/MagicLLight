print("Wait for it...")
import sys
sys.stdout.flush()
import speech_recognition as sr
import threading
import time
import keyboard
#import interpreter
from oi import interpreter
interpreter = interpreter.Interpreter()

import webbrowser
import os

interpreter

#from app import makeSmall, makeBig, start
import app

from keyboard_layout import get_keyboard

def do_flush():
    while True:
        sys.stdout.flush()
        time.sleep(0.01)
threading.Thread(target = do_flush,).start()


# Define the command
speak_command = '%USERPROFILE%\\nircmd.exe speak text $'
speak_command = 'C:\\Users\\User\\nircmd.exe speak text "$"'

threads = []
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame
import wave

await_1 = [False]
await_2 = False


audio_out = 'audio_out.mp3'
save_directory = os.path.expanduser("~/Desktop")
audio_out = os.path.join(save_directory, audio_out)

# Initialize the mixer module
pygame.mixer.init()

# Load the mp3 file

# Play the mp3 file
#from gtts import gTTS
import gtts
gTTS = gtts.gTTS
gtts.tts.Speed.NORMAL = True
gtts.tts.Speed.SLOW = None
stop_audio = [False]
from pydub import AudioSegment
from pydub.effects import speedup



def play_audio(file,speed = 1.2):
    #file_wav = wave.open(file)
    #frequency = file_wav.getframerate()
    #pygame.mixer.init()#frequency=frequency*speed)
    app.makeSize(220)
    stop_audio[0] = True
    pygame.mixer.music.load(file)
    pygame.mixer.music.play()
    stop_audio[0] = False
    while pygame.mixer.music.get_busy() and not stop_audio[0]:
        pass
    pygame.mixer.music.stop()
    app.makeSmall()
    pygame.mixer.quit()
    pygame.mixer.init()

  

def gSpeak(text, lang='he', do_speedup = True):
    # Create a gTTS text-to-speech object
    speech = gTTS(text, lang=lang, slow=False)
    # Save the speech audio into a file
    speech.save(audio_out)
    #TODO: Play Faster
    #print(":::",audio_out.replace("/","\\"))
    
    if do_speedup :
        audio = AudioSegment.from_mp3(audio_out.replace("/","\\"))
        new_file = speedup(audio,1.4)
        #do_speedup = False        
        #new_file = speedup(audio,1.7)
        #new_file = speedup(audio,1.3)
        new_file.export(audio_out.replace("/","\\"), format="mp3")
    
    gthread = threading.Thread(target=play_audio, args = (audio_out,))
    threads.append(gthread)
    gthread.start()

commands = {"reset": interpreter.reset
            ,}


# Run the command twice
#res = os.system('''echo %USERPROFILE%"''')
oldschool = False
#print(':::',res,"SYSTEM USER")

    
interpreter.auto_run = True
interpreter.api_key = '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'

# Initialize the recognizer
recognizer = sr.Recognizer()

next_up = []
defLanguage = 'iw-IL'
defLanguage = 'en-US'
done = [False]
control_key = 'ctrl+windows'  # Change this to the desired control key (e.g., 'ctrl', 'shift', 'alt')

def get_lang(key="speech_code"):
    current_keyboard = get_keyboard()
    return current_keyboard[key]

lang = [get_lang()]        
elabs_langs = ["en", "zh", "es", "hi", "pt", "fr", "de", "ja", "ar", "ko", "id", "it", "nl", "tr", "pl", "sv", "fil", "ms", "ro", "uk", "el", "cs", "da", "fi", "bg", "hr", "sk", "ta"]

import elabs
use_elabs = [False]

def speak(text, lang, speed = 1, volume = 100):
    global use_elabs
    lang = lang if "-" not in lang else lang.split("-")[0].lower()
    try:
        if oldschool:
            cmd = speak_command.replace("$",text)+f" {speed} {volume}"
            s = threading.Thread(target = lambda: os.system(cmd))
            threads.append(s)
            s.start()
        elif use_elabs[0] and (lang in elabs_langs):
            #app.makeSize(220)
            elabs.playText(text,lang,(app.makeSize,220),(app.makeSize,150))
            #app.makeSize(150)
        else:
            # gSpeak(text, lang = "en" if "en" in defLanguage else "iw")
            #lang = get_lang()
            gSpeak(text, lang )
    except:
        traceback.print_exc()
    #os.system(cmd)
    #print (" ::: SPOKEN", text)

background = "noisy_quick"
background = "normal"
#background = "noisy_quick"
dials = {
        "noisy_quick":{
            "pause_threshold":0.7001,
            "energy_threshold":2400,
            "non_speaking_duration":0.7},
        "noisy":{
            "pause_threshold":1.0001,
            "energy_threshold":2400,
            "non_speaking_duration":1},
        "normal":{
            "pause_threshold":1.0001, #0.7001,
            "energy_threshold":500,
            "non_speaking_duration":.7},
            }
import traceback

stream_back=True
clearOnce = [False]
def chat(text, lang, outloud = True):
    try:
        #result = interpreter.chat(text)
        #res = interpreter.chat(text, stream_back=stream_back)
        #print("TTTTTTT",type(res),res)
        #pretext = ""
        lastChunk = ""
        for chunk in interpreter.chat(text, stream_back=stream_back):
            #print("SSSSSSSSSS",type(stream),stream)
            #for chunk in stream:
            
            
            event, payload = chunk["event"], chunk["payload"]
            if event == "start_chat":
                if not clearOnce[0]:
                    clearOnce[0] = True
                    #app.clearText()
                    if payload == None or "last" not in payload:
                        app.sendText("\n\n ● ")
                    #pretext = "\n\n ● "
                else:
                    print(":::::::::::Mark new Conv piece")
                    if payload == None or "last" not in payload:
                        app.sendText("\n● *Answer:*\n")
                    
            elif event == "done":
                clearOnce[0] = False
            elif event == "finished_chat":
                #clearOnce[0] = False
                print("::::::::::::FFFFFFFFinished")
                #app.sendText("\n@@@")
                
            elif event == "start_call":
                print ("::::::::::::mark call")
                #app.sendText("<...")
                app.sendText("\n```\n")
            elif event == "finished_call":
                print (":::::::::::::mark finished call")
                app.sendText("\n```\n")
            elif event == "chunk":
                if payload["type"] == "content":
                    text = payload["data"]
                    if "last" not in payload:
                        app.sendText(text)
                        lastChunk = text
                    else:
                        if text == lastChunk:
                            print("dont send again 11111111")
                        elif len(text) != len(lastChunk):
                            if text[-1*len(lastChunk):] == lastChunk:
                                print("dont send again 2222222222")
                            else:
                                print("... DOUBLE oR NOTHING??  333333333")
                                app.sendText(text)
                        else:
                            print("???? 444444444 ",text,lastChunk)
                elif payload["type"] == "function_call":
                    # process it nicely
                    text = payload["data"]   
                    app.sendText(text)
                else:
                    print (":::::::::::::????",chunk)
            else:
                print("CCCCCCCCCC??????", chunk)
        #print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
        #print(interpreter.messages[-1]["content"])
        final = interpreter.messages[-1]["content"]
        #app.sendText(final)
        if outloud:
            speak(final, lang[0])
        #print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
    except:
        traceback.print_exc()
        print(" ::: Agent Failed :::")
    
from quick_answer import quick_answer
import random
### Text = [""]
Texts = []


def run_chat(Texts, await_1, lang):
    global use_elabs
    while not done[0]:
        sys.stdout.flush()
        ### if Text[0] != "":
        if len(Texts)>0 and not await_1[0]:#[0] != "":
            print("LLLLLLLLLLLLLLLLLLLL", lang[0], ":::", str(lang[0] if "-" not in lang[0] else lang[0].split("-")[0].lower()), ":::", use_elabs[0])
            use11 = (str(lang[0] if "-" not in lang[0] else lang[0].split("-")[0].lower()) in elabs_langs) and use_elabs[0]
            ### text, Text[0] = Text[0], ""
            #print("::: passing to chat...",Texts)
            app.makeSmall(-70)
            print("::: Please wait for agent to answer...", end="\r")#,Texts)
            text = "\n".join(Texts)
            Texts.clear()
            #print("::: passing to chat...",Texts)
            res = []
            #res.append(quick_answer(text))
            print("!!!!!!!!!!!!!!!",text)
            first_word = text.lower().split(" ")[0]
            #if first_word in ["exit"]:
            #    print("Exiting...")
            #    exit()
            if first_word in ["reset","clear"]:
                elabs.playText(f"resetai.wav",lang[0],(app.makeSize,220),(app.makeSize,150),file=True)
                interpreter.reset()
                time.sleep(2)
                app.clearText()
            elif first_word in ["disable","enable"]:
                if first_word == "disable":
                    print("disable 11Labs")
                    use_elabs[0] = False
                    elabs.playText(f"disable11.wav",lang[0],(app.makeSize,220),(app.makeSize,150),file=True)
                else:
                    print("enable 11Labs")
                    use_elabs[0] = True
                    elabs.playText(f"enable11.wav",lang[0],(app.makeSize,220),(app.makeSize,150),file=True)
            elif first_word in ["google","search","גוגל","חפש"]:
                prep, prep_file = True, "next_audio.wav"
                done_gen = [False]
                print("XXXXXXXXXXXXXX", prep, use11)
                if prep and use11:                    
                    elabs.prep_audio("searching "+" ".join(text.split(" ")[1:]), prep_file, done_gen)
                    #time.sleep(.5)
                    print("PRRRRRRREEEEEEPPPPING")
                    print("PRRRRRRREEEEEEPPPPING")
                    print("PRRRRRRREEEEEEPPPPING")
                    print("PRRRRRRREEEEEEPPPPING")
                    print("PRRRRRRREEEEEEPPPPING")
                    time.sleep(.9)
                #print("!!!!!!!!!!!!!!!",text)
                #gthread = threading.Thread(target=play_audio, args = ("chrome1.wav",))
                #threads.append(gthread)
                #gthread.start()
                elabs.playText(f"chrome{random.choice(range(3))+1}.wav",lang[0],(app.makeSize,220),(app.makeSize,150),file=True)
                url = "https://www.google.com/search?q="+"+".join(text.split(" ")[1:])
                webbrowser.open_new(url)
                #speak("Opening chrome, "+" ".join(text.split(" ")[1:]), lang[0])
                if not prep or not use11:
                    speak("searching "+" ".join(text.split(" ")[1:]), lang[0])
                else:
                    while(not done_gen[0]):
                        time.sleep(0.1)
                    elabs.playText(prep_file, lang,(app.makeSize,220),(app.makeSize,150),file=True)
                
            elif text.lower().split(" ")[0] in ["what","מה"]:
                res.append(quick_answer(text))
                if len(res) > 0:
                    answer = res.pop()
                    #print("QQQQQQQQQQQQQQQQQQQQ",answer)
                    cyan_text = f"\033[96m{answer}\033[0m"
                    print(cyan_text)
                    speak(answer, lang[0])
                
            else:
                new_task = threading.Thread(target=chat, args = (text,lang))
                new_task.start()
                threads.append(new_task)
        else:
            time.sleep(0.1)
            #print("waiting",Texts,await_1)
    

def check_rec_key():
    released_once = False
    while not done[0]:
        sys.stdout.flush()
        if keyboard.is_pressed(control_key):
            await_1[0] = True
            released_once = False
            time.sleep(0.01)
        else:
            if not released_once:
                released_once = True
                app.makeBig(-50)
            await_1[0] = False
            #print(await_1)
            
            time.sleep(0.1)

rec_thread = threading.Thread(target = check_rec_key )
rec_thread.start()
threads.append(rec_thread)

user_inputs = [""]

def check_user_inputs():
    try:
        while not done[0]:
            msg = input()
            if msg != "":
                user_inputs[0] = msg
                Texts.append(msg)
                #print(" ::: SENDING MANUAL TEXT TO AGENT :::",msg)
    except:
        done[0]=True
        exit()

check_user_inputs_thread = threading.Thread(target = check_user_inputs )
check_user_inputs_thread.start()
threads.append(check_user_inputs_thread)

RTL_LANGS = ["iw","ar"]

# Function to capture and recognize audio in a new thread
def recognize_audio(done, lang):
    while not done[0]:
        sys.stdout.flush()
        if len(next_up) > 0:
            try:
                ##if await_1[0]:
                #    await_2 = True
                #print("#######")
                audio = next_up.pop(0)
                # Recognize the audio
                #text = recognizer.recognize_google(audio, language=defLanguage)
                #lang = get_lang()
                #print(":::::::::::LANGUAGE:::::::::",lang)
                text = recognizer.recognize_google(audio, language=lang[0])
                yellow_text = f"\033[93m{text}\033[0m"
                print(yellow_text+"                                                                                        ")
                #speak(text)
                ### Text[0] = text
                Texts.append(text)
                if len(Texts)>1:
                    text = "\n"+text
                else:
                    app.clearText()
                    checkLang = lang[0] if "-" not in lang[0] else lang[0].split("-")[0].lower()
                    if checkLang in RTL_LANGS:
                        app.setDirectionRTL()
                    else:
                        app.setDirectionLTR()
                app.sendText(text+" ")
                #await_2 = False
                #print(text)
                #interpreter.chat(text)
            except sr.UnknownValueError:
                pass
                # Handle the case when recognition fails
            except sr.RequestError as e:
                print("Sorry, there was an error with the request. {0}".format(e))
        else:
            time.sleep(0.1)
            await_2 = False


# Create a new thread for recognition
recognition_thread = threading.Thread(target=recognize_audio, args=(done,lang))
chat_thread = threading.Thread(target=run_chat, args = (Texts, await_1, lang))

# Function to capture and recognize continuous audio
def listen_and_recognize(source):
    recognizer.pause_threshold = 1.0001 #0.7001 quick
    if recognizer.energy_threshold < dials[background]["energy_threshold"]:
        recognizer.energy_threshold = dials[background]["energy_threshold"]
    recognizer.non_speaking_duration = dials[background]["non_speaking_duration"] # 1 #0.7 quick
    audio = recognizer.listen(source)
    next_up.append(audio)
    #print("audio")

recognition_thread.start()
chat_thread.start()

def main_mic(done,lang):
    # Continuous listening loop
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source, 0.41)
        recognizer.dynamic_energy_threshold = False
        print("Listening... (Press and hold {} key to record)".format(control_key), end="\r")
        
        try:
            once = False
            once_not = False
            while not done[0]:
                sys.stdout.flush()
                if keyboard.is_pressed(control_key):
                    once_not = False
                    if not once:
                        lang[0] = get_lang()
                        #print(":::::::::::LANGUAGE:::::::::",lang)
                        ### await_1 = True                
                        print(f" ::: Recording... ({get_lang('native_name')})                                                " , end="\r")
                        app.makeBig()
                        app.prepWindow()
                    recognizer.operation_timeout = None
                    recognizer.energy_threshold = dials[background]["energy_threshold"]
                    listen_and_recognize(source)
                    if not once:
                        once = True
                        print("done listening                                                ",end="\r")
                else:
                    once = False
                    if not once_not:
                        once_not = True
                        #print(" :::                                                                    ", end="\r")#,Texts)
                        print(f" ::: Ready to Listen... (Press and hold {control_key} key to record)                                ", end="\r")#,Texts)
                        await_1[0] = False
                        app.makeSize(150)
                        
                    ### await_1 = False
                    #recognizer.operation_timeout = 0.01
                    recognizer.pause_threshold = 0.01
                    recognizer.non_speaking_duration = 0.001
                    recognizer.energy_threshold = 10000
                    time.sleep(0.01)
        except KeyboardInterrupt:
            # Ctrl+C was pressed, set the done flag to stop the thread
            done[0] = True

main_thread = threading.Thread(target=main_mic, args=(done,lang))
with_server = True
if with_server:
    main_thread.start()
    app.start(done)
else:
    main_mic(done,lang)
      
#recognition_thread.join()
#chat_thread.join()
#for t in threads:
    #t.join()
#    pass
print("\n\n ::: DONE :::                                               ")
exit(1)
