uv run python -m PyInstaller -n MDCx -F --noupx `
-i resources/Img/MDCx.ico `
-w main.py `
-p "./mdcx" `
--add-data "resources:resources" `
--add-data "libs:." `
--hidden-import _cffi_backend `
--collect-all curl_cffi

Write-Output 'Done'