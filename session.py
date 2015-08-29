from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from sys import version_info

driver = webdriver.Firefox()
py3 = version_info[0] > 2
if py3:
  response = input("Enter SWE url: ")
else:
  response = raw_input("Enter SWE url: ")
driver.get(response) 
driver.delete_cookie("_sn")
print "Session Cookie Deleted!"
print "========================="
print "Creating NULL session..."
print "========================="
cookie = {'name' : '_sn', 'value' : ''}
driver.add_cookie(cookie)
print driver.get_cookies()

