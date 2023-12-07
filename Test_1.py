# Task №1:

# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
#
# # Указать путь к веб-драйверу (здесь пример для Chrome)
# webdriver_path = '/Users/dimon/PycharmProjects/PROJECTS/Autotest/chromedriver.exe'
# # Создать экземпляр драйвера с использованием опции executable_path
# options = webdriver.ChromeOptions()
# options.add_argument("webdriver.chrome.driver=" + webdriver_path)
# driver = webdriver.Chrome(options=options)
#
# try:
#     # Открыть браузер и перейти на сайт Google
#     driver.get("https://www.google.com")
#
#     # Найти поле ввода поиска
#     search_box = driver.find_element("name", "q")
#     #search_box = driver.find_element_by_id("уникальный_id_поля_поиска")                                       #Использование "id"
#     #search_box = driver.find_element_by_class_name("уникальное_название_класса")                              #Использование "class"
#     #search_box = driver.find_element_by_xpath("//input[@placeholder='Введите поисковый запрос или URL']")     #Использование XPath (В данном примере предполагается, что у поля ввода есть атрибут "placeholder" со значением "Введите поисковый запрос или URL".)
#     #search_box = driver.find_element_by_css_selector("input[type='text']")                                    #Ищем элемент <input>, который имеет атрибут type равный "text"
#
#     #Ввести текст запроса
#     search_box.send_keys("Убийство на краю света смотреть онлайн")
#
#     # Нажать Enter для выполнения поиска
#     search_box.send_keys(Keys.RETURN)
#
#     # Добавьте некоторые дополнительные шаги взаимодействия с веб-сайтом здесь, если необходимо
#
#     # Сохранить скриншот страницы
#     driver.save_screenshot("screenshot.png")
# finally:
#     # Закрыть браузер после выполнения теста
#     driver.quit()

########################################################################################################################
# Task №2:

from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

webdriver_path = '/Users/dimon/PycharmProjects/PROJECTS/Autotest/chromedriver.exe'
options = webdriver.ChromeOptions()
options.add_argument("webdriver.chrome.driver=" + webdriver_path)
driver = webdriver.Chrome(options=options)

try:
    driver.get("https://www.djangoproject.com")            # заходим на сайт django (изначально был google, см. Task №1)
    search_box = driver.find_element(By.XPATH, "//*[@id=\"top\"]/div/div[2]/ul/li[2]")   # ищем вкладку "download" с использованием XPath; участок "top" необходимо экранировать - \"top\"
    search_box.click()                                                                   # жмакаем по вкладке "download"
    sleep(4)                                                                             #  делаем задержку на 4 секунды
    driver.save_screenshot("screenshot_2.png")                           # меняем название и сохраняем скриншот страницы
finally:
    driver.quit()

########################################################################################################################