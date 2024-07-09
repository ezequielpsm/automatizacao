import pyautogui
import time

pyautogui.PAUSE = 0.5

pyautogui.press("win") # aperta uma tecla no teclado
pyautogui.write("chrome") # escreve um texto

pyautogui.press("enter")


pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login") # Digitar Link para acessar o site
pyautogui.press("enter")

time.sleep(3)

pyautogui.click(x= 630, y= 409)

pyautogui.hotkey("ctrl", "a")
pyautogui.write("ezequielpacheco2@gmail.com")

pyautogui.press("tab")
pyautogui.write("sempreassims2")

pyautogui.click(x=800, y=575)

time.sleep(3)

import pandas

tabela = pandas.read_csv("produtos.csv")

print (tabela)



for linha in tabela.index:
    pyautogui.click(x=707, y=288)

    
    codigo = str(tabela.loc[linha, "codigo"])
    #cadastrou codigo
    pyautogui.write(codigo)


    #cadatrou marca
    pyautogui.press("tab")
    marca = str(tabela.loc[linha, "marca"])
    
    pyautogui.write(marca)

    #cadstrar tipo
    pyautogui.press("tab")
    tipo = str(tabela.loc[linha, "tipo"])
   
    pyautogui.write(tipo)

    #cadastrar categoria
    pyautogui.press("tab")
    categoria = str(tabela.loc[linha, "categoria"])
    
    pyautogui.write(categoria)

    #cadastrar preço
    pyautogui.press("tab")
    preco = str(tabela.loc[linha, "preco_unitario"])
    
    pyautogui.write(preco)

    #cadastrar custo
    pyautogui.press("tab")
    custo = str(tabela.loc[linha, "custo"])
    
    pyautogui.write(custo)

    #obs
    pyautogui.press("tab")
    pyautogui.write("obs")

    pyautogui.press("tab")
    pyautogui.press("enter")
    pyautogui.press("enter")


    pyautogui.scroll(1000)