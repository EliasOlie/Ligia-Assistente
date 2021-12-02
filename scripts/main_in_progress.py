import speech_recognition as sr
#import conversor_bot as Cb
import os
from speech import falar
import pickle


falar('Olá, sou a Lígia a sua assistente virtual!')
falar('Permita-me analisar seus dados só um segundo!')

loadead_data = pickle.load(open('user_preferences.dat', 'rb'))

nome = loadead_data['user_name']
tratamento = loadead_data['called']

if nome == '' and tratamento == '':
    falar('Vejo que essa é a nossa primeira vez! Que bom que me escolheu!')
    falar('Primeiro deixe-me saber algugumas coisas')
    nome = input(falar('Qual o seu nome? '))
    tratamento = input(falar('E como você gostaria que eu lhe chamasse? '))

    user_pref = {}

    user_pref['user_name'] = nome

    user_pref['called'] = tratamento

    user_pref = pickle.dump(user_pref, open('user_preferences.dat', 'wb'))

    falar(f'confira por favor, seu nome é {nome} e você quer que eu lhe chame de {tratamento}')

else:
    falar(f'Achei!, confira por favor, seu nome é {nome} e você quer que eu lhe chame de {tratamento}')

    falar('Se eu disse errado por favor, quando for conferir os dados aperte "n" e dê enter!')

    if input(falar('Confere os dados? "S" para sim e "N" para não ')).lower() == 'n':
        user_pref = {}

        user_pref['user_name'] = input(falar('Qual o seu nome? '))

        user_pref['called'] = input(falar('como você gostaria que eu lhe chamasse?'))

        user_pref = pickle.dump(user_pref, open('user_preferences.dat', 'wb'))

        falar(f'confira por favor, seu nome é {nome} e você quer que eu lhe chame de {tratamento}')




#refazer o pickle <- cuidado o picke é perigoso!!!

#preparar o laço while de interações na web

#Cb.Conversor_Bot()

#_-_-_-_-_-_-_-_-_-_-_-_-_- IMPLEMENTAR _-_-_-_-_-_-_-_-_-_-_-_-_-_#

#Rede neural, ou IA

#criar as instâncias de reconhecimento de voz
#r = sr.Recognizer()

#with sr.Microphone() as source:
    #print("Diga algo: ")
    #audio = r.listen(source)

#O script tentará printar no console o que o usuário falou, se for "dólar hoje" ele imprimirá na tela
#a variável "moeda" que colocamos o conteúdo desejado da página HTML
#try:
    #print(f'Você disse: {r.recognize_google(audio, language="pt-br")}')
    #if r.recognize_google(audio, language='pt-br') == 'dólar hoje':
        #print(f'O dólar está à R${moeda}.')

#Se o speech recognizer não entender o que foi dito (ruído ou outra língua p.ex) ele avisa do error
#except sr.UnknownValueError:
    #print('Desculpe mas Lígia não entendeu!')

#Se estiver sem internet ou por qualquer outro motivo não conseguir um get no Google Speech retorna o error
#except sr.RequestError as e:
    #print(f'Error ao chamar o Google Speech Recognition service; {e}')
