
def read_file(filename):
    with open(filename, 'r') as f:
        data = f.readlines()
    dataset = list()
    for line in data:
        line = line.strip('\n')
        dataset.append(line.split(','))
    
    return dataset

a = read_file('0x05525cde529c5212f1eab7f033146c8cc103cd5d_history.csv')
for x in a:
    print(x[4])