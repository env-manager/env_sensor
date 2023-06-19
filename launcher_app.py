import sys

sys.path.append('/home/orangepi/env_sensor/env_py_gui')
sys.path.append('/home/orangepi/env_sensor/info')



# sys.path.append('/home/orangepi/env_sensor/info')
# from device_number import DEVICE_NUM
from app import EnvSensor, FULL_SCREEN
from uart_data_thread import UartDataThread
from device_list import device_info
from device_number import DEVICE_NUM
import os, subprocess
import threading
from time import sleep

######################################################
######################## temp ########################
import paho.mqtt.client as mqtt

######################################################
# sangsang temp account test
# print('장치 번호 : ', device_info[DEVICE_NUM-1][0])
# print('장치 아이디 : ', device_info[DEVICE_NUM-1][1])
# print('장치 이름 : ', device_info[DEVICE_NUM-1][2])
# print('장치 토큰 : ', device_info[DEVICE_NUM-1][3])



# ThingsBoard 호스트와 포트 설정
THINGSBOARD_HOST = "210.117.143.37"
PORT = 10061
# 임의 토큰
ACCESS_TOKEN = device_info[DEVICE_NUM-1][3]
import json
# 임의로 잡아둠
client_id = device_info[DEVICE_NUM-1][1]

if __name__ == '__main__':

    app = EnvSensor()
    u = UartDataThread(app,app.uart_data_view)
    u.start()

    client = mqtt.Client(client_id = client_id)
    
    # connection call back <- 
    def on_connect(client, userdata, flags, rc):
        # print("Connected with result code " + str(rc))
        # access Good -> subscribe
        try:
            client.subscribe("v1/devices/me/rpc/request/+")
        except:
            print('No internet connection here')
    # 메시지 수신 콜백 함수 정의
    def on_message(client, userdata, msg):
        # print("Received message: " + msg.topic + " " + str(msg.payload))

        # print('topic : ', msg.topic)
        # print('payload : ', str(msg.payload))
        
        # print(dict_data)
        try:
            decode_code = msg.payload.decode('utf-8')    
            dict_data = json.loads(decode_code)
            if dict_data['method'] == 'setValue':           # 센서 보고 주기 설정
                # print('method is setValue')
                # print('params (type) : ', type(dict_data['params']))
                # print('params : ', dict_data['params'])
                # print(dict_data['params']['TIME'])
                # if dict_data['params'].key == 'Time':
                #     print(dict_data['params']['Time'])
                if dict_data['params']['TIME'] != None:
                    print(dict_data['params']['TIME'])
                    app.send_term = int(dict_data['params']['TIME'])
                    
                
            elif dict_data['method'] == 'execCmd':
                # print('method is execCmd')
                # print('params (type) : ', type(dict_data['params']))
                # print('params : ', dict_data['params'])
                # if dict_data['params'] ==
                # print(dict_data['params']['UPDATE'])

                #################################################### UPDATE ####################################################
                if dict_data['params']['UPDATE'] != None:

                    execute_cmd('rm -r /home/orangepi/env_sensor/env_py_gui')
                    repo_url = 'https://github.com/env-manager/env_py_gui.git'
                    destination_folder = '/home/orangepi/env_sensor/env_py_gui'
                    try:
                        subprocess.check_output(["git", "clone", repo_url, destination_folder], cwd='/tmp')
                        print('Process well done')
                        sleep(5)
                        execute_cmd('reboot')
                    except subprocess.CalledProcessError as e:
                        print(e)
                
            else:
                pass
        except:
            pass
        
        
        # print(type(payload))
    #     topic :  v1/devices/me/rpc/request/9
    # payload :  b'{"method":"execCmd","params":{"RESET":"ON"}}'

        # 수신한 메시지의 페이로드 확인
        # 원하는 RPC 명령을 처리하는 로직을 작성하세요.
        # print(msg.topic.startswith("v1/devices/me/rpc/request/"))
        if msg.topic.startswith("v1/devices/me/rpc/request/"):
            # RPC 메시지의 식별자 추출
            rpc_id = msg.topic[len("v1/devices/me/rpc/request/"):]

            # 예시: 'ping' RPC 메시지에 대한 응답 전송
            if msg.payload == b'ping':
                response_topic = "v1/devices/me/rpc/response/" + rpc_id
                client.publish(response_topic, "pong")
    client.on_connect = on_connect
    client.on_message = on_message
    client.username_pw_set(ACCESS_TOKEN)
    try:  
        client.connect(THINGSBOARD_HOST, PORT, 60)
    except:
        print("Plz reboot your COM")
    # client.loop_forever()
    mqtt_thread = threading.Thread(target=client.loop_forever)
    mqtt_thread.start()
    def execute_cmd(cmd):
        os.system(cmd)
    
    thingsboard_rpc = ''
    
    # if thingsboard_rpc == 'update':
    #     execute_cmd('rm -r /home/orangepi/env_sensor/env_py_gui')
    #     repo_url = 'https://github.com/env-manager/env_py_gui.git'
    #     destination_folder = '/home/orangepi/env_sensor/env_py_gui'
    #     try:
    #         subprocess.check_output(["git", "clone", repo_url, destination_folder], cwd='/tmp')
    #         print('Process well done')
    #         sleep(5)
    #         execute_cmd('reboot')
    #     except subprocess.CalledProcessError as e:
    #         print(e)
    
    
    
    
    app.home_frame.get_all_data()
    app.home_frame.time_update()

    # 꼭 풀어줘야함
    app.home_frame.lan_connection_update()
    app.wifi_frame.new_ver_wifi_func()
    app.wifi_frame.get_current_wifi()
    app.home_frame.send_mqtt_data()
    # app.element_frame.change_image()

    app.geometry("800x480")
    app.attributes('-fullscreen', FULL_SCREEN)
    app.mainloop()
    
    mqtt_thread.join()