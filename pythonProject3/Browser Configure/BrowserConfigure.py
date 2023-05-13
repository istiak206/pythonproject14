from selenium import webdriver

#launce browser
driver = webdriver.Firefox()

#Open Webpage
driver.get("https://pypi.org/project/selenium/")

driver.get("https://www.facebook.com/saucelabs")
#Browser Close
driver .close()