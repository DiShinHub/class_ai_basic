# 파이썬을 이용한 머신러닝, 딥러닝 실전 개발 입문 (개정판)

독자의 실습 편의를 위해 최신 환경에서 작동하는 코드로 수정했습니다([requirements.txt](requirements.txt) 참조).

## 강의 영상

- [강의 영상 목록](lecture_video_list.md)

## 다운로드

- 예제 코드
  - 현재 버전
      - [압축 파일](https://github.com/wikibook/pyml-rev/archive/refs/heads/main.zip) 다운로드  
         또는 터미널에서 `git clone https://github.com/wikibook/pyml-rev.git` 실행
  - [구 버전 코드](https://drive.google.com/uc?export=download&id=17YpSzwuQzuR79d48EiNmAu1uCeJwAkX1) (받지 않아도 됩니다.)

- 데이터 파일(1,2,3차 URL 중 하나만 받으시면 됩니다)
  - 1차 다운로드 링크: [pyml_rev_data_20191204.zip](https://drive.google.com/uc?export=download&id=1FEGuJTOwFaz1Zz3gRSIXV-Y-HCMf1-1U)
  - 2차 다운로드 링크: [pyml_rev_data_20191204.zip](https://drive.google.com/uc?export=download&id=1eGFjTtwqJWobqz_kvs84Wya411lcHLsX)
  - 3차 다운로드 링크: [pyml_rev_data_20191204.zip](https://drive.google.com/uc?export=download&id=1NxsNavBodYFMRapqQ43AHeBb_9Ks8zwE)

## 실습 환경 구축 방법

### 옵션 1: 가상 머신을 사용하지 않고 실습

가상 머신 없이 컴퓨터에 직접 실습 환경을 구축하려면 다음 순서를 따릅니다.
  1. 예제 코드 다운로드
  1. [아나콘다](https://www.anaconda.com/) 설치
  1. 터미널(또는 명령 프롬프트)에서 예제 코드 폴더로 가서 파이썬 패키지 설치 후 실습.  
     예:
     ```
     > cd C:\pyml-rev
     > pip install -r requirements.txt
     ```
  1. 텐서플로 작동 테스트
     ```
     python3 -c "import tensorflow as tf; print(tf.reduce_sum(tf.random.normal([1000, 1000])))"
     ```

  1. 예제 코드 실행
     ```
     > cd ch1
     > python3 download-png1.py
     ```

### 옵션 2: Vagrant 가상 머신 사용 (부록-1의 방법)

Vagrant를 이용해 우분투 가상 머신에 실습 환경을 구축하려면 다음 순서를 따릅니다.

  1. 예제 코드 다운로드  
  1. [VirtualBox](https://www.virtualbox.org/) 설치
  1. [Vagrant](https://www.vagrantup.com/) 설치
  1. 터미널에서 예제 코드 폴더(`Vagrantfile`이 있는 곳)로 가서 `vagrant up` 실행(실습에 필요한 프로그램과 파이썬 패키지가 자동으로 설치됨).  
     예:
     ```
     > cd C:\pyml-rev
     > vagrant up
     ```
     (문제 해결: Windows 호스트에서 게스트 창 하단에 녹색 거북이가 보이는 경우 https://blog.koasing.pe.kr/hyper-v-vbox-nem/ 참조)
  1. 터미널에서 SSH로 가상 머신에 연결  
     ```
     > vagrant ssh
     ```
     텐서플로 작동 테스트  
     ```
     $ python3 -c "import tensorflow as tf; print(tf.reduce_sum(tf.random.normal([1000, 1000])))"
     ```
     
     SSH 실습 코드가 있는 곳으로 이동
     
     ```
     $ cd /vagrant
     ```
     
     예제 코드 실행  
      
     ```
     $ cd ch1
     $ python3 download-png1.py
     ```
     
### 옵션 3: 도커 가상 환경 (부록-2의 방법)

도커를 이용해 실습 환경을 구축하려면 책의 부록-2 및 관련 영상을 참조.


### ch4 
use venv 


### ch5 
use conda

1. 아나콘다 설치 

https://www.anaconda.com/download

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/778ec731-3462-4e0d-9d2c-db986d81d45d/0aca4be5-5754-4ba2-9f4a-31702bfc0251/Untitled.png)

cd / Downloads

bash Anaconda3-2024.02-1-MacOSX-arm64.sh

2. 파이썬 3.9 설치 

텐서플로우는 파이썬 버전에 굉장히 민감함, 본 설치에서는 3.9로 강제함. 

https://www.python.org/downloads/release/python-390/

3. 가상환경 생성

conda create -n venv_tensor python=3.9

conda env list

conda activate venv_tensor

4. 패키지 설치

conda install -c apple tensorflow-deps

pip install tensorflow-macos

~~pip install tensorflow-metal (설치하면 오히려 애러가 난다)~~

5. 패키지 의존성 업그레이드

pip install numpy --upgrade

pip install pandas --upgrade

pip install matplotlib --upgrade

pip install scipy --upgrade

pip install plotly --upgrade

6. 확인 

(venv_tensor) sindong-ig@sindong-ig-ui-MacBookPro anaconda3 % python
Python 3.9.18 | packaged by conda-forge | (main, Dec 23 2023, 16:35:41)
[Clang 16.0.6 ] on darwin
Type "help", "copyright", "credits" or "license" for more information.

> import platform
platform.platform()
'macOS-14.2.1-arm64-arm-64bit'
> 

(venv_tensor) sindong-ig@sindong-ig-ui-MacBookPro anaconda3 % python
Python 3.9.18 | packaged by conda-forge | (main, Dec 23 2023, 16:35:41)
[Clang 16.0.6 ] on darwin
Type "help", "copyright", "credits" or "license" for more information.

> import tensorflow as tf
tf.version
'2.15.0'
> 

> gpu = len(tf.config.list_physical_devices("GPU")) > 0
gpu
True
tf.config.list_physical_devices("GPU")
[PhysicalDevice(name='/physical_device:GPU:0', device_type='GPU')]
>