from urllib.parse import quote
from selenium import webdriver
from selenium.webdriver.common.by import By

html = "<input id='task'><button id='save'>Salvar</button><p id='result'></p><script>document.querySelector('#save').onclick=()=>document.querySelector('#result').textContent=document.querySelector('#task').value</script>"
options = webdriver.ChromeOptions()
options.add_argument("--headless=new")
driver = webdriver.Chrome(options=options)
try:
    driver.get("data:text/html;charset=utf-8," + quote(html))
    driver.find_element(By.ID, "task").send_keys("Revisar API")
    driver.find_element(By.ID, "save").click()
    print(driver.find_element(By.ID, "result").text)
finally:
    driver.quit()
