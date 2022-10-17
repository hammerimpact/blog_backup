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
        self.Tags = {} # map<string>
        pass

    def IsValid(self) : 
        return self.ID != 0


class CPostAnalyzeContainer :
    def __init__(self) -> None:
        self.szFolderPosts = "posts"
        self.szFileDateMD = "links_date.md"
        self.szFileTagMD = "links_tag.md"
        self.szREADME = "README.md"

        self.repo               = [] # list<CPostInfo>
        self.repoYearMonth      = {} # map<string, string>
        self.repoTags           = {} # map<string, string>
        pass


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
            lstTags = szTags.split('/')
            for tag in lstTags :
                if tag not in retVal.Tags :
                    retVal.Tags[tag] = tag

        except Exception as e:
            print(f"CreatePostInfo : Failed to open MD File : {szMDFilePath} = {e}")
            return

        return retVal


    @staticmethod
    def CreatePostAnalyzeContainer() -> CPostAnalyzeContainer:
        retVal = CPostAnalyzeContainer()

        # set : repo
        lstParentDicName = os.listdir(retVal.szFolderPosts)
        for e1 in lstParentDicName :
            szPath1 = f"{retVal.szFolderPosts}/{e1}"
            if os.path.isdir(szPath1) == False :
                continue

            lstDicName = os.listdir(szPath1)
            for e2 in lstDicName:
                pInfo = CHelper.CreatePostInfo(szPath1, e2)
                if pInfo != None and pInfo.IsValid() :
                    retVal.repo.append(pInfo)

        # set : repoDate
        for e in retVal.repo :
            if e.YearMonth not in retVal.repoYearMonth :
                retVal.repoYearMonth[e.YearMonth] = e.YearMonth

        # set : repoTags
        for e in retVal.repo :
            for tag in e.Tags.keys() :
                if tag not in retVal.repoTags :
                    retVal.repoTags[tag] = tag

        # sort by ID
        retVal.repo = sorted(retVal.repo, key= lambda e: e.ID, reverse=True)
        return retVal

    @staticmethod
    def CreateLinksTagsMD(container:CPostAnalyzeContainer) -> None :
        # file name
        szFileName = container.szFileTagMD
        szFilePath = f"{szFileName}"
        szFileBackupPath = f"_backup_{szFileName}"

        # back up file
        if os.path.exists(szFileBackupPath) :
            os.remove(szFileBackupPath)

        if os.path.exists(szFilePath) :
            shutil.copy(szFilePath, szFileBackupPath)

        # create README.MD
        if os.path.exists(szFilePath) :
            os.remove(szFilePath)
        
        try :
            stream = open(szFilePath, 'wt', encoding='UTF8')
            
            stream.write("List by tags\n\n")

            for tag in container.repoTags :
                stream.write(f"# {tag}\n\n")
                for e in container.repo :
                    if tag in e.Tags :
                        stream.write(f"[{e.Title}]({e.Path})\n\n")

        except :
            # backup
            if os.path.exists(szFilePath) :
                os.remove(szFilePath)

            if os.path.exists(szFileBackupPath) :
                shutil.copy(szFileBackupPath, szFilePath)

        # (on complete)
        # remove backup file
        if os.path.exists(szFileBackupPath) :
            os.remove(szFileBackupPath)

        return

    @staticmethod
    def CreateLinksDateMD(container:CPostAnalyzeContainer) -> None :
        # file name
        szFileName = container.szFileDateMD
        szFilePath = f"{szFileName}"
        szFileBackupPath = f"_backup_{szFileName}"

        # back up file
        if os.path.exists(szFileBackupPath) :
            os.remove(szFileBackupPath)

        if os.path.exists(szFilePath) :
            shutil.copy(szFilePath, szFileBackupPath)

        # create README.MD
        if os.path.exists(szFilePath) :
            os.remove(szFilePath)
        
        try :
            stream = open(szFilePath, 'wt', encoding='UTF8')
            
            stream.write("Sorted by date\n\n")

            nYearMonth = 0
            nMonthDay = 0
            for e1 in container.repo :
                if nYearMonth != e1.YearMonth :
                    nYearMonth = e1.YearMonth
                    stream.write(f"# {e1.YearMonth}\n\n")
                
                if nMonthDay != e1.MonthDay :
                    nMonthDay = e1.MonthDay
                    stream.write(f"## {e1.MonthDay}\n\n")

                stream.write(f"[{e1.Title}]({e1.Path})\n\n")
        except :
            # backup
            if os.path.exists(szFilePath) :
                os.remove(szFilePath)

            if os.path.exists(szFileBackupPath) :
                shutil.copy(szFileBackupPath, szFilePath)

        # (on complete)
        # remove backup file
        if os.path.exists(szFileBackupPath) :
            os.remove(szFileBackupPath)

        return

    @staticmethod
    def CreateREADME(container:CPostAnalyzeContainer) -> None :
        # file name
        szFileName = container.szREADME
        szFileBackupName = f"_backup_{szFileName}"

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
            for e1 in container.repo :
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
    pAnalyzeContainer = CHelper.CreatePostAnalyzeContainer()
    CHelper.CreateLinksTagsMD(pAnalyzeContainer)
    CHelper.CreateLinksDateMD(pAnalyzeContainer)
    CHelper.CreateREADME(pAnalyzeContainer)
    print("complete")
    return


# call main
main()
