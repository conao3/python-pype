import subprocess


def assert_stdout(proc: subprocess.CompletedProcess[bytes], expected: str) -> None:
    res = proc.stdout.decode('utf-8')
    assert res.splitlines() == expected.splitlines()


def run_pype(args: list[str]) -> subprocess.CompletedProcess[bytes]:
    return subprocess.run(['pype', *args], capture_output=True, check=True)


def test_91d1d7b1():
    proc = run_pype(['-c', '-e', 'print("hello")'])
    expected = '''\
import sys

with open("tmp.fifo") as f:
    line = f.read()
    L = line
    _ = L
    print("hello")
'''
    assert_stdout(proc, expected)


def test_04da38f4():
    proc = run_pype(['-c', '-ne', 'print("hello")'])
    expected = '''\
import sys

with open("tmp.fifo") as f:
    for NR, line in enumerate(f, start=1):
        L = line
        _ = L
        print("hello")
'''
    assert_stdout(proc, expected)


def test_c604fcbf():
    proc = run_pype(['-c', '-nle', 'print("hello")'])
    expected = '''\
import sys

with open("tmp.fifo") as f:
    for NR, line in enumerate(f, start=1):
        line = line.strip()
        L = line
        _ = L
        print("hello")
'''
    assert_stdout(proc, expected)
