from selenium import webdriver 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.common.by import By 
import time 

# Initialising driver + whatsapp
driver = webdriver.Chrome('./chromedriver') 
driver.get("https://web.whatsapp.com/") 
wait = WebDriverWait(driver, 600) 
print("Scan QR Code then press enter...")
input()

target = 'Poppy'
count = int(input("Enter count: "))
string = "🥰"


def send_text_message(message): #' sends a message to the currently open contact'
	inp_xpath = '//*[@id="main"]//footer//div[contains(@contenteditable, "true")]'
	input_box = wait.until(EC.presence_of_element_located(( 
		By.XPATH, inp_xpath))) 
	print(f'Sending {message} to {input_box}')
	input_box.click()
	input_box.send_keys(message)
	input_box.send_keys(Keys.ENTER)

def select_contact(contact_name): # Clicks on target name in sidebar, openening chat window
	x_arg = '//span[contains(@title,"' + target + '")]'
	group_title = wait.until(EC.presence_of_element_located(( 
		By.XPATH, x_arg))) 
	group_title.click() 
	print("Found Target")

select_contact(target)

for i in range(count):
	send_text_message(string)