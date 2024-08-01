class Info():
    def __init__(self, id, level):
        self.id = id
        self.level = level
    
    def print_info(self):
        print("user", self.id, "lv", self.level)

info1 = Info("codetree", 10)
id, level = input().split()
info2 = Info(id, int(level))

info1.print_info()
info2.print_info()