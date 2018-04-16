from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def scrap():
    options = Options()
    options.binary_location = '/app/.apt/usr/bin/google-chrome'
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    driver = webdriver.Chrome(chrome_options=options)

    url = 'https://example.com'

    driver.get(url)
    print(driver.page_source)

    driver.quit()

if __name__ == "__main__":
    scrap()
