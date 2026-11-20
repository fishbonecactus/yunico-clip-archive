@echo off
cd /d "%~dp0"
echo YUNICO Clip Archive 서버 시작...
echo 새 서버 주소: http://localhost:8765/clip.html
start "" python -m http.server 8765
timeout /t 2 > nul
start "" "http://localhost:8765/clip.html"
exit
