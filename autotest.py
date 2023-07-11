from selenium import webdriver
from selenium.webdriver.chrome.options import Options  # импорт настроек
from selenium.webdriver.common.by import By
import random
import time


o = Options()
o.add_experimental_option("detach", True) # опция, позволяющая не закрывать страницу моментально после запуска драйвера и окна браузера.
driver = webdriver.Chrome(options=o)      # проблема кроется, скорее всего, в том, что версия вебдрайвера гораздо старее моей актуальной версии хрома.
driver.get('https://www.saucedemo.com/')
driver.set_window_size(1920, 1080)

# список всевозможных логинов для входа на сайт

user1 = "standard_user"
user2 = "locked_out_user"
user3 = "problem_user"
user4 = "performance_glitch_user"
userlist = [user1, user2, user3, user4]

# выбираем рандомный логин из списка

randomuser = random.choice(userlist)

# поиск инпута с логином; ввод данных

username = driver.find_element(By.ID, "user-name") # можно использовать разные варианты нахождения элемента: NAME, XPATH, CSS_SELECTOR, CLASS_NAME, TAG_NAME 
username.send_keys(randomuser)

# поиск инпута с паролем; ввод данных

password = driver.find_element(By.ID, "password") # можно использовать разные варианты нахождения элемента (By.{variative})
password.send_keys("secret_sauce")


# добавляю небольшой таймер, чтобы можно было убедиться в правильности заполнения данных перед кликом по кнопке "войти"
time.sleep(5)

# поиск кнопки для входа на сайт; вход на сайт

btn_login = driver.find_element(By.XPATH, "//*[@id='login-button']")
btn_login.click()

