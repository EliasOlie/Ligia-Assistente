import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException as Ue
from unicodedata import normalize



def Conversor_Bot(cambio=''):

    print("🤖 Iniciando o Conversor-Bot  \n")

    cambio = str(input('Qual moeda gostaria de consultar? '))
    cambio = cambio.lower()
    cambio = cambio.strip()
    if cambio == "dólar":
        cambio = 'dolar'

    print(cambio)
    # 1. Pegar conteúdo html a partir da url URL: https://www.melhorcambio.com/dolar-hoje
    try:
        url = "https://www.melhorcambio.com/dolar-hoje"

        url = url.replace('dolar', cambio)

        option = Options()
        option.headless = True

        driver = webdriver.Chrome(ChromeDriverManager().install(), 0, option)  

        driver.get(url)

        time.sleep(10)
        #Salvar o conteúdo desejado numa variável
        moeda = driver.find_element_by_class_name("text-verde").get_attribute("value")

        print(f'{cambio.title()} hoje está à: R${moeda}')
        #fechar o web browser
        driver.quit()

    #Pega a exeption de Error de URL (nesse caso porque o exeption real é o NoSuchElementException, dizendo que
    #o elemento que foi definido não foi encontrado, já que a classe ["text-verde"] só aparece em páginas de urls
    #válidos pode-se caracterizar como 90% dos casos serem error de urls que dão páginas que não tem o elemento
    # no DOM)

    except Ue:
        print('❌ Error de url! Tente: \nRevisar os dados inseridos\nChecar as moedas disponíveis\n')

flag = input("Consultar os dados novamente? S/N")
if flag.lower() == 's':
    Conversor_Bot('dolar')


    
