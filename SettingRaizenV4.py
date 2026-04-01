import os
import sys
import requests
import subprocess
import ctypes
import time
import socket
from colorama import Fore, Style, init

# เริ่มต้นระบบสี
init(autoreset=True)

# --- [ CONFIGURATION ] ---
FB_URL = "https://settingraizen-v3-default-rtdb.asia-southeast1.firebasedatabase.app/SettingRaizen%20V3"
FB_SECRET = "c4cqBrF4JwnYHk3EVKCUxQQybXvhvDJYFMUKhkzi"

def get_hwid():
    """ดึงรหัสเครื่อง (Unique ID)"""
    try:
        cmd = 'wmic csproduct get uuid'
        output = subprocess.check_output(cmd, shell=True).decode().split('\n')
        if len(output) > 1:
            return output[1].strip()
        return socket.gethostname()
    except:
        return socket.gethostname()

def run_cmd(cmd):
    """รันคำสั่ง System แบบไม่เปิดหน้าต่างเด้ง"""
    return subprocess.run(cmd, shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

def get_system_specs():
    """ดึงข้อมูล Hardware จริงเพื่อเขียนลงไฟล์ Settings"""
    specs = {"gpu": "NVIDIA GeForce GTX 1650", "width": "1920", "height": "1080", "refresh": "144"}
    try:
        # ดึงชื่อ GPU
        gpu_info = subprocess.check_output('wmic path win32_VideoController get name', shell=True).decode().split('\n')
        if len(gpu_info) > 1:
            specs["gpu"] = gpu_info[1].strip()
        
        # ดึง Resolution โดยใช้ ctypes (เร็วกว่า tkinter)
        user32 = ctypes.windll.user32
        specs["width"] = str(user32.GetSystemMetrics(0))
        specs["height"] = str(user32.GetSystemMetrics(1))
    except:
        pass
    return specs

def opt_fivem_settings():
    """ปรับแต่ง GTA V Settings ให้ Low ที่สุดเท่าที่จะเป็นไปได้"""
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
        with open(xml_path, 'w', encoding='utf-8') as f:
            f.write(xml_content)
        return True
    except:
        return False

def auto_god_optimize():
    os.system('cls')
    ctypes.windll.kernel32.SetConsoleTitleW("RAIZEN V4 [EXTREME] - DEPLOYING...")
    print(f"\n{Fore.MAGENTA}    [⚡] INITIALIZING GOD-TIER EXTREME OPTIMIZATION...")
    time.sleep(1)

    # 1. LATENCY & SYSTEM
    print(f"{Fore.CYAN}    [01/06] REDUCING SYSTEM LATENCY...", end="\r")
    system_tweaks = [
        'bcdedit /set disabledynamictick yes',
        'bcdedit /set useplatformclock no',
        'bcdedit /set tscsyncpolicy Enhanced',
        'reg add "HKLM\SYSTEM\CurrentControlSet\Control\PriorityControl" /v "Win32PrioritySeparation" /t REG_DWORD /d 38 /f',
        'reg add "HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Multimedia\SystemProfile" /v "NetworkThrottlingIndex" /t REG_DWORD /d 0xFFFFFFFF /f',
        'reg add "HKCU\Control Panel\Desktop" /v "MenuShowDelay" /t REG_SZ /d 0 /f',
        'reg add "HKCU\Control Panel\Keyboard" /v "KeyboardDelay" /t REG_SZ /d 0 /f',
        'reg add "HKCU\Control Panel\Keyboard" /v "KeyboardSpeed" /t REG_SZ /d 31 /f'
    ]
    for c in system_tweaks: run_cmd(c)
    print(f"{Fore.GREEN}    [01/06] LATENCY & CPU OPTIMIZATION SUCCESS!      ")

    # 2. NETWORK
    print(f"{Fore.CYAN}    [02/06] OVERCLOCKING NETWORK...", end="\r")
    net_tweaks = [
        'netsh int tcp set global autotuninglevel=disabled',
        'netsh int tcp set global rss=enabled',
        'netsh int tcp set global ecncapability=disabled',
        'reg add "HKLM\SYSTEM\CurrentControlSet\Services\Tcpip\Parameters\Interfaces" /v "TcpAckFrequency" /t REG_DWORD /d 1 /f',
        'reg add "HKLM\SYSTEM\CurrentControlSet\Services\Tcpip\Parameters\Interfaces" /v "TCPNoDelay" /t REG_DWORD /d 1 /f'
    ]
    for c in net_tweaks: run_cmd(c)
    print(f"{Fore.GREEN}    [02/06] NETWORK HYPER-DRIVE ENABLED!             ")

    # 3. XML SYNC
    print(f"{Fore.CYAN}    [03/06] SYNCING HARDWARE TO XML...", end="\r")
    opt_fivem_settings()
    print(f"{Fore.GREEN}    [03/06] XML SETTINGS SYNCED (ULTRA-LOW)!         ")

    # 4. DISK & TEMP CLEAN
    print(f"{Fore.CYAN}    [04/06] PURGING CACHE & JUNK...", end="\r")
    for p in [os.environ.get('TEMP'), 'C:\\Windows\\Temp', 'C:\\Windows\\Prefetch']:
        run_cmd(f'del /s /f /q "{p}\\*.*"')
    print(f"{Fore.GREEN}    [04/06] DISK & TEMP FILES WIPED CLEAN!           ")

    # 5. RAM PURGE
    print(f"{Fore.CYAN}    [05/06] PURGING RAM STANDBY LIST...", end="\r")
    ps_ram = "[System.GC]::Collect(); [System.GC]::WaitForPendingFinalizers();"
    subprocess.run(["powershell", "-Command", ps_ram], capture_output=True)
    print(f"{Fore.GREEN}    [05/06] MEMORY PURGED SUCCESSFULLY!              ")

    # 6. REFRESH EXPLORER
    print(f"{Fore.CYAN}    [06/06] REFRESHING EXPLORER...", end="\r")
    run_cmd('taskkill /f /im explorer.exe && start explorer.exe')
    print(f"{Fore.GREEN}    [06/06] ALL SYSTEMS ARE NOW GOD-TIER!            ")

    print(f"\n{Fore.MAGENTA}    " + "═"*55)
    print(f"{Fore.GREEN}    [✔] DEPLOYMENT COMPLETE: PC IS NOW UNLEASHED!")
    print(f"{Fore.YELLOW}    [!] แนะนำ: รีสตาร์ทคอมเพื่อความเสถียร")
    print(f"\n{Fore.WHITE}    PRESS ENTER TO EXIT...")
    input(); sys.exit()

def start_login():
    """ระบบ Login ที่เชื่อมต่อกับ Firebase"""
    while True:
        os.system('cls')
        ctypes.windll.kernel32.SetConsoleTitleW("RAIZEN V4 - SECURITY GATE")
        hwid = get_hwid()
        print(f"\n{Fore.MAGENTA}    R A I Z E N   V 4   //   G O D   M O D E")
        print(f"    {Fore.WHITE}─────────────────────────────────────────────")
        print(f"    {Fore.CYAN}ID: {Fore.WHITE}{hwid[:25]}...")
        user_key = input(f"\n    {Fore.YELLOW}▶ ENTER KEY : {Fore.WHITE}").strip()
        
        if not user_key: continue
        
        try:
            res = requests.get(f"{FB_URL}/Keys/{user_key}.json?auth={FB_SECRET}", timeout=10)
            data = res.json()
            if data:
                status = data.get('status')
                used_by = data.get('used_by')
                
                # ถ้าคีย์ยังไม่เคยใช้ หรือ ใช้โดยเครื่องเดิม
                if status == "unused" or used_by == hwid:
                    if status == "unused":
                        requests.patch(f"{FB_URL}/Keys/{user_key}.json?auth={FB_SECRET}", 
                                       json={"status": "active", "used_by": hwid})
                    return True
                
            print(f"{Fore.RED}    [!] INVALID OR USED KEY."); time.sleep(2)
        except Exception as e:
            print(f"{Fore.RED}    [!] CONNECTION ERROR."); time.sleep(2)

if __name__ == "__main__":
    # เช็ค Admin
    if not ctypes.windll.shell32.IsUserAnAdmin():
        print(f"{Fore.RED}PLEASE RUN AS ADMIN!"); time.sleep(2); sys.exit()
    
    # ตั้งค่า High Priority ให้ตัวโปรแกรม
    ctypes.windll.kernel32.SetPriorityClass(ctypes.windll.kernel32.GetCurrentProcess(), 0x00000080)
    
    if start_login():
        auto_god_optimize()
