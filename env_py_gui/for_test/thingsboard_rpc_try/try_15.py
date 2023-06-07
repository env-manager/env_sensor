import paho.mqtt.client as mqtt

# ThingsBoard 호스트와 포트 설정
THINGSBOARD_HOST = "210.117.143.37"
PORT = 10061

# 접근 토큰 설정
ACCESS_TOKEN = '51ZFhNEWFXLi4pW758Gy'


# d41e2660-f0a1-11ed-97fe-477ec4188e5d
# 클라이언트 ID 설정
client_id = 'd41e2660-f0a1-11ed-97fe-477ec4188e5d'

# MQTT 클라이언트 생성
client = mqtt.Client(client_id=client_id)

# 접속 콜백 함수 정의
def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))
    # 연결이 성공하면 구독 요청
    client.subscribe("v1/devices/me/rpc/request/+")

# 메시지 수신 콜백 함수 정의
def on_message(client, userdata, msg):
    print("Received message: " + msg.topic + " " + str(msg.payload))

    # 수신한 메시지의 페이로드 확인
    # 원하는 RPC 명령을 처리하는 로직을 작성하세요.
    print(msg.topic.startswith("v1/devices/me/rpc/request/"))
    if msg.topic.startswith("v1/devices/me/rpc/request/"):
        # RPC 메시지의 식별자 추출
        rpc_id = msg.topic[len("v1/devices/me/rpc/request/"):]

        # 예시: 'ping' RPC 메시지에 대한 응답 전송
        if msg.payload == b'ping':
            response_topic = "v1/devices/me/rpc/response/" + rpc_id
            client.publish(response_topic, "pong")

# 연결 및 메시지 수신 콜백 함수 설정
client.on_connect = on_connect
client.on_message = on_message

# ThingsBoard에 연결
client.username_pw_set(ACCESS_TOKEN)
client.connect(THINGSBOARD_HOST, PORT, 60)

# 메시지 수신 대기
client.loop_forever()
