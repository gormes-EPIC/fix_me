# Welcome to GitHub

## Part 1: Login to GitHub

- Open VS Code (not through CS50)
- Create a new directory for your Python files 
- Create a Hello World Python program in the directory
- Then, login to Git from the terminal with the two commands `git config --global user.name "your_username"` and `git config --global user.email "your_email_address@example.com"`
- Install the GItHub command line client for Ubuntu. [Copy/Paste from Here](https://github.com/cli/cli/blob/trunk/docs/install_linux.md)
- Login with `gh auth login` [Link](https://docs.github.com/en/enterprise-cloud@latest/github-cli/github-cli/quickstart)

Hopefully this will be enough to get you logged in. If you are still having issues, you may have to use SSH keys to authorize VS Code
- https://stackoverflow.com/questions/34731832/log-in-to-github-from-the-command-line-with-multiple-accounts
- https://docs.github.com/en/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account

You can also install the [GitHub Pull Requests and Issues Extension](https://marketplace.visualstudio.com/items?itemName=GitHub.vscode-pull-request-github) in VS Code. Here is the [start guide](https://code.visualstudio.com/docs/sourcecontrol/github). 

## Part 2: Hello World Repository

- Navigate to your Hello World file in your Terminal. 
- Initialize the repository on the main branch: `git init -b main`
- Add your files with `git add .`
- Then commit your changes with `git commit -m "First Commit"`
[Tutorial](https://docs.github.com/en/enterprise-cloud@latest/migrations/importing-source-code/using-the-command-line-to-import-source-code/adding-locally-hosted-code-to-github#initializing-a-git-repository)
- Then push to GitHub. You can either use `gh repo create` and follow the prompts or create a new repo on Github.com and use `git remote add origin REMOTE-URL`(with the URL of your repository) `git remote -v` and `git push origin main`.
[Tutorial](https://docs.github.com/en/enterprise-cloud@latest/migrations/importing-source-code/using-the-command-line-to-import-source-code/adding-locally-hosted-code-to-github#adding-a-local-repository-to-github-with-github-cli)

## Part 3: Add a New Repository
- Copy 3 of your most elegant/favorite CS50 solutions to new files in a new directory within the Python files directory you created in part 1
- Upload all three to a new GitHub repository 
- Share the link to your repository with me in Google Classroom

## Part 4: Fix Tic Tac Toe
- Pull my [tic tac toe program from GitHub](https://github.com/gormes-EPIC/fix_me.git)
- Fix the issues in the code
- Create a new branch with your name and push your complete code back to my repository. When you get to this step, let me know so I can add you as a collaborator on the project.

- Create a new branch with your name and push your complete code back to my repository. When you are ready for this step, let me know so I can add you as a collaborator on the project.


## Part 5: Update your GitHub Profile
- Add a professional photo, change your name, add your LinkedIn URL etc. to your GitHub profile. Assume that this profile will be listed on your resume in the future so make sure it is professional!

## Part 6: Login on your Pi
- Get logged in to Git and GItHub on your pi. (This will look different depending on how you typically code on your pi)
- Pull you three CS50 files to your pi
- Push one of your existing Python programs on your Pi to a new repository. 
- Share the link of the new repository with me

**Rubric**  
4 points - All requested items are present. HelloWorld and CS50 repositories are present and the links have been shared in classroom.  Tic Tac Toe program has been fixed and pushed to a new branch within my repository. GitHub profile is updated and professional. You can access GitHub files from your pi and can push a file to a new repository. 
3 points - Some of the required items are missing.
3 points - Did not attempt or the student should re-attempt.
