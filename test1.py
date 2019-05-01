"""对 [-2^31, 2^31-1]范围的int类型的数进行反转.
负号不会被反转
"""

class Solution:
    def reverse(self, x: int) -> int:
        if x < -2**31 or x > 2**31-1:
            return 0
        else:
            list_x = []
            ret = []
            [list_x.append(i) for i in str(x)]
            if list_x[0] == '-':
                ret.append('-')
                list_x.remove('-')
            while len(list_x) > 0:
                ret.append(list_x.pop())
            if int(''.join(ret)) < -2 ** 31 or int(''.join(ret)) > 2 ** 31 - 1:
                return 0
            return int(''.join(ret))

if __name__ == '__main__':
    nnn = Solution()
    print(nnn.reverse(1534236469))
