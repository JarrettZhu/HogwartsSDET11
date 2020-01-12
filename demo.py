# 字符串
# 使用r，可以不用写“\\”的转义字符
print(r'C:\sss\sss')
# 前后字符串会自动链接起来
print('Py' 'thon')
# f可以添加值
x = 'abc'
print(f'C:\\sss\\sss\\{x}')
# format用法
print('C:\\sss\\sss\\{}\\{}'.format(x, 123))
print('C:\\sss\\sss\\{y}\\{x}'.format(y=x, x=123))

# 列表
squares = [1, 4, 9, 16, 25]
# 堆栈：append、pop
# 队列：from collections import deque
# squares = [1, 4, 9, 16, 25]
# queue = deque(squares)
# queue.append('a')
# queue.popleft()
