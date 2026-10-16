from playwright.sync_api import sync_playwright

with sync_playwright() as playwright:
    browser = playwright.chromium.launch()
    page = browser.new_page()
    page.set_content('<label>Nome <input id="name"></label><button id="save">Salvar</button><p id="result"></p>')
    page.locator("#name").fill("Luiz Henrique")
    page.locator("#save").click()
    value = page.locator("#name").input_value()
    print(f"Formulário pronto para salvar: {value}")
    browser.close()
