from behave import *
from nose.tools import assert_true


@given('I am on the login docs page with username "{username}" and password "{password}"')
def step_impl(context, username, password):
    context.loginPage.navigateToAccountGoogle()
    context.loginPage.login(username, password)
    context.loginPage.navigateToDocs()

# @given('I am on the login page and input username and password')
# def step_impl(context):
#     context.loginPage.navigateToAccountGoogle()

@when('I click on add on')
def step_impl(context):
    context.loginPage.clickOnAddOnBtn()

@then('I click on Actable AI')
def step_impl(context):
    context.loginPage.clickOnActableAI()

@then('I click on Regression')
def step_impl(context):
    context.loginPage.clickOnRegression()

@then('I switch to iframe')
def step_impl(context):
    context.loginPage.switchToIframe()

@then('I select to predicted target and valuePredictedTarget "{valuePredictedTarget}"')
def step_impl(context, valuePredictedTarget):
    context.loginPage.selectToPredictedTarget(valuePredictedTarget)

@then('I click on select rendered')
def step_impl(context):
    context.loginPage.clickOnSelectRendered()
    
@then('I click on select all value')
def step_impl(context):
    context.loginPage.clickOnSelectAllValue()

@then('I click on run button')
def step_impl(context):
    context.loginPage.clickOnRunBtn()

@then('I quit iframe')
def step_impl(context):
    context.loginPage.quitIframe()

@then('I check to exist regression validation sheet')
def step_impl(context):
    context.loginPage.checkExistsRegressionValidationSheet()

@then('I right click on regression validation sheet to delete')
def step_impl(context):
    context.loginPage.rightClickOnRegressionValidationSheet()

@then('I click on delete button')
def step_impl(context):
    context.loginPage.clickOnDeleteBtn()

@then('I click on OK button to confirm')
def step_impl(context):
    context.loginPage.clickOnOKBtn()


@then('the user is not logged in')
def step_impl(context):
    assert_true(context.loginPage.get_login_error())
