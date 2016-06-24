#
# @author huangpingyi
# coding:utf-8
import queue


class Chat(object):
    def __init__(self):
        self.msg_queue_hpy = queue.Queue()


    def get_msg(self,request):
        new_msgs = []
        if self.msg_queue_hpy.qsize() > 0:
            for msg in range(self.msg_queue_hpy.qsize()):
                new_msgs.append(self.msg_queue_hpy.get_nowait())
        else:
        #没有消息但是等待60秒
            try:
                print('------no new msg,going to wait for 6secs------')
                new_msgs.append(self.msg_queue_hpy.get(timeout=6))
                print("\033[33;1m Found  new msg\033[0m",new_msgs)

                #60秒有消息就放进队列中
            except queue.Empty:
                print("\033[31;1m Time out , no new msg for user[%s]\033[0m" % request.user.userprofilehpy.name)
        print("\033[33;1m Found [%s] new msg\033[0m" % len(new_msgs))
        return new_msgs
