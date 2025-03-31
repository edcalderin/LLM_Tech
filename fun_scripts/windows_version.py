import wmi

def get_windows_version():
    data = wmi.WMI()
    for os_name in data.Win32_OperatingSystem():
        return os_name.Caption

if __name__ == "__main__":
    windows_version = get_windows_version()
    print(windows_version)