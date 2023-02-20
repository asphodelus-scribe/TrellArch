import flags
class logicState():
    def __init__(self):
        self.f = flags.CMD_SELECT
        self.r = [None]*4
        self.m = [None]*16
    def parseInput(self, x):
        # 17
        if self.f == flags.CMD_SELECT:
            self.f = x
        # 0
        elif self.f == flags.SET_VAR_NUM:
            self.r[0] = x
            self.f = flags.INPUT_NUM
        # 1
        elif self.f == flags.SET_VAR_VAR:
            self.r[0] = x
            self.r[3] = 21
            self.f = flags.SET_READ_FROM
        # 2
        elif self.f == flags.GET_VAR:
            self.r[1] = x
            self.r[3] = 20
            self.f = flags.READ_VAR
        # 18
        elif self.f == flags.READ_VAR:
            self.r[2] = self.m[self.r[1]]
            self.f = self.r[3]
        # 19
        elif self.f == flags.SET_READ_FROM:
            self.r[1] = x
            self.f = flags.READ_VAR
        # 20
        elif self.f == flags.SHOW_VAR:
            print("var",self.r[1],"=",self.r[2])
            self.f = flags.CMD_SELECT
        # 21
        elif self.f == flags.WRITE_VAR:
            self.m[self.r[0]] = self.r[2]
            self.f = flags.CMD_SELECT
        # 22
        elif self.f == flags.INPUT_NUM:
            self.r[2] = x
            self.f = flags.WRITE_VAR

        print(self.r)
        print(self.m)
        print(self.f)
