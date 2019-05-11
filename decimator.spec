# -*- mode: python -*-

block_cipher = None


a = Analysis(['decimator.py'],
             pathex=['C:\\Users\\Jake\\OneDrive\\Python\\EZPZ Offshoots\\EZPZ Decimator'],
             binaries=[],
             datas=[('C:\\Users\\Jake\\OneDrive\\Python\\EZPZ Offshoots\\EZPZ Decimator\\Assets\\icon.ico', 'assets'),
                    ('C:\\Users\\Jake\\OneDrive\\Python\\EZPZ Offshoots\\EZPZ Decimator\\Assets\\logo.png', 'assets')],
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
          name='EZPZ Decimator',
          debug=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=False , icon='C:\\Users\\Jake\\OneDrive\\Python\\EZPZ Offshoots\\EZPZ Decimator\\Assets\\icon.ico')
