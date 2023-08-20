import readCsv as rc

def cleanup(scrapedData):
    data = list()
    for line in scrapedData:
        temp = line.split(' ')

        temp[-1] = temp[-1].split('$')

        temp[-1][1] = temp[-1][1].split('(')

        temp[-1][-1] = temp[-1][-1][-1].split(')')

        if len(temp) > 1:
            data.append([temp[0], temp[-1][-1][0], temp[-1][-1][-1]])
    
    return data

# print(cleanup(rc.read_dataset('Scraped.csv')))