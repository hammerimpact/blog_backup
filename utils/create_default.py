import os

def main() :
    szFolderPosts = "posts"
    if os.path.exists(szFolderPosts) == False :
        os.mkdir(szFolderPosts)

    szFoldeREADME = "read_me"
    if os.path.exists(szFoldeREADME) == False :
        os.mkdir(szFoldeREADME)
    
    return

main()