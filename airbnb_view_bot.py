
import webbrowser
import time
from pykeyboard import PyKeyboard ## install from github
from pymouse import PyMouse

count = 0
max_views = 1000
urls = ["https://www.airbnb.com/rooms/20895036?s=67&shared_item_type=1&virality_entry_point=1",
        ]
k = PyKeyboard()
m = PyMouse()

print "Starting view bot: " + str(max_views) + " requests"

while count < 1000:
    for url in urls:
      webbrowser.open_new_tab(url)
      time.sleep(2)
      x_dim, y_dim = m.screen_size()
      # print x_dim, y_dim
      # print x_dim/5, y_dim/6
      m.click(x_dim/5, y_dim/2, 1)
      time.sleep(30)
      k.press_keys(['Control_L','w'])
      count += 1
      print "View " + str(count) + " complete."


else:
    pass
