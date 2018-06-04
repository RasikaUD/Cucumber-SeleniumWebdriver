from BDD_Common.CommonSteps.webstepscommon import *
from BDD_Common.CommonConfigs import locatorsconfig
from BDD_Common.CommonFuncs import webcommon

@then('the {nav_bar} bar should be visible')
def verify_nav_bars_visible(context, nav_bar):
    expected_bars=['main navigation', 'top navigation', 'options']
    if nav_bar not in expected_bars:
        raise Exception("The passed in nav_bar type is not one of expected""Actual: {}", "Expected in:{}".format(nav_bar,expected_bars))
   # if nav_bar == "top navigation":
    #    locator = '//*[@id="top"]'
     #   bar = context.driver.find_element_by_xpath(locator)
      #  if not bar.is_displayed():
      #      raise Exception('Not top navigation')
    #elif nav_bar == 'main navigation':
     #   locator = '//*[@id="mainnav"]/ul'
      #  bar = context.driver.find_element_by_xpath(locator)
       # if not bar.is_displayed():
        #    raise Exception('Not main navigation')
    #elif nav_bar == 'options':
     #   locator = '//*[@id="touchnav-wrapper"]/header/div/div[1]/form/fieldset'
      #  bar = context.driver.find_element_by_xpath(locator)
       # if not bar.is_displayed():
        #    raise Exception('Not options navigation')
    #else:
        #pass
        locator_info = locatorsconfig.LOCATORS.get(nav_bar)
        locator_type = locator_info['type']
        locator_text = locator_info['locator']

        nav_element = webcommon.find_element(context, locator_type,locator_text)
        webcommon.assert_element_visible(nav_element )


def is_element_visible(element):
    if element.is_displayed():
        return True
    else:
        return False

def assrt_element(element):
    if not element.is_displayed():
        raise AssertionError('The element is not displayed')