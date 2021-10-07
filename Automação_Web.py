#!/usr/bin/env python
# coding: utf-8

# # Automação Web
# 
# ## Desafio
# 
# Trabalhamos em ima importadora e o preço dos nossos produtos é vinculado a cotação de:
# - Dólar
# - Euro
# - Ouro
# Precisamos pegar na internet, de forma automática, a cotação desses 3 itens e saber quanto devemos cobrar pelos nossos produtos, considerando uma margem de contribuição que temos na nossa base de dados.
# 
# 
# Para isso, vamos criar uma automação web:
# - Usaremos o Selenium
#     - **Importante:** Baixar o Webdrive

# ### Objetivos
# - Capturar a cotação do Dólar
# - Capturar a cotação do Euro
# - Capturar a cotação do Ouro
# - Importar a base de dados
# - Atualizar a cotação, o preço de compra e o preço de vendas
# - Exportar o relatório atualizado
# 

# ## Preparando o Sistema
# - Baixar o Webdriver
#     - Google Chrome -> chromedriver
#     - Mozila Firefox -> geckodriver
#     - colocar na mesma pasta do código fonte
# - Importar bibliotecas
# - Criar o navegador

# In[26]:


#Importando o Selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#Criando navegador
navegador = webdriver.Chrome('chromedriver')


# ### Cotação do Dólar

# In[27]:


#Acessando o site do Google e acessando xpath
#Cotação Dólar
navegador.get('https://www.google.com/')
navegador.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys('cotação dólar')
navegador.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys(Keys.ENTER)
cot_dolar = navegador.find_element_by_xpath('//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]').get_attribute('data-value')
print(cot_dolar)


# ### Cotação do Euro

# In[28]:


#Cotação Euro
navegador.get('https://www.google.com/')
navegador.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys('cotação euro')
navegador.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys(Keys.ENTER)
cot_euro = navegador.find_element_by_xpath('//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]').get_attribute('data-value')
print(cot_euro)


# ### Cotação do Ouro

# In[29]:


#Cotação Ouro
navegador.get('https://www.melhorcambio.com/ouro-hoje')
cot_ouro = navegador.find_element_by_xpath('//*[@id="comercial"]').get_attribute('value').replace(',','.')
print(cot_ouro)


# ## Atualizando a base de dados

# In[32]:


import pandas as pd

df_produtos = pd.read_excel('datas/3_produtos.xlsx')
display(df_produtos)
