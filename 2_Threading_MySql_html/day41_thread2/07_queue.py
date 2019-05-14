"""队列 queue  线程间是数据共享的,应用队列主要是为了数据安全
     ---- 保证数据安全,线程安全的
queue.Queue
   q.put()
    q.put_nowait()
   q.get(timeout=)  设置timeout
    q.get_nowait()

queue.LifoQueue
        ----相当于栈

queue.PriorityQueue
        ---- 优先级队列
     """



import queue

q = queue.Queue()


q2 = queue.PriorityQueue()
q2.put(('陈', 'zxc'))
q2.put(('一', '陈'))  # 数字为优先级,越小越高.
                  # q2.put((num, obj))
                  # 优先级一样时,put的内容按照值的优先级

print(q2.get())
print(q2.get())
