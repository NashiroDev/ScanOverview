from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
import time
import os

def scrapData(urlList):

    # Set the path to the ChromeDriver executable
    path_to_chromedriver = 'C:/WebDriver/chromedriver.exe'

    # Create a Service object
    s = Service(executable_path=path_to_chromedriver)

    # Pass the Service object to the Chrome constructor
    driver = webdriver.Chrome(service=s)

    data, dataset = [], ""

    # try:
    for i in range(len(urlList)):

        # Construct the URL for the block page
        url = urlList[i]

        match urlList[i][0]:
            case 'eth':

                dataset = constructorScrap(driver, data, dataset, url)
            
            case 'arb':

                dataset = constructorScrap(driver, data, dataset, url)

            case 'matic':

                dataset = constructorScrap(driver, data, dataset, url)

            case 'base':
                
                dataset = constructorScrap(driver, data, dataset, url)

            case 'avax':
                
                dataset = constructorScrap(driver, data, dataset, url)

            case 'op':
                
                dataset = constructorScrap(driver, data, dataset, url)

            case 'zora':
                
                pass

            case 'bsc':
                
                dataset = constructorScrap(driver, data, dataset, url)

            case 'metis':
                pass

            case 'opbnb':
                pass

            case 'mnt':
                pass

            case 'era':
                pass

            case 'linea':
                
                dataset = constructorScrap(driver, data, dataset, url)

            case 'pze':
                pass

            case 'nova':
                
                dataset = constructorScrap(driver, data, dataset, url)

            case 'celo':
                pass

            case 'core':
                
                dataset = constructorScrap(driver, data, dataset, url, 'class name', "el-row power-description", 1)

            case 'kava':
                pass

            case 'canto':
                pass

            case 'mobm':
                pass
            
            case 'fuse':
                
                dataset = constructorScrap(driver, data, dataset, url, 'class name', "col-sm-9 col-lg-10", 1)

            case 'xdai':
                
                dataset = constructorScrap(driver, data, dataset, url)

            case 'ftm':
                
                dataset = constructorScrap(driver, data, dataset, url)

            case 'movr':
                pass
            
            case 'okt':
                pass

            case 'klay':
                pass

            case 'hmy':
                pass

        # Advancment feedback in terminal
        if i % 25 == 0:
            print(f"{i}/{len(urlList)} Transactions scalped")

        # Call writeToCsv method to save current block data
        writeToCsv(dataset.split("\n"))

        data, dataset = [], ""

    # except:
    #     print('Error while proccessing a block')

def constructorScrap(driver, data, dataset, url, findElem='id', elem='ContentPlaceHolder1_divTxFee', mode=0):

    time.sleep(0.32)
    driver.get(str(url[1]))

    WebDriverWait(driver, 10, 2.2)

    data.extend(driver.find_elements(findElem, elem))

    if mode:
        for line in data:
            if 'Transaction Fee' in line.text:
                dataset = line.text
    else:
        for line in data:
            dataset = line.text + str(url[0])
    
    return dataset

def writeToCsv(data):
    # Set the filename for the CSV file
    filename = f'Scraped.csv'

    # Check if the file exists
    file_exists = os.path.isfile(filename)

    toWrite = ''

    # Open the file in append mode
    with open(filename, 'a') as file:
        # If the file doesn't exist, write the header row
        if file_exists:
            for elem in data:
                if len(data) > 1:
                    if elem != data[0]:
                        toWrite += elem.replace(':', '') + '/'
                else: toWrite += elem.replace(':', '') + '/'
            try:
                if toWrite != '/':
                    file.write(toWrite + '\n')
            except:
                pass