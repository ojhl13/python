from git import Repo
import os, sys

in_path=os.path.dirname(os.path.abspath(__file__))
print(": sys.argv[0]=", sys.argv[0])
print(in_path)
# rorepo is a Repo instance pointing to the git-python repository.
# For all you know, the first argument to Repo is a path to the repository
# you want to work with.
repo = Repo(in_path)
assert not repo.bare
#result=get_status(repo,in_path)
diff_list = repo.head.commit.diff()

for diff in diff_list:
    print(diff.change_type) # Gives the change type. eg. 'A': added, 'M': modified etc.

    # Returns true if it is a new file
    print(diff.new_file) 
    
    # Print the old file path
    print(diff.a_path)

    # Print the new file path. If the filename (or path) was changed it will differ
    print(diff.b_path) 
