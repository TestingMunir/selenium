from selenium import webdriver
import time

driver = webdriver.Chrome()

urls = [
    "https://www.google.com",
    "https://www.wikipedia.org",
    "https://www.amazon.in"
]

# Open the first URL
driver.get(urls[0])
current_handle=driver.current_window_handle
time.sleep(2)



# Open other URLs in new tab

for url in urls[1:]:
    driver.switch_to.new_window("tab")
    driver.get(url)

list_handles=driver.window_handles

print("list of handles:-",list_handles)


for handle in list_handles:
    driver.switch_to.window(handle)
    print("current title:",driver.current_url,driver.title)

driver.switch_to.window(current_handle)
    


