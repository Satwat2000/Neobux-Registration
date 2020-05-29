from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.common import exceptions
from win32com.client import Dispatch
from selenium import webdriver 
import os, Db


from urllib import request

class func():
   
    def open_url(self):
        # option = webd.ChromeOptions()
        # option.add_argument("--headless")
        try:
            self.browser = webdriver.Chrome(executable_path=r'C:\Chrome\chromedriver.exe')
            self.browser.get("https://www.neobux.com/m/r/?vl=A3CF35334710E577")
            return True
        except Exception as e:
            print(e)
            return False
        # return (self.get_capta())
        
    def get_capta(self):
        images = self.browser.find_elements_by_tag_name('img')   #-----------> Find img tags form the source
        img = images[0].get_attribute('src')        #---------------> Find source of the found img tag
        self.data = request.urlretrieve(img)
        return self.data[0]

    def getSnap(self, name):
        path = 'review'+name
        self.browser.get_screenshot_as_file(path)
        
    def pg1_err(self):
        print("into for check")
        rdata={'pass':True,     # Limiter
                'usr':False,    # Username error
                'capt':False}   # Capta error
        try:
            element = WebDriverWait(self.browser, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'ul')))
            print("-----Error found-----")
            rdata['pass'] = False
            errs = element.get_attribute('textContent').split('.')
            print("Errors Identified")
            print(errs)
            for e in errs:
                if 'username' in e:
                    rdata['usr']= True
                if 'image' in e:
                    rdata['capt'] = True 
            print("returning data")
            return rdata    
        except TimeoutException:
            print ("No Errors found in 1st step")
            return rdata
           
    
    def fill_info(self):
        ksec1 = Keys.chord(Keys.CONTROL,'')
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
        return (self.pg1_err())



    
# func.open_url(func)

class support():
    def chrome_version(self):
        paths = [r"C:\Program Files\Google\Chrome\Application\chrome.exe",
                r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"]
        version = list(filter(None, [self.get_version_via_com(p) for p in paths]))[0]
        version = version.split('.')
        return(str(version[0]))

    def get_version_via_com(self,filename):
        parser = Dispatch("Scripting.FileSystemObject")
        try:
            version = parser.GetFileVersion(filename)
        except Exception:
            print("Chrome.exe not found")
            return None
        return version

