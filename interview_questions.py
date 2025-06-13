original_string = "hello"
reversed_string = ''.join (reversed(original_string))
print (reversed_string)

original_string = "hello"
reversed_string = reversed(original_string)
reversed_string_using_loop = ''
for i in reversed_string:
    reversed_string_using_loop = reversed_string_using_loop + i
    print(reversed_string_using_loop)
def reverse_string(word):
 return ''.join(reversed(word))
def test_reverse_string():
 input_str = "TripleTen"
 reversed_str = reverse_string(input_str)
assert reversed_str == "neTelpirT"
print ("Test Passed! " + input_str + "'s reverse is " + reversed_str)


    def reverse_string(word):
        return ''.join(reversed(word))
    def test_reverse_string():
        input_str = "UrbanRoutes"
        reversed_str = reverse_string(input_str)
        assert reversed_str == 'setuoRnabrU'
        print("Test Passed! " + input_str + "'s reverse is " + reversed_str)

 string = "hello"
reversed_string = "".join(reversed(string))
print(reversed_string)


def reverse_string(word):
    result = ''.join(reversed(word))


def test_reverse_string():
    input_str = "UrbanRoutes"

    reversed_str = reverse_string(input_str)

    assert reversed_str == 'setuoRnabrU'

    print("Test Passed! " + input_str + "'s reverse is " + reversed_str)