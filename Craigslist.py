# selenium for web driving
from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


def parse_page():
    # Using Chrome to access web
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 500)
    href_list = []
    address_list = []
    title_list = []

    # fileobject = open(file, "w+")

    url = 'https://kpr.craigslist.org/search/gms#search=1~list~0~0'
    driver.get(url)

    # radius = int(input("Radius (in miles): "))
    radius = 10
    # zipcode = int(input("Zipcode: "))
    zipcode = 99352

    # wait.until(EC.presence_of_element_located((By.NAME, 'search_distance')))
    # search_radius_input = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.NAME, "search_distance")))
    # search_radius_input = wait.until(EC.presence_of_element_located((By.NAME, "search_distance")))
    # search_radius_input = driver.find_element(By.NAME, 'search_distance')
    # search_radius_input.send_keys(radius)
    # search_radius_input.send_keys(Keys.RETURN)

    # wait.until(EC.presence_of_element_located((By.NAME, "postal")))
    # zipcode_input = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.NAME, "postal")))
    # zipcode_input.send_keys(zipcode)
    # zipcode_input.send_keys(Keys.RETURN)

    # identify elements with tag-name <a>
    wait.until(EC.presence_of_element_located((By.CLASS_NAME, "titlestring")))
    elements = driver.find_elements(By.CLASS_NAME, "titlestring")

    # traverse list
    for element in elements:
        # get_attribute() to get all href
        href = element.get_attribute('href')
        if href is not None:
            href_list.append(href)

    # remove duplicates
    unique_hrefs = set(href_list)

    for href in unique_hrefs:
        url = href
        driver.get(url)

        wait.until(EC.presence_of_element_located((By.CLASS_NAME, "mapaddress")))
        wait.until(EC.presence_of_element_located((By.CLASS_NAME, "postingtitletext")))

        address_element = driver.find_element(By.CLASS_NAME, "mapaddress")
        title_element = driver.find_element(By.CLASS_NAME, "postingtitletext")

        address = address_element.text
        title = title_element.text

        address_list += address
        title_list += title

    #  class ="mapaddress" > 6250 W.Clearwater Ave near Kellogg

    # sample of string to parse for address
    # <div class="mapaddress">1808 W 24th Ave near Rainer and Vancouver</div>

    for r in title_list:
        print(r)

    driver.quit()

    return


if __name__ == '__main__':
    # file_name = str(input("File to populate: "))
    # website = str(input("Auction to parse: "))
    # key_words = []
    # print("Enter '0' to finish list.")
    # while input != 0:
    #     name = str(input("Vehicle : "))
    #     key_words.append(name)
    #
    # parse_page1(file_name, website, key_words)
    parse_page()
