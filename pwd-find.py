```python
import subprocess

def get_wifi_profiles():
    profiles_data = subprocess.check_output('netsh wlan show profiles', shell=True, text=True)
    profiles = []
    for line in profiles_data.split('\n'):
        if "All User Profile" in line:
            profile = line.split(":")[1].strip()
            profiles.append(profile)
    return profiles

def get_password(profile):
    try:
        result = subprocess.check_output(f'netsh wlan show profile name="{profile}" key=clear', shell=True, text=True)
        for line in result.split('\n'):
            if "Key Content" in line:
                password = line.split(":")[1].strip()
                return password
        return None
    except:
        return None

if _name_ == "_main_":
    profiles = get_wifi_profiles()
    for profile in profiles:
        pwd = get_password(profile)
        print(f"SSID: {profile}  -->  Password: {pwd if pwd else 'No password found or open network'}")
```
