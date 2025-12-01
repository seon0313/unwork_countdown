# unwork Countdown

- [🇺🇸 English](https://github.com/seon0313/unwork_countdown/blob/main/README.md)
- [🇰🇷 한국어](https://github.com/seon0313/unwork_countdown/blob/main/README_KOR.md)

A minimalist desktop countdown widget designed for the finish line. It stays out of your way but keeps the goal in sight.

## 📝 Overview

![preview](https://github.com/seon0313/unwork_countdown/blob/main/image/img1.png)

**unwork Countdown** is a lightweight desktop widget that counts down the time remaining until 18:00 (6:00 PM). It is designed to be unobtrusive yet accessible, featuring smart positioning and gesture-based controls to ensure it never hinders your workflow.

## ✨ Key Features

-   **Target Time Countdown**: Displays a live countdown timer targeting your scheduled finish time (Default: 18:00).
-   **Fixed Positioning**: Anchored firmly at the bottom-right corner of your screen, sitting neatly just above the taskbar.

![smart_evasion](https://github.com/seon0313/unwork_countdown/blob/main/image/img2.png)
-   **Smart Evasion (Dodge Mode)**: Need to click something behind the timer? Just hover your mouse over it. The widget automatically moves to the right to reveal any underlying UI elements.

![gesture_exit](https://github.com/seon0313/unwork_countdown/blob/main/image/img3.png)
-   **Gesture Exit**: To close the program, simply move your mouse cursor to the **top-left corner** of the screen and hold it there. The app will countdown and terminate automatically.

## ⚙️ Configuration

You can fully customize the widget by editing the `setting.json` file in the root directory.

```json
{
    "target-time": "18:00",
    "background-color": {"r": 34, "g": 34, "b": 34},
    "font-color": "#fff",
    "shutdown-timer": 2.0
}
```


- **`target-time`**: Sets the countdown goal (24-hour format). The widget displays the time remaining from now until this target.
- **`background-color`**: Defines the widget's background color using RGB values.
- **`font-color`**: Defines the text color using Hex codes.
- **`shutdown-timer`**: The duration (in seconds) you must hold the mouse in the top-left corner to trigger the exit.

**🔥 Live Updates**: Changes made to `setting.json` are applied **instantly**. You do not need to restart the application to see your changes.

## 🚀 Getting Started

### Prerequisites

-   Python 3.4 or higher
-   **Standard Libraries Only**: No external packages or `pip install` required.

### Installation & Run

1.  Clone the repository:
    ```
    git clone https://github.com/seon0313/unwork_countdown.git
    cd unwork_countdown
    ```

2.  Run the application:
    ```
    python main.py
    ```

## 🎮 Controls

| Action | Result |
| :--- | :--- |
| **Hover** (Bottom-Right) | Widget moves right to unblock the view. |
| **Corner Hold** (Top-Left) | Triggers a countdown to exit the app (Duration configurable in settings). |
