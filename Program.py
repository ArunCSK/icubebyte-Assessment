from LoadAndFetchCustomer import *

def FetchCountryData():
    country = input("Enter Country code: ")
    filePath = IsValidCountryName(country)
    LoadCountryData(filePath)
    # print(country)

if __name__ == "__main__":
    Load()
    FetchCountryData()
    

