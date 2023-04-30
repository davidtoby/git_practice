#Hello Git and GitHub


git config --global user.name "xx xx"
git config --global user.name
git config --global user.email "xx@xx.com"
git config --global user.email
mkdir git_practice
ls
cd git_practice
git init
echo "Hello Git and GitHUb" >>README.txt
ls
git add README.txt
git commit -m "First commit"
git status
git remote add origin git@github.com:davidtoby/git_practice.git
git push -u origin main
git push --help



##A Git project can be thought of as having three parts:
  1. A Working Directory: where you’ll be doing all the work: creating, editing, deleting and organizing files
  2. A Staging Area: where you’ll list changes you make to the working directory
  3. A Repository: where Git permanently stores those changes as different versions of the project
The Git workflow consists of editing files in the working directory, adding files to the staging area, and saving changes to a Git repository. In Git, we save changes with a commit



git init
#Creates or initializes a new Git project, or repository. It creates a .git folder with all the tools and data necessary to maintain versions. This command only needs to be used once per project to complete the initial setup. 


git status
#Command is used within a Git repository to its current status including the current commit, any modified files, and any new files not being tracked by Git.


git add "filename-xx" 
#added file to the staging area.


git diff "filename-xx" 
#When we’re writing code, sometimes we want to compare two similar but different files. Diff tools, short for difference, allow programmers to look at the two files side by side and see exactly what differentiates them—where new lines of code have been added; if variable names have been changed; or if any lines of code have been removed.


git commit
#A commit is the last step in our Git workflow. A commit permanently stores changes from the staging area inside the repository.
#standard Conventions for Commit Messages 提交消息的标准约定：
#Must be in quotation marks 必须在引号内
#Written in the present tense 用现在时写的
#Should be brief (50 characters or less) when using -m 使用 -m 时应简短（50 个字符或更少）

git log
#refer back to an earlier version of a project. Commits are stored chronologically in the repository and can be viewed with git log.




###Generalizations
You have now been introduced to the fundamental Git workflow. You learned a lot! Let’s take a moment to generalize:
  - Git is the industry-standard version control system for web developers
  - Use Git commands to help keep track of changes made to a project:
    - git init creates a new Git repository
    - git status inspects the contents of the working directory and staging area
    - git add adds files from the working directory to the staging area
    - git diff shows the difference between the working directory and the staging area
    - git commit permanently stores file changes from the staging area in the repository
    - git log shows a list of all previous commits

Congratulations! You’ve learned three different ways to backtrack in Git. You can use these skills to undo changes made to your Git project.
Let’s take a moment to review the new commands:
  - git checkout HEAD filename: Discards changes in the working directory.
  - git reset HEAD filename: Unstages file changes in the staging area.
  - git reset commit_SHA: Resets to a previous commit in your commit history.
  

Let’s take a moment to review the main concepts and commands from the lesson before moving on.
  - Git branching allows users to experiment with different versions of a project by checking out separate branches to work on.
The following commands are useful in the Git branch workflow.
  - git branch: Lists all a Git project’s branches.
  - git branch branch_name: Creates a new branch.
  - git checkout branch_name: Used to switch from one branch to another.
  - git merge branch_name: Used to join file changes from one branch to another.
  - git branch -d branch_name: Deletes the branch specified.

Congratulations, you now know enough to start collaborating on Git projects! Let’s review.
  - A remote is a Git repository that lives outside your Git project folder. Remotes can live on the web, on a shared network or even in a separate folder on your local computer.
  - The Git Collaborative Workflow are steps that enable smooth project development when multiple collaborators are working on the same Git project.
We also learned the following commands
  - git clone: Creates a local copy of a remote.
  - git remote -v: Lists a Git project’s remotes.
  - git fetch: Fetches work from the remote into the local copy.
  - git merge origin/master: Merges origin/master into your local branch.
  - git push origin <branch_name>: Pushes a local branch to the origin remote.


###Reference
https://www.codecademy.com/practice/tracks/learn-git-introduction/modules/important-git-operations
https://www.codecademy.com/learn/learn-git/modules/learn-git-git-teamwork-u/cheatsheet
Learn Git: Introduction: Basic Git Workflow Cheatsheet | Codecademy
https://www.codecademy.com/article/what-is-diffing
