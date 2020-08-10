import speech_recognition as sr
import conversor_bot as Cb

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







