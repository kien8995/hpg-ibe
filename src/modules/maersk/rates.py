from seleniumwire import webdriver

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--ignore-certificate-errors-spki-list')
chrome_options.add_argument('--ignore-ssl-errors')

##  Get the URL
driver = webdriver.Chrome(executable_path="/workspaces/hpg-ibe/ungoogled-chromium_108.0.5359.98_1.vaapi_linux/chrome", chrome_options=chrome_options)
driver.get("https://www.maersk.com/instantPrice")

##  Print request headers
for request in driver.requests:
    print(request.url)  # <--------------- Request url
    print(request.headers)  # <----------- Request headers
    print(request.response.headers)  # <-- Response headers
