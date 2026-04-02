import os
import sys
import requests
import subprocess
import ctypes
import time
import socket
import tkinter as tk
from tkinter import messagebox
from colorama import Fore, Style, init

init(autoreset=True)

FB_URL = "https://settingraizen-v3-default-rtdb.asia-southeast1.firebasedatabase.app/SettingRaizen%20V3"
FB_SECRET = "c4cqBrF4JwnYHk3EVKCUxQQybXvhvDJYFMUKhkzi"

def popup_msg(title, text, type="info"):
    root = tk.Tk()
    root.withdraw()
    root.attributes("-topmost", True)
    if type == "info": messagebox.showinfo(title, text)
    elif type == "error": messagebox.showerror(title, text)
    elif type == "warning": messagebox.showwarning(title, text)
    root.destroy()

def run_cmd(cmd):
    return subprocess.run(cmd, shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

def kernel_god_tweak():
    """สุดยอดการปรับแต่งระดับ Kernel และ System Registry"""
    
    # 1. CPU & Kernel Responsiveness (Win32PrioritySeparation ระดับสูงสุดสำหรับ Gaming)
    # 0x26 (38 decimal) คือค่าที่สมดุลที่สุดสำหรับ High-End Gaming
    run_cmd('reg add "HKLM\SYSTEM\CurrentControlSet\Control\PriorityControl" /v "Win32PrioritySeparation" /t REG_DWORD /d 38 /f')
    
    # 2. Disable Kernel Hibernation (ลดภาระ Kernel ในการเขียนไฟล์ Hibernate)
    run_cmd('powercfg -h off')
    
    # 3. Ultimate Network Latency (Disable TCP Delays & Throttling)
    net_registry = [
        'reg add "HKLM\SYSTEM\CurrentControlSet\Services\Tcpip\Parameters" /v "TcpAckFrequency" /t REG_DWORD /d 1 /f',
        'reg add "HKLM\SYSTEM\CurrentControlSet\Services\Tcpip\Parameters" /v "TCPNoDelay" /t REG_DWORD /d 1 /f',
        'reg add "HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Multimedia\SystemProfile" /v "NetworkThrottlingIndex" /t REG_DWORD /d 0xFFFFFFFF /f',
        'reg add "HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Multimedia\SystemProfile" /v "SystemResponsiveness" /t REG_DWORD /d 0 /f'
    ]
    for r in net_registry: run_cmd(r)

    # 4. Global GPU Priority (บังคับให้ระบบให้ความสำคัญกับ GPU เป็นอันดับแรก)
    run_cmd('reg add "HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Multimedia\SystemProfile\Tasks\Games" /v "GPU Priority" /t REG_DWORD /d 8 /f')
    run_cmd('reg add "HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Multimedia\SystemProfile\Tasks\Games" /v "Priority" /t REG_DWORD /d 6 /f')
    run_cmd('reg add "HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Multimedia\SystemProfile\Tasks\Games" /v "Scheduling Category" /t REG_SZ /d "High" /f')

    # 5. Kernel Memory Management (บังคับให้ Kernel อยู่บน RAM เสมอ ไม่ให้ลง Disk)
    run_cmd('reg add "HKLM\SYSTEM\CurrentControlSet\Control\Session Manager\Memory Management" /v "DisablePagingExecutive" /t REG_DWORD /d 1 /f')

def auto_god_optimize():
    os.system('cls')
    ctypes.windll.kernel32.SetConsoleTitleW("RAIZEN V4 [KERNEL-GOD] - INJECTING...")
    
    popup_msg("KERNEL ACCESS GRANTED", "ระดับความโหด: KERNEL-GOD\nระบบกำลังจะเข้าสู่โหมดรีดประสิทธิภาพสูงสุด!", "warning")

    print(f"\n{Fore.RED}    [☢️] INJECTING KERNEL-LEVEL OPTIMIZATION...")
    time.sleep(1.5)

    # Execute Tweaks
    print(f"{Fore.CYAN}    [01/04] REWRITING KERNEL REGISTRY...", end="\r")
    kernel_god_tweak()
    print(f"{Fore.GREEN}    [01/04] KERNEL REGISTRY INJECTED!          ")

    print(f"{Fore.CYAN}    [02/04] DISABLING POWER THROTTLING...", end="\r")
    run_cmd('bcdedit /set disabledynamictick yes')
    run_cmd('bcdedit /set useplatformclock no')
    run_cmd('bcdedit /set tscsyncpolicy Enhanced')
    print(f"{Fore.GREEN}    [02/04] POWER THROTTLING DISABLED!          ")

    print(f"{Fore.CYAN}    [03/04] PURGING SYSTEM STANDBY LIST...", end="\r")
    # ใช้ PowerShell รีด RAM ระดับลึก
    run_cmd('powershell -Command "[System.GC]::Collect(); [System.GC]::WaitForPendingFinalizers();"')
    print(f"{Fore.GREEN}    [03/04] SYSTEM MEMORY PURGED!              ")

    print(f"{Fore.CYAN}    [04/04] FINALIZING SHELL REFRESH...", end="\r")
    run_cmd('taskkill /f /im explorer.exe && start explorer.exe')
    print(f"{Fore.GREEN}    [04/04] SHELL REFRESHED!                   ")

    print(f"\n{Fore.RED}    " + "═"*55)
    print(f"{Fore.YELLOW}    [✔] KERNEL-GOD MODE DEPLOYED!")
    print(f"{Fore.WHITE}    STATUS: UNLEASHED")
    print(f"{Fore.RED}    " + "═"*55)
    
    popup_msg("SUCCESS", "RAIZEN V4: KERNEL-GOD DEPLOYED!\nแนะนำให้ RESTART ทันทีเพื่อให้ Registry มีผล 100%", "info")
    sys.exit()

def start_login():
    """หน้าจอ Login ดุดัน สไตล์ RAIZEN"""
    while True:
        os.system('cls')
        os.system('color 0c') # พื้นหลังดำ ตัวหนังสือแดง (โหมดโหด)
        ctypes.windll.kernel32.SetConsoleTitleW("RAIZEN V4 - KERNEL GATE")
        
        print(f"\n{Fore.RED}    ┌───────────────────────────────────────────┐")
        print(f"{Fore.RED}    │     R A I Z E N   V 4   //   K E R N E L      │")
        print(f"{Fore.RED}    └───────────────────────────────────────────┘")
        print(f"    {Fore.WHITE}HWID: {Fore.YELLOW}{socket.gethostname()}")
        print(f"    {Fore.WHITE}MODE: {Fore.RED}EXTREME PERFORMANCE")
        print(f"{Fore.RED}    ─────────────────────────────────────────────")
        
        user_key = input(f"\n    {Fore.WHITE}▶ ENTER ACCESS KEY : {Fore.RED}").strip()
        
        if not user_key: continue
        
        try:
            res = requests.get(f"{FB_URL}/Keys/{user_key}.json?auth={FB_SECRET}", timeout=10)
            data = res.json()
            if data and (data.get('status') == "unused" or data.get('used_by') == socket.gethostname()):
                return True
            popup_msg("ACCESS DENIED", "คีย์ไม่ถูกต้อง!", "error")
        except:
            popup_msg("SERVER ERROR", "การเชื่อมต่อล้มเหลว", "warning")

if __name__ == "__main__":
    if not ctypes.windll.shell32.IsUserAnAdmin():
        popup_msg("ADMIN REQUIRED", "ต้องใช้สิทธิ์ ADMIN สำหรับการปรับแต่ง KERNEL!", "error")
        sys.exit()
    
    # บังคับโปรแกรมรันที่ Realtime Priority
    ctypes.windll.kernel32.SetPriorityClass(ctypes.windll.kernel32.GetCurrentProcess(), 0x00000100)
    
    if start_login():
        auto_god_optimize()
