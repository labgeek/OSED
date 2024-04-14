$share_path = "\\tsclient\mona-share\"
$install_dir = "C:\Users\Offsec\Desktop\install-mona"

echo "[+] creating installation directory: $install_dir"
mkdir $install_dir

# install old c++ runtime
echo "[+] installing old c++ runtime"
copy "$share_path\vcredist_x86.exe" $install_dir
cd $install_dir
.\vcredist_x86.exe 
start-sleep 60

echo "[+] backing up old pykd files"
move "C:\Program Files\Windows Kits\10\Debuggers\x86\winext\pykd.pyd" "C:\Program Files\Windows Kits\10\Debuggers\x86\winext\pykd.pyd.bak"
move "C:\Program Files\Windows Kits\10\Debuggers\x86\winext\pykd.dll" "C:\Program Files\Windows Kits\10\Debuggers\x86\winext\pykd.dll.bak"

# Installing personalized windbg workspace for labgeek
echo "[+] Installing the WINDBG workspace for labgeek"
copy "$share_path\windbg.reg" $install_dir
cd $install_dir
reg import .\windbg.reg


# install python2.7
echo "[+] installing python2.7"
copy "$share_path\python-2.7.17.msi" $install_dir
msiexec.exe /i $install_dir\python-2.7.17.msi /qn
start-sleep 60


# register Python2.7 binaries in path before Python3
echo "[+] adding python2.7 to the PATH"
$p = [System.Environment]::GetEnvironmentVariable('Path',[System.EnvironmentVariableTarget]::User)
[System.Environment]::SetEnvironmentVariable('Path',"C:\Python27\;C:\Python27\Scripts;"+$p,[System.EnvironmentVariableTarget]::User)

# copy mona files
echo "[+] bringing over mona files and fresh pykd"
copy "$share_path\windbglib.py" "C:\Program Files\Windows Kits\10\Debuggers\x86"
copy "$share_path\mona.py" "C:\Program Files\Windows Kits\10\Debuggers\x86"
copy "$share_path\pykd.pyd" "C:\Program Files\Windows Kits\10\Debuggers\x86\winext"

# register runtime debug dll
echo "[+] registering runtime debug dll"
cd "C:\Program Files\Common Files\Microsoft Shared\VC"


echo "[=] in case you see something about symbols when running mona, try executing the following (the runtime took too long to install)"
echo "regsvr32 C:\Program Files\Common Files\Microsoft Shared\VC\msdia90.dll"
