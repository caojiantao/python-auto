import time
import xlrd
from Event import Event
import config

#pyautogui库其他用法 https://blog.csdn.net/qingfengxd1/article/details/108270159

def processTable(table):
  row = 1
  while row < table.nrows:
    type = table.cell_value(row, 0)
    content = table.cell_value(row, 1)
    e = Event(type, content)
    e.process()
    row += 1

if __name__ == '__main__':
  print(f'欢迎使用自动化工具...')
  time.sleep()
  # 读取文件
  filename = 'cmd.xls'
  wb = xlrd.open_workbook(filename=filename)
  table0 = wb.sheet_by_index(0)
  table1 = wb.sheet_by_index(1)
  # 前置条件执行
  processTable(table1)
  # 无限循环逻辑
  loopTimes = 1
  while True:
    processTable(table0)
    print(f'单次运行结束...{loopTimes}')
    loopTimes += 1
    if config.maxLoopTimes > 0 and loopTimes > config.maxLoopTimes:
      break
