

from behave import given, when, then
from BDD_Common.CommonFuncs import webcommon
from BDD_Common.CommonConfigs import urlconfig
from BDD_Common.CommonConfigs import  locatorsconfig
import pdb
#logging.basicConfig(level='INFO')
#start of behave definitions

@given("I go to the site {site}")
def go_to_url(context,site):

    #pdb.set_trace()
    url= urlconfig.URNCONFIG.get(site)
    #pdb.set_trace()
    print("Navigating to the site: {}".format(url))
    context.driver = webcommon.go_to(url)


@then('the page title should be "{expected_title}"')
def verify_homepage_title(context, expected_title):
    webcommon.assert_page_title(context, expected_title)

@then('current url should be "{expected_url}"')
def verify_current_url(context, expected_url):
    webcommon.assert_current_url(context, expected_url)

