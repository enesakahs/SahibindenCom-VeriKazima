from selenium import webdriver
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.common.by import By
#selenıum uzerıden erıstıgımız sıtelerde klavye ıle ıslem yapmak ıstedıgımızde ımport etmemız gereken yapı. Örn: klavyeden enter a bas
import time

driver=webdriver.Chrome("C:/Users/enes_/OneDrive/Masaüstü/Python Egitimleri/ChromeDriver/chromedriver.exe")

url="https://www.sahibinden.com/"
driver.get(url)
time.sleep(5)
driver.maximize_window()
time.sleep(5)

arac_ara=driver.find_element("xpath","//*[@id='searchText']")
arac_ara.send_keys("bmw 3 serisi") #arama kısmına otomatık olarak yazılacak alan
arac_ara.send_keys(Keys.ENTER) #entera bassın arama gerceklessın
time.sleep(5)



for i in range(1,20): #sayfadaki 20 degeri istedik
    ilan_baslık=driver.find_element("xpath","//*[@id='searchResultsTable']/tbody/tr[{}]/td[2]/a[1]".format(i)) #tüm baslık ilanlarının xpatch i aynı adreste sadece tr kısmı artarak gittigi icin döngüye aldık
    fiyat=driver.find_element("xpath","//*[@id='searchResultsTable']/tbody/tr[{}]/td[3]/div/span".format(i))
    print(f"\nİlan Başlıgı: {ilan_baslık.text}\nFiyat: {fiyat.text}\n")
