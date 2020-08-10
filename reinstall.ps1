$scriptpath = $MyInvocation.MyCommand.Path
$dir = Split-Path $scriptpath
cd $dir

python -m pip uninstall pyvuejs_cli -y

& .\make_dist.ps1
$whlFile = Get-ChildItem .\dist\pyvuejs_cli*.whl -Name | select -first 1
python -m pip install .\dist\$whlFile
