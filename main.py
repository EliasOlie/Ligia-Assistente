import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import speech_recognition as sr

# 1. Pegar conteúdo html a partir da url URL: https://www.melhorcambio.com/dolar-hoje

url = "https://www.melhorcambio.com/dolar-hoje"

option = Options()
option.headless = True

driver = webdriver.Chrome(ChromeDriverManager().install(), 0, option) 

driver.get(url)

time.sleep(10)
#Salvar o conteúdo desejado numa variável
dol = driver.find_element_by_class_name("text-verde").get_attribute("value")

#fechar o web browser
driver.quit()

#criar as instâncias de reconhecimento de voz
r = sr.Recognizer()

with sr.Microphone() as source:
    print("Diga algo: ")
    audio = r.listen(source)

#O script tentará printar no console o que o usuário falou, se for "dólar hoje" ele imprimirá na tela
#a variável "dol" que colocamos o conteúdo desejado da página HTML
try:
    print(f'Você disse: {r.recognize_google(audio, language="pt-br")}')
    if r.recognize_google(audio, language='pt-br') == 'dólar hoje':
        print(f'O dólar está à R${dol}')

#Se o speech recognizer não entender o que foi dito (ruído ou outra língua p.ex) ele avisa do error
except sr.UnknownValueError:
    print('Desculpe mas Lígia não entendeu!')

#Se estiver sem internet ou por qualquer outro motivo não conseguir um get no Google Speech retorna o error
except sr.RequestError as e:
    print(f'Error ao chamar o Google Speech Recognition service; {e}')
