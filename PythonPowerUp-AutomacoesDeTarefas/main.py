import pyautogui
from time import sleep
import pandas as pd

pyautogui.PAUSE = 1

pyautogui.press("win")
sleep(1)
pyautogui.write("edge")
pyautogui.press("enter")
sleep(1)
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")
sleep(3)

pyautogui.click(x=2558, y=353)
pyautogui.write("davilimaoliveira@gmail.com")
pyautogui.press("tab")
pyautogui.write("pythondesenha")
pyautogui.press("tab")
pyautogui.press("enter")

tabela_produtos = pd.read_csv("PythonPowerUp-AutomacoesDeTarefas/produtos.csv")

for linha in tabela_produtos.index:
    pyautogui.click(x=2521, y=243)
    pyautogui.write(str(tabela_produtos.loc[linha, "codigo"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela_produtos.loc[linha, "marca"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela_produtos.loc[linha, "tipo"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela_produtos.loc[linha, "categoria"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela_produtos.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela_produtos.loc[linha, "custo"]))
    pyautogui.press("tab")

    if not pd.isna(tabela_produtos.loc[linha, "obs"]):
        pyautogui.write(str(tabela_produtos.loc[linha, "obs"]))

    pyautogui.press("tab")
    pyautogui.press("enter")
    pyautogui.scroll(5000)

