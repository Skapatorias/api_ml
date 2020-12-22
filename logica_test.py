import pytest
from logica import *


def test_vertical_T():
   assert vertical(ejemplo_v) == True

def test_horizontal_T():
    assert horizontal(ejemplo_h) == True

def test_diagonal_D_T():
    assert diagonal(ejemplo_d) == True

def test_diagonal_A_T():
    assert diagonal(ejemplo_d_a) == True

def test_vertical_F():
    assert vertical(ejemplo_h) == False

def test_horizontal_F():
    assert horizontal(ejemplo_d) == False

def test_diagonal_F():
    assert diagonal(noesmutante) == False

def test_isMutant_T():
    assert isMutant(ejemplo_h) == True

def test_isMutant_F():
    assert isMutant(noesmutante) == False



ejemplo_d = ["DTGCGA",
             "CAGGGC",
             "TTATGA",
             "AGACAG",
             "CCCDTD",
             "TCACTG"]

ejemplo_d_a = ["DTGCGA",
             "CAGGGC",
             "TTACGA",
             "AGCCAD",
             "CCCDTD",
             "CCACTG"]


ejemplo_h = ["ATGCGA",
             "CAGTGC",
             "TTATGT",
             "AGAAAG",
             "CCCCTA",
             "TCACTG"]


ejemplo_v = ["ATTCGC",
             "CTTTGD",
             "TTTCGD",
             "ATGDSC",
             "TTCCTC",
             "TTACTC"]

noesmutante = ["QWERTY","YUIOPA","ASDFGH","ZXCVBN","MJHFRS","TCACTG"]