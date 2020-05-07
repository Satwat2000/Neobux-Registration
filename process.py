from selenium.webdriver.common.by import By
from selenium import webdriver 
import os, Db


from urllib import request

class func():
    def __init__(self):
        pass

    def open_url(self):
        # option = webd.ChromeOptions()
        # option.add_argument("--headless")
        self.browser = webdriver.Chrome(executable_path=r'C:\Chrome\chromedriver.exe')
        self.browser.get("https://www.neobux.com/m/r/?vl=2ADF6C09815021CD")
        return (self.get_capta())
        
    def get_capta(self):
        images = self.browser.find_elements_by_tag_name('img')   #-----------> Find img tags form the source
        img = images[0].get_attribute('src')        #---------------> Find source of the found img tag
        self.data = request.urlretrieve(img)
        return self.data[0]

    def fill_info(self):
        user = self.browser.find_element_by_id("nomedeutilizador")
        passw = self.browser.find_element_by_id("palavrapasse")
        repass = self.browser.find_element_by_id("palavrapasseconfirmacao")
        email = self.browser.find_element_by_id("emailprincipal")
        Birth_year = self.browser.find_element_by_id("anonascimento")
        capta = self.browser.find_element_by_id("codigo")
        cont = self.browser.find_element_by_id("botao_registo")
        tick1 = self.browser.find_element_by_id("tosagree")
        tick2 = self.browser.find_element_by_id("ppagree")
        tick1.click()
        tick2.click()
        data = Db.get_val()
        user.send_keys(data["user"])
        passw.send_keys(data["pswd"])
        repass.send_keys(data["pswd"])
        email.send_keys(data["mail"])
        Birth_year.send_keys(data["year"])
        capta.send_keys(data["code"])
        cont.click()