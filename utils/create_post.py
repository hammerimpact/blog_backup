from datetime import date, datetime
import os

def main() :
    # post root directory
    szRootPath = "posts"

    # "YYYY/MM/DD/HH/MM/SS" => "YYYYMMDDHHMMSS"
    nowtime = datetime.utcnow()
    szParentName = nowtime.strftime("%Y%m%d")
    szDirectoryName = nowtime.strftime("%Y%m%d%H%M%S")

    # file name
    file_name = "index.md"

    # create parent directory
    szRootParentPath = f"{szRootPath}/{szParentName}"
    if os.path.isdir(szRootParentPath) == False :
        os.mkdir(f"{szRootPath}/{szParentName}")

    # create directory
    os.mkdir(f"{szRootPath}/{szParentName}/{szDirectoryName}")

    # create md file
    f = open(f"{szRootPath}/{szParentName}/{szDirectoryName}/{file_name}", "wt", encoding='UTF8')
    f.write("(no_title)\n\n")
    f.write("(no_tag)\n\n")

    return

# call main
main()