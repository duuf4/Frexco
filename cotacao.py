#Frexco

import xlsxwriter
import time
from selenium import webdriver
from datetime import datetime
import chromedriver_binary

from selenium.webdriver.support import expected_conditions as EC


dia_de_hoje = datetime.now().strftime("%d-%m-%Y")
workbook = xlsxwriter.Workbook(dia_de_hoje + '_cotação.csv')
worksheet = workbook.add_worksheet()



chrome_options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications" : 2}
chrome_options.add_experimental_option("prefs",prefs)
web = webdriver.Chrome(chrome_options=chrome_options)



web.get('https://br.frubana.com/spo/')

for i in range(6):
    web.execute_script ( "window.scrollTo (0, document.body.scrollHeight)" )
    time.sleep(2)

web.execute_script ( "window.scrollTo (0, document.body.scrollHeight)" )
time.sleep(5)



produtos = web.find_elements_by_css_selector('.product-box .product-info .product-title')
time.sleep(5)
worksheet.write(0,0, 'Produtos')
linha_de_escrita = 1
for produto in produtos:
    worksheet.write(linha_de_escrita, 0, produto.text)

    print(produto.text)
    linha_de_escrita = linha_de_escrita+1



precos = web.find_elements_by_css_selector('.product-box .product-price-container .price-new')
time.sleep(5)
worksheet.write(0,1, 'precos')
linha_de_escrita = 1
for preco in precos:
    worksheet.write(linha_de_escrita, 1, preco.text)

    print(preco.text)
    linha_de_escrita = linha_de_escrita+1



web.close()
workbook.close()
