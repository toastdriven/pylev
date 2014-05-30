#!/bin/bash
echo -ne "py2.7 recursive_levenshtein\t"
python2.7 -m timeit -s "import pylev" "pylev.recursive_levenshtein('Levenshtein', 'Frankenstein')"
echo -ne "py2.7 wf_levenshtein\t\t"
python2.7 -m timeit -s "import pylev" "pylev.wf_levenshtein('Levenshtein', 'Frankenstein')"
echo -ne "py2.7 wfi_levenshtein\t\t"
python2.7 -m timeit -s "import pylev" "pylev.wfi_levenshtein('Levenshtein', 'Frankenstein')"

echo -ne "py3.3 recursive_levenshtein\t"
python3.3 -m timeit -s "import pylev" "pylev.recursive_levenshtein('Levenshtein', 'Frankenstein')"
echo -ne "py3.3 wf_levenshtein\t\t"
python3.3 -m timeit -s "import pylev" "pylev.wf_levenshtein('Levenshtein', 'Frankenstein')"
echo -ne "py3.3 wfi_levenshtein\t\t"
python3.3 -m timeit -s "import pylev" "pylev.wfi_levenshtein('Levenshtein', 'Frankenstein')"

echo -ne "pypy recursive_levenshtein\t"
pypy -m timeit -s "import pylev" "pylev.recursive_levenshtein('Levenshtein', 'Frankenstein')"
echo -ne "pypy wf_levenshtein\t\t"
pypy -m timeit -s "import pylev" "pylev.wf_levenshtein('Levenshtein', 'Frankenstein')"
echo -ne "pypy wfi_levenshtein\t\t"
pypy -m timeit -s "import pylev" "pylev.wfi_levenshtein('Levenshtein', 'Frankenstein')"

