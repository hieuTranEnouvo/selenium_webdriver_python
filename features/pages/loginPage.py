from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from features.browser import Browser
from features.interfaces.loginPageUI import LoginPageUI
from features.common.basePage import BasePage

class LoginPage(Browser):

    def navigateToAccountGoogle(self):
        BasePage.open(self, LoginPageUI.urlAccount)

    def navigateToDocs(self):
        BasePage.open(self, LoginPageUI.urlDocs)

    def setUsername(self, username):
        BasePage.sendKeyFindByIdElement(self,LoginPageUI.USER, username)
        BasePage.clickToFindByIdElement(self, LoginPageUI.USER_SUBMIT)

    def setPassword(self, password):
        BasePage.sendKeyFindByNameElement(self,LoginPageUI.PASS, password)
    
    def submitLogin(self):
        BasePage.clickToFindByIdElement(self,LoginPageUI.SUBMIT)

    def login(self, username, password):
        self.setUsername(username)
        self.setPassword(password)
        self.submitLogin()

    def clickOnAddOnBtn(self):
        BasePage.clickToFindByIdElement(self, LoginPageUI.addOnBtn)

    def clickOnActableAI(self):
        BasePage.clickToFindByXpathElement(self, LoginPageUI.actableAIBtn)
    
    def clickOnRegression(self):
        BasePage.clickToFindByXpathElement(self, LoginPageUI.regressionBtn)    
          
    def switchToIframe(self):
        BasePage.switchIframeByXpathElement(self, LoginPageUI.iframe1)
        BasePage.switchIframeByIdElement(self, LoginPageUI.iframe2)
        BasePage.switchIframeByIdElement(self, LoginPageUI.iframe3)

    def selectToPredictedTarget(self, valuePredictedTarget):
        BasePage.selectToFindByIdElement(self, LoginPageUI.predictedTarget, valuePredictedTarget)

    def clickOnSelectRendered(self):
        BasePage.clickToFindByXpathElement(self, LoginPageUI.selectRendered)

    def clickOnSelectAllValue(self):
        BasePage.clickToFindByXpathElement(self, LoginPageUI.selectAll)

    def clickOnRunBtn(self):
        BasePage.clickToFindByXpathElement(self, LoginPageUI.runBtn)
    
    def checkExistsRegressionValidationSheet(self):
        BasePage.checkExistsByXpath(self, LoginPageUI.regressionValidation)

    def rightClickOnRegressionValidationSheet(self):
        BasePage.rightClickToByXpath(self, LoginPageUI.regressionValidation)
    
    def clickOnDeleteBtn(self):
        BasePage.clickToFindByXpathElement(self, LoginPageUI.deleteBtn)

    def clickOnOKBtn(self):
        BasePage.clickToFindByXpathElement(self, LoginPageUI.okBtn)   
    
     
    def quitIframe(self):
        BasePage.quitIframe(self)
