#!/usr/bin/env python
# coding: utf-8

# In[5]:


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
import pandas as pd
import urllib

navegador = webdriver.Chrome("C:/Users/leandro.dias/Downloads/chromedriver.exe")


lojas = pd.read_excel ("accout_magento.xlsx" )
dado2 = pd.read_excel ("dado2.xlsx" )
#loga nos magentos



        
def cadastro2(): 
    
    time.sleep(5)
    navegador.find_element_by_xpath('//*[@id="user_username"]').click()
    time.sleep(3)
    navegador.find_element_by_xpath('//*[@id="user_username"]').send_keys(f"{email}")
  
    time.sleep(1)
    #navegador.find_element_by_xpath('//*[@id="user_base_fieldset"]/div[2]/div').send_keys(f"{Sobre_nome}" + Keys.TAB)
    #time.sleep(1)
    #navegador.find_element_by_xpath('//*[@id="user_lastname"]').send_keys(f"{Sobre_nome}" + Keys.TAB)
    #time.sleep(1)
    #navegador.find_element_by_xpath('//*[@id="user_email"]').send_keys(f"{email}" + Keys.TAB)
    #time.sleep(1)
    #navegador.find_element_by_xpath('//*[@id="user_password"]').send_keys("Synapcom@2022" + Keys.TAB)
    #time.sleep(1)
    #navegador.find_element_by_xpath('//*[@id="user_confirmation"]').send_keys("Synapcom@2022" + Keys.TAB)
    #time.sleep(1)
    #navegador.find_element_by_xpath('//*[@id="user_current_password"]').send_keys("Synapcom2020@" + Keys.TAB)
    #time.sleep(1)
    #navegador.find_element_by_xpath('//*[@id="page_tabs_roles_section"]').click()
    #time.sleep(1)
    #navegador.find_element_by_xpath('//*[@id="permissionsUserRolesGrid_table"]/tbody/tr[1]/td[2]').click()
    #time.sleep(1)
    #navegador.find_element_by_xpath('//*[@id="permissionsUserRolesGrid_table"]/tbody/tr[1]/td[1]').click()
    #time.sleep(1)
    #navegador.find_element_by_xpath('//*[@id="save"]').click()
    
    
def menu():
    time.sleep(10)
    navegador.find_element_by_xpath('//*[@id="menu-magento-backend-system"]/a').click()
    time.sleep(1)
    navegador.find_element_by_xpath('//*[@id="menu-magento-backend-system"]/div/ul/li[2]/ul/li[2]/div/ul/li[1]/a').click()
    time.sleep(1)
    navegador.find_element_by_xpath('//*[@id="add"]').click()
    
def fim():   
    navegador.quit()    

def loga():
    for i, conta in enumerate(lojas['conta' ]):
        URL = lojas.loc[i,"URL"]
        print(conta)
        link = f"{URL}"
        navegador.get(link)
        delay = 3
        try:
            myElem = WebDriverWait(navegador, delay).until(EC.presence_of_element_located((By.ID, 'username')))
            print("Page is ready!")
        except TimeoutException:
            print("Loading took too much time!")
        navegador.find_element_by_xpath('//*[@id="username"]').send_keys("leandro.dias" + Keys.TAB)
        time.sleep(10)
        navegador.find_element_by_xpath('//*[@id="login"]').send_keys("Synapcom2020@" + Keys.TAB)
        time.sleep(1)
        navegador.find_element_by_xpath('//*[@id="login-form"]/fieldset/div[3]/div[1]/button').click()
        time.sleep(3)
             
        
def cadastro():
            for i, nome in enumerate(dado2['Nome_completo' ]):  
                Sobre_nome = dado2.loc[i, "Sobre_nome"]
                alcunha = dado2.loc[i, "Login"]
                email = dado2.loc[i, "E-mail"]
                yami = dado2.loc[i, "Gp_Yami"]
                silt = dado2.loc[i, "Gp_Silt"]
                vtex = dado2.loc[i, "Gp_Vtex"]
                abacos = dado2.loc[i,"Gp_Abacos"]
                magento = dado2.loc[i, "Gp_Magento"]
                cadastro2()

#seguencia de execução

    
loga()
menu()
cadastro()
fim()


# In[ ]:


import requests
import pandas as pd

#montar base de dados
#fazer laço de dados do usuário
#Fazer laço do request


dados = pd.read_excel ("dados.xlsx" )

url = "f"https://{conta}.vtexcommercestable.com.br/api/license-manager/users"

payload = {
    "f"name": "Leandro Dias",
    "email": "lefernandias@hotmail.com"
}
headers = {
    "Content-Type": "application/json",
    "X-VTEX-API-AppKey": "vtexappkey-larocheposay-OUTVAH",
    "X-VTEX-API-AppToken": "PQEMPUJXXBWADNETHVIRYSJSLNGABVGVXNJJXQHJAXUYLSWBHSVRUVQWGMACOIWBVACQEUWRNZQAYLGTQFTIZOBBXMCKPFVRASDLPGXMWEEVEPXUGHLJOOCGZBTRSLCI"
}

response = requests.request("POST", url, json=payload, headers=headers)

print(response.text)


# In[ ]:




