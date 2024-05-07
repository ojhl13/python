from git import Repo
import os

in_path=os.path.dirname(os.path.abspath(__file__))#this could be ask to the user or use the route where the file is run

def getModifiedfiles(Rep):
   return Rep.head.commit.diff()

def main():
    #result=get_status(repo,in_path)
    repo = Repo(in_path)
    assert not repo.bare
    diff_list = getModifiedfiles(repo)
    
    for diff in diff_list:
        if("M"==(diff.change_type)):
            print(diff.b_path) 
            #call function to add log
            #Addinglog(filename,text2add)

if __name__ == "__main__":
    main()