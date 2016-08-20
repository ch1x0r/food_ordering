from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from food_libraries import *

def driver():
    order = []
    print (saved_orders)
    order = int(raw_input('Which of the saved orders do you want? ')) -1 #to correspond to the lists 0 based counting
    if order not in range(0,6):
        print('you entered an invalid order number! Restarting')
        driver()
    else:
        print("You chose " + saved_orders[order] + " enter 'no' if this wrong, just hit enter otherwise.\n")
        confirm = raw_input('Is this the right order? ')
        if confirm == 'no':
            print('Restarting')
            driver()

    wings = webdriver.Firefox()
    wings.get('http://wingsoveramherst.com/')

    handle_order(wings, order)
    configure_address(wings)
    configure_payment(wings)
    after_payment(order)

    wings.close()

def handle_order(wings, order):
    for instruction in order_instructions[str(order+1)]:
        wings.execute_script("window.scrollTo(0, 500)")
        wings.find_elements_by_css_selector(instruction)[0].click()
    
    wings.execute_script("window.scrollTo(0, 500)")
    wings.find_element_by_css_selector(confirm_order[str(order+1)]).click()
        
def configure_address(wings):
    firstname = wings.find_element_by_css_selector("#ordreview > form:nth-child(1) > table:nth-child(4) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(5) > td:nth-child(2) > input:nth-child(1)")
    firstname.send_keys("")
    lastname = wings.find_element_by_css_selector('#ordreview > form:nth-child(1) > table:nth-child(4) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(6) > td:nth-child(2) > input:nth-child(1)')
    lastname.send_keys("")
    phone = wings.find_element_by_css_selector('#ordreview > form:nth-child(1) > table:nth-child(4) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(8) > td:nth-child(2) > input:nth-child(1)')
    phone.send_keys('')
    phone = wings.find_element_by_css_selector('input.forminputs:nth-child(2)')
    phone.send_keys('')
    phone = wings.find_element_by_css_selector('#ordreview > form:nth-child(1) > table:nth-child(4) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(8) > td:nth-child(2) > input:nth-child(3)')
    phone.send_keys('')
    email = wings.find_element_by_css_selector('#ordreview > form:nth-child(1) > table:nth-child(4) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(9) > td:nth-child(2) > input:nth-child(1)')
    email.send_keys('')
    street = wings.find_element_by_css_selector('#ordreview > form:nth-child(1) > table:nth-child(4) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(3) > td:nth-child(2) > input:nth-child(1)')
    street.send_keys('')
    city = wings.find_element_by_css_selector('#ordreview > form:nth-child(1) > table:nth-child(4) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(6) > td:nth-child(2) > select:nth-child(1)')
    Select(wings.find_element_by_css_selector('#ordreview > form:nth-child(1) > table:nth-child(4) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(6) > td:nth-child(2) > select:nth-child(1)')).select_by_index(1)
    zipcode = wings.find_element_by_css_selector('#ordreview > form:nth-child(1) > table:nth-child(4) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(8) > td:nth-child(2) > input:nth-child(1)')
    zipcode.send_keys('')

def configure_payment(wings):
    wings.execute_script("window.scrollTo(0, 500)")
    select = Select(wings.find_element_by_css_selector('#ordreview > form:nth-child(1) > table:nth-child(4) > tbody:nth-child(1) > tr:nth-child(3) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(3) > td:nth-child(2) > select:nth-child(1)'))
    #payment option order = [cash, visa, mastercard, ocmp, ucard debit]. Dont use 0 indexing with these.
    select.select_by_index(5)
    #next step is to enter card # either automatically or through the GUI. #tailor to who is going to be using the code.
    number = wings.find_element_by_css_selector('#ordreview > form:nth-child(1) > table:nth-child(4) > tbody:nth-child(1) > tr:nth-child(3) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(4) > td:nth-child(2) > input:nth-child(1)')
    number.send_keys('') #replace with real ucard number if used. 
    instructions_for_driver = wings.find_element_by_css_selector('textarea.forminputs')
    instructions_for_driver.send_keys('Call cell number upon arrival') #replace this with custom message
    """
    Danger zone! This will actually place the order, or try to. Uncomment the below line in order to make the 
    ordering mechanism go live.
    """
    #wings.find_element_by_css_selector('#submitButtonSpan > a:nth-child(1)').click()

def after_payment(order):
    print('------------------------------------------------------------------------------\n')
    print('Your total for this order is: '+ cost_matrix[str(order+1)]+ '\n')
    print('Check your email for the receipt.\n')
    print('------------------------------------------------------------------------------\n')

driver()
