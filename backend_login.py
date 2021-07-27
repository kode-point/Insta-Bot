from selenium import webdriver
from time import sleep


def login(username, password):

    browser = webdriver.Chrome(executable_path="webdriver/chromedriver")
    browser.get('https://www.instagram.com/accounts/login/')
    sleep(2)
    username_input = browser.find_element_by_css_selector("input[name='username']")
    password_input = browser.find_element_by_css_selector("input[name='password']")
    username_input.send_keys(username)
    password_input.send_keys(password)
    login_button = browser.find_element_by_xpath("//button[@type='submit']")
    login_button.click()
    sleep(3)
    login.valid = False

    try:
        browser.find_element_by_id("slfErrorAlert")
        
    
    except:

        login.valid = True
        
        notn = browser.find_element_by_class_name("yWX7d")# dont save info button
        notn.click()
        notnow = browser.find_element_by_class_name("aOOlW.HoLwm ")
        notnow.click()
        # pic = browser.find_element_by_class_name("kIKUG")
        # pic.click()