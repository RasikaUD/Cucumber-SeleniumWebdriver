"""
Module containing common function used in several tests.
Functions that are not test or feature specific
"""
from selenium import webdriver

def go_to(url, browser_type=None):
    #if not browser_type:
     #   driver = webdriver.Firefox()
    #elif browser_type.lower() == 'chrome':"""
    driver = webdriver.Chrome()
    #else:
     #   raise Exception("The browser type '{}' is not supported", browser_type)

    #import pdb;pdb.set_trace()
    url = url.strip()
    #url = 'https://' + url
    #print "Here I am ", url
    driver.get(url)

    return driver

def assert_text_visible(text):
    pass

def assert_element_visible(element):
    pass

#check the title
def assert_page_title(context, expected_title):
    actual_title = context.driver.title
    print("The actual title is : {}".format(actual_title))
    print("The expected title is : {}".format(expected_title))

    assert expected_title == actual_title,"The title is not as expected." "Expected: {},Actual: {}".format(expected_title)
    print("The page title is as expected")

#check the current url
def assert_current_url(context, expected_url):
    current_url= context.driver.current_url
    if not expected_url.startswith('http') or not expected_url.startswith('https'):
        expected_url = 'https://' + expected_url + '/'

    assert current_url == expected_url,"The current url is not as expected""Actual:{}, Expected:{}".format(current_url)
    print("The page url is as expected")

def find_element(context, locator_attribute, locator_text):
    possible_locators = ["id","xpath","link text","partial link", "name"]
    if locator_attribute not in possible_locators:
        raise Exception('The locator attribute provided is not approved', 'The approved attributes are: %s' %possible_locators)
    try:
        element = context.driver.find_element(locator_attribute,locator_text)
        return element
    except Exception as e:
        raise Exception(e)


