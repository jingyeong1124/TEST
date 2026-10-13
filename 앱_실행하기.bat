@echo off
chcp 65001 > nul
echo ========================================================
echo        🎓 VocaQuiz (영단어 퀴즈 앱) 실행기
echo ========================================================
echo   [1] 웹 브라우저(PC)에서 바로 실행 (추천)
echo   [2] 모바일 스마트폰(Expo Go) QR 코드로 실행
echo ========================================================
set /p choice="실행할 모드를 선택해 주세요 (1 또는 2, 엔터시 1): "

if "%choice%"=="2" (
    echo.
    echo [스마트폰 모드] 터미널에 나타나는 QR 코드를 Expo Go 앱으로 스캔하세요!
    cd /d "%~dp0\adsp-app"
    npx expo start
) else (
    echo.
    echo [웹 브라우저 모드] 로컬 개발 서버가 열리고 브라우저가 실행됩니다...
    cd /d "%~dp0\adsp-app"
    npx expo start --web
)
pause
