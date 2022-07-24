import pyautogui
import pydirectinput

class Event:
  def __init__(self, type, content):
    self.type = type
    self.content = content

  def isImg(self):
    suffixs = ['jpg', 'png']
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
  