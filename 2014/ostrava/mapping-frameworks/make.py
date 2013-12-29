#!/usr/bin/env python

import subprocess
from subprocess import Popen
import os

R_SCRIPT = "plot.r"


def get_table(data):
    """Generate LaTeX table
    """
    n = len(data)

    table = "\\begin{tabularx}{\\textwidth}{| l || %s |}\n" %\
            " | ".join([" X " for i in range(len(data[0].split()))])

    header  = "\\hline\n \\rowcolor{Gray} & %s \\\\ \n\\hline \n" % " & ".join(map(lambda v: "\\textbf{%s}" % v ,data[0].split()))

    table += header

    def mark(v):
        if (v == min_value):
            return "\\cellcolor{green!25}\\textbf{%.2f}" % v
        elif (v == max_value):
            return "\\cellcolor{red!25}\\textbf{%.2f}" % v
        else:
            return "%.2f" % v

    for x in range(1, n):
        times = map(lambda v: float(v), data[x].split()[1:])
        min_value = min(times)
        max_value = max(times)
        times = map(lambda (v): mark(v), times)
        features = data[x].split()[0]
        table += "%s & %s \\\\ \n \\hline \n" % (features," & ".join(times))


    table += "\\end{tabularx}"
    return table


def graphs():
    """Generate graphs using R
    """

    proc = Popen(["R", "--vanilla"], stdout=subprocess.PIPE, stdin=open(R_SCRIPT))
    proc.wait()

def latex():
    """Generate LaTeX beamer slides
    """

    tmpl = """
    \\begin{frame}{%(title)s}
    \\begin{center}
        \includegraphics[width=0.75\\textwidth]{%(file)s}
        \\\\
        \\tiny
        %(table)s
    \\\\
    %(title)s [s]
    \\end{center}
    \\end{frame}
    """

    out_all = open(os.path.join('latexs', 'slides.tex'), 'w')

    for result in os.listdir('results'):
        if (result == 'result-raw.txt'):
            continue
        out = os.path.join('latexs', result.replace('txt', 'tex'))
        out_all.write("%% \\input{%s}\n" % result.replace(".txt", ""))
        out_file = open(out, 'w')

        data = {
            'file': os.path.join('graphs', result.replace("txt", "png")),
            'table': get_table(open(os.path.join('results', result)).readlines()),
            'title': " ".join(result.replace(".txt", "").replace("result", "").split("-"))
        }
        out_file.write(tmpl % data)
        out_file.close()
        out_all.write(tmpl % data)
    out_all.close()

if __name__ == '__main__':
    graphs()
    latex();
