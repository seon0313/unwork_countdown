# unwork Countdown

- [🇺🇸 English](https://github.com/seon0313/unwork_countdown/blob/main/README.md)
- [🇰🇷 한국어](https://github.com/seon0313/unwork_countdown/blob/main/README_KOR.md)

정시 퇴근을 위한 미니멀 데스크톱 카운트다운 위젯입니다.
작업에 방해되지 않으면서도 목표 시간까지 남은 시간을 직관적으로 보여줍니다.

## 📝 개요

![preview](https://github.com/seon0313/unwork_countdown/blob/main/image/img1.png)

**unwork Countdown**은 오후 6시(18:00)까지 남은 시간을 카운트다운하는 가벼운 데스크톱 위젯입니다. 작업표시줄 위, 화면 우측 하단에 고정되어 평소에는 거슬리지 않지만, 필요할 때 언제든 퇴근까지 남은 시간을 확인할 수 있습니다. 스마트 회피 기능과 제스처 종료 기능을 탑재하여 사용자의 워크플로우를 방해하지 않도록 설계되었습니다.

## ✨ 주요 기능

-   **목표 시간 카운트다운**: 설정된 퇴근 시간(기본값: 18:00)까지 남은 시간을 실시간으로 표시합니다.
-   **고정 위치**: 화면 우측 하단(작업표시줄 바로 위)에 항상 단단히 고정되어 시선을 분산시키지 않습니다.

![smart_evasion](https://github.com/seon0313/unwork_countdown/blob/main/image/img2.png)
-   **스마트 회피 (Dodge Mode)**: 위젯 뒤에 있는 버튼을 눌러야 하나요? 마우스를 올리기만 하면 위젯이 알아서 오른쪽으로 비켜나 UI를 가리지 않습니다.

![gesture_exit](https://github.com/seon0313/unwork_countdown/blob/main/image/img3.png)
-   **제스처 종료**: 프로그램을 끄고 싶을 땐, 마우스 포인터를 화면 **왼쪽 맨 위 모서리**로 가져가 유지하세요. 앱이 자동으로 카운트다운 후 종료됩니다.

## ⚙️ 환경 설정

루트 디렉토리에 있는 `setting.json` 파일을 편집하여 위젯을 완전히 커스터마이징할 수 있습니다.

```json
{
    "target-time": "18:00",
    "background-color": {"r": 34, "g": 34, "b": 34},
    "font-color": "#fff",
    "shutdown-timer": 2.0
}
```


- **`target-time`**: 카운트다운 목표 시간을 설정합니다 (24시간 형식). 현재 시간부터 이 목표 시간까지 남은 시간을 표시합니다.
- **`background-color`**: RGB 값을 사용하여 위젯의 배경색을 정의합니다.
- **`font-color`**: 헥스(Hex) 코드를 사용하여 텍스트 색상을 정의합니다.
- **`shutdown-timer`**: 종료를 트리거하기 위해 마우스를 왼쪽 상단 모서리에 유지해야 하는 시간(초)입니다.

**🔥 실시간 업데이트**: `setting.json`의 변경 사항은 **즉시** 반영됩니다. 변경 내용을 확인하기 위해 애플리케이션을 재시작할 필요가 없습니다.

## 🚀 시작하기

### 사전 요구 사항

-   Python 3.4 이상
-   **표준 라이브러리 전용**: 외부 패키지나 `pip install`이 필요 없습니다.

### 설치 및 실행

1.  저장소를 복제(clone)합니다:
    ```
    git clone https://github.com/seon0313/unwork_countdown.git
    cd unwork_countdown
    ```

2.  애플리케이션을 실행합니다:
    ```
    python main.py
    ```

## 🎮 조작 방법

| 동작 | 결과 |
| :--- | :--- |
| **마우스 오버** (우측 하단) | 위젯이 시야를 가리지 않도록 오른쪽으로 이동합니다. |
| **모서리 대기** (좌측 상단) | 앱 종료 카운트다운을 시작합니다 (유지 시간은 설정에서 변경 가능). |
