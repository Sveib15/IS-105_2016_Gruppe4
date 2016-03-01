import speech_recognition as sr
import pyttsx


engine = pyttsx.init()
engine.setProperty('rate', 70)
voices = engine.getProperty('voices')
#engine.setProperty('voice', voices[10].id)

r = sr.Recognizer()
m = sr.Microphone()

try:
    print("A moment of silence, please...")
    with m as source: r.adjust_for_ambient_noise(source)
    print("Set minimum energy threshold to {}".format(r.energy_threshold))
    while True:
        print("Say something!")
        with m as source: audio = r.listen(source)
        print("Got it! Now to recognize it...")
        try:
            # recognize speech using Google Speech Recognition
            value = r.recognize_google(audio)
            if value == "no":
                engine.say("Fine, be that way")
                engine.runAndWait()                
            elif value == "4":
                engine.say("The number four")
                engine.runAndWait()
            # we need some special handling here to correctly print unicode characters to standard output
            elif str is bytes: # this version of Python uses bytes for strings (Python 2)
                print(u"You said {}".format(value).encode("utf-8"))
                engine.say("You said {}".format(value))
                engine.runAndWait()
            else: # this version of Python uses unicode for strings (Python 3+)
                print("You said {}".format(value))
        except sr.UnknownValueError:
            engine.say("What?")
            engine.runAndWait()            
            print("Oops! Didn't catch that")
        except sr.RequestError as e:
            print("Uh oh! Couldn't request results from Google Speech Recognition service; {0}".format(e))
    
except KeyboardInterrupt:
    pass