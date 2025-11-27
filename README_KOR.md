# unwork Countdown

- [🇺🇸 English](https://github.com/seon0313/unwork_countdown/blob/main/README.md)
- [🇰🇷 한국어](https://github.com/seon0313/unwork_countdown/blob/main/README_KOR.md)

6시 정시 퇴근을 위한 미니멀 데스크톱 카운트다운 위젯입니다.
작업에 방해되지 않으면서도 목표 시간까지 남은 시간을 직관적으로 보여줍니다.

## 📝 개요

![preview](https://github.com/seon0313/unwork_countdown/blob/main/image/img1)

**unwork Countdown**는 오후 6시(18:00)까지 남은 시간을 카운트다운하는 가벼운 데스크톱 위젯입니다. 작업표시줄 위, 화면 우측 하단에 고정되어 평소에는 거슬리지 않지만, 필요할 때 언제든 퇴근까지 남은 시간을 확인할 수 있습니다. 스마트 회피 기능과 제스처 종료 기능을 탑재하여 사용자의 워크플로우를 방해하지 않도록 설계되었습니다.

## ✨ 주요 기능

-   **퇴근 카운트다운**: 18:00 (오후 6시)를 기준으로 실시간 카운트다운을 표시합니다.
-   **고정 위치**: 화면 우측 하단(작업표시줄 바로 위)에 항상 위치하여 시선을 분산시키지 않습니다.

![smart_evasion](https://github.com/seon0313/unwork_countdown/blob/image/main/img2)
-   **스마트 회피 (Dodge Mode)**: 위젯 뒤에 있는 버튼을 눌러야 하나요? 마우스를 올리기만 하면 위젯이 알아서 오른쪽으로 비켜나 UI를 가리지 않습니다.

![gesture_exit](https://github.com/seon0313/unwork_countdown/blob/image/main/img3)
-   **제스처 종료**: 프로그램을 끄고 싶을 땐, 마우스 포인터를 화면 **왼쪽 맨 위 모서리**로 가져가 **2초간 유지**하세요. 별도의 종료 버튼 없이 직관적인 제스처로 깔끔하게 종료됩니다.

## 🚀 시작하기

이 프로그램은 Python 기본 내장 라이브러리만 사용하여, 별도의 패키지 설치 없이 바로 실행 가능합니다.

### 사전 요구 사항

-   Python 3.x 이상

### 설치 및 실행

1.  저장소를 clone합니다.
    ```
    git clone https://github.com/seon0313/unwork_countdown.git
    cd unwork_countdown
    ```

2.  프로그램을 실행합니다. (별도 설치 과정 없음)
    ```
    python main.py
    ```

## 🎮 조작 방법

| 동작 | 기능 설명 |
| :--- | :--- |
| **마우스 오버** (우측 하단) | 위젯이 오른쪽으로 이동하여 뒤쪽 화면을 보여줍니다. |
| **모서리 대기** (좌측 상단) | 마우스를 2초간 유지하면 프로그램이 카운트다운 후 종료됩니다. |
