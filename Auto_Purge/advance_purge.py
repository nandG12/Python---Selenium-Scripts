from selenium import webdriver
import time
import csv
from selenium.webdriver.support.select import Select

def purge(test,bul):
    driver = webdriver.Chrome('chromedriver')
    if bul == "y" or bul == "yes" or bul == "Y" or bul == "Yes" or bul == "YES":
        #driver.set_window_position(-10000,0)
        print("")
        print("browser is visible")
    else:
        driver.set_window_position(-10000,0)
        print("")
        print("browser is not visible, running in background")
    print("State - Entering username and password")
    driver.get('https://id.vdms.io')
    username=driver.find_element_by_id('Username')
    username.send_keys("techops2@asite.com")
    password=driver.find_element_by_id('Password')
    password.send_keys("T3ch0p5@29")
    password.submit()
    print("State - Submited and opening purge URl")
    driver.get('https://my.edgecast.com/ADN/PurgeLoad')
    time.sleep(7)
    driver.get('https://my.edgecast.com/ADN/PurgeLoad')
    time.sleep(3)
    print("--------------------------------------------------Starting--------------------------------------------------")

    #New Code For Loop
    driver.find_element_by_partial_link_text('Bulk').click()
    for i in range(len(test)):
        bulk=driver.find_element_by_name('bulkPaths')
        bulk.send_keys(test[i])
        print("URL - ",test[i]," Done")
        driver.find_element_by_xpath('//*[@id="purgeFormBody"]/div/div/div[1]/cache-manager-form/div/div/div[5]/div[1]/ng-form/div/div[1]/a').click()
        time.sleep(4)

    print("-----------------------------------------------Run Successfully---------------------------------------------")

    driver.close()

def stime():
    driver = webdriver.Chrome('chromedriver')
    #driver.set_window_position(-10000,0)
    print("browser is visible")
    print("State - Entering username and password")
    driver.get('https://id.vdms.io')
    username=driver.find_element_by_id('Username')
    username.send_keys("techops2@asite.com")
    password=driver.find_element_by_id('Password')
    password.send_keys("T3ch0p5@29")
    password.submit()
    print("State - Submited and opening purge URl")
    driver.get('https://my.edgecast.com/ADN/PurgeLoad')
    time.sleep(7)
    driver.get('https://my.edgecast.com/ADN/PurgeLoad')
    time.sleep(3)
    driver.find_element_by_xpath('/html/body/div/section/section/div/div/div/div[4]/div/div/div[2]/div')
    time.sleep(20)
    driver.close()


if __name__ == "__main__":
    #List
    LinkDict = {
        "ad1" : ["http://adoddleqaak.asite.com/*","http://adoddleqab.asite.com/*"],
        "ad2" : ["http://adoddleqa2ak.asite.com/*","http://adoddleqa2b.asite.com/*"],
        "ad3" : ["http://adoddleqa3ak.asite.com/*","http://adoddleqa3b.asite.com/*"],
        "view1" : ["http://3dviewerqa.asite.com/*","http://3dviewerqab.asite.com/*"],
        "view2" : ["http://3dviewerqa2ak.asite.com/*","http://3dviewerqa2b.asite.com/*"],
        "batch1" : ["http://batchprintqaak.asite.com/*","http://batchprintqab.asite.com/*"],
        "batch2" : ["http://batchprintqa2ak.asite.com/*","http://batchprintqa2b.asite.com/*"],
        "dms2" : ["http://dmsqa2ak.asite.com/*","http://dmsqa2b.asite.com/*"],
        "mar1" : ["http://marketplaceqab.asite.com/*","http://marketplaceqaak.asite.com/*"],
        "mar2" : ["http://marketplaceqa2b.asite.com/*","http://marketplaceqa2ak.asite.com/*"]
    }
    print(LinkDict.keys())
    now = True  
    while(now):
        print("--------------------------------------------------Enter--------------------------------------------------")
        print("")
        print("For exit the program enter \"end\"")
        buf = input("Chrome Window should be visible or not(defualt value is no): ")
        if buf == None:
            buf = "No"
        print("Enter Show for timing")
        which = input("Enter the Applicaion Name: ")
        if which == "show" or which == "Show" or which == "SHOW":
            print("--------------------------------------------------Showing the Time--------------------------------------------------")
            stime()
        elif which == "d":
            daily()
        elif which != "end":
            app=LinkDict.get(which)
            for i in range(len(app)):
                print("URL -", app[i])
            purge(app,buf)
            print("--------------------------------------------------Exit--------------------------------------------------")
            print("")
        else:
            now = False
            print("Program Completed")

