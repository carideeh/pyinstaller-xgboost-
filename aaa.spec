# -*- mode: python ; coding: utf-8 -*-

block_cipher = None
import sys
sys.setrecursionlimit(1000000)
added_files=[
	("C:\\Users\\Anaconda3\\Lib\\site-packages\\xgboost\\*.dll*","xgboost"),
	("C:\\xgboost\\*.dll*","xgboost"),
]


a = Analysis(['aaa.py'],
             pathex=['######要打包的PY檔位置'],
             binaries=[],
             datas=[],
             hiddenimports=['cython','xgboost','sklearn.utils._cython_blas','sklearn','sklearn.ensemble','sklearn.neighbors.typedefs','sklearn.neighbors.quad_tree','sklearn.tree._utils','scipy._lib.messagestream','sklearn.linear_model','sklearn.metrics','sklearn.model_selection'],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='aaa',
          debug=True,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=True )
