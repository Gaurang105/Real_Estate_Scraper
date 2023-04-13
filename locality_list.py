from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

def get_localities(sro):
    url = "https://esearch.delhigovt.nic.in/Complete_search.aspx"

    # Set up Chrome options for headless browsing
    chrome_options = Options()
    chrome_options.add_argument("--headless")

    driver = webdriver.Chrome(options=chrome_options)  # Add the chrome_options argument
    driver.get(url)

    # Select the SRO
    sro_element = driver.find_element(By.ID, "ctl00_ContentPlaceHolder1_ddl_sro_s")
    sro_element.send_keys(sro)

    # Scrape localities from the dropdown
    localities_element = driver.find_element(By.ID, "ctl00_ContentPlaceHolder1_ddl_loc_s")
    localities = [option.text for option in localities_element.find_elements(By.TAG_NAME, "option")]

    driver.quit()

    return localities[1:]  # Remove the first element from the list

if __name__ == "__main__":
    sro = "Central -Asaf Ali (SR III)"
    localities = get_localities(sro)
    print(localities)
