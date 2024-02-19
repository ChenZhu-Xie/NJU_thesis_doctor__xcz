<!-- ![fig](https://raw.githubusercontent.com/ChenZhu-Xie/NJU_thesis_doctor__xcz/master/img/cover.png "『谢尘竹 博士论文』封面") -->
![fig](https://gitee.com/ChenZhu-Xie/NJU_thesis_doctor__xcz/raw/master/img/cover.png "『谢尘竹 博士论文』封面")

* English「README」ⓔ 👉 [Stardust_DDTank](https://github.com/ChenZhu-Xie/NJU_thesis_doctor__xcz)

# NJU Thesis: 南京大学学位论文 LaTeX 模板

![build status](https://github.com/nju-lug/NJUThesis/actions/workflows/build.yml/badge.svg)
[![CTAN](https://img.shields.io/ctan/v/njuthesis.svg)](https://www.ctan.org/pkg/njuthesis)
[![GitHub release](https://img.shields.io/github/release/nju-lug/NJUThesis/all.svg)](https://github.com/nju-lug/NJUThesis/releases/latest)
[![overleaf](https://img.shields.io/badge/online_editor-supported-brightgreen)](https://tex.nju.edu.cn/template)
[![nju-git](https://img.shields.io/gitlab/stars/nju-lug/nju-latex-templates/njuthesis?gitlab_url=https%3A%2F%2Fgit.nju.edu.cn&style=social)](https://git.nju.edu.cn/nju-lug/nju-latex-templates/njuthesis)

`njuthesis` 是制作南京大学本科生毕业论文、研究生学位论文、博士后出站报告的 LaTeX 文档类。本模板基于本科生院的论文撰写规范制作，同时参考研究生院提供的硕士、博士学位材料包，用于生成符合南京大学排版要求和相应的国家标准的学位论文，力求通过 LaTeX3 语法实现清晰的实现逻辑、较高的可定制性以及友好的用户接口。

## 快速开始

请首先阅读[用户手册](http://mirrors.ctan.org/macros/unicodetex/latex/njuthesis/njuthesis.pdf)，其中详尽阐述了模板的特性和使用方法。

对于普通用户，首要推荐使用下述的**南大 TeX 编译方法**。

### 南大 TeX 编译

[南大 TeX](https://tex.nju.edu.cn) 是 [eScience 中心](https://sci.nju.edu.cn)为南大在校师生提供的在线 LaTeX 写作平台，已*安装有本模板的最新版*。注册登录后，只需在**创建新项目**菜单中选择**论文模板**即可开始写作。

**使用本平台时，请积极备份自己的文稿。**

### 本地编译

推荐使用包管理器安装 `njuthesis` 和 `njuvisual` 的最新版。

新手同学不妨直接使用以下流程：

1. [从南大镜像站下载](https://mirror.nju.edu.cn/download/app/TeX%20%E6%8E%92%E7%89%88%E7%B3%BB%E7%BB%9F)并安装最新的 TeX 发行版，并更新所有宏包
2. 下载包含[模板全部文件](https://github.com/nju-lug/NJUThesis/releases/latest)的压缩包 `njuthesis-user-v*.zip`
3. 根据需要更改 `njuthesis-sample.tex` 文件中的内容
4. 在模板根目录下运行 `latexmk -xelatex` 运行编译，得到对应的 PDF 文件

### 典型结构

```LaTeX
\documentclass{njuthesis}
\njusetup{}
\begin{document}
\maketitle
\tableofcontents
\mainmatter
\chapter{欢迎}
使用 \LaTeX{}！
\printbibliography
\end{document}
```

## 反馈

在你遇到模板问题时，请遵守以下步骤：

1. 在《[修订记录](https://github.com/nju-lug/NJUThesis/blob/master/CHANGELOG.md)》查看该问题是否已经修复但未发布；
    - 若是，则可以使用仓库中的开发版本解决问题
1. 在 [GitHub Issues](https://github.com/nju-lug/NJUThesis/issues) 和 [Discussions](https://github.com/nju-lug/NJUThesis/discussions) 中搜索该问题的关键词；
1. 浏览[本项目 Wiki](https://github.com/nju-lug/NJUThesis/wiki) 和[用户手册](http://mirrors.ctan.org/macros/unicodetex/latex/njuthesis/njuthesis.pdf)；
1. 在你确定这是一个新问题时
    - 对于模板 bug、请求新功能、文档笔误等提出[新 issue](https://github.com/nju-lug/NJUThesis/issues/new/choose)
    - 对于用法的疑惑、格式上的斟酌等提出[新 discussion](https://github.com/nju-lug/NJUThesis/discussions/new)
    - 两个划分不绝对，区别在于 issue 是解决即关闭的
    - 如果确实重复了，会打上 duplicate 标签并将你引导至本问题首条提问

如果导师或院系有额外要求，请一同附上要求原文或格式截图。

## 贡献

欢迎提交 [PR](https://github.com/nju-lug/NJUThesis/pulls)。

## 许可

本模板的发布遵守 [LaTeX Project Public License（版本 1.3c 或更高）](https://www.latex-project.org/lppl/lppl-1-3c/)。
