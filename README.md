FinAPI service
===============

*The following service is used in combination with the FinAPP found [here.](https://github.com/mfazari/FinApp)*

Introduction
------------

This is a backend API service using the yfinance library provided by Yahoo. For more information on the library, please check this [link.](https://pypi.org/project/yfinance/)

How to run
------------------
1. 
    ```
    pip install -r requirements.txt
    ```
2.
    ```
    python app.py
    ```

Calls
-----------

You can use [curl](https://curl.haxx.se/) to test the following route:

### `/v1/manager/search/<symbol>`

Replace "symbol" with any search term.


Copyright
------------
Massimo Fazari 2022.