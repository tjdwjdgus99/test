# 베이스 이미지를 선택합니다. 예를 들어, Python을 사용할 경우:
FROM python:3.10.3-slim

# 작업 디렉토리를 설정합니다.
WORKDIR /mz01

# 애플리케이션의 종속성을 포함한 requirements.txt 파일을 복사합니다.
COPY requirements.txt .

# 종속성을 설치합니다.
RUN pip install --no-cache-dir -r requirements.txt

# 애플리케이션 파일을 복사합니다.
COPY . .

# 모델 파일을 포함시킵니다 (예: 모델 파일을 "models" 디렉토리에 위치시킨 경우)
COPY deidentification/models/3t.onnx mz01/deidentification/models/3t.onnx

# 컨테이너가 시작될 때 아무 작업도 하지 않고 대기하도록 설정합니다.
CMD ["sleep", "infinity"]
