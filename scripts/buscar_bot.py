import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException as Ue
from selenium.webdriver import ActionChains
import pyperclip

def Buscar_Bot(termo=''):
    print("🤖 Iniciando o Bot de buscas \n")

    # 1. Pegar conteúdo html a partir da url URL: https://www.melhorcambio.com/dolar-hoje
    url = 'https://google.com/'
    
    termo = input('Qual termo? ')

    option = Options()
    option.headless = False

    driver = webdriver.Chrome(ChromeDriverManager().install(), 0, option)

    driver.get(url)

    caixa_de_pesquisa = driver.find_element_by_class_name('gLFyf.gsfi').get_attribute("text")

    ActionChains(driver).click(caixa_de_pesquisa).pyperclip.paste()

    #time.sleep(2)

    #driver.quit()
    
    #Salvar o conteúdo desejado numa variável

Buscar_Bot()


