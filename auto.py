import time
import xlrd
from Event import Event

#pyautogui库其他用法 https://blog.csdn.net/qingfengxd1/article/details/108270159

if __name__ == '__main__':
  print('欢迎使用自动化工具...')
  time.sleep(1)

  # 读取文件
  filename = 'cmd.xls'
  wb = xlrd.open_workbook(filename=filename)
  table = wb.sheet_by_index(0)
  while True:
    row = 1
    while row < table.nrows:
      type = table.cell_value(row, 0)
      content = table.cell_value(row, 1)

      e = Event(type, content)
      e.process()

      row += 1
    print('单次运行结束...')
    time.sleep(0.5)