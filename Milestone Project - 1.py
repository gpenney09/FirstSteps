rows1 = [' ','*',' ','*',' ']
rows2 = ['*','*','*','*','*']
rows3 = [' ','*',' ','*',' ']
rows4 = ['*','*','*','*','*']
rows5 = [' ','*',' ','*',' ']
x_turn = True

def display(row1,row2,row3,row4,row5):
    print(row1), print(row2), print(row3), print(row4), print(row5)

def play(yes):
    if yes == "Yes":
        print("\n Tic-Tac-Toe ... Start! \n")
        display(' '.join(rows1),' '.join(rows2),' '.join(rows3),' '.join(rows4),' '.join(rows5))
        _ = True
        while _ == True:
            print("\n")
            if rows1[0] == "X" and rows1[2] == "X" and rows1[4] == "X" or rows3[0] == "X" and rows3[2] == "X" and rows3[4] == "X" or rows5[0] == "X" and rows5[2] == "X" and rows5[4] == "X" or rows1[0] == "X" and rows3[2] == "X" and rows5[4] == "X" or rows1[4] == "X" and rows3[2] == "X" and rows5[0] == "X" or rows1[0] == "X" and rows3[0] == "X" and rows5[0] == "X" or rows1[2] == "X" and rows3[2] == "X" and rows5[2] == "X" or rows1[4] == "X" and rows3[4] == "X" and rows5[4] == "X":
                _ = False
                print("X player wins!")
            elif  rows1[0] == "O" and rows1[2] == "O" and rows1[4] == "O" or rows3[0] == "O" and rows3[2] == "O" and rows3[4] == "O" or rows5[0] == "O" and rows5[2] == "O" and rows5[4] == "O" or rows1[0] == "O" and rows3[2] == "O" and rows5[4] == "O" or rows1[4] == "O" and rows3[2] == "O" and rows5[0] == "O" or rows1[0] == "O" and rows3[0] == "O" and rows5[0] == "O" or rows1[2] == "O" and rows3[2] == "O" and rows5[2] == "O" or rows1[4] == "O" and rows3[4] == "O" and rows5[4] == "O":
                _ = False
                print("O player wins!")
            elif  rows1[0] != " " and rows1[2] != " " and rows1[4] != " " and rows3[0] != " " and rows3[2] != " " and rows3[4] != " " and rows5[0] != " " and rows5[2] != " " and rows5[4] != " ":
                _ = False
                print("Tie game!")
            else:
                def user_choice():
                    choose_row = 'NOPE'
                    while choose_row.isdigit() == False and choose_row.isdigit() != range(1,4):
                        choose_row = input("Choose a row (1, 2 or 3): ")
                        if choose_row.isdigit() == False:
                            print("Invalid entry. Please choose a row number (1,2 or 3).")
                            display(' '.join(rows1),' '.join(rows2),' '.join(rows3),' '.join(rows4),' '.join(rows5))
                        else:
                            if int(choose_row) == 1:
                                position_index = int(input("Choose a column (1, 2 or 3): "))
                                if position_index == 1:
                                    inputpls = input("Confirm: X or O? ").upper()
                                    if inputpls == "X" and rows1[0] == " ":
                                        rows1[0] = "X"
                                        display(' '.join(rows1),' '.join(rows2),' '.join(rows3),' '.join(rows4),' '.join(rows5))
                                    elif inputpls == "O" and rows1[0] == " ":
                                        rows1[0] = "O"
                                        display(' '.join(rows1),' '.join(rows2),' '.join(rows3),' '.join(rows4),' '.join(rows5))
                                    else:
                                        print("\n Invalid choice. Please enter 'X' or 'O'. \n")
                                        display(' '.join(rows1),' '.join(rows2),' '.join(rows3),' '.join(rows4),' '.join(rows5))
                                elif position_index == 2:
                                    inputpls = input("Confirm: X or O? ").upper()
                                    if inputpls == "X" and rows1[2] == " ":
                                        rows1[2] = "X"
                                        display(' '.join(rows1),' '.join(rows2),' '.join(rows3),' '.join(rows4),' '.join(rows5))
                                    elif inputpls == "O" and rows1[2] == " ":
                                        rows1[2] = "O"
                                        display(' '.join(rows1),' '.join(rows2),' '.join(rows3),' '.join(rows4),' '.join(rows5))
                                    else:
                                        print("\n Invalid choice. Please choose a valid option. \n")
                                        display(' '.join(rows1),' '.join(rows2),' '.join(rows3),' '.join(rows4),' '.join(rows5))
                                elif position_index == 3:
                                    inputpls = input("Confirm: X or O? ").upper()
                                    if inputpls == "X" and rows1[4] == " ":
                                        rows1[4] = "X"
                                        display(' '.join(rows1),' '.join(rows2),' '.join(rows3),' '.join(rows4),' '.join(rows5))
                                    elif inputpls == "O" and rows1[4] == " ":
                                        rows1[4] = "O"
                                        display(' '.join(rows1),' '.join(rows2),' '.join(rows3),' '.join(rows4),' '.join(rows5))
                                    else:
                                        print("\n Invalid choice. Please choose a valid option. \n")
                                        display(' '.join(rows1),' '.join(rows2),' '.join(rows3),' '.join(rows4),' '.join(rows5))
                                else:
                                    print("\n Invalid choice. Please choose a valid option. \n")
                                    display(' '.join(rows1),' '.join(rows2),' '.join(rows3),' '.join(rows4),' '.join(rows5))
                            elif int(choose_row) == 2:
                                position_index = int(input("Choose a column (1, 2 or 3): "))
                                if position_index == 1:
                                    inputpls = input("Confirm: X or O? ").upper()
                                    if inputpls == "X" and rows3[0] == " ":
                                        rows3[0] = "X"
                                        display(' '.join(rows1),' '.join(rows2),' '.join(rows3),' '.join(rows4),' '.join(rows5))
                                    elif inputpls == "O" and rows3[0] == " ":
                                        rows3[0] = "O"
                                        display(' '.join(rows1),' '.join(rows2),' '.join(rows3),' '.join(rows4),' '.join(rows5))
                                    else:
                                        print("\n Invalid choice. Please choose a valid option. \n")
                                        display(' '.join(rows1),' '.join(rows2),' '.join(rows3),' '.join(rows4),' '.join(rows5))
                                elif position_index == 2:
                                    inputpls = input("Confirm: X or O? ").upper()
                                    if inputpls == "X" and rows3[2] == " ":
                                        rows3[2] = "X"
                                        display(' '.join(rows1),' '.join(rows2),' '.join(rows3),' '.join(rows4),' '.join(rows5))
                                    elif inputpls == "O" and rows3[2] == " ":
                                        rows3[2] = "O"
                                        display(' '.join(rows1),' '.join(rows2),' '.join(rows3),' '.join(rows4),' '.join(rows5))
                                    else:
                                        print("\n Invalid choice. Please choose a valid option. \n")
                                        display(' '.join(rows1),' '.join(rows2),' '.join(rows3),' '.join(rows4),' '.join(rows5))
                                elif position_index == 3:
                                    inputpls = input("Confirm: X or O? ").upper()
                                    if inputpls == "X" and rows3[4] == " ":
                                        rows3[4] = "X"
                                        display(' '.join(rows1),' '.join(rows2),' '.join(rows3),' '.join(rows4),' '.join(rows5))
                                    elif inputpls == "O" and rows3[4] == " ":
                                        rows3[4] = "O"
                                        display(' '.join(rows1),' '.join(rows2),' '.join(rows3),' '.join(rows4),' '.join(rows5))
                                    else:
                                        print("\n Invalid choice. Please choose a valid option. \n")
                                        display(' '.join(rows1),' '.join(rows2),' '.join(rows3),' '.join(rows4),' '.join(rows5))
                                else:
                                    print("\n Invalid choice. Please choose a valid option. \n")
                                    display(' '.join(rows1),' '.join(rows2),' '.join(rows3),' '.join(rows4),' '.join(rows5))
                            elif int(choose_row) == 3:
                                position_index = int(input("Choose a column (1, 2 or 3): "))
                                if position_index == 1:
                                    inputpls = input("Confirm: X or O? ").upper()
                                    if inputpls == "X" and rows5[0] == " ":
                                        rows5[0] = "X"
                                        display(' '.join(rows1),' '.join(rows2),' '.join(rows3),' '.join(rows4),' '.join(rows5))
                                    elif inputpls == "O" and rows5[0] == " ":
                                        rows5[0] = "O"
                                        display(' '.join(rows1),' '.join(rows2),' '.join(rows3),' '.join(rows4),' '.join(rows5))
                                    else:
                                        print("\n Invalid choice. Please choose a valid option. \n")
                                        display(' '.join(rows1),' '.join(rows2),' '.join(rows3),' '.join(rows4),' '.join(rows5))
                                elif position_index == 2:
                                    inputpls = input("Confirm: X or O? ").upper()
                                    if inputpls == "X" and rows5[2] == " ":
                                        rows5[2] = "X"
                                        display(' '.join(rows1),' '.join(rows2),' '.join(rows3),' '.join(rows4),' '.join(rows5))
                                    elif inputpls == "O" and rows5[2] == " ":
                                        rows5[2] = "O"
                                        display(' '.join(rows1),' '.join(rows2),' '.join(rows3),' '.join(rows4),' '.join(rows5))
                                    else:
                                        print("\n Invalid choice. Please choose a valid option. \n")
                                        display(' '.join(rows1),' '.join(rows2),' '.join(rows3),' '.join(rows4),' '.join(rows5))
                                elif position_index == 3:
                                    inputpls = input("Confirm: X or O? ").upper()
                                    if inputpls == "X" and rows5[4] == " ":
                                        rows5[4] = "X"
                                        display(' '.join(rows1),' '.join(rows2),' '.join(rows3),' '.join(rows4),' '.join(rows5))
                                    elif inputpls == "O" and rows5[4] == " ":
                                        rows5[4] = "O"
                                        display(' '.join(rows1),' '.join(rows2),' '.join(rows3),' '.join(rows4),' '.join(rows5))
                                    else:
                                        print("\n Invalid choice. Please choose a valid option. \n")
                                        display(' '.join(rows1),' '.join(rows2),' '.join(rows3),' '.join(rows4),' '.join(rows5))
                                else:
                                    print("\n Invalid choice. Please choose a valid option. \n")
                                    display(' '.join(rows1),' '.join(rows2),' '.join(rows3),' '.join(rows4),' '.join(rows5))
                            else:
                                print("\n Invalid choice. Please choose a valid option. \n")
                                display(' '.join(rows1),' '.join(rows2),' '.join(rows3),' '.join(rows4),' '.join(rows5))
                user_choice()
        else:
            print("Good game.")
    else:
        print("Nevermind then.")

play_game_request = input("Want to play Tic-Tac-Toe? " )
if play_game_request == "Yes" or play_game_request == "yes" or play_game_request == "Y" or play_game_request == "y" or play_game_request == "":
    play("Yes")
else:
    print("\n Nevermind then.")
