# Derivation of Israel-Stewart Bulk Viscosity from a Non-Minimally Coupled Scalar Field

This repository contains the LaTeX source code and symbolic verification scripts for the paper:

**"Derivation of Israel-Stewart Bulk Viscosity from a Non-Minimally Coupled Scalar Field"**
by F. A. López

## Contents

- `paper.tex`: Main LaTeX file (uses revtex4-2).
- `sympy_verification.py`: Python script using SymPy to verify the algebraic derivation of the transport coefficients τ and ζ.
- `requirements.txt`: List of Python dependencies.
- `Makefile`: Automates PDF compilation.
- `LICENSE`: MIT License.
- `.gitignore`: Files to ignore in version control.

## Requirements

- **LaTeX distribution**: TeX Live 2020 or later (with revtex4-2, amsmath, etc.).
- **Python 3.8+** with:
  - sympy
  - numpy (optional, for numerical checks)
  - matplotlib (optional, for plots)

Install Python dependencies with:
```bash
pip install -r requirements.txt
```

## Compiling the PDF

Run `make` to compile `paper.tex` into `paper.pdf`. Alternatively, use:
```bash
pdflatex paper
bibtex paper
pdflatex paper
pdflatex paper
```

## Reproducing the symbolic verification

Execute the SymPy script:
```bash
python sympy_verification.py
```
It will print the final expressions for τ and ζ and can be extended to perform numerical checks.

## License

This work is licensed under the MIT License. See `LICENSE` for details.

## Contact

For questions or comments, please contact the author at neoatomismo@gmail.com.
