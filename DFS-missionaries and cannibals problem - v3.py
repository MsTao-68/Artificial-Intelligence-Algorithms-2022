'''
深度优先搜索
'''

class States:
    def __init__(self, leftMis, leftCann, posShip):
        self.leftMis = leftMis
        self.leftCann = leftCann
        self.rightMis = 3 - self.leftMis
        self.rightCann = 3 - self.leftCann
        self.posShip = posShip
        self.Misnum = 3
        self.Cannum = 3

class Solution:
    def __init__(self):
        self.notFindFlag = True
    def check(self,state:States) -> bool:
        if ((state.leftCann > state.leftMis) and (state.leftMis != 0)
            or (state.rightMis > state.rightMis) and (state.rightMis != 0)
            or (state.leftCann < 0)
            or (state.leftMis < 0 )
            or (state.rightCann < 0)
            or (state.rightMis < 0)
            or (state in stateSet)):
            return False
        else:
            return True
    def DFS(self,state:States):
        if not state: return
        stateSet.add(state)
        res.append(state)
        if (state.leftCann == 0 and state.leftMis == 0):
            self.notFindFlag = False
            return False
        # 船在左边
        if state.posShip == 0:
            for i in range(3):
                new = States(state.leftMis + missionaryMove[i],
                                   state.leftCann + cannibalMove[i],
                                    (state.posShip + 1) % 2)
                if (self.check(new) and self.notFindFlag):
                    self.DFS(new)

        else:
            for i in range(3):
                new = States(state.leftMis + missionaryMove[i],
                             state.leftCann + cannibalMove[i],
                            (state.posShip + 1) % 2)
                if (self.check(new) and self.notFindFlag):
                    self.DFS(new)

    def result(self):
        for i in range(len(res) - 1):
            if res[i].posShip == 0:  # 船在左岸
                print("左岸->右岸：{}传教士，{}野人".format( res[i + 1].rightMis - res[i].rightMis, res[i + 1].rightCann - res[i].rightCann))
            else:
                print("右岸->左岸：{}传教士，{}野人".format( res[i + 1].leftMis - res[i].leftMis, res[i + 1].leftCann - res[i].leftCann))

if __name__ == "__main__":
    res = []  # 存储搜索路径
    # 数组格式 state = 【左边传教士人数，左边野人人数，船位置（0左边，1右边）】
    stateSet = set([])
    cannibalMove = [1, 1, 0]  # 移动时要减去的数组
    missionaryMove = [1, 0, 2]  # 移动时要减去的数组
    status = States(3, 3, 0,)
    Solution().DFS(status)
    Solution().result()





