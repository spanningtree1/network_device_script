import cflw代码库py.cflw字符串 as 字符串
import cflw代码库py.cflw工具_序列 as 序列
import cflw代码库py.cflw工具_运算 as 运算
from ..基础接口 import 数据表
from ..基础接口 import 信息
from . import 接口 as 实现接口
def f解析速率(a速率: str):
	if "-" in a速率:
		return int(字符串.f提取字符串之间(a速率, "-", None))
	if a速率.isdigit():
		return int(a速率)
	return 0
class C接口状态表ev6:
	"""show interface status
	适用于: 浪潮s5350"""
	c标题行0 = "Port        Status     Duplex  Speed   Mode    Type                    Description  "
	c标题行1 = "------------------------------------------------------------------------------------------"
	c接口 = 0
	c状态 = 12	#链路状态
	c双工 = 23
	c速率 = 31
	c模式 = 39	#链路类型
	c类型 = 47	#以太网类型
	c描述 = 71
	ca列 = (c接口, c状态, c双工, c速率, c模式, c类型, c描述)
	def __init__(self, a文本):
		self.m文本 = a文本
	def __iter__(self):
		return self.fe处理数据表(self.m文本)
	fe处理数据表 = 数据表.Fe一行记录数据表(
		数据表.F去标题行(c标题行0, c标题行1),
		运算.f总是真,
		[
			数据表.F处理列(数据表.E字段.e本端接口, 序列.F切片(c接口, c状态), 实现接口.f创建接口ev6),
			数据表.F处理列(数据表.E字段.e本端链路状态, 序列.F切片(c状态, c双工), 信息.f解析起宕状态),
			数据表.F处理列(数据表.E字段.e本端双工模式, 序列.F切片(c双工, c速率), 信息.f解析双工模式),
			数据表.F处理列(数据表.E字段.e本端速率, 序列.F切片(c速率, c模式), f解析速率),
			数据表.F处理列(数据表.E字段.e本端描述, 序列.F切片(c描述, None), 运算.f原值)
		],
		运算.f总是假
	)