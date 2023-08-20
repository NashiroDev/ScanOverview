import readCsv as rc

def cleanup(scrapedData):
    data = list()
    for line in scrapedData:
        temp = line.split(' ')

        temp[-1] = temp[-1].split('$')

        temp[-1][1] = temp[-1][1].split('(')

        temp[-1][-1] = temp[-1][-1][-1].split(')')

        temp2 = temp[-1][-1][0]
        temp[-1][-1] = temp[-1][-1][-1].rsplit('/')

        if len(temp) > 1:
            if temp[-1][-1][0] != '':
                data.append([temp[0], temp[-1][-1][0], temp[-1][-1][1]])
            else: data.append([temp[0], temp2, temp[-1][-1][1]])
    return data

def getStatistics(data):
    panel = dict()
    for line in data:
        if line[-1] in panel:
            panel[line[-1]].append((line[0], line[1]))
        else:
            panel[line[-1]] = [(line[0], line[1])]
    
    return panel

def buildFeedback(panel):
    stat = dict()
    for key in panel.keys():
        if key not in stat:
            stat[key] = 0
            stat[key+'_'] = 0
        for value in panel[key]:
            stat[key] += float(value[0])
            stat[key+'_'] += float(value[1])

    stat['total'] = 0
    for key in stat.keys():
        if '_' in key:
            stat['total'] += stat[key]

    stat['totalEth'], stat['totalMatic'], stat['totalBnb'], stat['totalFtm'], stat['totalXdai'], stat['totalAvax'] = float(0), float(0), float(0), float(0), float(0), float(0)
    for key in stat.keys():
        if '_' not in key:
            if key not in ['matic', 'bsc', 'ftm', 'xdai', 'avax', 'total', 'totalEth', 'totalMatic', 'totalBnb', 'totalFtm', 'totalXdai', 'totalAvax']:
                stat['totalEth'] += stat[key]
            elif key == 'matic':
                stat['totalMatic'] += stat[key]
            elif key == 'bsc':
                stat['totalBnb'] += stat[key]
            elif key == 'ftm':
                stat['totalFtm'] += stat[key]
            elif key == 'xdai':
                stat['totalXdai'] += stat[key]
            elif key == 'avax':
                stat['totalAvax'] += stat[key]

    return stat


# print(cleanup(rc.read_dataset('Scraped.csv')))