def vogal(c):
    if c == "a" or c == "e" or c == "i" or c == "o" or c == "u" or c == "A" or c == "E" or c == "I" or c == "O" or c == "U":
        return True
    else:
        return False

def test_vogal1():
    assert vogal("a") == True
def test_vogal2():
    assert vogal("e") == True
def test_vogal3():
    assert vogal("i") == True
def test_vogal4():
    assert vogal("o") == True
def test_vogal5():
    assert vogal("u") == True
def test_vogal6():
    assert vogal("A") == True
def test_vogal7():
    assert vogal("E") == True
def test_vogal8():
    assert vogal("I") == True
def test_vogal9():
    assert vogal("O") == True
def test_vogal10():
    assert vogal("U") == True
def test_vogal11():
    assert vogal("Q") == False
def test_vogal12():
    assert vogal("T") == False
def test_vogal12():
    assert vogal("K") == False
def test_vogal13():
    assert vogal("L") == False
def test_vogal14():
    assert vogal("z") == False
def test_vogal15():
    assert vogal("x") == False
def test_vogal16():
    assert vogal("b") == False
def test_vogal17():
    assert vogal("n") == False
def test_vogal18():
    assert vogal("m") == False
def test_vogal19():
    assert vogal("g") == False
def test_vogal20():
    assert vogal("y") == False
