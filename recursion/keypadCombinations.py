def get_characters(num):
    if num == 2:
        return "abc"
    elif num == 3:
        return "def"
    elif num == 4:
        return "ghi"
    elif num == 5:
        return "jkl"
    elif num == 6:
        return "mno"
    elif num == 7:
        return "pqrs"
    elif num == 8:
        return "tuv"
    elif num == 9:
        return "wxyz"
    else:
        return ""

# Recursive solution
def keypad(num):
    # Base case
    print('I am here!')
    print('num')
    print(num)
    if num <= 1:
        print('base_case')
        return [""]

    elif 1 < num <= 9:
        print('i have a lower number!')
        print(get_characters(num))
        return list(get_characters(num))

   
    last_digit = num % 10
    print('last_digit')
    print(last_digit)
    print('');


    print('num//10')
    print(num//10)
    print('')

    small_output = keypad(num//10)
    print('small_output')
    print(small_output)
    print('')
  
    keypad_string = get_characters(last_digit)
    print('keypad_string')
    print(keypad_string)
    print('')
    output = list()

    
    for character in keypad_string:
        for item in small_output:
            new_item = item + character
            print('new_item')
            print(new_item)
            output.append(new_item)

    print(output)
    return output

def test_keypad(input, expected_output):
    if sorted(keypad(input)) == expected_output:
        print("Yay. We got it right.")
    else:
        print("Oops! That was incorrect.")

input = 354
expected_output = sorted(["djg", "ejg", "fjg", "dkg", "ekg", "fkg", "dlg", "elg", "flg", "djh", "ejh", "fjh", "dkh", "ekh", "fkh", "dlh", "elh", "flh", "dji", "eji", "fji", "dki", "eki", "fki", "dli", "eli", "fli"])
test_keypad(input, expected_output)

    