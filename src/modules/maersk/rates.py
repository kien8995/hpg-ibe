from seleniumwire import webdriver

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--ignore-certificate-errors-spki-list')
chrome_options.add_argument('--ignore-ssl-errors')
# chrome_options.add_argument('--proxy-server=45.119.80.22:8087')
chrome_options.add_argument('--ignore-certificate-errors')

chrome_capabilities = {
    "browserName": "chrome",
    "version": "",
    "platform": "ANY",
    "javascriptEnabled": True,
    'applicationName': 'test1'
}


fireFoxOptions = webdriver.FirefoxOptions()
fireFoxOptions.headless = True

seleniumwire_options = {
    'proxy': {
        'http': 'http://root:Se@r@t3vn@45.119.80.22:46711',
        'https': 'https://root:Se@r@t3vn@45.119.80.22:46711',
        'no_proxy': 'localhost,127.0.0.1'
    }
}

##  Get the URL
# driver = webdriver.Chrome(executable_path="/workspaces/hpg-ibe/ungoogled-chromium_108.0.5359.98_1.vaapi_linux/chrome", chrome_options=chrome_options)
# seleniumwire_options = {
#         'suppress_connection_errors': False,
#         'auto_config': True,
#         'addr': '45.119.80.22:4444',
#         'port': 8087
#     }
driver = webdriver.Remote(
    command_executor="http://45.119.80.22:4444",
    options=fireFoxOptions,
    # desired_capabilities=chrome_capabilities,
    # seleniumwire_options=seleniumwire_options
    desired_capabilities={
            "browserName": "firefox",
            "browserVersion": "latest",
            "video": True,
            "platform": "ANY",
            "javascriptEnabled": True
        }
    )
driver.get("https://www.maersk.com/instantPrice")

##  Print request headers
for request in driver.requests:
    print(request.url)  # <--------------- Request url
    print(request.headers)  # <----------- Request headers
    print(request.response.headers)  # <-- Response headers
