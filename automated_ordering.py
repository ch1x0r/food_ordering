from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from food_libraries import *
order = []
# wings.find_element_by_css_selector("#mnuitems > form:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(3) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(4) > td:nth-child(4) > a:nth-child(1)").click()
# wings.execute_script("window.scrollTo(0, 500)")
# wings.find_element_by_css_selector("#id116186294633720").click()
# wings.find_element_by_css_selector("li.TabbedPanelsTab:nth-child(2) > font:nth-child(1) > b:nth-child(1)").click()
# wings.find_element_by_css_selector("#id116185794632700").click()
# wings.find_element_by_css_selector("#itemdetails > form:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(3) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(4) > td:nth-child(2) > a:nth-child(2)").click()
# wings.find_element_by_css_selector(".review-order").click()
# wings.find_element_by_css_selector("#ordreview > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > form:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(26) > td:nth-child(1) > a:nth-child(4)").click()
# firstname = wings.find_element_by_css_selector("#ordreview > form:nth-child(1) > table:nth-child(4) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(5) > td:nth-child(2) > input:nth-child(1)")
# firstname.send_keys("Mike")
# lastname = wings.find_element_by_css_selector('#ordreview > form:nth-child(1) > table:nth-child(4) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(6) > td:nth-child(2) > input:nth-child(1)')
# lastname.send_keys("Schiller")
# phone = wings.find_element_by_css_selector('#ordreview > form:nth-child(1) > table:nth-child(4) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(8) > td:nth-child(2) > input:nth-child(1)')
# phone.send_keys('781')
# phone = wings.find_element_by_css_selector('input.forminputs:nth-child(2)')
# phone.send_keys('799')
# phone = wings.find_element_by_css_selector('#ordreview > form:nth-child(1) > table:nth-child(4) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(8) > td:nth-child(2) > input:nth-child(3)')
# phone.send_keys('2065')
# street = wings.find_element_by_css_selector('#ordreview > form:nth-child(1) > table:nth-child(4) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(3) > td:nth-child(2) > input:nth-child(1)')
# street.send_keys('115 Belchertown RD')
# city = wings.find_element_by_css_selector('#ordreview > form:nth-child(1) > table:nth-child(4) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(6) > td:nth-child(2) > select:nth-child(1)')
# #figure out how to set to amherst
# Select(wings.find_element_by_css_selector('#ordreview > form:nth-child(1) > table:nth-child(4) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(6) > td:nth-child(2) > select:nth-child(1)')).select_by_index(1)
# zipcode = wings.find_element_by_css_selector('#ordreview > form:nth-child(1) > table:nth-child(4) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(8) > td:nth-child(2) > input:nth-child(1)')
# zipcode.send_keys('01002')
#
# #payment stuff
# wings.execute_script("window.scrollTo(0, 500)")
# select = Select(wings.find_element_by_css_selector('#ordreview > form:nth-child(1) > table:nth-child(4) > tbody:nth-child(1) > tr:nth-child(3) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(3) > td:nth-child(2) > select:nth-child(1)'))
# #payment option order = [cash, visa, mastercard, ocmp, ucard debit]. Dont use 0 indexing with these.
# select.select_by_index(2)
# #next step is to enter card # either automatically or through the GUI. #tailor to who is going to be using the code.


def driver():
    print('Format order Like so: Size flavor bone/less + optional: fries drink extra dressing\n')
    print('Or say Hangar n where n is the number combo you want.\n')
    print("Or if you have ordering presets enter the corresponding #. To see them enter 'print'\n")
    print('Example order: 1lb wimpy buffalo boneless small waffle fry coke 1 bleu cheese\n')
    print('Example combo: Hangar 1 wimpy buffalo garlic parmasean bleu cheese plain waffle fries sprite\n')
    order = raw_input('How are you going to order? Interactive or by using a saved meal? Type i or s for your choice:  ')
    if 'i' in order:
        order = interactive_order()
    elif 's' in order:
        order = saved_order()
    else:
        print ("Error with handling the input, make sure you're entering the right stuff\n")
        driver() #restarts the program trace because of input error.

    order = handle_order(order)
    wings = webdriver.Firefox()
    wings.get('https://www.wingsoveramherst.com')


