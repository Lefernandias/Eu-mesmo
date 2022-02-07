#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time
import pyautogui 
from selenium.webdriver.support.select import Select
import urllib

navegador = webdriver.Chrome("C:/Users/leandro.dias/Downloads/chromedriver.exe")


# função de login
def loga():
    navegador.get("https://wms.synapcom.com.br/siltwms/")
    delay = 8
    try:
        myElem = WebDriverWait(navegador, delay).until(EC.presence_of_element_located((By.ID, 'x-auto-5')))
        print("Page is ready!")
    except TimeoutException:
        print("Loading took too much time!")
    time.sleep(3)
    navegador.find_element_by_xpath('//*[@id="LoginDialog_loginText"]').send_keys("leandro.dias" + Keys.TAB)
    time.sleep(5)
    navegador.find_element_by_xpath('//*[@id="LoginDialog_passwordText"]').send_keys("Synapcom2022@@")
    time.sleep(8)
    navegador.find_element_by_xpath('//*[@id="LoginDialog_armazemComboBox"]').click()
    time.sleep(8)
    navegador.find_element_by_xpath('//*[@id="LoginDialog_armazemComboBox"]').send_keys(Keys.DOWN, Keys.RETURN) # Cajamar
    time.sleep(5)


# função entrar no menu de gerenciador de expedição
def menu():
    time.sleep(10)
    navegador.find_element_by_xpath('//*[@id="x-auto-674-input"]').click()
    time.sleep(1)
    navegador.find_element_by_xpath('//*[@id="x-auto-674-input"]').send_keys("gerenciador de ex" + Keys.ENTER)
    time.sleep(1)
    navegador.find_element_by_xpath('//*[@id="x-auto-679__NavigationView_tree-ItemGerenciadordeExpedicao"]/span[2]').click()
    time.sleep(10)
    
       
    
# função de cadastro da onda
def onda():
    time.sleep(10)
    navegador.find_element_by_xpath('//*[@id="tb-Onda-AssistentedeFormacao"]').click()
    time.sleep(10)           
    navegador.find_element_by_xpath('//*[@id="AssistenteFormacaoOndaDataPage_configuracaoOndaField"]').send_keys(Keys.DOWN, Keys.DOWN, Keys.DOWN, Keys.ENTER)
    time.sleep(10)
    #INICIO SELEÇÃO DA TRANSPORTADORA
    navegador.find_element_by_xpath('//*[@id="AssistenteFormacaoOndaDataPage_transportadoraButton"]').click()
    time.sleep(10)
    navegador.find_element_by_xpath('//*[@id="SiltTransfere_buscarText"]').send_keys("CORREIOS" + Keys.ENTER)
    time.sleep(10)
    navegador.find_element_by_xpath('//*[@id="grid_row_0"]/img').click()
    time.sleep(10)
    navegador.find_element_by_xpath('//*[@id="SiltTransfere_fecharButton"]').click()
    time.sleep(10)
    #FIM SELEÇÃO DA TRANSPORTADORA
    #INICIO SELEÇÃO DO DEPOSITANTE
    navegador.find_element_by_xpath('//*[@id="AssistenteFormacaoOndaDataPage_depositanteButton"]').click()
    time.sleep(10)
    navegador.find_element_by_xpath('//*[@id="SiltTransfere_buscarText"]').send_keys("302190" + Keys.ENTER)
    time.sleep(10)
    navegador.find_element_by_xpath('//*[@id="grid_row_0"]/img').click()
    time.sleep(10)
    navegador.find_element_by_xpath('//*[@id="SiltTransfere_fecharButton"]').click()
    time.sleep(10)
    #FIM SELEÇÃO DO DEPOSITANTE
    # inicio da aplicação dos filtros
    navegador.find_element_by_xpath('//*[@id="AssistenteFormacaoOndaDataPage_btnAplicarFiltros"]').click()
    time.sleep(10)
    navegador.find_element_by_xpath('//*[@id="AssistenteFormacaoOndaDataPage_tituloOndaField"]').send_keys("Nome da onda")
    time.sleep(10)
    navegador.find_element_by_xpath('//*[@id="Wizard_finalizeButton"]').click()
    time.sleep(10)
    
#fecha o programa
def fim():
    time.sleep(10)
    navegador.quit()

#seguencia de execução

loga()
menu()
onda()
fim()


# In[ ]:





# In[ ]:




