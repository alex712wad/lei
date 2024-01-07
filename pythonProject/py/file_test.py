import json
def luck_number():
    num=eval(input('please enter your lucky number !'))
    with open('lucknum.txt','w') as file:
        json.dump(num,file)
def get_number():
    try:
        with open('lucknum.txt','r') as file:
            print(file.read())
    except FileNotFoundError:
        luck_number()
        get_number()
if __name__ == '__main__':
    get_number()