import pandas as pd
import os

#Change this path as per your local directory
#Example  '{Directory}:\\FolderName\\FolderName\\{ProjectDirectory = incubyte}\\FolderName\\'
ExcelPath = 'D:\Arundev\icubebyte-Assessment\CustomerCountryWise'

def Load():
    #Read CSV File
    dataset = pd.read_csv('CustomerData.csv'
                            ,header=0
                            ,delimiter='|')

    #Filter CSV data to DataFrame with requiered Columns
    df = pd.DataFrame(dataset.iloc[: , 2:12])

    unique_Conturies = df['Country'].unique() 
    
    Countries_FileName = ""

    #Check and Create Directory to save data Courties wise
    if not os.path.exists(ExcelPath):
        os.makedirs(ExcelPath)

    #Iterate Unique country values and write into files
    for countries in unique_Conturies:
        Countries_FileName = countries+ ".csv"
        FilePath = ExcelPath +"\\"+ Countries_FileName

        #filter data Country wise
        fileData = df[df['Country'] == countries]

        if os.path.isfile(FilePath):
            #DataFrame to CSV
            WriteCSVFile(fileData, FilePath)
            #print(fileData)
        else:
            #Create csv file and write 
            open(FilePath, "w")
            WriteCSVFile(fileData, FilePath)

        Countries_FileName = ""
        FilePath = ""
        #print(df.Country.unique)

def WriteCSVFile(fileData,FilePath):
    fileData.to_csv (FilePath, index = False, header=True)

def IsValidCountryName(Name):
    #print(Name)
    filePath = ExcelPath +"\\"+ Name +".csv"
    if os.path.exists(filePath):
        print("Country Code " + Name + " exits. Fetching Data...")
        return filePath
    else:
        print("Country Code " + Name + " does not exists.")
        return ""

def LoadCountryData(ExcelFilePath):
    dataset = pd.read_csv(ExcelFilePath
                            ,header=0
                            ,delimiter=',')
    
    data = pd.DataFrame(dataset.iloc[: , 0:10])
    data['Open_Date'] = pd.to_datetime(data['Open_Date'], format='%Y%m%d')
    data['Last_Consulted_Date'] = pd.to_datetime(data['Last_Consulted_Date'], format='%Y%m%d')
    data['DOB'] = pd.to_datetime(data['DOB'], format='%m%d%Y')

    print(data)
