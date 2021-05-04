from LoadAndFetchCustomer import *

def FetchCountryData():
    country = input("Enter Country code: ")
    filePath = IsValidCountryName(country)
    if (filePath != ""):
        LoadCountryData(filePath)

if __name__ == "__main__":
    Load()
    FetchCountryData()
    

