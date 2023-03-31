from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import visibility_of_element_located

servico = Service(GeckoDriverManager().install())
#Criar o Navegador
navegador = webdriver.Firefox(service=servico)

#Abrir um Site
navegador.get('https://www.animestc.net/animes')

#navega pelo site
'''ops_ano = navegador.find_element('xpath', '/html/body/div[1]/div/div/div[2]/div/section/div[1]/form/div/select[1]')
ops_ano.click()

opcoes = ['1500','1776','2020']
wait = WebDriverWait(navegador, 10)
option_list = wait.until(EC.visibility_of_element_located((By.XPATH, "//select[@name='year']")))

for opcao in opcoes:
    desired_option = option_list.find_element(By.XPATH, f"//option[contains(text(), '{opcao}')]")
    desired_option.click()
ops_ano.quit()'''

navegador.find_element('xpath', '/html/body/div[1]/div/div/div[2]/div/section/div[1]/form/div/select[2]/option[1]').click()

navegador.find_element('xpath', '/html/body/div[1]/div/div/div[2]/div/section/div[1]/form/input').send_keys("Shingeki no Kyojin")

navegador.find_element('xpath', '/html/body/div[1]/div/div/div[2]/div/section/div[2]/a[1]/article/figure/figcaption').click()

navegador.find_element('xpath', '/html/body/div[1]/div/div/div[2]/div/section/div[2]/a[1]/article/div/div/div[1]').click()
