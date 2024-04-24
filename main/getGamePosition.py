import winreg


def get_program_install_location(program_name):
    uninstall_key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r"Software\Microsoft\Windows\CurrentVersion\Uninstall")
    for i in range(0, winreg.QueryInfoKey(uninstall_key)[0]):
        subkey_name = winreg.EnumKey(uninstall_key, i)
        subkey = winreg.OpenKey(uninstall_key, subkey_name)
        try:
            display_name = winreg.QueryValueEx(subkey, "DisplayName")[0]
            install_location = winreg.QueryValueEx(subkey, "InstallLocation")[0]
            if program_name in display_name:
                return install_location
        except FileNotFoundError:
            pass
        finally:
            subkey.Close()
    uninstall_key.Close()
    return None
