import readCsv as rc
import scrapTxs as st

def askInt(toAsk, incorrectMessage="Error: Invalid entry", possibleAnswear=False):
    while True:
        try:
            userInput = int(input(toAsk))
        except:
            print("Error, please retry.\n")
        else:
            if not possibleAnswear:
                return userInput
            elif userInput in possibleAnswear:
                return userInput
        print(incorrectMessage)

def askStr(toAsk, incorrectMessage="Error: Invalid entry.\n", possibleAnswear=False):
    while True:
        try:
            userInput = str(input(toAsk))
        except:
            print("Error, please retry.\n")
        else:
            if not possibleAnswear:
                return userInput
            elif userInput in possibleAnswear:
                return userInput
        print(incorrectMessage)




if __name__ == "__main__":
    dataset = rc.read_file('0x05525cde529c5212f1eab7f033146c8cc103cd5d_history.csv')
    input = askStr("Scalp every transaction ? ({} Txs) [Y/N] ?\n>>> ".format(len(dataset)), possibleAnswear=['Y','N'])

    if input == "Y":
        urlList = []

        for tx in [(x[2], x[4]) for x in dataset]:
            if tx == ('', ''):
                pass
            else: urlList.append(tx)
        # print(urlList[0], len(urlList))
        # test=[]
        # for x in urlList:
        #     if x[0] not in test:
        #         test.append(x[0])
        # print(test, test[:], test[1:], len(test))
        st.scrapData(urlList[1:])
    else: 
        pass
        
    
