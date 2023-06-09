from tabnanny import check
from time import sleep
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import datetime

browser  = webdriver.Chrome(ChromeDriverManager().install())

minv = 20
rev = 0

user = ""
passwrd = ""

browser.implicitly_wait(1)

#Goto robinhood exon mobil page
browser.get("https://robinhood.com/crypto/ETH")

sleep(1)

                            #Login
#Press Login from nav bar
browser.find_element_by_xpath("//div[@class='_3VgtNTJk4xjbgN0dDvs4U9']/a[5]").click()

#Input username and password
browser.find_element_by_name("username").send_keys(user)
browser.find_element_by_name("password").send_keys(passwrd)
sleep(1)

#Press continute
browser.find_element_by_class_name("css-1vvsyzd-UnstyledButton-BaseButton").click()

                            #SMS Test
#Click sms button
browser.find_element_by_xpath("//div[@class='css-d8froh']/div/button/span[@class='css-1o0fjrg']").click()

#Enter code from phone
code = int(input("Enter code from phone: "))

#Sends code from phone to input box
browser.find_element_by_xpath("//div[@class='css-cgvuc8-InternalInput']/input[@type='text']").send_keys(code)

#Press Continue: Pass sms test
browser.find_element_by_class_name("css-1vvsyzd-UnstyledButton-BaseButton").click()


sleep(5)


                            #Selling
def sell(amt):
    browser.find_element_by_xpath("//div[@class='_1XsyCTEfumrBN7lTuT0E3K']/div[2]").click()
    browser.find_element_by_name("amount").send_keys("{}".format(amt))
    browser.find_element_by_class_name("css-jowa3o-UnstyledButton-BaseButton").click()
    browser.find_element_by_class_name("css-jowa3o-UnstyledButton-BaseButton").click()
                            #Buying
def buy(amt):
    browser.find_element_by_xpath("//div[@class='_1XsyCTEfumrBN7lTuT0E3K']/div").click()
    browser.find_element_by_name("amount").send_keys("{}".format(amt))
    browser.find_element_by_class_name("css-jowa3o-UnstyledButton-BaseButton").click()
    browser.find_element_by_class_name("css-jowa3o-UnstyledButton-BaseButton").click()

                            #Checkprice
def checkprice():
    x = str(browser.find_element_by_xpath("//h2[@class='css-i16h77']/span/span/div/div/span[2]").text)
    x = x + str((browser.find_element_by_xpath("//h2[@class='css-i16h77']/span/span/div/div/span[4]").text))
    x = x + str((browser.find_element_by_xpath("//h2[@class='css-i16h77']/span/span/div/div/span[5]").text))
    x = x + str((browser.find_element_by_xpath("//h2[@class='css-i16h77']/span/span/div/div/span[6]").text))
    x = x + str((browser.find_element_by_xpath("//h2[@class='css-i16h77']/span/span/div/div/span[7]").text))
    x = x + str((browser.find_element_by_xpath("//h2[@class='css-i16h77']/span/span/div/div/span[8]").text))
    x = x + str((browser.find_element_by_xpath("//h2[@class='css-i16h77']/span/span/div/div/span[9]").text))
    #print(x)
    x.strip()
    #print(x)
    try:
        x = float(x)
        if x<3001.01:
            checkprice()
    except:
        return checkprice()
    else:
        x = float(x)
        if x<3001.01:
            checkprice()
        return x


#sell(1)
#buy(1)
sleep(5)
ogp = float(checkprice())
if ogp>3001.01:   
    print(ogp)
while True:
    print(datetime.datetime.now())
    sleep(1)
    cur = float(checkprice())
    #print(cur)
    if cur < 3001.01:
        continue
    else:
        if (ogp * 1.002 <= cur):
            print("Sell: {}".format(cur))
            sellamt = minv * (cur/ogp)
            minv = 0 
            sell(sellamt)
            if sellamt>0:
                rev = sellamt
            browser.refresh()
            #ogp = cur
            #print("NEW OGP: {}".format(ogp))
        elif (cur * 1.002 <= ogp):
            if rev > 0:
                print("Buy: {}".format(cur))
                minv += rev
                buy(rev)
                rev = 0
                browser.refresh()
            #ogp = cur
            #print("NEW OGP: {}".format(cur))
        else:
            print("CUR: ",cur," , OGP: ",ogp)
            print("Price needed to sell: {}".format(round(ogp*1.002,2)))
            print("Price needed to buy: {}".format(round(ogp/1.002,2)))
            print("Current money invested: {}".format(minv))
            print("Cash available to use: {}".format(rev)) 
        sleep(20)
