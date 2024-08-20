import requests
import os
import sys
import zipfile
import shutil

# GitHub Repository 정보
GITHUB_REPO = "tjdwjdgus99/test"
API_SERVER_URL = f"https://api.github.com/repos/{GITHUB_REPO}"

# 현재 스크립트의 디렉토리 경로를 얻습니다.
if getattr(sys, 'frozen', False):
    # 패키징된 실행 파일의 경로
    application_path = os.path.dirname(sys.executable)
else:
    # Python 스크립트가 있는 경로
    application_path = os.path.dirname(os.path.abspath(__file__))

# version.txt 파일의 절대 경로
version_file_path = os.path.join(application_path, "version.txt")

# public REPO에서 최신 릴리스 정보 가져오기
response = requests.get(f"{API_SERVER_URL}/releases/latest")

# private REPO의 경우 인증 정보 추가
# response = requests.get(f"{API_SERVER_URL}/releases/latest", auth=("gitHub 아이디", GITHUB_API_TOKEN))

if response.status_code != 200:
    print("릴리스 체크 실패")
    sys.exit(1)

receive = response.json()

# 현재 버전 정보 읽기
if not os.path.exists(version_file_path):
    with open(version_file_path, "w") as f:
        f.write("0.0.0")  # 기본 버전 초기화
    now_current = "0.0.0"
else:
    with open(version_file_path, "r") as f:
        now_current = f.read().strip()

print(f"현재 버전 ==> {now_current}")

if receive["tag_name"] != now_current:
    # assets 다운로드 URL 가져오기
    if not receive.get("assets"):
        print("다운로드 가능한 자산이 없습니다.")
        sys.exit(1)

    download_url = receive["assets"][0]["browser_download_url"]

    # public REPO에서 파일 다운로드
    response = requests.get(download_url, headers={'Accept': 'application/octet-stream'}, stream=True)

    # private REPO의 경우 인증 정보 필요
    # response = requests.get(download_url, auth=("gitHub 아이디", GITHUB_API_TOKEN), headers={'Accept': 'application/octet-stream'}, stream=True)

    if response.status_code == 200:
        # 다운로드 받은 zip 파일명 설정하기
        update_newFile = os.path.join(application_path, "newAssets.zip")

        with open(update_newFile, "wb") as update_file:
            for chunk in response.iter_content(chunk_size=8192 * 1024):  # 8MB 씩 다운로드
                update_file.write(chunk)
        print("파일 다운로드 완료")
    else:
        print("다운로드 요청 실패")
        sys.exit(1)

    # 압축 해제
    update_temp_DIR = os.path.join(application_path, "update_temp_DIR")
    with zipfile.ZipFile(update_newFile, 'r') as zip_ref:
        zip_ref.extractall(update_temp_DIR)

    # 파일 덮어쓰기
    shutil.copytree(update_temp_DIR, application_path, dirs_exist_ok=True, ignore=shutil.ignore_patterns('version.txt'))

    # 다운로드 파일 및 압축 해제된 폴더 삭제
    os.remove(update_newFile)
    shutil.rmtree(update_temp_DIR)

    # 버전 업데이트
    with open(version_file_path, "w") as f:
        f.write(receive["tag_name"])
    print(f"{receive['tag_name']} 버전으로 업데이트 완료")

    sys.exit(0)

else:
    print("이미 최신 버전")
