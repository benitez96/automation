from selenium import webdriver

browser = webdriver.Firefox()
browser.get('https://www.google.com.ar')
elem = browser.find_element_by_css_selector('.FPdoLc > center:nth-child(1) > input:nth-child(1)')
print(elem)
elems = browser.find_elements_by_css_selector('p')
#this match 'P'aragraph elementS on the page
print(len(elems))