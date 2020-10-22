from PyInstaller.utils.hooks import collect_submodules
from PyInstaller.utils.hooks import collect_dynamic_libs
from PyInstaller.utils.hooks import collect_all

hiddenimports = collect_submodules('xgboost')
binaries = collect_dynamic_libs('xgboost')
datas, binaries, hiddenimports = collect_all("xgboost")