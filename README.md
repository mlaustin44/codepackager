# CodePackager

**CodePackager** is a CLI tool that compiles all source code files in a project into a single, cleanly formatted `.txt` file for use with large language models (LLMs). It was created to work around limits many tools (claude.ai, ChatGPT, Google AI Studio, etc) have on the number and type of files you're allowed to upload.  This approach also helps keep the LLM's understanding of the current project state syncronized with the actual state for people who don't like IDE integrated AI tools (like me).

---

## 🔧 Features

* ✅ **Supports Python, C++, and Go** (.py, .cpp, .h, .hpp, .go) - to add additional languages, just edit main.py to add your extensions
* ✅ **Recursively collects** all matching files in the current Git repo or folder
* ✅ **Formatted output** includes:

  * A directory listing of source files
  * Delimited sections per file with relative paths
* ✅ **Exclusion support** to skip specific files or folders
* ✅ **Cross-platform**: tested on Linux and macOS
* ✅ **Output placed on Desktop** automatically

---

## 📦 Installation

```bash
git clone https://github.com/YOURNAME/codepackager.git
cd codepackager
./install.sh
```

This will install `codepackager` to your user Python path and automatically add it to your shell's `$PATH` (`.bashrc` and `.zshrc`). You may need to restart your terminal afterward.

---

## 🚀 Usage

### Standard (Git repo root)

```bash
cd ~/projects/myrepo
codepackager
```

Produces: `~/Desktop/myrepo.llm.txt`

### Only current folder (monorepo support)

```bash
codepackager --local
```

Only includes files from the current folder down.

### Exclude paths

```bash
codepackager --exclude venv/ docs/ src/legacy/ build/temp.cpp
```

You can exclude both files and directories.

---

## 💡 Why CodePackager?

Modern LLMs perform best when provided with focused, structured input. Rather than dumping raw repositories into prompts, `CodePackager`:

* Filters only relevant source files
* Clearly separates each file for analysis or summarization
* Makes reviewing full projects via LLMs (e.g., GPT-4, Claude, etc.) practical

Whether you’re working on autonomous code agents, prompt-tuned evaluations, or refactoring at scale—`CodePackager` provides a reliable, scriptable input format.

---

## 🛠 Development

This tool is implemented in Python using only the standard library.

```bash
python -m codepackager.main [args]
```

---

## 📄 License

MIT License

---

## 📬 Feedback

Please open an issue or PR with suggestions, bugs, or feature requests.
