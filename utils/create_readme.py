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
    if os.path.isdir(szRoot + szDicName) == False :
        return

    szMDFilePath = szRoot + szDicName + "/index.md"
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
        stream = open(szMDFilePath, 'r')
        retVal.Title = stream.readline()
        retVal.Title = retVal.Title.replace('\n', '').replace('\r','')
    except:
        print(f"CreatePostInfo : Failed to open MD File : {szMDFilePath}")
        return

    return retVal

def main() :
    # file name
    szFileName = "README.md"
    szFileBackupName = "_backup_README.md"

    # print directories 
    lstPostInfo = []
    szPostRootName = "posts/"
    lstDicName = os.listdir(szPostRootName)
    for e in lstDicName :
        if os.path.isdir(szPostRootName + e) == False :
            continue
        
        retVal = CreatePostInfo(szPostRootName, e)
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
        stream = open(szFileName, 'w')
        
        stream.write("HammerImpact Blog Markdown Documents backup\n\n")
        nYearMonth = 0
        nMonthDay = 0
        for e in lstPostInfo :
            if nYearMonth != e.YearMonth :
                nYearMonth = e.YearMonth
                stream.write(f"# {e.YearMonth}\n\n")
            
            if nMonthDay != e.MonthDay :
                nMonthDay = e.MonthDay
                stream.write(f"## {e.MonthDay}\n\n")

            stream.write(f"[{e.Title}]({e.Path})\n\n")
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
