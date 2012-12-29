% !Mode:: "TeX:UTF-8"
% +-----------------------------------------------------------------------------
% | File: yaldc
% | Author: huxuan
% | E-mail: i(at)huxuan.org
% | Created: 2012-12-11
% | Last modified: 2012-12-11
% | Description:
% |     Yet Another LaTeX Document Class
% |
% | Copyrgiht (c) 2012 by huxuan. All rights reserved.
% | License GPLv3
% +-----------------------------------------------------------------------------

%%%%%%%%%% class clarification %%%%%%%%%%
\NeedsTeXFormat{LaTeX2e}[2007/10/19]
\ProvidesClass{yaldc}
              [2012/07/06 v0.8
Yet Another LaTeX Document Class]

\newif\ifyaldc@color\yaldc@colorfalse
\DeclareOption{color}{\yaldc@colortrue}

\DeclareOption*{\PassOptionsToClass{\CurrentOption}{ctexart}}
\ProcessOptions\relax
\LoadClass[cs4size,a4paper,fancyhdr]{ctexart}[2007/10/19]

\let\stdsection\section
\renewcommand\section{\clearpage\stdsection}

%%%%%%%%%% geometry %%%%%%%%%%
\RequirePackage[top=1in,bottom=1in,left=1.25in,right=1.25in]{geometry}
\renewcommand{\baselinestretch}{1.5}

%%%%%%%%%% color %%%%%%%%%%
\RequirePackage{color}
\definecolor{dkgreen}{rgb}{0,0.6,0}
\definecolor{gray}{rgb}{0.5,0.5,0.5}
\definecolor{mauve}{rgb}{0.58,0,0.82}

%%%%%%%%%% hyperref %%%%%%%%%%
\RequirePackage{hyperref}
\hypersetup{colorlinks}

%%%%%%%%%% listings %%%%%%%%%%
\RequirePackage{listings}
\renewcommand{\lstlistingname}{代码}
\lstset{
    backgroundcolor=\color{white},
    basicstyle=\zihao{5}\ttfamily,
    columns=flexible,
    breakatwhitespace=false,
    breaklines=true,
    captionpos=b,
    frame=single,
    numbers=left,
    numbersep=5pt,
    showspaces=false,
    showstringspaces=false,
    showtabs=false,
    stepnumber=1,
    rulecolor=\color{black},
    tabsize=2,
    title=\lstname,
    escapeinside={\%*}{*)},
    extendedchars=false,
    mathescape=true,
    xleftmargin=3em,
    xrightmargin=3em,
    numberstyle=\color{gray},
    keywordstyle=\color{blue},
    commentstyle=\color{dkgreen},
    stringstyle=\color{mauve},
}

%%%%%%%%%% dirtree %%%%%%%%%%
\RequirePackage{dirtree}
\renewcommand*\DTstylecomment{\ttfamily\color{dkgreen}}
\renewcommand*\DTstyle{\ttfamily\color{red}}
