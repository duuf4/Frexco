# Frexco

import xlsxwriter
import time
from selenium import webdriver
from datetime import datetime
import chromedriver_binary

dia_de_hoje = datetime.now().strftime("%d-%m-%Y")
workbook = xlsxwriter.Workbook(dia_de_hoje + '_cotação.csv')
worksheet = workbook.add_worksheet()



web = webdriver.Chrome()
web.get('https://br.frubana.com/spo')
time.sleep(1)



produtos = web.find_elements_by_css_selector('.product-box .product-info .product-title')
worksheet.write(0,0, 'Produtos')

linha_de_escrita = 1
for produto in produtos:
    worksheet.write(linha_de_escrita, 0, produto.text)
    print(produto.text)
    linha_de_escrita = linha_de_escrita+1

    

precos = web.find_elements_by_css_selector('.product-box .product-price-container .price-new')
worksheet.write(0,1, 'precos')

linha_de_escrita = 1
for preco in precos:
    worksheet.write(linha_de_escrita, 1, preco.text)
    print(preco.text)
    linha_de_escrita = linha_de_escrita+1


web.close()
workbook.close()


