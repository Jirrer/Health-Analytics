import src.PullData as PullData

with open('.txt\\ScriptTests.txt', 'r') as file:
    Selected_Tests = [f for f in file]

def TEST_pullMedianIncome():
    return PullData.pullMedianIncome()

def TEST_pullHealthRank():
    return PullData.pullHealthRank()


if __name__ == "__main__":
    print("Running Python Tests")
    
    for functionName in Selected_Tests:
        print(f"\tStarting {functionName}")
        print(f"\t\tReturned - {globals()[functionName]()}")
