from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import time
import random
import pyfiglet
import os


def collect_info():
    init_info = {'phone_num': int(input('Enter phone number:')),
                 'loops': int(input('Enter number of loops (loops mean how many sms w'
                                    'ill be sent from the same service):'))}
    print("Good, We are working!")
    return init_info


def collect_sites_with_elements():
    sites = []
    for file in os.listdir('dictionary'):
        if file.endswith('.txt'):
            sites.append(file)

    sites_with_elements = []

    for site in sites:
        with open(f'dictionary/{site}') as temp_file:
            elements_list = []
            for element in temp_file:
                elements_list.append(element)
            sites_with_elements.append({'site': site, "items": elements_list})
    return sites_with_elements


if __name__ == "__main__":
    print(collect_sites_with_elements())

#            'webdrivers' folder should contain the same chrome driver version as your chrome browser version
#             service = Service(executable_path="webdrivers/chromedriver.exe")
#             browser = webdriver.Chrome(service=service)
#
#             browser.get(item["url"])
#             time.sleep(random.randint(2, 5))
#             field_on_page = browser.find_element(By.XPATH, value=item['xpath'])
#             # sometime need to focus on element .click()
#             field_on_page.click()
#             field_on_page.clear()
#             field_on_page.send_keys(phone_number)
#             time.sleep(1)
#             field_on_page.send_keys(Keys.ENTER)
#             time.sleep(random.randint(2, 5))
#             input()
#             browser.close()
#             browser.quit()
