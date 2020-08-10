$scriptpath = $MyInvocation.MyCommand.Path
$dir = Split-Path $scriptpath
cd $dir

python .\setup.py clean --all
Remove-Item -Recurse -Force .\dist
python .\setup.py bdist_wheel
python .\setup.py sdist
