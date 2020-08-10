$scriptpath = $MyInvocation.MyCommand.Path
$dir = Split-Path $scriptpath
cd $dir

& .\make_dist.ps1

python -m pip install twine
twine upload .\dist\*
