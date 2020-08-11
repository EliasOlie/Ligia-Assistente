import speech_recognition as sr
import pyttsx3
from random import choice


lista_erros = [
		"Não entendi nada",
		"Desculpe, não entendi",
		"Repita novamente por favor"
]


reproducao = pyttsx3.init()

def falar (frase):
    reproducao.say(frase)
    reproducao.runAndWait()
    			

def AudioErrorLog(lista_de_erros):
    falar(choice(lista_de_erros))

def Voice_Recognizer_Currency():
    print('Qual cotação deseja ver hoje?')
    
    falar("Qual cotação deseja ver hoje?")

    
    r = sr.Recognizer()

    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        print("Diga algo: ")
        audio = r.listen(source)
    try:
        #print(f'Você disse: {r.recognize_google(audio, language="pt-br")}\n')
        som_detectado = r.recognize_google(audio, language="pt-br")
        falar(f'O nosso bot de cotação vai consultar o preço do {som_detectado} aguarde...')

    #Se o speech recognizer não entender o que foi dito (ruído ou outra língua p.ex) ele avisa do error
    except sr.UnknownValueError:
        AudioErrorLog(lista_erros)

    #Se estiver sem internet ou por qualquer outro motivo não conseguir um get no Google Speech retorna o error
    except sr.RequestError as e:
        print(f'Error ao chamar o Google Speech Recognition service; {e}\n')
    return som_detectado


def Voice_Recognizer():
    while True:
        r = sr.Recognizer()

    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        print("Diga algo: ")
        audio = r.listen(source)
    try:
        print(f'Você disse: {r.recognize_google(audio, language="pt-br")}\n')
        som_detectado = r.recognize_google(audio, language="pt-br")
        falar(som_detectado)

    #Se o speech recognizer não entender o que foi dito (ruído ou outra língua p.ex) ele avisa do error
    except sr.UnknownValueError:
        AudioErrorLog(lista_erros)

#Se estiver sem internet ou por qualquer outro motivo não conseguir um get no Google Speech retorna o error
    except sr.RequestError as e:
        print(f'Error ao chamar o Google Speech Recognition service; {e}\n')
    
    return som_detectado
