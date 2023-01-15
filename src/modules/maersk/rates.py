import json
import time

from selenium.webdriver import DesiredCapabilities
from seleniumwire import webdriver

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--headless')
chrome_options.add_argument('--ignore-certificate-errors-spki-list')
chrome_options.add_argument('--ignore-ssl-errors')
# chrome_options.add_argument('--proxy-server=45.119.80.22:8087')
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument('--ignore-certificate-errors')
chrome_options.add_argument('--no-proxy-server')
# chrome_options.add_argument('--remote-debugging-port=9222')
# chrome_options.add_argument("--proxy-server={}".format('host.docker.internal:8098'))

# chrome_capabilities = {
#     "browserName": "chrome",
#     "version": "",
#     "platform": "ANY",
#     "javascriptEnabled": True,
#     'applicationName': 'test1'
# }
# 
# fireFoxOptions = webdriver.FirefoxOptions()
# fireFoxOptions.headless = True
# 
# seleniumwire_options = {
#     'proxy': {
#         'http': 'http://root:Se@r@t3vn@45.119.80.22:46711',
#         'https': 'https://root:Se@r@t3vn@45.119.80.22:46711',
#         'no_proxy': 'localhost,127.0.0.1'
#     }
# }

# def start_browser():
#     # Ensure mobile-friendly view for parsing
#     useragent = "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0"
# 
#     profile = webdriver.FirefoxProfile()
#     profile.set_preference("general.useragent.override", useragent)
#     options = webdriver.FirefoxOptions()
#     options.set_preference("dom.webnotifications.serviceworker.enabled", False)
#     options.set_preference("dom.webnotifications.enabled", False)
#     options.add_argument('--headless')
# 
#     browser = webdriver.Firefox(firefox_profile=profile, options=options)
#     return browser


##  Get the URL
# driver = webdriver.Chrome(executable_path="/workspaces/hpg-ibe/ungoogled-chromium_108.0.5359.98_1.vaapi_linux/chrome", chrome_options=chrome_options)
# seleniumwire_options = {
#         'suppress_connection_errors': False,
#         'auto_config': True,
#         'addr': '45.119.80.22:4444',
#         'port': 8087
#     }

# useragent = "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0"
# profile = webdriver.FirefoxProfile()
# profile.set_preference("general.useragent.override", useragent)

# PROXY = "45.119.80.22:55466"
# webdriver.DesiredCapabilities.CHROME['proxy'] = {
#     "httpProxy": PROXY,
#     "ftpProxy": PROXY,
#     "sslProxy": PROXY,
#     "proxyType": "MANUAL",
# 
# }
# 
# webdriver.DesiredCapabilities.CHROME['acceptSslCerts'] = True

# driver = webdriver.Remote(
#     command_executor="http://45.119.80.22:4444",
#     options=chrome_options,
#     # desired_capabilities=chrome_capabilities,
#     # seleniumwire_options=seleniumwire_options
#     desired_capabilities={
#         "browserName": "chrome",
#         "javascriptEnabled": True,
#         "acceptInsecureCerts": True,
#         "moz:debuggerAddress": True
#     },
# 
# 
firefox_options = webdriver.FirefoxOptions()
firefox_options.add_argument("--headless")
firefox_options.add_argument('--disable-blink-features=AutomationControlled')
# Create a webdriver.DesiredCapabilities object
capabilities = webdriver.DesiredCapabilities.FIREFOX.copy()

# Set the accept_insecure_certs capability to True
capabilities['accept_insecure_certs'] = True

# 
# profile = webdriver.FirefoxProfile()
# profile.set_preference('network.proxy.Kind', 'Direct')
# profile.set_preference("network.proxy.type", 0)

# driver = webdriver.Remote(
#     desired_capabilities={
#         "browserName": "firefox",
#         "acceptInsecureCerts": True,
#         "moz:debuggerAddress": True,
#         "proxy": None
#     },
#     command_executor="http://45.119.80.22:4444/wd/hub",
#     options=firefox_options
# )

print("initialize web driver...")
driver = webdriver.Firefox(options=firefox_options, capabilities=capabilities)

driver.get("http://info.cern.ch")

##  Print request headers
for request in driver.requests:
    print(request.url)  # <--------------- Request url
    print(request.headers)  # <----------- Request headers
    print(request.response.headers)  # <-- Response headers

driver.quit()
