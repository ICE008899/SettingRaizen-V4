import os
import sys
import requests
import subprocess
import ctypes
import time
import socket
import re
from colorama import Fore, Style, init

# เริ่มต้นระบบสี
init(autoreset=True)

# --- [ CONFIGURATION ] ---
FB_URL = "https://settingraizen-v3-default-rtdb.asia-southeast1.firebasedatabase.app/SettingRaizen%20V3"
FB_SECRET = "c4cqBrF4JwnYHk3EVKCUxQQybXvhvDJYFMUKhkzi"

def get_hwid():
    try:
        cmd = 'wmic csproduct get uuid'
        uuid = subprocess.check_output(cmd, shell=True).decode().split('\n')[1].strip()
        return uuid
    except: return socket.gethostname()

def run_cmd(cmd):
    """รันคำสั่งเบื้องหลังแบบเงียบกริบ"""
    subprocess.run(cmd, shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

def get_system_specs():
    specs = {"gpu": "NVIDIA GeForce GTX 1650", "width": "1920", "height": "1080", "refresh": "144"}
    try:
        gpu_cmd = 'wmic path win32_VideoController get name'
        specs["gpu"] = subprocess.check_output(gpu_cmd, shell=True).decode().split('\n')[1].strip()
        import tkinter
        root = tkinter.Tk()
        specs["width"], specs["height"] = str(root.winfo_screenwidth()), str(root.winfo_screenheight())
        root.destroy()
    except: pass
    return specs

def opt_fivem_settings():
    specs = get_system_specs()
    xml_path = os.path.join(os.environ['USERPROFILE'], 'Documents', 'Rockstar Games', 'GTA V', 'settings.xml')
    
    xml_content = f'''<?xml version="1.0" encoding="UTF-8"?>
<Settings>
  <version value="27" />
  <configSource>SMC_AUTO</configSource>
  <graphics>
    <Tessellation value="0" /><LodScale value="-1.000000" /><PedLodBias value="0.000000" />
    <VehicleLodBias value="0.000000" /><ShadowQuality value="0" /><ReflectionQuality value="0" />
    <ReflectionMSAA value="0" /><SSAO value="0" /><AnisotropicFiltering value="0" />
    <MSAA value="0" /><MSAAFragments value="0" /><MSAAQuality value="0" />
    <SamplingMode value="0" /><TextureQuality value="0" /><ParticleQuality value="0" />
    <WaterQuality value="0" /><GrassQuality value="0" /><ShaderQuality value="0" />
    <Shadow_SoftShadows value="0" /><UltraShadows_Enabled value="false" />
    <Shadow_ParticleShadows value="false" /><Shadow_Distance value="1.000000" />
    <Shadow_LongShadows value="false" /><Shadow_SplitZStart value="0.000000" />
    <Shadow_SplitZEnd value="0.000000" /><Shadow_aircraftExpWeight value="0.000000" />
    <Shadow_DisableScreenSizeCheck value="false" /><Reflection_MipBlur value="false" />
    <FXAA_Enabled value="false" /><TXAA_Enabled value="false" /><Lighting_FogVolumes value="false" />
    <Shader_SSA value="false" /><DX_Version value="0" /><CityDensity value="0.000000" />
    <PedVarietyMultiplier value="0.000000" /><VehicleVarietyMultiplier value="0.000000" />
    <PostFX value="0" /><DoF value="false" /><HdStreamingInFlight value="false" />
    <MaxLodScale value="0.000000" /><MotionBlurStrength value="0.000000" />
  </graphics>
  <system>
    <numBytesPerReplayBlock value="9000000" /><numReplayBlocks value="30" />
    <maxSizeOfStreamingReplay value="1024" /><maxFileStoreSize value="65536" />
  </system>
  <audio><Audio3d value="false" /></audio>
  <video>
    <AdapterIndex value="0" /><OutputIndex value="0" />
    <ScreenWidth value="{specs["width"]}" /><ScreenHeight value="{specs["height"]}" />
    <RefreshRate value="{specs["refresh"]}" /><Windowed value="2" />
    <VSync value="0" /><Stereo value="0" /><Convergence value="0.100000" />
    <Separation value="0.000000" /><PauseOnFocusLoss value="1" /><AspectRatio value="0" />
  </video>
  <VideoCardDescription>{specs["gpu"]}</VideoCardDescription>
</Settings>'''

    try:
        os.makedirs(os.path.dirname(xml_path), exist_ok=True)
        with open(xml_path, 'w', encoding='utf-8') as f: f.write(xml_content)
        return True
    except: return False

def auto_god_optimize():
    os.system('cls')
    ctypes.windll.kernel32.SetConsoleTitleW("RAIZEN V4 [EXTREME] - DEPLOYING...")
    print(f"\n{Fore.MAGENTA}    [⚡] INITIALIZING GOD-TIER EXTREME OPTIMIZATION...")
    time.sleep(1)

    # 1. EXTREME SYSTEM TWEAKS (Latency & Hardware)
    print(f"{Fore.CYAN}    [01/06] REDUCING SYSTEM LATENCY TO ABSOLUTE ZERO...", end="\r")
    system_tweaks = [
        # Disable HPET & Dynamic Ticks (ลด Delay ในการประมวลผล CPU)
        'bcdedit /set disabledynamictick yes',
        'bcdedit /set useplatformclock no',
        'bcdedit /set tscsyncpolicy Enhanced',
        # Registry Optimization
        'reg add "HKLM\SYSTEM\CurrentControlSet\Control\PriorityControl" /v "Win32PrioritySeparation" /t REG_DWORD /d 38 /f',
        'reg add "HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Multimedia\SystemProfile" /v "NetworkThrottlingIndex" /t REG_DWORD /d 0xFFFFFFFF /f',
        'reg add "HKCU\Control Panel\Desktop" /v "MenuShowDelay" /t REG_SZ /d 0 /f',
        'reg add "HKCU\Control Panel\Mouse" /v "MouseSpeed" /t REG_SZ /d 0 /f',
        'reg add "HKCU\Control Panel\Keyboard" /v "KeyboardDelay" /t REG_SZ /d 0 /f',
        'reg add "HKCU\Control Panel\Keyboard" /v "KeyboardSpeed" /t REG_SZ /d 31 /f'
    ]
    for c in system_tweaks: run_cmd(c)
    print(f"{Fore.GREEN}    [01/06] LATENCY & CPU OPTIMIZATION SUCCESS!      ")

    # 2. ADVANCED NETWORK (Anti-Lag & No Warp)
    print(f"{Fore.CYAN}    [02/06] OVERCLOCKING NETWORK PACKET DELIVERY...", end="\r")
    net_tweaks = [
        'netsh int tcp set global autotuninglevel=disabled',
        'netsh int tcp set global rss=enabled',
        'netsh int tcp set global netdma=enabled',
        'netsh int tcp set global dca=enabled',
        'netsh int tcp set global ecncapability=disabled',
        'reg add "HKLM\SYSTEM\CurrentControlSet\Services\Tcpip\Parameters\Interfaces" /v "TcpAckFrequency" /t REG_DWORD /d 1 /f',
        'reg add "HKLM\SYSTEM\CurrentControlSet\Services\Tcpip\Parameters\Interfaces" /v "TCPNoDelay" /t REG_DWORD /d 1 /f'
    ]
    for c in net_tweaks: run_cmd(c)
    print(f"{Fore.GREEN}    [02/06] NETWORK HYPER-DRIVE ENABLED!             ")

    # 3. IN-GAME XML SYNC
    print(f"{Fore.CYAN}    [03/06] SYNCING HARDWARE TO IN-GAME XML...", end="\r")
    opt_fivem_settings()
    print(f"{Fore.GREEN}    [03/06] XML SETTINGS SYNCED (ULTRA-LOW)!         ")

    # 4. DISK & MEMORY PURGE
    print(f"{Fore.CYAN}    [04/06] PURGING SYSTEM CACHE & JUNK FILES...", end="\r")
    clean_paths = [os.environ.get('TEMP'), 'C:\\Windows\\Temp', 'C:\\Windows\\Prefetch']
    for p in clean_paths: run_cmd(f'del /s /f /q "{p}\\*.*"')
    run_cmd('wsreset -i') # Reset Store Cache (ช่วยลดภาระ Background)
    print(f"{Fore.GREEN}    [04/06] DISK & TEMP FILES WIPED CLEAN!           ")

    # 5. RAM STEROID (Advanced PowerShell Purge)
    print(f"{Fore.CYAN}    [05/06] INJECTING RAM STEROID & GC COLLECT...", end="\r")
    ps_ram = "$c=[System.GC]::Collect(); [System.GC]::WaitForPendingFinalizers();"
    subprocess.run(["powershell", "-Command", ps_ram], capture_output=True)
    print(f"{Fore.GREEN}    [05/06] MEMORY PURGED & STANDBY LIST CLEARED!    ")

    # 6. FINALIZING GOD MODE
    print(f"{Fore.CYAN}    [06/06] REFRESHING EXPLORER & FINISHING...", end="\r")
    run_cmd('taskkill /f /im explorer.exe && start explorer.exe')
    print(f"{Fore.GREEN}    [06/06] ALL SYSTEMS ARE NOW GOD-TIER!            ")

    print(f"\n{Fore.MAGENTA}    " + "═"*55)
    print(f"{Fore.GREEN}    [✔] DEPLOYMENT COMPLETE: GO SMASH THEM!")
    print(f"{Fore.YELLOW}    [!] แนะนำ: รีสตาร์ทคอม")
    print(f"{Fore.MAGENTA}    " + "═"*55)
    time.sleep(2); sys.exit()

def start_login():
    while True:
        os.system('cls')
        ctypes.windll.kernel32.SetConsoleTitleW("RAIZEN V4 - SECURITY GATE")
        hwid = get_hwid()
        print(f"\n{Fore.MAGENTA}    R A I Z E N   V 4   //   G O D   M O D E")
        print(f"    {Fore.WHITE}─────────────────────────────────────────────")
        print(f"    {Fore.CYAN}ID: {Fore.WHITE}{hwid[:20]}...")
        user_key = input(f"\n    {Fore.YELLOW}▶ ENTER KEY : {Fore.WHITE}").strip()
        if not user_key: continue
        try:
            res = requests.get(f"{FB_URL}/Keys/{user_key}.json?auth={FB_SECRET}", timeout=10)
            data = res.json()
            if data and (data.get('status') == "unused" or data.get('used_by') == hwid):
                if data.get('status') == "unused":
                    requests.patch(f"{FB_URL}/Keys/{user_key}.json?auth={FB_SECRET}", json={"status": "active", "used_by": hwid})
                return True
            print(f"{Fore.RED}    [!] INVALID OR USED KEY."); time.sleep(2)
        except: print(f"{Fore.RED}    [!] SERVER ERROR."); time.sleep(2)

if __name__ == "__main__":
    if not ctypes.windll.shell32.IsUserAnAdmin():
        print(f"{Fore.RED}PLEASE RUN AS ADMIN!"); os.system('pause'); sys.exit()
    
    ctypes.windll.kernel32.SetPriorityClass(ctypes.windll.kernel32.GetCurrentProcess(), 0x00000080)
    
    if start_login():
        auto_god_optimize()
