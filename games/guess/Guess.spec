# -*- mode: python ; coding: utf-8 -*-

a = Analysis(
    ['Guess.py'],
    pathex=[],
    binaries=[],
    datas=[('assets/lamp.ico', 'assets')],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False
)

pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='Guess',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,
    icon='assets/lamp.ico',
    version='versionfile.txt'
)