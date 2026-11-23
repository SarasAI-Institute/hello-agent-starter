# Git readiness: selected refresher topics

Optional support for Module 1. Estimated reading time: 8-10 minutes, excluding practice. This selection adapts chapters 1-2 of the course GitHub Developer Refresher Guide. It focuses on the local state you need to understand before reviewing agent edits. Section 3 Resources links to Pro Git for a fuller explanation.

## Git and GitHub

Git records versions in a repository on your computer. GitHub hosts repositories and collaboration features. A local commit does not publish your work to GitHub.

The course starters are archives, so extract each one before opening it. Work in the intended project directory. If the extracted starter is not already a repository, initialize Git there using `git init`, following its README. Run `git status` to confirm which files Git sees.

## Three states to distinguish

- **Working tree:** the files you are editing now.
- **Staging area:** the content selected for the next commit.
- **Commit:** a saved repository snapshot with a message and identifier.

A new file is untracked until it is added. An existing file can have both staged and unstaged changes if it is edited after staging. Staging captures the content at that moment; it is not a promise to include all future edits to that file.

## Inspect before staging

Run these commands inside your practice repository:

```sh
git status
git diff
```

`git status` lists the state of files. `git diff` shows changes to tracked files that have not yet been staged. It does not show the contents of untracked files: open and read those separately.

Before a checkpoint, run the project's tests and inspect the code. Read the test assertions as well as the result. Do not treat the agent's success summary as a substitute for this evidence.

## Stage specific files, then inspect again

For example, if you intentionally changed `app.py` and its existing test file, stage those paths. Replace the example names with the actual paths you reviewed.

```sh
git add app.py tests/test_app.py
git diff --staged
git status
```

`git diff --staged` shows what the next commit would change relative to the previous commit. Check that unrelated files are absent. If you edit a staged file again, run both diff commands and decide which version belongs in the checkpoint. Stage the later edit only after reviewing it.

If you staged a file by mistake in a repository with an existing commit, `git restore --staged path/to/file` removes it from the staging area while keeping the working file. Read command help if the repository has no first commit yet. You do not need history rewriting for this module.

## Commit and recognize the checkpoint

```sh
git commit -m "Describe the small verified change"
git status
git log --oneline -5
```

Choose a message that describes the actual change. A commit can contain buggy code, so its existence is not proof of correctness. The useful checkpoint is the combination of reviewed changes, relevant checks, and a recorded commit.

## Readiness check

Explain why an empty `git diff` does not necessarily mean there is nothing to commit. Identify the command that displays staged changes and the way you would inspect a new file. Keep independent starter copies for the two tools; the course does not require publishing them remotely.
