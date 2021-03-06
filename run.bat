call venv\scripts\activate
rem pytest -v -m "sanity" --html=./Reports/report_chrome.html testCases/ --browser chrome
pytest -v -m "sanity" --html=./Reports/report_firefox.html testCases/ --browser firefox

rem chrome
rem pytest -v -m "sanity or regression" --html=./Reports/report.html testCases/ --browser chrome
rem pytest -v -m "sanity and regression" --html=./Reports/report.html testCases/ --browser chrome
rem pytest -v -m "regression" --html=./Reports/report.html testCases/ --browser chrome

rem firefox
rem pytest -v -m "sanity or regression" --html=./Reports/report.html testCases/ --browser firefox
rem pytest -v -m "sanity and regression" --html=./Reports/report.html testCases/ --browser firefox
rem pytest -v -m "regression" --html=./Reports/report.html testCases/ --browser firefox
