from selenium import webdriver

driver = webdriver.Chrome(r"C:\Users\Admin\Downloads\chromedriver.exe")
driver.get('https://web.whatsapp.com/')

name = input('To User: ')
msg = input('Message: ')
count = int(input('Count: '))

input('HIT ENTER BRUH NUKE EM')

user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
user.click()

msg_box = driver.find_element_by_class_name('_3uMse')

for i in range(count):
	msg_box.send_keys(msg)
	button = driver.find_element_by_class_name('_1U1xa')
	button.click()