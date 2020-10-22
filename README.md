# xgboost  
pyinstaller打包xgboost可能遇到問題  
環境:anaconda3  
  
step1: 先到  
https://www.lfd.uci.edu/~gohlke/pythonlibs/  
下載自己所對應的python版本  
(cmd下打python可以看到  

step2:安裝whl檔  

step3:到anaconda下面 site-package裡找pyinstaller/hooks  
裡面新增hook-xgboost.py  
  
step4:aaa.spec裡把 aaa.py改成自己的py檔名稱  
或者自己包 先打pyinstaller -F .\自己的py檔名稱.py  
會生成 自己的py檔名稱.spec  
裡面改  
import sys  
sys.setrecursionlimit(5000)  
from PyInstaller.utils.hooks import collect_all   
datas,binaries,hiddenimports = collect_all("xgboost")  
a = Analysis......  
    hiddenimports=['xgboost'],.....  
      
    或者  
import sys  
sys.setrecursionlimit(1000000)  
added_files=[  
	("C:\\Users\\Anaconda3\\Lib\\site-packages\\xgboost\\*.dll*","xgboost"),      (改自己anaconda3在的位置)  
	("C:\\Users\\Anaconda3\\Lib\\site-packages\\distributed\\*.yaml*","distributed"), (改自己anaconda3在的位置)  
	("C:\\xgboost\\*.dll*","xgboost"), (改自己anaconda3在的位置)  
]      
a = Analysis......  
    hiddenimports=['xgboost'],.....  
      
      
step5: pyinstaller -F .\aaa.spec  
自己打的就 pyinstaller -F .\自己的py檔名稱.spec    
等打包    
  
  
打包還是有問題:  
1.我一直出錯在distributed裡的資料  
手動pip uninstall distributed就好了(但可能會影響其他使用 目前還沒遇到)  
2.找不到xgboost.dll檔的error用第四步驟added_files可以解決  
  
