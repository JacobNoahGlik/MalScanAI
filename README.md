# MalScanAI 🧠🐍

*AI-assisted Malware Classification for Ghidra*

MalScanAI is a Python-powered plugin for [Ghidra](https://ghidra-sre.org/) that integrates with Ghidra's decompiler output to predict the type of malware being analyzed. It leverages static features and AI/ML models to identify suspicious patterns and behaviors, providing contextual annotations directly inside Ghidra.

## 🚀 Features

- 📜 Reads decompiled code or function metadata from Ghidra
- 🧠 Uses an ML model to predict likely malware family/type (e.g., ransomware, keylogger, RAT)
- 🔍 Extracts static features like:
  - API calls
  - String references
  - Opcode patterns
  - Control-flow structure
- 🧩 Plugin-compatible with GhidraBridge
- 🗂 Can tag or comment on functions in Ghidra based on predictions

## 🛠 Requirements

- Python 3.8+
- Ghidra + [GhidraBridge](https://github.com/JustMaku/GhidraBridge)
- ML libraries: `scikit-learn`, `joblib`, (or PyTorch if using deep models)

## 💡 Getting Started

1. Install GhidraBridge and connect Python to Ghidra.
2. Clone this repo:
   ```bash
   git clone https://github.com/JacobNoahGlik/MalScanAI.git
   cd MalScanAI
   ```
