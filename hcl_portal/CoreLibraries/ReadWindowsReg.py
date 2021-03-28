'''
System imports
'''
import platform
if platform.system() == "Windows":
    import winreg

'''
Manipulates the windows registry for AppliedDPI
This is mainly required for windows explorer and edge browsers
'''
def getDisplayScale():
    if not platform.system()== "Windows":
        return 100
    # Open the key and return the handle object.
    hKey = winreg.OpenKey(winreg.HKEY_CURRENT_USER,"Control Panel\\Desktop\\WindowMetrics")

    # Read the value.
    result = winreg.QueryValueEx(hKey, "AppliedDPI")

    # Close the handle object.
    winreg.CloseKey(hKey)

    # value from the resulting tuple (value, type_as_int).
    if result[0] == 96:
        Scale = 100
    elif result[0] == 120:
        Scale = 125
    elif result[0] == 144:
        Scale = 150
    elif result[0] == 192:
        Scale = 20
    else:
        assert False , "Not able to get the display parameter"
    return Scale

