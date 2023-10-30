#elabs.py

from elevenlabs import set_api_key
#set_api_key("6699e11c3c0aa6d859912d06c561d02a")
set_api_key("8216e74caf815a05239387d29b2c1e5f")

from pprint import pprint as pp
import threading

import os
os.environ['PATH'] += os.pathsep + 'C:\\Users\\User\\Downloads\\bootstrapper\\'

from elevenlabs import voices, generate, play, stream, save as elabs_save

voices = voices()
#audio = generate(text="Hello world", voice="Nicole", model="eleven_multilingual_v2")
pp(voices)
#input()
#play(audio)
models = ["eleven_multilingual_v2","",]
model = models[0]
#vo = "Nicole"

vo = voices[-2]
print(vo,model)
#input()

def prep_audio(text, file, done_gen):
    playText(text,"",None,None,file=file,save=True, done_gen=done_gen)
    

def do_play(text, lang="EN",pre=None,pro=None, file=False,save=False, done_gen = []):
    global vo
    print("$$$$$$$$$", text, lang, vo, len(voices))
    play_when_done = True
    if not file or save:
        audio = generate(text=str(text), voice=vo)
        if save:
            elabs_save(audio,file)
            print("SSSSSSSSSAAAAAAAAVVVVVVVEEEEEEEDDDDDDDDDD AUDIO: ",file)
            play_when_done = False
            if len(done_gen)>0:
                done_gen[0] = True
    else:
        with open(text, "rb") as file:
        # Read the binary data from the file
            audio = file.read()
    if play_when_done:
        if pre:
            pre[0](pre[1])
        play(audio)
        if pro:
            pro[0](pro[1])
    print("$$$$$$$$$ DONE", text, lang)

#do_play("hi","eng",vo)
    
#do_play("hi","eng",vo.name)
    
#do_play("hi","eng",vo.name)
    
def playText(text, lang = "English",pre=None,pro=None,file=False, save=False, done_gen = []):
    global vo
    print("############################",text,lang)
    print("############################",text,lang)
    print("############################",text,lang)
    if text != "":
        threading.Thread(target=do_play,args=(text,lang,pre,pro,file,save,done_gen)).start()
    
once = False
if __name__ == "__main__":
    while(next != "q" and once != True):
        once = True    
        print("Enter Text")
        next = input()
        lcount = 0
        vc = "x"
        try:
            vc = int(next)
        except:
            pass
        if vc != "x":
            vo = voices[vc]
            print("changed to voice",vo)
        elif next != "" and next[0] == "=":
            vo = next[1:]
            print("changed to voice",vo)
        elif next == "!":
            lcount+=1
            model = models[lcount%len(models)]
            print("changed to model",model)

        elif next != "" and next != "q":
            print(next, ":::", vo,model)
            if model == "":
                audio = generate(text=next, voice=vo)
            else:
                audio = generate(text=next, voice=vo, model="eleven_multilingual_v2")
            play(audio)
            print(".....................")
            print(".....................")
            print(".....................")
        
    if False:
        def text_stream():
            yield "Hi there, I'm Eleven "
            yield "I'm a text to speech API "
            next=""
            print("!!!!!!!!")
            while(next != "q"):
                next = input()
                if next != "" and next != "q":
                    yield next
                


        audio_stream = generate(
            text=text_stream(),
            voice="Nicole",
            model="eleven_monolingual_v1",
            stream=True,
        )

        stream(audio_stream)