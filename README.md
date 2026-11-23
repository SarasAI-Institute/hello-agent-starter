# hello-agent: Module 1 setup practice

Starter for **10x Coding with AI - Module 1, Section 3** at Saras AI Institute.

This is the original greeting application and its two baseline tests. The duration-formatting task is intentionally absent: you add it during the lesson. Use two independent starter copies to compare Codex and Claude Code fairly.

## Download and start

1. [Download the starter ZIP](https://github.com/SarasAI-Institute/hello-agent-starter/archive/refs/heads/main.zip), or choose **Code > Download ZIP** on this repository.
2. Extract it twice into separate folders, for example `hello-agent-codex` and `hello-agent-claude`. Do not begin the second exercise from the first tool's modified files.
3. Open a terminal in the extracted project folder (the one containing `app.py`). Use Python 3.10 or later; the recording uses Python 3.12. No third-party Python packages are required.
4. Run the app and baseline tests:

```sh
python3 app.py Luka
python3 -m unittest discover -s tests -v
```

Expect `Hello, Luka!` and **two passing tests**. On Windows, use your installed Python launcher, such as `py -3.12`, instead of `python3` if needed.

5. Create a starter checkpoint in each extracted folder:

```sh
git init
git add .gitignore README.md app.py tests docs .gitattributes
git commit -m "add hello-agent starter"
```

Git may ask you to configure your author name and email before your first commit. A local commit does not publish your work. This exercise does not require you to push to GitHub.

## Course task

Follow Section 3 Course Notes for the exact duration-formatting contract. Ask your chosen agent to add `format_duration(seconds)` and meaningful tests, preserve the greeting, review the changes, run the tests yourself, and commit the working result. Begin the second tool's exercise from the original download.

Do not copy a completed implementation into the second starter. The purpose is to practice a small, verifiable change independently with each tool.

## Resources

- [Section 3 resources PDF](docs/M1_S3_Resources.pdf)
- [Git readiness refresher](docs/Git_Readiness_Selection.md)

Tool installation and account access are separate from running this Python starter. Keep credentials out of this repository.
