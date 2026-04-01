# Git Basics

This file is a simple reference for daily Git and GitHub use.

## 1. Git vs GitHub

- Git is the version control tool on your computer.
- GitHub is the website that stores your repository online.
- You can make commits locally with Git even before pushing to GitHub.

## 2. The 3 Main Ideas

- Working directory: your files as they are right now.
- Staging area: files selected for the next commit.
- Commit history: saved checkpoints of your work.

## 3. Most Important Commands

```powershell
git status
git add <file>
git commit -m "message"
git push
git pull
```

## 4. What Each Command Does

### `git status`

Shows:
- current branch
- changed files
- staged files
- whether you are ahead or behind remote

### `git add`

Selects files for the next commit.

Example:

```powershell
git add test2.html
```

### `git commit`

Creates a local checkpoint.

Example:

```powershell
git commit -m "Update test page"
```

### `git push`

Sends your local commits to GitHub.

### `git pull`

Brings the latest remote changes from GitHub to your machine.

## 5. Daily Workflow

```powershell
git pull
git status
git add .
git commit -m "Describe changes"
git push
```

Safer version when you only want one file:

```powershell
git add test2.html
git commit -m "Update test page"
git push
```

## 6. Branch Basics

A branch is a separate line of work inside the same repository.

- `main` is usually the stable branch.
- feature branches are for experiments, fixes, or new work.

Useful commands:

```powershell
git branch
git branch --show-current
git checkout -b new-branch-name
git checkout main
git push -u origin new-branch-name
```

## 7. Commands To Run When Confused

```powershell
git status
git branch --show-current
git remote -v
git config --get user.name
git config --get user.email
git log --oneline -5
```

These tell you:
- your repo state
- your current branch
- the connected GitHub repo
- the identity your commits use
- the last few commits

## 8. Common Terms

- `modified`: file changed but not committed
- `untracked`: new file Git has not started tracking yet
- `staged`: ready for next commit
- `ahead 1`: one local commit has not been pushed
- `working tree clean`: no pending changes

## 9. Good Habits

- Run `git status` often.
- Pull before starting work.
- Commit in small steps.
- Use clear commit messages.
- Check branch before pushing.
- Avoid force-push unless you understand why you need it.

## 10. Safe Recovery Habit

If Git feels confusing, stop and run:

```powershell
git status
git branch --show-current
git remote -v
git log --oneline -5
```

That usually explains almost everything.
