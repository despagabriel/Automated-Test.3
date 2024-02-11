from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
import time
import json
import pyautogui as pa

# pa.prompt
driver = webdriver.Chrome()
# este nevoie de un timp pentru ca butoanele sa se incarce in pagina, setam asta prin functia urmatoare
wait = WebDriverWait(driver, 10)
driver.get("https://www.youtube.com/")
# aici apas pe butonul de  agree termeni si conditii
agree_button = wait.until(EC.element_to_be_clickable((By.XPATH,
                                                      "/html/body/ytd-app/ytd-consent-bump-v2-lightbox/tp-yt-paper-dialog/div[4]/div[2]/div[6]/div[1]/ytd-button-renderer[2]/yt-button-shape/button")))
agree_button.click()
# time.sleep(10)
# acesez comanda vocala
vocal_recognition = wait.until(EC.element_to_be_clickable((By.XPATH,
                                                           r'/html/body/ytd-app/div[1]/div/ytd-masthead/div[4]/div[2]/div/ytd-button-renderer/yt-button-shape/button/yt-touch-feedback-shape/div')))
vocal_recognition.click()
time.sleep(2)
# aici trebuie sa fac un artificiu, nu merge cu x-path sau alt tip ci utilizez o imagine ca mijloc de identificare
# deoarece butonul de allow microfon este generat de pc nu youtube, deci nu tine de youtube
# utilizez pyautogui pentru a apasa pe butonul care permite youtube-ului accesul la microfon
# trebuie sa descarc si sau sa editez o imagine care seamana cu butonul pe care trebuie sa apas, deci identificarea se
# face ca la google lens
# accesez locatia imaginii identificate, imagine salvata anterior, utilizez path-ul imagini, deocamdata nu merge doar cu numele simplu
allow_location = pa.locateCenterOnScreen(r'C:\Users\Gabi\Pictures\allow_access_to_microphone.PNG')
# acum mut mouse-ul pe butonul identificat
acces = pa.moveTo(allow_location)
# acum dau click pe buton si permit accesul
pa.click()

# search = driver.find_element_by_xpath(r"/html/body/ytd-app/div[1]/div/ytd-masthead/div[4]/div[2]/ytd-searchbox/form/div[1]/div[1]/input")
# text = search.get_attribute("value")
# print(text)
# pentru a vedea toate tittlurile este necesar sa scrolam toate pagina de youtube pana la ultima valoare gasita
# pentru asta vom face o bucla care sa scroleze in toata pagina, utilizand inaltimea in pixeli a paginii web
time.sleep(5)
height = driver.execute_script("return document.documentElement.scrollHeight")
while True:
    html = driver.find_element(By.TAG_NAME, "html")
    html.send_keys(Keys.END)
    time.sleep(1.5)
    New_height = driver.execute_script("return document.documentElement.scrollHeight")
    if New_height == height:
        break
    height = New_height
#
# in liniile urmatoare copiez automat din youtube titlurile tutorialelor gasite si le pun intr-o lista

new_list = []
class_access = driver.find_elements(By.CLASS_NAME, "style-scope ytd-playlist-renderer")
for detail in class_access:
    title = detail.find_element(By.ID, "video-title")
    title_1 = title.text
    # if title_1 !='':
    new_list.append(title_1)


print(len(new_list))
for x,y in enumerate(new_list):
    print(x, "---->",y)

# with open(r'C:\Users\Gabi\PycharmProjects\pycharmproject\selenium_test\fisier.json', 'r+') as file:
#     data = json.load(file)

# print(len(new_list))
# for x,y in enumerate(new_list):
#     print(x, "---->",y)

# salvez numele tutorialelor intr-un fisier tip json, in format lista(array)
# aici este functia de scriere in fisier(fisierul trebuie creat inainte, este mai simplu, si ii dati path-ul

with open(r'C:\Users\Gabi\PycharmProjects\pycharmproject\selenium_test\fisier.json', "w") as file:
    json.dump(new_list, file)

driver.close()


# Point(x=329, y=186)
# time.sleep(10)
# driver.close()
# print(pa.size())
# print(pa.position())
