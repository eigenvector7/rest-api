#Functional Test for Django powered rest APIs
#credit book titled: "Test driven development with Python"
#credit book author: Percival
from selenium import webdriver
browser = webdriver.Chrome()
browser.get('http://localhost:8000')

assert 'Django' in browser.title
