@echo off
chcp 65001 > nul
title برنامج حساب تكلفة الوجبات والتسعير
cd /d "%~dp0"
py food_cost_app.py
pause