def interactive_order():
    def bone_type():
        boneless = raw_input('Boneless? yes/no :  ')
        if boneless == 'yes':
            return 'yes'
        else:
            return 'no'

    def size(bone):
        if bone == 'yes':
            order_size = raw_input('How Much? enter the number of pieces (7, 10, 15, 25, 60, 120): ')
            if order_size not in ['7', '10', '15', '25', '60', '120']:
                print('You entered an invalid size!')
                return size(bone)
            else:
                return order_size
        else:
            order_size = raw_input('How Much? enter the number of pounds (.5, 1, 1.5, 2, 4, 6):  ')
            if order_size not in ['.5', '1', '1.5', '2', '4', '6']:
                print('You entered an invalid size!')
                return size(bone)
            else:
                return order_size
    def flavor():
        wing_flavor = raw_input("What flavor do you want?   ")
        if wing_flavor not in flavors_matrix:
            print('You entered an invalid flavor')
            return flavor()
        else:
            return wing_flavor
    def dressing():
        added_dressing = raw_input('What type of dressing?   ')
        if added_dressing not in dressings_matrix:
            print('You entered an invalid dressing')
            return dressing()
        else:
            return added_dressing
    #needs to be bleu cheese, ranch, no dressing.
    def fries():
        print("You said you wanted fries, what kind? Waffle, onion rings, or regular? Say 'none' to skip fries\n")
        side_fries = raw_input("What kind?  ")
        if side_fries == 'waffle':
            side_fries+= ' '+ raw_input("What type of flavor waffle fries? Choices: Cajun Blackened, West Texas Mesquite, Mustang Ranch, Garlic Parmasean, or Plain?  ")
            if side_fries in waffle_fries_matrix:
                return side_fries
            else:
                print("Malformed fry order")
                return fries()
        elif side_fries == 'regular':
            return fries
        elif side_fries == 'onion rings':
            return fries
        elif side_fries == 'none':
            return
        else:
            print("Malformed fry request")
            return fries()
    def drink():
        print("You said you wanted a drink, what kind?")
        print("Choices: coke, diet coke,  sprite, ice tea, fanta grape, root beer, cherry coke dr. pepper, fanta orange or none")
        side_drink = raw_input("Drink: ")
        if side_drink in drink_matrix:
            return side_drink
        elif side_drink == 'none':
            return
        else:
            print('Drink not recognized')
            return drink()

    def side_dressing():
        dressing = raw_input("What type of dressing? Ranch, bleu cheese, ketchup or none?  ")
        if dressing in dressings_matrix:
            return dressing
        elif dressing == 'none':
            return
        else:
            print('Dressing not recognized, try again')
            return side_dressing()

    def optional_items():
        choice = raw_input('Do you want fries, a drink, or extra dressing? Enter "y" or "n"  ')
        optional = []
        if choice == 'y':
            print("What do you want? Say 'fries' for fries, 'drink' for a drink, 'dressing' for extra dressing\n")
            print("Example: 'fries drink' for a fries and drink\n")
            sides = raw_input("What do you want?  ").split(' ')
            if 'fries' in sides:
                optional.append(fries())
            if('drink') in sides:
                optional.append(drink())
            if('dressing') in sides:
                optional.append(side_dressing())
            if ('fries' or 'drink' or 'dressing') not in sides:
                print("malformed request for sides, try again")
                optional_items()
        else:
            return
        return optional
        # core of the order
    order.append(bone_type())
    order.append(size(bone_type))
    order.append(flavor())
    order.append(dressing())
        # optional
    order.append(optional_items()) #need to parse the optional items
    #then move onto optional things.
    return order

def saved_order():
    pass
def handle_order(wings, order):
    #creates the list of instructions to be executed
    steps = []
    if order[0] == 'no':
        steps.append(wings.find_element_by_css_selector("li.menulist_menu_name_link:nth-child(2) > a:nth-child(1) > b:nth-child(1)"))
        steps.append(wings.find_element_by_css_selector(bone_matrix[order[1]]))
    else:
        steps.append(None)
        steps.append(wings.find_element_by_css_selector(boneless_matrix[order[1]]))
    steps.append()


def select_order():#TODO
    pass

def config_address():#TODO
    pass

def configure_payment():#TODO
    pass
driver()
