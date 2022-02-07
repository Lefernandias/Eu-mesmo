#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import requests
import json

lojas = pd.read_excel ("accout_vtex.xlsx")
dado2 = pd.read_excel ("dado2.xlsx")
#display(lojas)
#display(dado2)

def conta():
    for i, nome in enumerate(dado2['Nomecompleto']):
        nome = str(dado2.loc[i,"Nomecompleto"])
        email = str(dado2.loc[i,"Email"])
        payload = { "name": f"{nome}", "email": f"{email}" }
        for i, nome in enumerate(lojas['conta']):
            account = lojas.loc[i,"conta"]
            akey = str(lojas.loc[i,"aKey"])
            aToken = str(lojas.loc[i,"aToken"])
            url = f"https://{account}.vtexcommercestable.com.br/api/license-manager/users"
            headers = {"Content-Type": "application/json", "X-VTEX-API-AppKey": f"{akey}", "X-VTEX-API-AppToken": f"{aToken}"  }
            response = requests.request("POST", url, json=payload, headers=headers)
            response = response.json()
            #response_id = response['id']
            print(response)
            #grvar o response em outra tabela
    
conta()


# In[ ]:




