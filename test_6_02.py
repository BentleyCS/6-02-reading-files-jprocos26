import HW_6_02 as HW

# tests files
print("Creating test files...")

f = open("ExampleText.txt", "w")
f.write("Here is the text\ni am another line")
f.close()

f = open("SingleLine.txt", "w")
f.write("Just one line")
f.close()

f = open("LongestLineTest.txt", "w")
f.write("short\nthis is a much longer line\nmedium line")
f.close()

f = open("BinaryTest.txt", "w")
f.write("011010010010101010101010")
f.close()

f = open("BinaryTest2.txt", "w")
f.write("111100001010")
f.close()

print("Test files created!\n")


# Test functions
def test_toString():
    assert HW.toString("ExampleText.txt") == "Here is the text\ni am another line"
    assert HW.toString("SingleLine.txt") == "Just one line"

def test_longestLine():
    assert HW.longestLine("LongestLineTest.txt") == "this is a much longer line"
    assert HW.longestLine("ExampleText.txt") == "i am another line"

def test_toBinary():
    assert HW.toBinary("BinaryTest.txt") == ['01101001', '00101010', '10101010']
    assert HW.toBinary("BinaryTest2.txt") == ['11110000', '1010']


# Run the tests
test_toString()
print(" toString passed")

test_longestLine()
print(" longestLine passed")

test_toBinary()
print(" toBinary passed")

print(" All tests passed")