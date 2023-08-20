
def read_file(filename):
    with open(filename, 'r') as f:
        data = f.readlines()
    dataset = list()
    for line in data:
        line = line.strip('\n')
        dataset.append(line.split(','))
    
    return dataset

def read_dataset(filename):
    with open(filename, 'r') as f:
        data = f.readlines()
    dataset = list()
    for line in data:
        dataset.append(line.replace('\n', ''))
    # data = data.split('\n')
    print(dataset)
    return dataset

# a = read_dataset('Scraped.csv')
# for x in a:
#     print(x)