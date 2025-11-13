# Horizontal Time Safety Margin (HTSM)

[![CC BY-NC 4.0][cc-by-nc-shield]][cc-by-nc]

Horizontal Time Safety Margin is a method of estimating available margin during ground test

## Manuscript

Available as [cook_horizontal_time_safety_margin_2025.pdf](quarto/_pdf/cook_horizontal_time_safety_margin_2025.pdf)

## Technologies 

### git

[git](https://git-scm.com/) is a free and open source distributed version control system designed to handle everything from small to very large projects with speed and efficiency.

The files in this repository are version controlled using git.

### GitHub

[GitHub](https://github.com/) is a proprietary developer platform that allows developers to create, store, manage, and share their code. It is commonly used to host open source software development projects. It uses git to provide distributed version control and GitHub itself provides access control, bug tracking, software feature requests, task management, continuous integration, and wikis for every project. GitHub has been a subsidiary of Microsoft since 2018.

The files in this repository are hosted and available on GitHub at <https://github.com/cooknl/htsm>. GitHub also hosts the website for the web pages rendered from this repository. 

You can make a copy of this repository using the tools provided by GitHub.

### Quarto

[Quarto](https://quarto.org) is an open-source scientific and technical publishing system.

The manuscript for the paper describing HTSM is rendered from the[quarto.qmd](quarto/htsm.qmd) Quarto markdown file.

If you have made a copy of this repository, you can [render the manuscript](https://quarto.org/docs/projects/quarto-projects.html#rendering-projects) by opening a terminal (Windows: PowerShell, MacOS or Linux: terminal), navigating to the `/quarto` directory and typing 

```shell
# For HTML in a docs directory for GitHub pages
quarto render --to html --output-dir ../docs --o index.html

# For PDF
quarto render --to pdf --output-dir ./_pdf
```


### uv

[uv](https://docs.astral.sh/uv/) is an extremely fast Python package and project manager, written in Rust.

The python environment used to run the notebook is managed using uv.

### marimo

[marimo](https://marimo.io/) is a reinvention of the Python notebook as a reproducible, interactive, and shareable Python program that can be executed as scripts or deployed as interactive web apps.

The notebook for exploration of HTSM is a marimo notebook.

---

This work is licensed under a
[Creative Commons Attribution-NonCommercial 4.0 International License][cc-by-nc].

[![CC BY-NC 4.0][cc-by-nc-image]][cc-by-nc]

[cc-by-nc]: https://creativecommons.org/licenses/by-nc/4.0/
[cc-by-nc-image]: https://licensebuttons.net/l/by-nc/4.0/88x31.png
[cc-by-nc-shield]: https://img.shields.io/badge/License-CC%20BY--NC%204.0-lightgrey.svg
