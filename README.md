### 赛博数码管
+ 模拟数码管：字母&数字
+ 模拟4x4像素屏：符号
+ 一定程度上防烧屏：每次显示后会移动一个像素
+ 复古扫屏动画（参考旧电子秤的启动画面）
+ 顺序切换动画（从当前显示的数字开始逐个切换数字直至到达目标数字）
#### <a href='https://github.com/adafruit/micropython-adafruit-ssd1306'>ssd1306驱动fork自adafruit</a>
#### <a href='https://www.bilibili.com/video/BV1QA411r744/'>BiliBili</a>
<img href='https://github.com/rtyfghvbnlndl/OLED_Segment_Displays_MicroPython/数码管.jpg'></img>   
使用0.91寸OLED 128X32 MicroPython

### 说明

```python
import digitron,ssd1306
#esp32
lcd = I2C(1,scl=Pin(25), sda=Pin(26), freq=400000)
#esp8266
#lcd = I2C(scl=Pin(5), sda=Pin(4), freq=400000)
display = ssd1306.SSD1306_I2C(128, 32, lcd)
d = digitron.digitron (display)
#显示数字1（0-9）
d.num(1)
#显示字母（a-z)
d.ab('a')#必须是str
#动态动画
d.effNum(9)#如目前显示1，会依次显示2、3、4、5、6、7、8、9。
d.effNum(2)#如目前显示8，会依次显示9、0、1。
#自检动画
d.start()
#显示转圈圈的动画
```