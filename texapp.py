from selenium import webdriver 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.common.by import By 
import time 

# Replace below path with the absolute path 
# to chromedriver in your computer 
driver = webdriver.Chrome('./chromedriver') 

driver.get("https://web.whatsapp.com/") 
wait = WebDriverWait(driver, 600) 

# Replace 'Friend's Name' with the name of your friend 
# or the name of a group 
target = 'L6 Further Maths'
count = int(input("Enter count: "))
# Replace the below string with your own message 
string = "bruh"

x_arg = '//span[contains(@title,"' + target + '")]'
group_title = wait.until(EC.presence_of_element_located(( 
	By.XPATH, x_arg))) 
group_title.click() 

print("Found Target")

inp_xpath = '//*[@id="main"]//footer//div[contains(@contenteditable, "true")]'
input_box = wait.until(EC.presence_of_element_located(( 
	By.XPATH, inp_xpath))) 

print("Found input ", input_box)

input_box.click()

for i in range(count): 
	input_box.send_keys(string)
	input_box.send_keys(Keys.ENTER) 