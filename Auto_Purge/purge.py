from selenium import webdriver
from selenium.webdriver.support.select import Select
import time
import csv

#List
LinkDict = {
#Edit the URL
    "ad1" : [""],
    "ad2" : [""],
    "ad3" : [""],
    "view1" : [""],
    "view2" : [""],
    "batch1" : [""],
    "batch2" : [""],
    "dms1" : [""] 
}
print(LinkDict.keys())
which = input("Enter the Applicaion Name: ")
test=LinkDict.get(which)
print(test[0],",",test[1])

driver = webdriver.Chrome('chromedriver')
driver.set_window_position(-10000,0)
driver.get('https://id.vdms.io')
username=driver.find_element_by_id('Username')

#Enter The User Name
username.send_keys("")
password=driver.find_element_by_id('Password')

#Enter the Password
password.send_keys("")
password.submit()
driver.get('https://my.edgecast.com/ADN/PurgeLoad')
time.sleep(7)
driver.get('https://my.edgecast.com/ADN/PurgeLoad')
time.sleep(3)
print("Now CLicking")
#Auto 1
driver.find_element_by_partial_link_text('Bulk').click()
bulk=driver.find_element_by_name('bulkPaths')
bulk.send_keys(test[0])

#To CLick
driver.find_element_by_xpath('//*[@id="purgeFormBody"]/div/div/div[1]/cache-manager-form/div/div/div[5]/div[1]/ng-form/div/div[1]/a').click()

time.sleep(3)

#Auto 2
#driver.find_element_by_partial_link_text('Bulk').click()
bulk=driver.find_element_by_name('bulkPaths')
bulk.send_keys(test[1])

#To CLick
driver.find_element_by_xpath('//*[@id="purgeFormBody"]/div/div/div[1]/cache-manager-form/div/div/div[5]/div[1]/ng-form/div/div[1]/a').click()

#Manual
#time.sleep(5)
#bulk=driver.find_element_by_name('bulkPaths')
#bulk.send_keys("test")
