import string
import sys
import os
import platform

class CMDImageData :
    def __init__(self) -> None:
        pass

class CFolderImageData :
    def __init__(self) -> None:
        pass

class CMainDataManager :
    def __init__(self) -> None:
        self.szRootPath = ""
        self.MDImageDataRepo = []
        self.FolderImageDataRepo = []
        self.LogRepo = []
        pass

class CHelper :
    @staticmethod
    def AddLog(mgr : CMainDataManager, log : string):
        mgr.LogRepo.append(log)
        return
    
    @staticmethod
    def CreateMDImageDataRepo(mgr :CMainDataManager) -> int:
        lstLines = []
        try:
            stream = open(mgr.szRootPath, 'rt', encoding='UTF8')
            lstLines = stream.read()
            stream.close()
        except Exception as e:
            print(f"CreateMDImageDataRepo : Failed to open MD File : {mgr.szRootPath} = {e}")
            return -1


        for e in lstLines :
            szText = str(e)
            if szText.find("![]") < 0 :
                continue

            

        return 0
    

def main() :

    lstArgs = sys.argv

    if len(lstArgs) < 2 :
        szPlatform = platform.platform()
        if szPlatform.find("mac") >= 0 :
            lstArgs.append("/Users/hammerimpactmacpro/my_root/for_blog/blog_backup/posts/20221025/20221025015140/index.md")
        elif szPlatform.find("Windows") >= 0:
            lstArgs.append("/Users/hammerimpactmacpro/my_root/for_blog/blog_backup/posts/20221025/20221025015140/index.md")

    for i in range(1, len(lstArgs)) :
        print (f"sort_post_images arg {i} : {str(lstArgs[i])}")

    # 기능

    # ---(MD 파일 오픈)---
    # 1. MD 파일을 분석한다
    # ---(MD 파일 닫기)---

    # 2. MD 파일에서 이미지 줄을 찾고 이미지 정보 목록을 만든다 (+ 로그)
    # 3. MD 파일이 위치한 폴더 안에 있는 이미지 파일들(png, gif, jpg 등)의 목록을 만든다 (+ 로그)
    # 4. MD 파일에서 사용되지 않는 폴더 안 이미지 파일들을 삭제한다 (+ 로그)
    # 4-1. 삭제할 파일들은 모아서 임시 압축 파일로 압축해둔다. 

    # ---(MD 파일 오픈)---
    # 5. MD 파일에서 "사용한다"고 되어 있지만 실제 이미지 파일이 없는 경우, MD 파일에서 해당 줄을 공백 처리한다 (줄 자체에 변동이 있으면 안되니까)
    # 6. MD 파일에서 이미지 정보 목록을 순회하면서 인덱스 순으로 파일 이름을 변경하고, 원본 파일의 이름도 변경한다.
    # ---(MD 파일 닫기)---
    
    mgr = CMainDataManager()
    mgr.szRootPath = lstArgs[1]

    retVal = CHelper.CreateMDImageDataRepo(mgr)
    if retVal != 0 :
        return retVal



    return 0


main()