from numb3rs import validate
def main():
    test_validate()

def test_validate():
    assert validate("127.0.0.1") == True
    assert validate("225.225.255.255") == True
    assert validate("1.2.3.1000") == False
    assert validate("127.0.0.1.2") == False
    assert validate("cat") == False
    assert validate("0") == False

if __name__ == "__main__":
    main()