# PyAutoGUI使用的是模拟按键码，而对于这些游戏或软件来说需要直接从设备中获取数据，而不是模拟的
import pyautogui
import pydirectinput
import config

class Event:
  def __init__(self, type, content):
    self.type = type
    self.content = content

  def isImg(self):
    suffixs = ['jpg', 'jpeg', 'png']
    for suf in suffixs:
      if self.content.endswith(suf):
        return True
    return False

  def process(self):
    print(self.type, self.content)
    if self.type == '移动':
      if self.isImg():
        p = pyautogui.locateCenterOnScreen(self.content, confidence=0.9)
      else:
        splits = self.content.split(',')
        p.x = int(splits[0])
        p.y = int(splits[1])
      if p is not None:
        pyautogui.moveTo(p.x, p.y)
    elif self.type == '按压':
      pydirectinput.press(self.content)
    elif self.type == '压住':
      pydirectinput.keyDown(self.content)
    elif self.type == '弹起':
      pydirectinput.keyUp(self.content)
    elif self.type == '单击':
      pydirectinput.click(self.content)
    elif self.type == '输入':
      pydirectinput.typewrite(self.content)
    elif self.type == '循环延迟':
      config.loopDelay = float(self.content)
