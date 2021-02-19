import pytest
import time
from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from pageObjects.AddcustomerPage import AddCustomer
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
import string
import random

class Test_003_AddCustomer:
    baseURL = ReadConfig.getApplicationURL()
    username= ReadConfig.getUseremail()
    password = ReadConfig.getPassword()
    logger=LogGen.loggen()

    @pytest.mark.sanity
    def test_addCustomer(self,setup):
        self.logger.info("*********Test_003_AddCustomer************ ")
        self.driver=setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp=LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("**********Login Successful********")

        self.logger.info("**********Starting Add Customer Test*************")

        self.addcust = AddCustomer(self.driver)
        self.addcust.clickOnCustomersMenu()
        self.addcust.clickOnCustomersMenuItem()
        time.sleep(3)
        self.addcust.clickOnAddnew()

        self.logger.info("***********8 Provinding Customer Info**********")
        time.sleep(3)
        self.email = random_generator() + "@gmail.com"
        self.addcust.setEmail(self.email)
        self.addcust.setPassword("test123")
        time.sleep(3)
        self.addcust.setCustomerRoles("Vendors")
        time.sleep(3)
        self.addcust.setManagerOfVendor("Vendor 2")
        self.addcust.setGender("Female")
        self.addcust.setFirstName("Sivapriya")
        self.addcust.setLastName("Manikandan")
        self.addcust.setDob("10/20/1987")
        self.addcust.setCompanyName("Home")
        self.addcust.setAdminContent("..... This is for Testing........")
        self.addcust.clickOnSave()

        self.logger.info("************ Saving customer info**********")

        self.logger.info("*********** Add customer validation started*************")

        self.msg = self.driver.find_element_by_tag_name("body").text

        print(self.msg)
        if 'customer has been added successfully.' in self.msg:
            assert True == True
            self.logger.info("********** Add customer Test Passed**********")
        else:
            self.driver.save_screenshot(".\\Screenshots\\"+"test_addCustomer_scr.png")
            self.logger.error("******** Add customer Test Failed ********")
            assert True == False

        self.driver.close()
        self.logger.info("***** Ending Test_003_AddCustomer Test *********")

def random_generator(size=8, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))