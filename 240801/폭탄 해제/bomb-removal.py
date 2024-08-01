class Bomb():
    def __init__(self, code, color, second):
        self.code = code
        self.color = color
        self.second = second
    
    def print_info(self):
        print("code :", self.code)
        print("color :", self.color)
        print("second :", self.second)


code, color, second = input().split()
bomb1 = Bomb(code, color, second)

bomb1.print_info()