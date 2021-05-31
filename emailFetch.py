from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os
import time

browser = webdriver.Chrome(
    executable_path=os.getcwd() + "/python-selenium-basic/drivers/chromedriver")

f = open("contact_info.csv", "w")

f.write("club name, email\n")

home = "https://www.ulife.utoronto.ca"


def switchPage(pg_num):
    page = "/organizations/list/campus/utm/page/{}/type/all".format(pg_num)
    url = home + page
    browser.get(url.strip().encode('ascii', 'ignore').decode('unicode_escape'))
    return url


def filterPageList(redirect):
    functional = True
    for c in range(0,24):
        clubList = browser.find_elements_by_class_name("innerListing")
        clubs = clubList[0].find_elements_by_xpath(".//li")
        cp = clubs[c].find_elements_by_xpath(".//a")
        # url = cp[0].get_attribute("href")
        # browser.execute_script(f"window.open({url});")
        browser.get(cp[0].get_attribute("href"))
        try:
            name = browser.find_element_by_tag_name("h1").text
            f.write(name + ", ")
            try:
                contact = browser.find_elements_by_xpath("//*[text() = 'Contact Us']")
                email = contact[1].get_attribute("href")
                f.write(email)
            except Exception:
                pass
            except TypeError:
                pass
        except AttributeError:
            browser.get(redirect)
        f.write("\n")
        browser.get(redirect)


def main():
    for i in range(1,8):
        # time.sleep(1)
        filterPageList(switchPage(i))

main()