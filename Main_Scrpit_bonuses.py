def main():
    print('Welcome to our currency converter ')  # print our first screen
    third_screen(get_user_value())


def usd_to_ils():
    from class_USD import USD  # calling our class of currency and using our api function to get up-to-date result
    usd = USD.live_currency()
    return usd


def ils_to_usd():
    from class_ILS import ILS  # calling our class of currency and using our api function to get up-to-date result
    ils = ILS.live_currency()
    return ils


def ils_to_eur():
    from class_EUR import EUR  # calling our class of currency and using our api function to get up-to-date result
    eur = EUR.live_currency()
    return eur


def get_user_value():
    from class_USD import USD  # importing our class of currency
    from class_ILS import ILS
    from class_EUR import EUR
    print('Please choose an option (1/2/3): ')
    user_answer = input('1. Dollars to Shekels''\n2. Shekels to Dollars''\n3. Shekels to Euro''\n')
    # let the user chose currency option
    if user_answer == '1':  # checking which option the user chose
        while True:
            try:
                value_to_convert = float(input('how much would you like to convert'))
                while value_to_convert < 0:
                    print('Invalid choice,please enter a positive number')
                    value_to_convert = float(input('please enter amount again'))
                else:
                    num_for_list = USD.calculate_live(usd_to_ils(), value_to_convert)
                    dollar_list.append(num_for_list)
                    return num_for_list  # converting the amount to shekel/dollar
            except ValueError:
                print('Invalid choice.please enter valid amount.')
    elif user_answer == '2':
        while True:
            try:
                value_to_convert = float(input('how much would you like to convert'))
                while value_to_convert < 0:
                    print('Invalid choice,please enter a positive number')
                    value_to_convert = float(input('please enter amount again'))
                num_for_list = ILS.calculate_live(ils_to_usd(), value_to_convert)
                shekel_list.append(num_for_list)
                return num_for_list
            except ValueError:
                print('Invalid choice.please enter valid amount.')
    elif user_answer == '3':
        while True:
            try:
                value_to_convert = float(input('how much would you like to convert'))
                while value_to_convert < 0:
                    print('Invalid choice,please enter a positive number')
                    value_to_convert = float(input('please enter amount again'))
                num_for_list = EUR.calculate_live(ils_to_eur(), value_to_convert)
                euro_list.append(num_for_list)
                return num_for_list

            except ValueError:
                print('Invalid choice.please enter valid amount.')

        return get_user_value()
    else:  # making sure the user chose 1/2/3 and not enter wrong string
        print('Invalid Choice, please try again.')
        return get_user_value()  # returning the result


shekel_list = ['all of your ILS to USD conversion:']
dollar_list = ['all of your USD to ILS conversion:']
euro_list = ['all of your ILS to EUR conversion:']


def third_screen(num):
    print('your currency is: ')
    print(num)
    results_list = []
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


def last_screen(results_list):
    print('Thanks for using our currency converter.')
    print('all of your conversions:')  # printing the final list for the user
    print(results_list)
    results_file = open('results_list.txt', 'w+')
    if len(shekel_list) > 1:
        print(shekel_list)
        results_file.write(str(shekel_list)+'\n')
    if len(dollar_list) > 1:
        print(dollar_list)
        results_file.write(str(dollar_list) + '\n')
    if len(euro_list) > 1:
        print(euro_list)
        results_file.write(str(euro_list)+'\n')
    results_file.write(str(results_list))
    import subprocess  # calling the subprocess class to pop our file
    file_path = '/Users/kfirzand/PycharmProjects/First_Project/results_list.txt'
    subprocess.Popen(['open', file_path])
    results_file.close()
    tkinter()  # calling the tkinter function to open a GUI window with our result list


def tkinter():
    import tkinter as tk
    root = tk.Tk()
    root.geometry("800x500")  # making a custom size of window
    root.title("currency result")
    file = open('/Users/kfirzand/PycharmProjects/First_Project/results_list.txt', 'r')
    # calling the file with the result list
    label = tk.Label(root, text='Thanks for using our currency converter', font=('Arial', 18))
    # crating a title in the window
    label.pack()  # calling the title working
    text_widget = tk.Text(root)
    text_widget.pack(fill=tk.BOTH, expand=True)  # creating our body text
    text_widget.configure(bg='white')  # making sure the background is colored white. in mac doesn't appear right
    file_contents = file.read()
    text_widget.insert("1.0", '\n' + file_contents)  # adding your text from the file to your window
    root.mainloop()  # calling our GUI window


main()
