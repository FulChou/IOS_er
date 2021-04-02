# mac os中 address alread in use如何解决：

在进行socket编程时，我们在运行server端代码的时候遇到了如下的问题：


显示地址已经被占用，那么我们如何解决这个问题？

首先我们看一下server端的代码：

s = socket.socket()
host = socket.gethostname()
port = 12345
s.bind((host,port))
s.listen(5)
1
2
3
4
5
Use lsof -i :5000 This will give you a list of processes using the port if any. Once the list of processes is given, use the id on the PID column to terminate the process: e.g kill 379

我们可以使用lsof指令来找出正在使用此端口的进程，然后根据PID（ProcessID，进程ID）进行kill操作即可（PID就是各进程的身份标识，程序一运行系统就会自动分配给进程一个独一无二的PID。进程中止后PID被系统回收，可能会被继续分配给新运行的程序）。

例如：

当然这不是根本的解决为何stop了server.py程序，但是还被占用的问题。究其原因，是socket选项在捣鬼。下面是IBM官网上对这一情况的具体解释，参见http://www.ibm.com/developerworks/cn/linux/l-sockpit/。
bind 普遍遭遇的问题是试图绑定一个已经在使用的端口。该陷阱是也许没有活动的套接字存在，但仍然禁止绑定端口（bind 返回 EADDRINUSE），它由 TCP 套接字状态 TIME_WAIT 引起。该状态在套接字关闭后约保留 2 到 4 分钟。在 TIME_WAIT 状态退出之后，套接字被删除，该地址才能被重新绑定而不出问题。
等待 TIME_WAIT 结束可能是令人恼火的一件事，特别是如果您正在开发一个套接字服务器，就需要停止服务器来做一些改动，然后重启。幸运的是，有方法可以避开 TIME_WAIT 状态。可以给套接字应用 SO_REUSEADDR 套接字选项，以便端口可以马上重用。也可以参见如下博客