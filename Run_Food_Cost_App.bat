@echo off
chcp 65001 > nul
title برنامج حساب تكلفة الوجبات والتسعير
cd /d "%~dp0"
node server.js
pause
