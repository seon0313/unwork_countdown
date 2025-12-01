from datetime import datetime
import time
import sys
import os
from tkinter import *
from pathlib import Path
import json

BASE_DIR = Path(__file__).resolve().parent

setting_path = BASE_DIR / 'setting.json'
if setting_path.exists():
	setting = json.loads(setting_path.read_text(encoding='utf-8'))
else:
	setting = None

current_mtime = setting_path.stat().st_mtime

target_time = setting.get('target-time', '18:00').split(':')
bg_color = setting.get('background-color', {'r': 34, 'g': 34, 'b': 34})
bg_color_hex = f"#{bg_color['r']:02x}{bg_color['g']:02x}{bg_color['b']:02x}"
font_color = setting.get('font-color', '#ffffff')
shutdown_timer = setting.get('shutdown-timer', 2.0)

root = Tk()
root.overrideredirect(True)
root.wm_attributes('-topmost', True)
alpha = 0.8
root.wm_attributes('-alpha', alpha)

if sys.platform == 'win32':
	try:
		import ctypes
		from ctypes import wintypes

		rect = wintypes.RECT()
		# SPI_GETWORKAREA = 48
		ctypes.windll.user32.SystemParametersInfoW(48, 0, ctypes.byref(rect), 0)

		# work area is the usable screen area (excludes taskbar)
		work_left, work_top, work_right, work_bottom = rect.left, rect.top, rect.right, rect.bottom

		x = work_right - 150
		y = work_bottom - 50
	except Exception:
		# fallback to full screen size if anything goes wrong
		screen_w = root.winfo_screenwidth()
		screen_h = root.winfo_screenheight()
		x = screen_w - 150
		y = screen_h - 50
else:
	screen_w = root.winfo_screenwidth()
	screen_h = root.winfo_screenheight()
	x = screen_w - 150
	y = screen_h - 50

root.geometry(f"{150}x{50}+{x}+{y}")

label = Label(root, text='ㅁ', font=(None, 18), bg=bg_color_hex, fg=font_color)
label.place(relwidth=1, relheight=1)

last_pointer = {'rel': (None, None), 'abs': (None, None), 'over': False, 'ts': None}

def _update_pointer_from_event(event=None):
	try:
		abs_x = root.winfo_pointerx()
		abs_y = root.winfo_pointery()
	except Exception:
		abs_x, abs_y = None, None

	rel_x = rel_y = None
	if event is not None:
		try:
			rel_x, rel_y = int(event.x), int(event.y)
		except Exception:
			rel_x, rel_y = None, None
	else:
		if abs_x is not None and abs_y is not None:
			try:
				rel_x = abs_x - root.winfo_rootx()
				rel_y = abs_y - root.winfo_rooty()
			except Exception:
				rel_x, rel_y = None, None

	import time as _time
	last_pointer['rel'] = (rel_x, rel_y)
	last_pointer['abs'] = (abs_x, abs_y)
	last_pointer['ts'] = _time.time()


def get_pointer_position(force_read=False):
	if force_read:
		_update_pointer_from_event(None)
	rel = last_pointer['rel']
	abspos = last_pointer['abs']
	return (rel[0], rel[1], abspos[0], abspos[1], last_pointer['over'], last_pointer['ts'])
endtime = 0
def timeSet():
	global endtime
	_update_pointer_from_event()
	ax, ay = last_pointer['abs']
	root.geometry(f"{150}x{50}+{max(ax+15, x) if ay >= y and ay < y+50 else x}+{y}")
	
	_y,m,d = time.strftime('%Y-%m-%d').split('-')
	target_date = datetime(int(_y), int(m), int(d), int(target_time[0]), int(target_time[1]), 0)
	label.config(text=f'{target_date-datetime.now()}'.split('.')[0])

	base_rgb = tuple(bg_color.values())
	red_rgb = (255, 0, 0)

	
	if not ax and not ay:
		if endtime == 0:
			endtime = time.time()
		elif time.time()-endtime >= shutdown_timer:
			root.destroy()
		else:
			elapsed = time.time() - endtime
			label.config(text="%.1f" % (elapsed))
			clamped = max(0.0, min(elapsed, shutdown_timer))
			t = clamped / shutdown_timer
			r = int(base_rgb[0] + (red_rgb[0] - base_rgb[0]) * t)
			g = int(base_rgb[1] + (red_rgb[1] - base_rgb[1]) * t)
			b = int(base_rgb[2] + (red_rgb[2] - base_rgb[2]) * t)
			color_hex = f"#{r:02x}{g:02x}{b:02x}"
			label.config(bg=color_hex)
			try:
				root.configure(bg=color_hex)
			except Exception:
				pass
	else:
		endtime = 0
		base_hex = f"#{base_rgb[0]:02x}{base_rgb[1]:02x}{base_rgb[2]:02x}"
		try:
			label.config(bg=base_hex)
			root.configure(bg=base_hex)
		except Exception:
			pass
			
	root.after(50, timeSet)

def checkSettingJsonLoop():
	if current_mtime != setting_path.stat().st_mtime:
		os.execl(sys.executable, sys.executable, *sys.argv)
	root.after(1000, checkSettingJsonLoop)


root.bind('<Escape>', lambda e: root.destroy())

def increase_alpha(event=None):
	global alpha
	alpha = min(alpha + 0.1, 1.0)
	root.wm_attributes('-alpha', alpha)


def decrease_alpha(event=None):
	global alpha
	alpha = max(alpha - 0.1, 0.1)
	root.wm_attributes('-alpha', alpha)


root.bind('<Up>', increase_alpha)
root.bind('<Down>', decrease_alpha)

try:
	root.update_idletasks()
	hwnd = root.winfo_id()
except Exception:
	enabled = False
root.after(1, timeSet)
root.after(1, checkSettingJsonLoop)
root.mainloop()
root.quit()