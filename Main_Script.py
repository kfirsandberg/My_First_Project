def main():
    print('Welcome to our currency converter ')  # print our first screen
    third_screen(get_user_value())
    # calling all the functions. third_screen contain the last screen function


def get_user_value():
    from class_USD import USD  # importing our class of currency
    from class_ILS import ILS
    print('Please choose an option (1/2): ')
    user_answer = input('1. Dollars to Shekels''\n2. Shekels to Dollars''\n')
    # let the user chose currency option
    if user_answer == '1':  # checking which option the user chose
        while True:  # making sure the user choose a valid answer
            try:
                value_to_convert = float(input('how much would you like to convert'))
                while value_to_convert < 0:  # making sure the user didn't choose a negative members
                    print('Invalid choice,please enter a positive number')
                    value_to_convert = float(input('please enter amount again'))
                return USD.calculate(value_to_convert)
                # converting the amount to shekel/dollar using our function from our class
            except ValueError:
                print('Invalid choice.please enter valid amount.')
    elif user_answer == '2':
        while True:
            try:
                value_to_convert = float(input('how much would you like to convert'))
                while value_to_convert < 0:
                    print('Invalid choice,please enter a positive number')
                    value_to_convert = float(input('please enter amount again'))
                return ILS.calculate(value_to_convert)
            except ValueError:
                print('Invalid choice.please enter valid amount.')

        return get_user_value()
    else:  # making sure the user chose 1/2 and not enter wrong string
        print('Invalid Choice, please try again.')
        return get_user_value()  # returning the result


def third_screen(num):
    print('your currency is: ')
    print(num)
    results_list = ['this is all of your conversion:']
    results_list.append(num)    # adding the first result to the list
    first_answer = input('would you like to start over answer: y/n')

    def wrong(answer2):  # function that check the user answer and let the user start again the currency calculator
        while answer2 not in {'y', "Y", 'yes', 'YES'} and answer2 not in {'n', 'N', 'no', 'NO'}:
            # making sure the user enter the right string
            print('Invalid Choice, please try again.')
            answer2 = input('would you like to start over answer: y/n')
        else:
            while answer2 == 'y' or answer2 == 'Y' or answer2 == 'yes' or answer2 == 'YES':
                # let the user start again the calculator
                num2 = get_user_value()
                print('your currency is: ')
                print(num2)
                results_list.append(num2)
                answer3 = input('would you like to start over answer: y/n')
                wrong(answer3)
                answer2 = ''  # preventing the loop and make sure the loop doesn't enter to infinite loop
            while answer2 == 'n' or answer2 == 'N' or answer2 == 'NO' or answer2 == 'no':
                last_screen(results_list)  # calling the last screen function with our list result
                break  # stopping the loop
    wrong(first_answer)
    return results_list


def last_screen(results_list):
    print('Thanks for using our currency converter.')
    print('all of your conversions:')  # printing the final list for the user
    print(results_list)
    results_file = open('results_list.txt', 'w+')  # opening our file and writing our result list to the file
    results_file.write(str(results_list))
    results_file.close()  # making sure we're closing our file and cleaning our memory
    return results_list


main()
