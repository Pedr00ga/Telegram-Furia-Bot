@echo off
title FURIA Telegram Bot
color 0A
cls

:: Inicia o bot em uma nova janela
start "FURIA Bot" cmd /k python bot\main.py

echo Bot do Telegram iniciado com sucesso!
echo.
echo Acesse o Telegram e teste com: /start
pause