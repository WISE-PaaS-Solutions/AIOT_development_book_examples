import time
import adafruit_dht
from influxdb import InfluxDBClient

GPIO_PIN = 4
client = InfluxDBClient(host = '<WISE-PaaS/InfluxDB網址>',
                        port = '<埠號>',
                        username = '<使用者名稱>',
                        password = '<使用者密碼>')

try:
    client.switch_database('<資料庫編號>')
    print('資料庫連結成功')
    while True:
        h, t = adafruit_dht.read_retry(adafruit_dht.DHT11, GPIO_PIN)
        if h is not None and t is not None:
            print('溫度={0:0.1f}度C 濕度={1:0.1f}%'.format(t, h))
            data = [{"measurement": "DHT11",
                    "fields": {"temp": t, "humi": h},
                    "tags":{"location": "THU-C306", "sensor": "DHT11"}
                    }]
            client.write_points(data)
        else:
            print('讀取失敗，重新讀取。')
        time.sleep(10)
except:
    print('資料庫連結失敗')
