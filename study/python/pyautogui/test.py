# 案例获取鼠标的位置，方便复制我们定位的鼠标坐标点到代码中
import pyautogui
import time


# 获取鼠标位置
def get_mouse_positon():
  time.sleep(5) # 准备时间
  print('开始获取鼠标位置')
  try:
    for i in range(10):
      # Get and print the mouse coordinates.
      x, y = pyautogui.position()
      positionStr = '鼠标坐标点（X,Y）为：{},{}'.format(str(x).rjust(4), str(y).rjust(4))
      pix = pyautogui.screenshot().getpixel((x, y)) # 获取鼠标所在屏幕点的RGB颜色
      positionStr += ' RGB:(' + str(pix[0]).rjust(3) + ',' + str(pix[1]).rjust(3) + ',' + str(pix[2]).rjust(
        3) + ')'
      print(positionStr)
      time.sleep(0.5) # 停顿时间
  except:
    print('获取鼠标位置失败')

#if __name__ == "__main__":
#  time.sleep(5) # 准备时间
#  pyautogui.click('1.jpg')


#if __name__ == "__main__":
#  time.sleep(5) # 准备时间
#  pyautogui.click(x=200,y=200,button='right')


#if __name__ == "__main__":
#  pyautogui.moveTo(x=300,y=300,duration=0.25)


#if __name__ == "__main__":
#  get_mouse_positon()


if __name__ == "__main__":
  print(pyautogui.size())
  Size(width=1280, height=800)