from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

URL = "https://www.linkedin.com/jobs/search/?f_LF=f_AL&geoId=102257491&keywords=python%20developer&location=London%2C%20England%2C%20United%20Kingdom&redirect=false&position=1&pageNum=0"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get(URL)
time.sleep(3)
sign = driver.find_element(By.CSS_SELECTOR, value="a.cta-modal__primary-btn.btn-md.btn-primary.inline-block.w-full.mt-3")
sign.click()
time.sleep(1)
mail_input = driver.find_element(By.CSS_SELECTOR, value="div.form__input--floating.mt-24 input#username")
password_input = driver.find_element(By.CSS_SELECTOR, value="div.form__input--floating.mt-24 input#password")
mail_input.send_keys("minniethepuf@gmail.com", Keys.TAB)
password_input.send_keys("2005supremacy", Keys.ENTER)
time.sleep(2)
jobs = driver.find_elements(By.CSS_SELECTOR, value="a.disabled.ember-view.job-card-container__link.job-card-list__title strong")

for job in jobs:
    job.click()
    time.sleep(1)
    save = driver.find_element(By.CSS_SELECTOR, value="button.jobs-save-button.artdeco-button.artdeco-button--3.artdeco-button--secondary span")
    save.click()

driver.quit()
