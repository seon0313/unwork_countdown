# GoHome Timer 🏠

A minimalist desktop countdown widget designed for the 6 PM finish line. It stays out of your way but keeps the goal in sight.

## 📝 Overview

**GoHome Timer** is a lightweight desktop widget that counts down the time remaining until 18:00 (6:00 PM). It is designed to be unobtrusive yet accessible, featuring smart positioning and gesture-based controls to ensure it never hinders your workflow.

## ✨ Key Features

-   **Target Time Countdown**: Displays a live countdown timer targeting 18:00 (6 PM).
-   **Fixed Positioning**: Anchored firmly at the bottom-right corner of your screen, sitting neatly just above the taskbar.
-   **Smart Evasion (Dodge Mode)**: Need to click something behind the timer? Just hover your mouse over it. The widget automatically moves to the right to reveal any underlying UI elements.
-   **Gesture Exit**: To close the program, simply move your mouse cursor to the **top-left corner** of the screen and hold it there for **2 seconds**. The app will countdown and terminate automatically.

## 🚀 Getting Started

### Prerequisites

-   Python 3.x
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
| **Corner Hold** (Top-Left) | Triggers a 2-second countdown to exit the app. |
