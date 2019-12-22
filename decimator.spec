# -*- mode: python -*-

block_cipher = None


a = Analysis(['main.py'],
             pathex=[r'C:\Users\Jake\OneDrive\Python\EZPZ Family\EZPZ Decimator'],
             binaries=[],
             datas=[(r'C:\Users\Jake\OneDrive\Python\EZPZ Family\EZPZ Decimator\Assets\icon.ico', 'assets'),
                    (r'C:\Users\Jake\OneDrive\Python\EZPZ Family\EZPZ Decimator\Assets\logo.png', 'assets')],
             hiddenimports=[],
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
          name='EZPZ Reducer',
          debug=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=False,
          icon=r'C:\Users\Jake\OneDrive\Python\EZPZ Family\EZPZ Decimator\Assets\icon.ico')
