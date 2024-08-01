class Secret():
    def __init__(self, code, space, time):
        self.code = code
        self.space = space
        self.time = time
    
    def print_secret(self):
        print("secret code :", self.code)
        print("meeting point :", self.space)
        print("time :", self.time)

code, space, time = input().split()
secret1 = Secret(code, space, time)
secret1.print_secret()