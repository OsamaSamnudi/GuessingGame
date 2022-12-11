# 1-Show Game Level
def Game_Details():
    print('''Hi; Wellcome to (Gussing Game);
    The below is Game Leveles:
    1-Easy :
        Limit (1-10)      
        Trailes Number (3)
    2-Intermediate :
        Limit (1-100)      
        Trailes Number (5)
    3-Hard :
        Limit (1-100)   
        Trailes Number (15)''')

# 2-Get Gamel Level from User:


def User_GameLevel():
    UserName = input("Enter your Name")
    print(f"Hi {UserName} Wich you success")
    while True:
        GLevels = input(
            f"Hi {UserName} Enter Game Level (1)>>'Easy',(2)>>'Intermediate',(3)>>'Hard'\t")
        if GLevels in ['1', '2', '3']:
            GLevels = int(GLevels)
            if GLevels == 1:
                T = 3
            elif GLevels == 2:
                T = 5
            elif GLevels == 3:
                T = 15
            print(f"Your Game Level is {GLevels} and your Triles# is {T}")
            break
        else:
            print(
                "Sorry Incorrect Level Number.\nYou've to choies one of below:\n(1) or (2) for or (3)")
            continue
    return GLevels

# 3-Game Setting:


def Game_S(GLevels):
    if GLevels == 1:
        Game_Range = range(1, 11)
        Game_Triales = 3
    elif GLevels == 2:
        Game_Range = range(1, 101)
        Game_Triales = 5
    else:
        Game_Range = range(1, 1001)
        Game_Triales = 15
    return Game_Range, Game_Triales

# 4-Star Playing:


def Start_Play(Game_Range, Game_Triales):
    from random import choice
    Hidden_Value = choice(Game_Range)
    while Game_Triales > 0:
        Get_Choise = int(input("Please Chose a Number"))
        Game_Triales -= 1
        if int(Hidden_Value) == int(Get_Choise):
            print(f"<<<YOU WIN>>>\nYour Choise#({Get_Choise})")
            break
        else:
            if int(Game_Triales) == 0:
                print(f"Sorry Triles Finished\nThe Hidden# is {Hidden_Value}")
                break
            elif int(Hidden_Value) > int(Get_Choise):
                print(
                    f"No {Get_Choise} is Incorrect ;Increase\nYour New Triales is : {Game_Triales}")
            elif int(Hidden_Value) < int(Get_Choise):
                print(
                    f"No {Get_Choise} is Incorrect;Decrease\nYour New Triales is : {Game_Triales}")
            else:
                continue
# 5-Play:


def Play():
    Game_Details()
    while True:
        GLevels = User_GameLevel()
        Game_Range, Game_Triales = Game_S(GLevels)
        Start_Play(Game_Range, Game_Triales)
        break


Play()
