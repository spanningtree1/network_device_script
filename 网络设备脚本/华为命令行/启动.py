import time
import cflw代码库py.cflw时间 as 时间
from ..基础接口 import 操作
from ..命令行接口 import 命令
from ..基础接口 import 协议
from ..基础接口 import 接口 as 北向接口
c启动字符 = '\x02'
c旧密码 = "huawei"
c新密码 = "Admin@huawei.com"
class C启动(设备.I启动模式):
	def __init__(self, a):
		设备.I启动模式.__init__(self, a)
	def f登录(self, a密码 = c新密码, a超时 = 60):
		v秒表 = 时间.C秒表()
		while True:
			self.m设备.f输入(c启动字符)
			time.sleep(1)
			v输出 = self.m设备.f输出(a等待 = False)
			#继续判断
			if "password:" in v输出:
				break
			#超时判断
			if v秒表.f滴答() >= a超时:
				raise TimeoutError()
		self.m设备.f输入(a密码)
		self.m设备.f输入_回车()
