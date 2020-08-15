import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException as Ue
from selenium.webdriver.common.keys import Keys
from speech import falar
from speech import Voice_Recognizer_Search

def Buscar_Bot(termo= Voice_Recognizer_Search()):
    print("🤖 Iniciando o Bot de buscas \n")

    # 1. Pegar conteúdo html a partir da url URL: https://www.melhorcambio.com/dolar-hoje
    url = 'https://google.com/'
    
    #termo = input('Qual termo? ')

    option = Options()
    option.headless = True

    driver = webdriver.Chrome(ChromeDriverManager().install(), 0, option)

    driver.get(url)
   
    caixa_de_pesquisa = driver.find_element_by_xpath('//*[@id="tsf"]/div[2]/div[1]/div[1]/div/div[2]/input')

    caixa_de_pesquisa.click()

    caixa_de_pesquisa.send_keys(termo)

    driver.find_element_by_xpath('//*[@id="tsf"]/div[2]/div[1]/div[3]/center/input[1]').click()

    time.sleep(3)
    
    try:
        nutshell = driver.find_element_by_xpath('//*[@id="kp-wp-tab-overview"]/div[1]/div/div/div/div/div/div/div/div').text
        if 'wikipedia' in nutshell:
            nutshell = nutshell.replace('wikipedia', '')
    except Ue:
        print('❌ Error de url! Tente: \nRevisar os dados inseridos\n')
        
    driver.quit()

    return f'segundo a wikipedia, {nutshell}'


    


falar(Buscar_Bot())


# teste = 'bla bla bla wikipedia'

# if 'wikipedia' in teste:
#     print(teste.replace('wikipedia', ''))


