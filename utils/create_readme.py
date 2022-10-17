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
        self.Tags = [] # list<string>
        pass

    def IsValid(self) : 
        return self.ID != 0

class CHelper :
    @staticmethod
    def CreatePostInfo(szRoot, szDicName) -> CPostInfo :
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
        
        # Extract data from MD File
        try:
            stream = open(szMDFilePath, 'rt', encoding='UTF8')

            # Extract title (1st line)
            retVal.Title = stream.readline()
            retVal.Title = retVal.Title.replace('\n', '').replace('\r','')

            # Extract tags (3rd line)
            stream.readline() # 2nd line pass
            szTags = stream.readline() # 3rd line = tag strings
            szTags = szTags.replace('\r', '').replace('\n', '') # remove invalid chars for tag
            retVal.Tags = szTags.split('/')

        except Exception as e:
            print(f"CreatePostInfo : Failed to open MD File : {szMDFilePath} = {e}")
            return

        return retVal


    @staticmethod
    def CreatePostInfoList() -> list:
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
                retVal = CHelper.CreatePostInfo(szPath1, e2)
                if retVal != None and retVal.IsValid() :
                    lstPostInfo.append(retVal)

        # sort by ID
        lstPostInfo = sorted(lstPostInfo, key= lambda e: e.ID, reverse=True)
        return lstPostInfo


    @staticmethod
    def CreateREADME(lstPostInfo:list) -> None :
        # file name
        szFileName = "README.md"
        szFileBackupName = "_backup_README.md"

        # back up file
        if os.path.exists(szFileBackupName) :
            os.remove(szFileBackupName)

        if os.path.exists(szFileName) :
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

            if os.path.exists(szFileBackupName) :
                shutil.copy(szFileBackupName, szFileName)

        # (on complete)
        # remove backup file
        if os.path.exists(szFileBackupName) :
            os.remove(szFileBackupName)

        return

def main() :
    lstPostInfo = CHelper.CreatePostInfoList()
    CHelper.CreateREADME(lstPostInfo)
    print("complete")
    return


# call main
main()
