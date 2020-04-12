from selenium import webdriver
from config import keys
import time
import random


def orderMeal():
    driver = webdriver.Chrome()
    driver.get(keys["url"])
    time.sleep(random.randint(1,3))
    email = driver.find_element_by_xpath('//*[@id="email"]')
    email.send_keys(keys["email"])
    time.sleep(random.randint(1,3))
    searchButton = driver.find_element_by_xpath('//*[@id="password"]')
    searchButton.send_keys(keys["password"])
    time.sleep(random.randint(1,3))
    signin = driver.find_element_by_xpath('//*[@id="ghs-outerWrapper"]/div/ghs-router-outlet/ghs-login/div/div/div/ghs-authentication-wizard/div/div/ghs-step-sign-in/ghs-sign-in/form/div[3]/div/ghs-sign-in-btn/button')
    signin.click()
    time.sleep(random.randint(4,9))
    address = driver.find_element_by_xpath('//*[@id="ghs-start-order-new-address-input"]/div/div/div/input')
    address.send_keys(keys["location"])
    time.sleep(random.randint(4,9))
    findfood = driver.find_element_by_xpath('//*[@id="ghs-outerWrapper"]/div/ghs-router-outlet/ghs-homepage-logged-in/div/div[2]/ghs-imf-wrapper/div/div/div/form/ghs-start-order-form/div/div[2]/button')
    findfood.click()
    time.sleep(random.randint(4,9))
    selection = driver.find_element_by_xpath('//*[@id="ghs-select-sort"]')
    selection.send_keys("Delivery Estimate")
    time.sleep(random.randint(7,10))
    # dollarSign = int(input("Number of dollar signs:"))
    dollarSign = 3
    if dollarSign == 1:
        price = driver.find_element_by_xpath(
            '//*[@id="ghs-search-results-container"]/div/div[1]/div/ghs-facets/div/div[6]/div/div/ghs-facet-radio/ghs-facet-container/aside/section/div[2]/div/div/div/div/button[1]')
    if dollarSign == 2:
        price = driver.find_element_by_xpath(
            '//*[@id="ghs-search-results-container"]/div/div[1]/div/ghs-facets/div/div[6]/div/div/ghs-facet-radio/ghs-facet-container/aside/section/div[2]/div/div/div/div/button[2]')
    if dollarSign == 3:
        price = driver.find_element_by_xpath(
            '//*[@id="ghs-search-results-container"]/div/div[1]/div/ghs-facets/div/div[6]/div/div/ghs-facet-radio/ghs-facet-container/aside/section/div[2]/div/div/div/div/button[3]')
    if dollarSign == 4:
        price = driver.find_element_by_xpath(
            '//*[@id="ghs-search-results-container"]/div/div[1]/div/ghs-facets/div/div[6]/div/div/ghs-facet-radio/ghs-facet-container/aside/section/div[2]/div/div/div/div/button[4]')
    if dollarSign == 5:
        price = driver.find_element_by_xpath(
            '//*[@id="ghs-search-results-container"]/div/div[1]/div/ghs-facets/div/div[6]/div/div/ghs-facet-radio/ghs-facet-container/aside/section/div[2]/div/div/div/div/button[5]')

    price.click()
    time.sleep(random.randint(5, 9))

    tacobell = driver.find_element_by_xpath('//*[@id="ghs-search-results-restaurantId-926164"]/h5')
    tacobell.click()

    time.sleep(random.randint(4,7))
    shredded = driver.find_element_by_xpath('//*[@id="menuItem-781059027"]/div[1]/div[1]/div/a')
    shredded.click()
    time.sleep(random.randint(4,8))

    addBag = driver.find_element_by_xpath('//*[@id="Site"]/ghs-modal-backdrop/ghs-modal-container/div/dialog/ghs-modal-content/ghs-menu-item-modal/div/ghs-lazy/ghs-menu-item-add/form/footer/div/button')
    addBag.click()
    time.sleep(random.randint(3,8))
    order = driver.find_element_by_xpath('//*[@id="ghs-cart-checkout-button"]')
    order.click()
    time.sleep(random.randint(4,7))

    driver.find_element_by_xpath('//*[@id="firstNameField"]').send_keys(keys["clientFirstName"])
    time.sleep(1)
    driver.find_element_by_xpath('//*[@id="lastNameField"]').send_keys(keys["clientLastName"])
    time.sleep(1)
    driver.find_element_by_xpath('//*[@id="accountPhone"]').send_keys(keys["clientPhone"])
    time.sleep(1)
    driver.find_element_by_xpath('//*[@id="address1"]').send_keys(keys["address"])
    time.sleep(1)
    driver.find_element_by_xpath('//*[@id="city"]').send_keys(keys["city"])
    time.sleep(1)
    driver.find_element_by_xpath('//*[@id="state"]').send_keys(keys["state"])
    time.sleep(1)
    driver.find_element_by_xpath('//*[@id="zip"]').send_keys(keys["zipcode"])
    time.sleep(1)
    driver.find_element_by_xpath('//*[@id="ghs-checkout-gather-submit"]').click()
    time.sleep(random.randint(5,9))
    driver.find_element_by_xpath('//*[@id="cardNumber"]').send_keys(keys["card"])
    time.sleep(1)
    driver.find_element_by_xpath('//*[@id="expirationDate"]').send_keys(keys["expire"])
    time.sleep(1)
    driver.find_element_by_xpath('//*[@id="securityCode"]').send_keys(keys["security"])
    time.sleep(1)
    driver.find_element_by_xpath('//*[@id="postalCode"]').send_keys(keys["postal"])
    time.sleep(1)



