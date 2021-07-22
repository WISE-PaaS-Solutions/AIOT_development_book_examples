import time
import Adafruit_DHT

GPIO_PIN = 4

try:
    print('按下 Ctrl-C 可停止程式')
    while True:
        h, t = Adafruit_DHT.read_retry(Adafruit_DHT.DHT11, GPIO_PIN)
        if h is not None and t is not None:
            print('溫度={0:0.1f}度C 濕度={1:0.1f}%'.format(t, h))
        else:
            print('讀取失敗，重新讀取。')
        time.sleep(10)
except KeyboardInterrupt:
    print('關閉程式')
