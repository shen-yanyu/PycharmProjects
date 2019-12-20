from selenium import webdriver
import time

driver = webdriver.Chrome()
response = driver.get('http://www.cfbond.com/kechuangban/index.html')
#print(driver.page_source)

time.sleep(2)
for i in range(5):
    js = 'var q=document.documentElement.scrollTop=' + str(i*500)
    driver.execute_script(js)
    time.sleep(3)
#for i in range(3):
 #   button_tag = driver.find_element_by_class_name('load_more')
    #button_tag.click()
    #time.sleep(3)
driver.quit()



    

'''
#设置chromedriver不加载图片
chrome_opt = webdriver.ChromeOptions()
prefs = {"profile.managed_default_content_setting.images":2}
chrome_opt.add_experimental_option("prefs", prefs)
driver = webdriver.Chrome(options=chrome_opt)
driver.get('http://www.cfbond.com/kechuangban/index.html')
'''