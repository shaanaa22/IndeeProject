import csv
@staticmethod
def countCSV():
    with open('../Resources/data.csv') as csvFile:
        reader = csv.DictReader(csvFile)
        data = list(reader)
        row_count = len(data)
        print row_count
    return row_count
@staticmethod
def readCSV():
    with open('../Resources/data.csv') as csvfile:
        reader = csv.DictReader(csvfile)
        Emails = []
        Passwords = []
        ConfirmPass = []
        FNames = []
        LNames = []
        CNames = []
        for row in reader:
            #print(row['email'], row['password'])
            Emails.append(row['email'])
            Passwords.append(row['password'])
            ConfirmPass.append(row['password'])
            FNames.append(row['name'])
            LNames.append(row['surname'])
            CNames.append(row['company'])
        print(Emails)
        print(Passwords)
        print(FNames)
        print(LNames)
        print(CNames)
    return Emails,Passwords,FNames,LNames,CNames

Emails,Passwords,Fnames,Snames,Cnames=readCSV()
Rowcount=countCSV()
