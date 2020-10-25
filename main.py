from selenium import webdriver
driver = webdriver.Chrome()
driver.get("https://www.thrifty.co.nz/")

driver.find_element_by_xpath('//*[@id="ccw-search-form-2"]/div[1]/div[1]/label')

#print(driver.title)
#driver.quit()
#print(driver.page_source)