from playwright.sync_api import sync_playwright, expect

with sync_playwright() as playwright:
    browser = playwright.chromium.launch()
    page = browser.new_page()
    page.set_content('''
        <label>Nome <input id="name"></label>
        <button id="save">Salvar</button>
        <p id="result"></p>
        <script>document.querySelector('#save').onclick = () => {
          document.querySelector('#result').textContent = document.querySelector('#name').value;
        }</script>
    ''')
    page.locator("#name").fill("Luiz Henrique")
    page.locator("#save").click()
    expect(page.locator("#result")).to_have_text("Luiz Henrique")
    print(page.locator("#result").inner_text())
    browser.close()
