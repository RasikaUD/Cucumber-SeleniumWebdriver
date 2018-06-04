

from behave import given, when, then
from BDD_Common.CommonFuncs import webcommon

#logging.basicConfig(level='INFO')
#start of behave definitions

@given("I go to the site {url}")
def go_to_url(context,url):
    print("Navigating to the site: {}".format(url))
    context.driver = webcommon.go_to(url)


@then('the page title should be "{expected_title}"')
def verify_homepage_title(context, expected_title):
    webcommon.assert_page_title(context, expected_title)

@then('current url should be "{expected_url}"')
def verify_current_url(context, expected_url):
    webcommon.assert_current_url(context, expected_url)

