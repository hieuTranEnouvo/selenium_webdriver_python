# from selenium import webdriver
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.ui import Select
# from selenium.common.exceptions import NoSuchElementException 
# from selenium.webdriver.common.action_chains import ActionChains

# urlAcc = 'https://accounts.google.com/o/oauth2/v2/auth/oauthchooseaccount?redirect_uri=https%3A%2F%2Fdevelopers.google.com%2Foauthplayground&prompt=consent&response_type=code&client_id=407408718192.apps.googleusercontent.com&scope=email&access_type=offline&flowName=GeneralOAuthFlow'
# urlDocs = 'https://docs.google.com/spreadsheets/d/1bq0oBrpu4Ur2goqyJOf2bwsjynzrxB_JEwLHrzUQWdo/edit?addon_dry_run=AAnXSK9pEBV4ZBG5xi2SIEKPHhS_j_Q-qHYrAsbqR2j3ADWjH5Ao-zWmL7tBXXka7G2W9PPEfsHH1x_UW2iTBFee-fdkaF7zsrQTAorLqC_EAk1U0u1MIbNLMm91Sn1G733brnlNrVNN#gid=0'
# gmail = 'username'
# gmail_password = 'password'
# driver = webdriver.Firefox(executable_path='..//python-cucumber/features/drivers/geckodriver')
# driver.get(urlAcc)
# driver.implicitly_wait(60)
# driver.find_element_by_xpath('//input[@id="identifierId"]').send_keys(gmail)
# driver.find_element_by_id('identifierNext').click()
# button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.NAME, 'password')))
# button.send_keys(gmail_password)
# driver.find_element_by_id('passwordNext').click()
# driver.get(urlDocs)
# WebDriverWait(driver, 8000).until(EC.visibility_of_element_located((By.ID, 'docs-extensions-menu'))).click()
# WebDriverWait(driver, 2000).until(EC.visibility_of_element_located((By.XPATH, '//div[@class="goog-menuitem-content" and contains(text(), "Actable AI ")]'))).click()
# WebDriverWait(driver, 2000).until(EC.visibility_of_element_located((By.XPATH, '//div[@class="goog-menuitem-content" and contains(text(), "Regression")]'))).click()

# WebDriverWait(driver, 2000).until(EC.frame_to_be_available_and_switch_to_it((By.XPATH, '(//iframe[@frameborder=0])[2]')))
# WebDriverWait(driver, 2000).until(EC.frame_to_be_available_and_switch_to_it((By.ID, 'sandboxFrame')))
# WebDriverWait(driver, 2000).until(EC.frame_to_be_available_and_switch_to_it((By.ID, 'userHtmlFrame')))

# # select =Select(WebDriverWait(driver, 2000).until(EC.visibility_of_element_located((By.ID, 'regression-predicted-target')))) 
# # select.select_by_value('rental_price')
# # WebDriverWait(driver, 2000).until(EC.visibility_of_element_located((By.XPATH, '//ul[@class="select2-selection__rendered"]'))).click()
# # WebDriverWait(driver, 2000).until(EC.visibility_of_element_located((By.XPATH, '//li[@role="treeitem"]/span[contains(text(),"Select All")]'))).click()
# # select =Select(WebDriverWait(driver, 2000).until(EC.visibility_of_element_located((By.ID, 'regression-predicted-target')))) 
# # select.select_by_value('rental_price')
# # # WebDriverWait(driver, 2000).until(EC.visibility_of_element_located((By.ID, 'btn-query'))).click()

# driver.switch_to.default_content()
# logo = driver.find_element_by_xpath('//span[@class="docs-sheet-tab-name" and contains(text(),"_validation")]') 
# ActionChains(driver).context_click(logo).perform()
# WebDriverWait(driver, 20000).until(EC.visibility_of_element_located((By.XPATH, '//div[@class="goog-menuitem-content" and contains(text(),"Delete")]'))).click()
# WebDriverWait(driver, 20000).until(EC.visibility_of_element_located((By.XPATH, '//button[@name="cancel"]'))).click()
