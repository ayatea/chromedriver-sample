from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# Chrome Optionsの設定
options = Options()
# headlessモードを使用する
options.add_argument('--headless') 

driver_path = '/Users/ayatea/.pyenv/versions/3.6.4/lib/python3.6/site-packages/chromedriver_binary/chromedriver'

# Chrome Driverを起動する
driver = webdriver.Chrome(executable_path=driver_path, chrome_options=options)

driver.get('https://www.yahoo.co.jp/')

data = driver.page_source.encode('utf-8')

print(data)

# Chrome Driverを終了する
driver.quit()
