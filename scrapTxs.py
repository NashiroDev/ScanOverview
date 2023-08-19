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

        print(urlList[i][1])

        # Construct the URL for the block page
        url = urlList[i]

        match urlList[i][0]:
            case 'eth':

                # Wait 0.31s to avoid ban while browsing blocks
                time.sleep(0.31)

                driver.get(str(url[1]))

                WebDriverWait(driver, 10, 2.2)

                data.extend(driver.find_elements('id', 'ContentPlaceHolder1_divTxFee'))

                for line in data:
                    dataset = line.text
            
            case 'arb':

                time.sleep(0.31)

                driver.get(str(url[1]))

                WebDriverWait(driver, 10, 2.2)

                data.extend(driver.find_elements('id', 'ContentPlaceHolder1_divTxFee'))

                for line in data:
                    dataset = line.text

            case 'matic':
                pass

            case 'base':
                pass

            case 'avax':
                pass

            case 'op':
                pass

            case 'zora':
                pass

            case 'bsc':
                pass

            case 'metis':
                pass

            case 'opbnb':
                pass

            case 'mnt':
                pass

            case 'era':
                pass

            case 'linea':
                pass

            case 'pze':
                pass

            case 'nova':
                pass

            case 'celo':
                pass

            case 'core':
                pass

            case 'kava':
                pass

            case 'canto':
                pass

            case 'mobm':
                pass
            
            case 'fuse':
                pass

            case 'xdai':
                pass

            case 'ftm':
                pass

            case 'movr':
                pass
            
            case 'okt':
                pass

            case 'klay':
                pass

            case 'hmy':
                pass

        # Advancment feedback in terminal
        if i % 10 == 0:
            print(f"{i}/{len(urlList)} Transactions scalped")

        print(dataset)
        # Call writeToCsv method to save current block data
        writeToCsv(dataset.split("\n"))

        data, dataset = [], ""

    # except:
    #     print('Error while proccessing a block')

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
                toWrite += elem.replace(':', '') + '/'
            try:
                if toWrite != '/':
                    file.write(toWrite + '\n')
            except:
                pass