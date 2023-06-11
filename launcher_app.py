import sys

sys.path.append('/home/orangepi/env_sensor/env_py_gui')


# sys.path.append('/home/orangepi/env_sensor/info')
# from device_number import DEVICE_NUM
from app import EnvSensor, FULL_SCREEN
from uart_data_thread import UartDataThread

if __name__ == '__main__':

    app = EnvSensor()
    u = UartDataThread(app,app.uart_data_view)
    u.start()


    app.home_frame.get_all_data()
    app.home_frame.time_update()

    # 꼭 풀어줘야함 519
    app.home_frame.lan_connection_update()
    app.wifi_frame.new_ver_wifi_func()
    app.wifi_frame.get_current_wifi()
    app.home_frame.send_mqtt_data()
    app.element_frame.change_image()

    app.geometry("800x480")
    app.attributes('-fullscreen', FULL_SCREEN)
    app.mainloop()