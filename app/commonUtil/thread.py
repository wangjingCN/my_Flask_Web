#!/usr/bin/env python
# -*- coding: utf-8 -*-
import threadingTest
import random
import Queue
from time import sleep
import sys
#
#需求分析：有大批量数据需要执行，而且是重复一个函数操作（例如爆破密码），如果全部开始线程数N多，这里控制住线程数m个并行执行，其他等待
#
#继承一个Thread类，在run方法中进行需要重复的单个函数操作
class Test(threadingTest.Thread):
  def __init__(self,queue,lock,num):
    #传递一个队列queue和线程锁，并行数
    threadingTest.Thread.__init__(self)
    self.queue=queue
    self.lock=lock
    self.num=num
  def run(self):
    #while True:#不使用threading.Semaphore，直接开始所有线程，程序执行完毕线程都还不死，最后的print threading.enumerate()可以看出
    with self.num:#同时并行指定的线程数量，执行完毕一个则死掉一个线程
      #以下为需要重复的单次函数操作
      n=self.queue.get()#等待队列进入
      lock.acquire()#锁住线程，防止同时输出造成混乱
      print '开始一个线程：',self.name,'模拟的执行时间：',n
      print '队列剩余：',queue.qsize()
      print threadingTest.enumerate()
      lock.release()
      sleep(n)#执行单次操作，这里sleep模拟执行过程
      self.queue.task_done()#发出此队列完成信号
threads=[]
queue=Queue.Queue()
lock=threadingTest.Lock()
num=threadingTest.Semaphore(3)#设置同时执行的线程数为3，其他等待执行
#启动所有线程
for i in range(10):#总共需要执行的次数
  t=Test(queue,lock,num)
  t.start()
  threads.append(t)
  #吧队列传入线程，是run结束等待开始执行，放下面单独一个for也行，这里少个循环吧
  n=random.randint(1,10)
  queue.put(n)#模拟执行函数的逐个不同输入
#吧队列传入线程，是run结束等待开始执行
#for t in threads:
#  n=random.randint(1,10)
#  queue.put(n)
#等待线程执行完毕
for t in threads:
  t.join()
queue.join()#等待队列执行完毕才继续执行，否则下面语句会在线程未接受就开始执行
print '所有执行完毕'
# print threading.active_count()
# print threading.enumerate()