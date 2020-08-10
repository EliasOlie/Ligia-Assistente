# import speech_recognition as sr
# import pyttsx3
# from random import choice

# error_logs = ['Desculpe, não entendi', 'Repita, por gentiliza', 'Não consegui entender, repita mais devagar']
# msg = choice(error_logs)

# fala = pyttsx3.init('sapi5')

# def som(resposta):
#     fala.say(resposta)
#     fala.runAndWait
    
# def falar():
#     while True:
#         r = sr.Recognizer()

#         with sr.Microphone() as source:
#             print("Diga algo: ")
#             audio = r.listen(source)
#         try:
#             print(f'Você disse: {r.recognize_google(audio, language="pt-br")}\n')
#             maq = r.recognize_google(audio, language="pt-br")
#             fala(maq)
#             if r.recognize_google(audio, language="pt-br") == 'sair':
#                 break

#         #Se o speech recognizer não entender o que foi dito (ruído ou outra língua p.ex) ele avisa do error
#         except sr.UnknownValueError:
#             som(msg)

#         #Se estiver sem internet ou por qualquer outro motivo não conseguir um get no Google Speech retorna o error
#         except sr.RequestError as e:
#             print(f'Error ao chamar o Google Speech Recognition service; {e}\n')

# falar()

import speech_recognition as sr
import pyttsx3
from random import choice


lista_erros = [
		"Não entendi nada",
		"Desculpe, não entendi",
		"Repita novamente por favor"
]


reproducao = pyttsx3.init()


def sai_som(reposta):
	reproducao.say(reposta)
	reproducao.runAndWait()


# def reconhece(resposta_erro_aleatoria):
# 	rec = sr.Recognizer()

# 	with sr.Microphone() as s:
# 		rec.adjust_for_ambient_noise(s)

# 		while True:
# 			try:
# 				audio = rec.listen(s)
# 				entrada = rec.recognize_google(audio, language="pt")
# 				return "{}".format(entrada)
# 			except sr.UnknownValueError:
# 				return resposta_erro_aleatoria
			

print("Ouvindo...\n-----------------\n")
# while True:
# 	resposta_erro_aleatoria = choice(lista_erros)
# 	fala = reconhece(resposta_erro_aleatoria)
# 	print("Você disse: {}".format(fala))
# 	sai_som(fala)

def currency():
    rec = sr.Recognizer()

    with sr.Microphone() as s:
        rec.adjust_for_ambient_noise(s)

    while True:
        try:
            audio = rec.listen(s)
            entrada = rec.recognize_google(audio, language="pt")
            return f'{entrada}'
        except sr.UnknownValueError:
            return 'Error não entendi'



while True:
    result = currency()
    print(result)

