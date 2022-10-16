from genericpath import isdir, isfile
from operator import attrgetter
import os
import shutil

class CPostInfo :
    def __init__(self) -> None:
        self.ID = 0
        self.Title = ""
        self.DicName = ""
        self.Path = ""
        self.YearMonth = 0
        self.MonthDay = 0
        pass

    def IsValid(self) : 
        return self.ID != 0
    

def CreatePostInfo(szRoot, szDicName) :
    szPath = f"{szRoot}/{szDicName}"
    if os.path.isdir(szPath) == False :
        return

    szMDFilePath = f"{szPath}/index.md"
    if os.path.isfile(szMDFilePath) == False :
        return

    retVal = CPostInfo()
    retVal.DicName = szDicName
    retVal.Path = szMDFilePath

    # Extract id, yearmonth from DicName
    try:
        retVal.ID = int(szDicName)
        # Extract YearMonth
        retVal.YearMonth = int(retVal.ID / 100000000) 
        # Extract YearMonthDay - Year
        retVal.MonthDay = int((retVal.ID - int(retVal.ID / 10000000000) * 10000000000) / 1000000)
    except ValueError:
        print(f"CreatePostInfo : DicName is not int : {szDicName}")
        return
    
    # Extract title from MD File
    try:
        stream = open(szMDFilePath, 'rt', encoding='UTF8')
        retVal.Title = stream.readline()
        retVal.Title = retVal.Title.replace('\n', '').replace('\r','')
    except Exception as e:
        print(f"CreatePostInfo : Failed to open MD File : {szMDFilePath} = {e}")
        return

    return retVal

def main() :
    # file name
    szFileName = "README.md"
    szFileBackupName = "_backup_README.md"

    # print directories 
    lstPostInfo = []
    szPostRootName = "posts"
    lstParentDicName = os.listdir(szPostRootName)
    for e1 in lstParentDicName :
        szPath1 = f"{szPostRootName}/{e1}"
        if os.path.isdir(szPath1) == False :
            continue

        lstDicName = os.listdir(szPath1)
        for e2 in lstDicName:
            retVal = CreatePostInfo(szPath1, e2)
            if retVal != None and retVal.IsValid() :
                lstPostInfo.append(retVal)
        

    # sort by ID
    lstPostInfo = sorted(lstPostInfo, key= lambda e: e.ID, reverse=True)

    # back up file
    if os.path.exists(szFileBackupName) :
        os.remove(szFileBackupName)
    shutil.copy(szFileName, szFileBackupName)

    # create README.MD
    if os.path.exists(szFileName) :
        os.remove(szFileName)
    
    try :
        stream = open(szFileName, 'wt', encoding='UTF8')
        
        stream.write("HammerImpact Blog Markdown Documents backup\n\n")
        nYearMonth = 0
        nMonthDay = 0
        for e1 in lstPostInfo :
            if nYearMonth != e1.YearMonth :
                nYearMonth = e1.YearMonth
                stream.write(f"# {e1.YearMonth}\n\n")
            
            if nMonthDay != e1.MonthDay :
                nMonthDay = e1.MonthDay
                stream.write(f"## {e1.MonthDay}\n\n")

            stream.write(f"[{e1.Title}]({e1.Path})\n\n")
    except :
        # backup
        if os.path.exists(szFileName) :
            os.remove(szFileName)
        shutil.copy(szFileBackupName, szFileName)

    # (on complete)
    # remove backup file
    if os.path.exists(szFileBackupName) :
        os.remove(szFileBackupName)

    print("complete")
    return


# call main
main()
