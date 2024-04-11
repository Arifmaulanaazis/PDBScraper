import requests, os, multiprocessing
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service


def dapatkan_data_PDB(kode_pdb):
    anchor_url = "https://www.rcsb.org/structure/"
    req = requests.get(anchor_url + kode_pdb)
    soup = BeautifulSoup(req.text, "html.parser")
    deskripsi = soup.find('span', {'id': 'structureTitle'}).text
    try:
        classification = soup.find('li', {'id': 'header_classification'}).text.strip().replace('Classification:', '')
    except:
        classification = "-"
    try:
        organism = soup.find('li', {'id': 'header_organism'}).text.strip().replace('Organism(s):', '')
    except:
        organism = "-"
    try:
        expression_system = soup.find('li', {'id': 'header_expression-system'}).text.strip().replace('Expression System:', '')
    except:
        expression_system = "-"
    try:
        mutation = soup.find('li', {'id': 'header_mutation'}).text.strip().replace('Mutation(s):', '')
    except:
        mutation = "-"
    try:
        deposited_released_dates = soup.find('li', {'id': 'header_deposited-released-dates'}).text.strip().replace('Deposited:', '').replace('Released:', '')
    except:
        deposited_released_dates = "-"
    try:
        deposition_authors = soup.find('li', {'id': 'header_deposition-authors'}).text.strip().replace('Deposition Author(s):', '')
    except:
        deposition_authors = "-"
    os.system('cls')
    print(f"PDB ID: {kode_pdb}")
    print(f"Description: {deskripsi}")
    print(f"Classification: {classification}")
    print(f"Organism(s): {organism}")
    print(f"Expression System: {expression_system}")
    print(f"Mutation(s): {mutation}")
    print(f"Deposited: {deposited_released_dates}")
    print(f"Deposition Author(s): {deposition_authors}")

    return [kode_pdb, deskripsi, classification, organism, expression_system, mutation, deposited_released_dates, deposition_authors]



def dapatkan_kode_PDB(keywoard):
    DRIVER_PATH = './driver/chromedriver.exe'
    options = Options()
    options.add_argument('log-level=3')
    options.add_argument("--disable-popup-blocking")
    options.add_argument('--disable-gpu')
    options.add_argument("--disable-notifications")
    options.add_argument("--headless=new")
    options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36")
    prefs = {"profile.managed_default_content_settings.images": 2}
    options.add_experimental_option("prefs", prefs)
    driver = webdriver.Chrome(options=options, service=Service(DRIVER_PATH))
    driver.get("https://www.rcsb.org/")
    wait = WebDriverWait(driver, 30)
    input_keywoard = wait.until(EC.visibility_of_element_located((By.ID, "search-bar-input-text"))).send_keys(keywoard)
    cari = wait.until(EC.visibility_of_element_located((By.ID, "search-bar-input-text"))).send_keys(Keys.ENTER)
    tombol_unduh = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".glyphicon-download-alt"))).click()
    
    try:
        list_PDB = wait.until(EC.visibility_of_element_located((By.XPATH, "//textarea[@id=\'downloadsIdList\']"))).text
    except:
        peringatan = driver.execute_script("window.alert = function() {};")
        list_PDB = wait.until(EC.visibility_of_element_located((By.XPATH, "//textarea[@id=\'downloadsIdList\']"))).text
    driver.quit()
    return list_PDB


def cek_chrome_driver():
    if os.path.isfile('./driver/chromedriver.exe'):
        print("""
                ██████╗░██████╗░██████╗░  ░██████╗░█████╗░██████╗░░█████╗░██████╗░███████╗██████╗░
                ██╔══██╗██╔══██╗██╔══██╗  ██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗██╔════╝██╔══██╗
                ██████╔╝██║░░██║██████╦╝  ╚█████╗░██║░░╚═╝██████╔╝███████║██████╔╝█████╗░░██████╔╝
                ██╔═══╝░██║░░██║██╔══██╗  ░╚═══██╗██║░░██╗██╔══██╗██╔══██║██╔═══╝░██╔══╝░░██╔══██╗
                ██║░░░░░██████╔╝██████╦╝  ██████╔╝╚█████╔╝██║░░██║██║░░██║██║░░░░░███████╗██║░░██║
                ╚═╝░░░░░╚═════╝░╚═════╝░  ╚═════╝░░╚════╝░╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░░░░╚══════╝╚═╝░░╚═╝
                𝓥1.0 || 𝑪𝒐𝒑𝒚𝒓𝒊𝒈𝒉𝒕 𝑨𝒓𝒊𝒇 𝑴𝒂𝒖𝒍𝒂𝒏𝒂 2023
                """)
    else:
        print("Chrome Driver belum tersedia, silahkan download terlebih dahulu")
        print("https://chromedriver.chromium.org/downloads")
        exit()



def main():
    cek_chrome_driver()
    keywoard = ""
    if sys.stdin.isatty():
        keywoard = str(input("Masukkan keywoard: "))
    list_pdb = dapatkan_kode_PDB(keywoard)
    list_pdb_baru = list_pdb.split(",")
    print(f"Jumlah PDB ID: {len(list_pdb_baru)}")
    pool = multiprocessing.Pool()
    data_pdb = pool.map(dapatkan_data_PDB, list_pdb_baru)
    pool.close()
    pool.join()
    df = pd.DataFrame(data_pdb, columns=['PDB ID', 'Description', 'Classification', 'Organism(s)', 'Expression System', 'Mutation(s)', 'Deposited', 'Deposition Author(s)'])
    try:
        os.mkdir('./hasil')
    except:
        pass
    df.to_excel(f'./hasil/{keywoard}.xlsx', index=False)
    os.system('cls')
    print(f"Jumlah data didapatkan: {len(df)}")
    print(f"File {keywoard}.xlsx berhasil disimpan di folder hasil (hasil/{keywoard}.xlsx)")
    print("Program selesai")

if __name__ == '__main__':
    main()
