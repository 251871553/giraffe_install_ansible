import os
try:
   import zookeeper
except ImportError,e:
   print(e)
   os.system('ldconfig  -v  /usr/local/lib')
import  sys
#zk = zookeeper.init("10.10.1.201:6181,10.10.1.212:6181,10.10.1.213:6181")
zookeeper.set_debug_level(zookeeper.LOG_LEVEL_ERROR)
zk = zookeeper.init("10.0.17.162:6181")

try:
    zookeeper.create(zk,"/cn","null",[{"perms":0x1f,"scheme":"world","id":"anyone"}],0)
    zookeeper.create(zk,"/cn/onebank","null",[{"perms":0x1f,"scheme":"world","id":"anyone"}],0)
    zookeeper.create(zk,"/cn/onebank/giraffe","null",[{"perms":0x1f,"scheme":"world","id":"anyone"}],0)
    zookeeper.create(zk,"/cn/onebank/giraffe/nameserver","8.8.8.8:6606;10.11.17.215:6606",[{"perms":0x1f,"scheme":"world","id":"anyone"}],0)
    zookeeper.create(zk,"/cn/onebank/giraffe/nameserverAll","8.8.8.8:6606;10.11.17.215:6606",[{"perms":0x1f,"scheme":"world","id":"anyone"}],0)
    zookeeper.create(zk,"/cn/onebank/giraffe/nameserverOut","8.8.8.8:6606;10.11.17.215:6606",[{"perms":0x1f,"scheme":"world","id":"anyone"}],0)
    zookeeper.create(zk,"/cn/onebank/giraffe/nameserverOutAll","8.8.8.8:6606;10.11.17.215:6606",[{"perms":0x1f,"scheme":"world","id":"anyone"}],0)
    zookeeper.create(zk,"/cn/onebank/giraffe/logstash","8.8.8.8:6221",[{"perms":0x1f,"scheme":"world","id":"anyone"}],0)
    # print  zookeeper.get(zk,'/test3')
except zookeeper.NodeExistsException,e:
    print 'create  node failure ,because the node  is  existent.'


print('------check------')

print('nameserver: ' + zookeeper.get(zk,'/cn/onebank/giraffe/nameserver')[0])
print('nameserverAll: ' + zookeeper.get(zk,'/cn/onebank/giraffe/nameserverAll')[0])
print('nameserverOut: ' + zookeeper.get(zk,'/cn/onebank/giraffe/nameserverOut')[0])
print('nameserverOutAll: ' + zookeeper.get(zk,'/cn/onebank/giraffe/nameserverOutAll')[0])
print('logstash: ' + zookeeper.get(zk,'/cn/onebank/giraffe/logstash')[0])
def set(i):
      nodeinfo='/node%d' %i
      datainfo='datajfajdfkjaslkjdfajsfiwerkjkjelkjkljafd%d'  %i
      zookeeper.create(zk,nodeinfo  ,datainfo  ,[{"perms":0x1f,"scheme":"world","id":"anyone"}],0)
      print  'insert  number %d is ok! ' %i

def get(i):
      nodeinfo='/node%d' %i
      data=zookeeper.get(zk,nodeinfo)
      print  data

