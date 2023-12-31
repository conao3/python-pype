import subprocess


def assert_stdout(proc: subprocess.CompletedProcess[bytes], expected: str) -> None:
    res = proc.stdout.decode('utf-8')
    assert res.splitlines() == expected.splitlines()


def run_pype(args: list[str]) -> subprocess.CompletedProcess[bytes]:
    return subprocess.run(['pype', *args], capture_output=True, check=True)


def test_91d1d7b1():
    proc = run_pype(['-c', '-e', 'print("hello")'])
    expected = '''\
# pype
with open("tmp.fifo") as f:
    line = f.read()
    __ors = ''
    L = line
    _ = L
    print("hello")
'''
    assert_stdout(proc, expected)


def test_bb9de651():
    proc = run_pype(['-c', '-e', 'print("hello")', 'print("world")'])
    expected = '''\
# pype
with open("tmp.fifo") as f:
    line = f.read()
    __ors = ''
    L = line
    _ = L
    print("hello")
    print("world")
'''
    assert_stdout(proc, expected)


def test_04da38f4():
    proc = run_pype(['-c', '-ne', 'print("hello")'])
    expected = '''\
# pype
with open("tmp.fifo") as f:
    for NR, line in enumerate(f, start=1):
        __ors = ''
        L = line
        _ = L
        print("hello")
'''
    assert_stdout(proc, expected)


def test_c604fcbf():
    proc = run_pype(['-c', '-nle', 'print("hello")'])
    expected = '''\
# pype
with open("tmp.fifo") as f:
    for NR, line in enumerate(f, start=1):
        __ors = None
        line = line.strip()
        L = line
        _ = L
        print("hello")
'''
    assert_stdout(proc, expected)


def test_1aa48b99():
    proc = run_pype(['-c', '-n0le', 'print("hello")'])
    expected = '''\
# pype
with open("tmp.fifo") as f:
    for NR, line in enumerate(f.read().rstrip('\\0').split('\\0'), start=1):
        __ors = None
        line = line.strip()
        L = line
        _ = L
        print("hello")
'''
    assert_stdout(proc, expected)


def test_66260b0f():
    proc = run_pype(['-c', '-a', '-nle', 'print("hello")'])
    expected = '''\
# pype
import re as __re
with open("tmp.fifo") as f:
    for NR, line in enumerate(f, start=1):
        __ors = None
        line = line.strip()
        __fs = None
        words = [e for e in __re.split(__fs or ' ', line) if e]
        F = words
        L = line
        _ = L
        print("hello")
'''
    assert_stdout(proc, expected)


def test_ed4ca3c4():
    proc = run_pype(['-c', '-aF,', '-nle', 'print(F[0])'])
    expected = '''\
# pype
import re as __re
with open("tmp.fifo") as f:
    for NR, line in enumerate(f, start=1):
        __ors = None
        line = line.strip()
        __fs = ','
        words = [e for e in __re.split(__fs or ' ', line) if e]
        F = words
        L = line
        _ = L
        print(F[0])
'''
    assert_stdout(proc, expected)


def test_e089f925():
    proc = run_pype(['-c', '-aF-', '-nle', 'print(F[0])'])
    expected = '''\
# pype
import re as __re
with open("tmp.fifo") as f:
    for NR, line in enumerate(f, start=1):
        __ors = None
        line = line.strip()
        __fs = '-'
        words = [e for e in __re.split(__fs or ' ', line) if e]
        F = words
        L = line
        _ = L
        print(F[0])
'''
    assert_stdout(proc, expected)


def test_0dc91605():
    proc = run_pype(['-c', r"-aF\s", '-nle', 'print(F[0])'])
    expected = '''\
# pype
import re as __re
with open("tmp.fifo") as f:
    for NR, line in enumerate(f, start=1):
        __ors = None
        line = line.strip()
        __fs = '\\s'
        words = [e for e in __re.split(__fs or ' ', line) if e]
        F = words
        L = line
        _ = L
        print(F[0])
'''
    assert_stdout(proc, expected)


def test_dce9b4ec():
    proc = run_pype(['-c', '-m', 'datetime', '-nle', 'print("hello")'])
    expected = '''\
# pype
import datetime
with open("tmp.fifo") as f:
    for NR, line in enumerate(f, start=1):
        __ors = None
        line = line.strip()
        L = line
        _ = L
        print("hello")
'''
    assert_stdout(proc, expected)


def test_468cf587():
    proc = run_pype(['-c', '-m', 'datetime', 're', '-nle', 'print("hello")'])
    expected = '''\
# pype
import datetime
import re
with open("tmp.fifo") as f:
    for NR, line in enumerate(f, start=1):
        __ors = None
        line = line.strip()
        L = line
        _ = L
        print("hello")
'''
    assert_stdout(proc, expected)


def test_2811f31f():
    proc = run_pype(['-c', '-m', 'datetime', 'os.path[join,exists]', '-nle', 'print("hello")'])
    expected = '''\
# pype
import datetime
from os.path import join,exists
with open("tmp.fifo") as f:
    for NR, line in enumerate(f, start=1):
        __ors = None
        line = line.strip()
        L = line
        _ = L
        print("hello")
'''
    assert_stdout(proc, expected)


def test_ee6aaa3b():
    proc = run_pype(['-c', '-m', 'os', 'datetime=dt', 'os.path[join=jn,exists]', '-nle', 'print("hello")'])
    expected = '''\
# pype
import os
import datetime as dt
from os.path import join as jn,exists
with open("tmp.fifo") as f:
    for NR, line in enumerate(f, start=1):
        __ors = None
        line = line.strip()
        L = line
        _ = L
        print("hello")
'''
    assert_stdout(proc, expected)


def test_b6da375e():
    proc = run_pype(['-c', '-m', 'datetime[*]', '-M', 're', '-nle', 'print("hello")'])
    expected = '''\
# pype
from datetime import *
from re import *
with open("tmp.fifo") as f:
    for NR, line in enumerate(f, start=1):
        __ors = None
        line = line.strip()
        L = line
        _ = L
        print("hello")
'''
    assert_stdout(proc, expected)


def test_ffd5b397():
    proc = run_pype(['-c', '-nlp'])
    expected = '''\
# pype
with open("tmp.fifo") as f:
    for NR, line in enumerate(f, start=1):
        __ors = None
        line = line.strip()
        L = line
        _ = L
        print(line, end=__ors)
'''
    assert_stdout(proc, expected)


def test_f9105054():
    proc = run_pype(['-c', '-nlp', '-e', 'line = line[:-1]'])
    expected = '''\
# pype
with open("tmp.fifo") as f:
    for NR, line in enumerate(f, start=1):
        __ors = None
        line = line.strip()
        L = line
        _ = L
        line = line[:-1]
        print(line, end=__ors)
'''
    assert_stdout(proc, expected)
