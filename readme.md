# Stock Report Maker

## *Important Disclamer* 
The information this program presents **should not** be used to make actual financial decisions. This project is a personal project with the sole purpose of learning, and it is therefore not quality checked, there are no guarantees it will work as intended or that the information presented is accurate. The information presented by this program may be inaccurate or false due to various reasons, and I do not take responsibility for any inaccuracies or false information presented using this code.

**ALWAYS CHECK MULTIPLE OTHER SOURCES BEFORE MAKING ANY FINANCIAL DECISIONS**

The information used to produce the report is captured using the yfinance module, which gets it's data from Yahoo's publicly available API. I am not associated, affiliated or endorsed by yfinance or Yahoo! INC.
If you decide to use this code you should refer to Yahoo!'s terms of use for your rights to use the actual data captured. The Yahoo! Finance API is intended for personal use only.

Yahoo!'s terms of service: 
1. https://legal.yahoo.com/us/en/yahoo/terms/product-atos/apiforydn/index.html
2. https://legal.yahoo.com/us/en/yahoo/terms/otos/index.html
3. https://policies.yahoo.com/us/en/yahoo/terms/index.htm

\
\
<br />
# How to use

The intent is to run makeReport.py with a stock ticker symbol (such as EQNR or MSFT) as the second argument. The program will then produce a PDF called "tickerSymbol".pdf in the directory the program is ran in.

Example: ```python makeReport.py EQNR``` will make a report for the stock Equinor ASA. Symbol tickers can be found using online databases or websites. Every ticker symbol might not work, it has to be suppored by the yfinance module.

Examples of how a report might look is EQNR.pdf in this repository.

More features and content will be coming ...

Suggestions, comments and concerns can be sent to my e-mail: michaelingemann@hotmail.com