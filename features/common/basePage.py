from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException 
from selenium.webdriver.common.action_chains import ActionChains


class BasePage(object):
    TIMEOUT = 10000
 
    def __init__(self, driver):
        super(BasePage, self).__init__()
        self.driver = driver
 
    def open(self, url):
        self.driver.get(url)
 
    def maximize(self):
        self.driver.maximize_window()        
        
    def close(self):
        self.driver.quit()
        
    def sendKeyFindByXpathElement(self, xpath, value):
        WebDriverWait(self.driver, BasePage.TIMEOUT).until(EC.visibility_of_element_located((By.XPATH, xpath))).send_keys(value)
 
    def sendKeyFindByNameElement(self, name, value):
        WebDriverWait(self.driver, BasePage.TIMEOUT).until(EC.visibility_of_element_located((By.NAME, name))).send_keys(value)
 
    def sendKeyFindByIdElement(self, id, value):
        WebDriverWait(self.driver, BasePage.TIMEOUT).until(EC.visibility_of_element_located((By.ID, id))).send_keys(value)

    def clickToFindByIdElement(self, id):
        WebDriverWait(self.driver, BasePage.TIMEOUT).until(EC.visibility_of_element_located((By.ID, id))).click()

    def clickToFindByNameElement(self, name):
        WebDriverWait(self.driver, BasePage.TIMEOUT).until(EC.visibility_of_element_located((By.NAME, name))).click()

    def clickToFindByXpathElement(self, xpath):
        WebDriverWait(self.driver, BasePage.TIMEOUT).until(EC.visibility_of_element_located((By.XPATH, xpath))).click()

    def switchIframeByIdElement(self, id):
        WebDriverWait(self.driver, BasePage.TIMEOUT).until(EC.frame_to_be_available_and_switch_to_it((By.ID, id)))

    def switchIframeByXpathElement(self, xpath):
        WebDriverWait(self.driver, BasePage.TIMEOUT).until(EC.frame_to_be_available_and_switch_to_it((By.XPATH, xpath)))

    def switchIframeByNameElement(self, name):
        WebDriverWait(self.driver, BasePage.TIMEOUT).until(EC.frame_to_be_available_and_switch_to_it((By.NAME, name)))

    def selectToFindByXpathElement(self, xpath, value):
        select =Select(WebDriverWait(self.driver, BasePage.TIMEOUT).until(EC.visibility_of_element_located((By.XPATH, xpath)))) 
        select.select_by_value(value)

    def selectToFindByIdElement(self, id, value): 
        select =Select(WebDriverWait(self.driver, BasePage.TIMEOUT).until(EC.visibility_of_element_located((By.ID, id)))) 
        select.select_by_value(value)

    def checkExistsById(self, id):
        try:
            WebDriverWait(self.driver, BasePage.TIMEOUT).until(EC.visibility_of_element_located((By.ID, id))).click()
        except NoSuchElementException:
            return False
        return True

    def checkExistsByXpath(self, xpath):
        try:
            WebDriverWait(self.driver, BasePage.TIMEOUT).until(EC.visibility_of_element_located((By.XPATH, xpath))).click()
        except NoSuchElementException:
            return False
        return True

    def quitIframe(self):
        self.driver.switch_to.default_content()
    
    def rightClickToByXpath(self, xpath): 
        ActionChains(self.driver).context_click(WebDriverWait(self.driver, BasePage.TIMEOUT).until(EC.visibility_of_element_located((By.XPATH, xpath)))).perform()