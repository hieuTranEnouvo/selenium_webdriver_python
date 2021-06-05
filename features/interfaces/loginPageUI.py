from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPageUI(object):

    USER = 'identifierId'
    USER_SUBMIT = 'identifierNext'
    PASS = 'password'
    SUBMIT = 'passwordNext'
    urlAccount = 'https://accounts.google.com/o/oauth2/v2/auth/oauthchooseaccount?redirect_uri=https%3A%2F%2Fdevelopers.google.com%2Foauthplayground&prompt=consent&response_type=code&client_id=407408718192.apps.googleusercontent.com&scope=email&access_type=offline&flowName=GeneralOAuthFlow'
    urlDocs = 'https://docs.google.com/spreadsheets/d/1bq0oBrpu4Ur2goqyJOf2bwsjynzrxB_JEwLHrzUQWdo/edit?addon_dry_run=AAnXSK9pEBV4ZBG5xi2SIEKPHhS_j_Q-qHYrAsbqR2j3ADWjH5Ao-zWmL7tBXXka7G2W9PPEfsHH1x_UW2iTBFee-fdkaF7zsrQTAorLqC_EAk1U0u1MIbNLMm91Sn1G733brnlNrVNN#gid=0'
    addOnBtn = 'docs-extensions-menu'
    actableAIBtn = '//div[@class="goog-menuitem-content" and contains(text(), "Actable AI ")]'
    regressionBtn = '//div[@class="goog-menuitem-content" and contains(text(), "Regression")]'
    selectPredictedTarget = '//select[@id="regression-predicted-target"]'
    iframe1 = '(//iframe[@frameborder=0])[2]'
    iframe2 = 'sandboxFrame'
    iframe3 = 'userHtmlFrame'
    predictedTarget = 'regression-predicted-target'
    selectRendered = '//ul[@class="select2-selection__rendered"]'
    selectAll = '//li[@role="treeitem"]/span[contains(text(),"Select All")]'
    runBtn = '//button[@id="btn-query"]'
    regressionValidation = '//span[@class="docs-sheet-tab-name" and contains(text(),"_validation")]'
    deleteBtn = '//div[@class="goog-menuitem-content" and contains(text(),"Delete")]'
    okBtn = '//button[@name="ok"]'