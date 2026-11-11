# -*- mode: python ; coding: utf-8 -*-
from PyInstaller.utils.hooks import collect_all
import os

datas = []
binaries = []
hiddenimports = []

# --- 第三方依赖 ---
for pkg in ('PIL', 'requests', 'pywebview', 'pythonnet', 'clr_loader'):
    tmp = collect_all(pkg)
    datas += tmp[0]; binaries += tmp[1]; hiddenimports += tmp[2]

# --- 本地包 ---
hiddenimports += ['providers', 'providers.geostationary', 'providers.sdo',
                  'archive', 'tasks', 'backfill', 'export', 'timelapse_player']

# --- web 静态资源 ---
web_dir = os.path.join(os.path.dirname(SPEC), 'web')
datas += [(web_dir, 'web')]

a = Analysis(
    ['main.py'],
    pathex=[],
    binaries=binaries,
    datas=datas,
    hiddenimports=hiddenimports,
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=['customtkinter'],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='LivingEarth Wallpaper',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=False,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon='docs/app.ico',
)
