
# Задание:
# Напишите код на python  автоматизированного теста с использованием библиотеки Selenium. Необходимы скрипты открытия
# браузера, взаимодействие с веб-сайтом (ввод текст в поле поиска Google) и сохранения скриншота страницы.

# Написание Автотеста:
# - Создаем какую-нибудь папку для проекта (у меня все проекты хранятся в PROJECTS)
# - Создаем репозиторий на GitHub
# - Копируем репозиторий (вкладка SSH-ключ) из GitHub, например - git@github.com:DimonYrievich/Autotest.git
# - В терминале заходим в папку PROJECTS и клонируем репозиторий: git clone git@github.com:DimonYrievich/Autotest.git
# - Устанавливаем библиотеку "selenium"(инструмент для автоматизации веб-браузера). Позволяет писать тесты, скрипты, боты.
#   команда - pip install selenium
# - Затем нам понадобится веб-драйвер для выбранного браузера. Скачиваем ChromeDriver (https://chromedriver.chromium.org/downloads)
#   для версии браузера (версию см. в настройках Chrome)
# - Распаковываем ChromeDriver и перетаскиваем его в папку проекта (в данном случае Autotest)
# - Пишем код в соответствии с заданием.


from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Указать путь к веб-драйверу (здесь пример для Chrome)
webdriver_path = '/Users/dimon/PycharmProjects/PROJECTS/Autotest/chromedriver.exe'
# Создать экземпляр драйвера с использованием опции executable_path
options = webdriver.ChromeOptions()
options.add_argument("webdriver.chrome.driver=" + webdriver_path)
driver = webdriver.Chrome(options=options)

try:
    # Открыть браузер и перейти на сайт Google
    driver.get("https://www.google.com")

    # Найти поле ввода поиска
    search_box = driver.find_element("name", "q")
    #search_box = driver.find_element_by_id("уникальный_id_поля_поиска")                                       #Использование "id"
    #search_box = driver.find_element_by_class_name("уникальное_название_класса")                              #Использование "class"
    #search_box = driver.find_element_by_xpath("//input[@placeholder='Введите поисковый запрос или URL']")     #Использование XPath (В данном примере предполагается, что у поля ввода есть атрибут "placeholder" со значением "Введите поисковый запрос или URL".)
    #search_box = driver.find_element_by_css_selector("input[type='text']")                                    #Ищем элемент <input>, который имеет атрибут type равный "text"

    #Ввести текст запроса
    #search_box.send_keys("тестирование с помощью Selenium")
    search_box.send_keys("Убийство на краю света смотреть онлайн")

    # Нажать Enter для выполнения поиска
    search_box.send_keys(Keys.RETURN)

    # Добавьте некоторые дополнительные шаги взаимодействия с веб-сайтом здесь, если необходимо

    # Сохранить скриншот страницы
    driver.save_screenshot("screenshot.png")
finally:
    # Закрыть браузер после выполнения теста
    driver.quit()




# Ниже код автотеста из вебинара Skillfactory. НЕ РАБОТАЕТ!!!
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from time import sleep
#
# # запускаем браузер
# driver = webdriver.Chrome("/Users/dimon/PycharmProjects/PROJECTS/Autotest/chromedriver.exe")
# driver.get("https://google.com")
# driver.find_element(By.XPATH, "//*[@id=\"input\"]").send_keys("PROJECTS" + Keys.RETURN)
# sleep(2)
# driver.save_screenshot("at.png")
# driver.quit()