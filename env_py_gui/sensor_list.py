# from enum import Enum

# class SensorList(Enum):
#     TVOC = 1
#     CO = 2
#     CO2 = 3
#     NO2 = 4
#     PM25 = 5
#     H2S = 6
#     PM10 = 7
#     LIGHT = 8
#     CH2O = 9
#     SOUND = 10
#     SM = 11
#     RN = 12
#     NH3 = 13
#     O3 = 14

# sensorname : ['main에서 쓰이는 img.png', 'element_page에서 쓰이는 img.png']
SENSOR_DICT = {
    'TVOC':['/home/orangepi/env_sensor/env_py_gui/img/sensor/Main-TVOC.png','/home/orangepi/env_sensor/env_py_gui/img/sensor/TVOC.png', 200, 600, 2000,400,'ppb'],  # ~200 : 좋음(1) || ~600 : 보통(2) || ~2000 : 나쁨(3) || 2000~ : 아주나쁨(4)        마지막은 권고치
    'CO2':['/home/orangepi/env_sensor/env_py_gui/img/sensor/Main-CO2.png','/home/orangepi/env_sensor/env_py_gui/img/sensor/CO2.png', 450, 1000, 2000,1000, 'ppm'],
    'PM1' :['','',1,2,3,2, 'ug/m3'],         # <= temp range
    'PM25':['/home/orangepi/env_sensor/env_py_gui/img/sensor/Main-PM2.5.png','/home/orangepi/env_sensor/env_py_gui/img/sensor/PM2.5.png', 15, 35, 75,35,'ug/m3'],
    'PM10':['/home/orangepi/env_sensor/env_py_gui/img/sensor/Main-PM10.png','/home/orangepi/env_sensor/env_py_gui/img/sensor/PM10.png', 30, 80, 150,75,'ug/m3'],
    'CH2O':['/home/orangepi/env_sensor/env_py_gui/img/sensor/Main-CH2O.png','/home/orangepi/env_sensor/env_py_gui/img/sensor/CH2O.png', 0.001, 0.01, 0.08,0.1, 'ppm'],
    'SM':['/home/orangepi/env_sensor/env_py_gui/img/sensor/Main-Sm.png','/home/orangepi/env_sensor/env_py_gui/img/sensor/Sm.png', 0.0001, 1, 2,1, 'ppm'],  # temp
    'NH3':['/home/orangepi/env_sensor/env_py_gui/img/sensor/Main-NH3.png','/home/orangepi/env_sensor/env_py_gui/img/sensor/NH3.png', 0.15, 1, 5,1, 'ppm'],
    'CO':['/home/orangepi/env_sensor/env_py_gui/img/sensor/Main-CO.png','/home/orangepi/env_sensor/env_py_gui/img/sensor/CO.png', 2, 9, 15,10, 'ppm'],
    'NO2':['/home/orangepi/env_sensor/env_py_gui/img/sensor/Main-NO2.png','/home/orangepi/env_sensor/env_py_gui/img/sensor/NO2.png', 0.03, 0.05, 0.2,0.05, 'ppm'],
    'H2S':['/home/orangepi/env_sensor/env_py_gui/img/sensor/Main-H2S.png','/home/orangepi/env_sensor/env_py_gui/img/sensor/H2S.png', 0.005, 0.02, 0.3,0.005, 'ppm'],
    'LIGHT':['/home/orangepi/env_sensor/env_py_gui/img/sensor/Main-LIGHT.png','/home/orangepi/env_sensor/env_py_gui/img/sensor/LIGHT.png', 3, 5, 10, 10, 'Lx'],
    'SOUND':['/home/orangepi/env_sensor/env_py_gui/img/sensor/Main-Sound.png','/home/orangepi/env_sensor/env_py_gui/img/sensor/Sound.png', 35, 40, 60,60, 'dB'],
    'RN':['/home/orangepi/env_sensor/env_py_gui/img/sensor/Main-Rn.png','/home/orangepi/env_sensor/env_py_gui/img/sensor/Rn.png', 74, 200, 300,200, 'Bq/m3'],  # unit 설정 필수 일단 pCi/l
    'O3':['/home/orangepi/env_sensor/env_py_gui/img/sensor/Main-O3.png','/home/orangepi/env_sensor/env_py_gui/img/sensor/O3.png', 0.03, 0.09, 0.15,0.02, 'ppm'],
}
