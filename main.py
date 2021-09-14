from Downloader import Downloader as dw

"""
to complile ui files: pyuic5 -x test.ui -o Downloader.py
to complile qrc files: pyrcc5 resource.qrc -o resource_rc.py

token-id: 235469-c5009876-28a2-45de-a0d8-107fab26a6c7
image-size for preview = 175 w x 248 h
"""

dw = dw.Downloader("19p8102@eng.asu.edu.eg", "Omar2211")
dw.get_files(["CSE111"])