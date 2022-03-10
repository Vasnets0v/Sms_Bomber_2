from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import time
import random
import pyfiglet

pyfiglet.print_figlet("sms bomber 2")


def collect_info():
    init_info = {}
    print("Enter phone number:")
    init_info['phone_num'] = int(input())
    print("Enter number of loops (loops mean how many sms will be sent from the same service)")
    init_info['loops:'] = int(input())
    return init_info


def open_one_field_txt():
    with open("dictionary/one_field.txt", 'r') as one_field:
        content = []
        for field in one_field:
            content.append({"url": field.split()[0], "xpath": field.split()[1]})
        return content


# function use pages with one field (phone number field only)
# loops mean how many sms will be sent from the same service
def render_one_field_page(phone_number, loops):

    content = open_one_field_txt()

    for i in range(loops):
        # 'webdrivers' folder should contain the same chrome driver version as your chrome browser version on the system
        service = Service(executable_path="webdrivers/chromedriver.exe")
        browser = webdriver.Chrome(service=service)

        for item in content:
            browser.get(item["url"])
            time.sleep(random.randint(2, 5))
            field_on_page = browser.find_element(By.XPATH, value=item['xpath'])
            field_on_page.clear()
            field_on_page.send_keys(phone_number)
            field_on_page.send_keys(Keys.ENTER)
            time.sleep(random.randint(2, 5))
            browser.close()
            browser.quit()


if __name__ == "__main__":
    info = collect_info()
    render_one_field_page(info['phone_num'], info['loops'])
