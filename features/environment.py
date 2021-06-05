from features.browser import Browser
from features.pages.loginPage import LoginPage

def before_all(context):
    
    username = 'test_e2e@actable.ai'
    password = 'Saobang9889'

    context.browser = Browser()
    context.loginPage = LoginPage()
    context.loginPage.navigateToAccountGoogle()
    context.loginPage.login(username, password)
    context.loginPage.navigateToDocs()

def after_all(context):
    context.browser.close()
