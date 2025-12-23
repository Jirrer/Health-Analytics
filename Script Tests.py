import src.PullData as PullData

def TEST_pullMedianIncome():
    return PullData.pullMedianIncome()

def TEST_pullHealthRank():
    return PullData.pullHealthRank()

Selected_Tests = [TEST_pullHealthRank]

if __name__ == "__main__":
    print("Running Python Tests")
    
    for test in Selected_Tests:
        print(f"\tStarting {test.__name__}")
        print(f"\t\tReturned - {test()}")
