from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

def get_localities(sro):
    url = "https://esearch.delhigovt.nic.in/Complete_search.aspx"

    
    chrome_options = Options()
    chrome_options.add_argument("--headless")

    driver = webdriver.Chrome(options=chrome_options)  
    driver.get(url)

    
    sro_element = driver.find_element(By.ID, "ctl00_ContentPlaceHolder1_ddl_sro_s")
    sro_element.send_keys(sro)

    
    localities_element = driver.find_element(By.ID, "ctl00_ContentPlaceHolder1_ddl_loc_s")
    localities = [option.text for option in localities_element.find_elements(By.TAG_NAME, "option")]

    driver.quit()

    return localities[1:] 

if __name__ == "__main__":
    sro = "Central -Asaf Ali (SR III)"
    localities = get_localities(sro)
    print(localities)
