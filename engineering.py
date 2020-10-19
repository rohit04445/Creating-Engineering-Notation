def multiply(num, power_of_ten):
    num = str(num)
    if num.find('.') == -1:
        num = num + '.'
    point_index = num.find('.')
    while len(num[point_index + 1:len(num)]) < power_of_ten:
        num = num + '0'
    point_index = num.find('.')
    num = num.replace('.', '')
    num = num[0:point_index + power_of_ten] + '.' + num[point_index + power_of_ten:]
    minusSignPresent = False
    if num[0] == '-':
        minusSignPresent = True
        num = num[1:]
    iterate = 0
    while iterate < num.find('.'):
        if num[iterate] != "0":
            break
        else:
            num = num[iterate + 1:]
        iterate = iterate + 1
    if num[0] == '.':
        num = '0' + num
    if num[len(num) - 1] == '.':
        num = num + '0'
    if minusSignPresent:
        num = '-' + num
    return num


# this function return the rounded value to the required number of significant numbers
def round_to_given_significant_figures(x, p):
    return round(x, p)


# In eng_notation we first find the e notation of the given number i.e if number is 1250000
# gives 1.250000e+06.As from here we an see this the last two characters gives the power of 10 required
# and the characters before e gives the Actual number to be presented
# And according to the no. of significant figures the required string is given back
def eng_notation(number, sigfigs=3):
    Scientific_Notation = "{:e}".format(number)  # Scientific_Notation contains the scientific notation
    # By string slicing and type conversion the power_of_ten contains the power of 10
    power_of_ten = int(Scientific_Notation[Scientific_Notation.__len__() - 2:Scientific_Notation.__len__()])

    # Sign contains the sign i.e. the power of 10 is +ve or -ve
    sign = Scientific_Notation[Scientific_Notation.__len__() - 3]

    # no contains the actual value in such a way that there is only single digit
    # before decimal point
    no = float(Scientific_Notation[0:Scientific_Notation.__len__() - 4])

    # m will contain  the value we have to use the while loop before loop ends because by this number we have
    # to multiply our number to get correct answer
    m = 0

    # if condition will check if sign is +ve or -ve because for +ve sign the suffix are like 'M','G'
    # but for -ve sign the suffix are 'm','u'

    if sign.__eq__('+'):
        suffix = ["", "k", "M", "G", "T", "P"]
        while 1:
            if power_of_ten % 3 == 0:
                Suffix_index = int(power_of_ten / 3)
                Suffix_Notation_Used = suffix[Suffix_index]
                break
            # power_of_ten is decreased because it is not matching with the required suffix index so by decreasing it
            # we will try for next option and also have to increase m as now no to be multiplied by 10
            power_of_ten = power_of_ten - 1
            m = m + 1
        # for getting the number of significant figures we use round function but in another way we will first convert
        # our number to a number like 0.233 etc. so then calling the round function will five us the correct number of
        # significant figures so we will have to divide the no by 10 and also increment m
        rounded_number = round_to_given_significant_figures(no / 10, sigfigs)
        m += 1
        # for getting correct decimal point after notation we will call multiple function
        Scientific_Notation = multiply(rounded_number, m)
        return str(Scientific_Notation) + Suffix_Notation_Used


    else:
        suffix = ["", "m", "u", "n", "p", "f"]
        while 1:
            if power_of_ten % 3 == 0:
                Suffix_index = int(power_of_ten / 3)
                Suffix_Notation_Used = suffix[Suffix_index]
                break
            # power_of_ten is decreased because it is not matching with the required suffix index so by decreasing it
            # we will try for next option and also have to increase m as now no to be multiplied by 10
            power_of_ten = power_of_ten - 1
            m = m + 1
    # for getting the number of significant figures we use round function but in another way we will first convert
    # our number to a number like 0.233 etc. so then calling the round function will five us the correct number of
    # significant figures so we will have to divide the no by 10 and also increment m
    rounded_number = round_to_given_significant_figures(no / 10, sigfigs)
    m += 1
    # for getting correct decimal point after notation we will call multiple function
    Scientific_Notation = multiply(rounded_number, m)
    return str(Scientific_Notation) + Suffix_Notation_Used


if __name__ == "__main__":
    test_cases = [0.0, 1.2345, 23.456, -345.67, 4567.8, -56789, 12345e6,
                  -2345.6e9]
    for i in range(1, 5):
        print("i is", i)
        for case in test_cases:
            print(case, "-->", eng_notation(case, i))
