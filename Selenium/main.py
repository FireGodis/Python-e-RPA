from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_argument("--headless=new")
driver = webdriver.Chrome(options=options)
try:
    driver.get("data:text/html,<input id='task'><button id='save'>Salvar</button>")
    driver.find_element(By.ID, "task").send_keys("Revisar API")
    driver.find_element(By.ID, "save").click()
    print(driver.find_element(By.ID, "task").get_attribute("value"))
finally:
    driver.quit()
