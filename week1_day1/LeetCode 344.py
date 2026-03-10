'''编写一个函数，其作用是将输入的字符串反转过来。输入字符串以字符数组 s 的形式给出。'''
'''输入字符串s，输出以字符数组s给出（考虑变换数据类型为字符串）'''


def reverseString(s):
    # 1. 【关键步骤】如果是字符串，先转成列表
    if isinstance(s, str):
        s_list = list(s)
    else:
        s_list = s

    # 2. 执行反转逻辑
    left, right = 0, len(s_list) - 1
    while left < right:
        s_list[left], s_list[right] = s_list[right], s_list[left]
        left += 1
        right -= 1

    # 3. 【关键步骤】如果原本是字符串，再转回字符串
    if isinstance(s, str):
        return "".join(s_list)
    else:
        return s_list


# 测试
print(reverseString("hello"))  # 输出："olleh" (字符串)
print(reverseString(["h", "e"]))  # 输出：['e', 'h'] (列表)
