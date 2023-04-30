Hello Git and GitHub


  597  git config --global user.name "xx xx"
  598  git config --global user.name
  599  git config --global user.email "xx@xx.com"
  600  git config --global user.email
  601  mkdir git_practice
  602  ls
  603  cd git_practice
  604  git init
  605  echo "Hello Git and GitHUb" >>README.txt
  606  ls
  607  git add README.txt
  608  git commit -m "First commit"
  609  git status
  610  git remote add origin git@github.com:davidtoby/git_practice.git
  611  git push -u origin main
  612  git push --help
