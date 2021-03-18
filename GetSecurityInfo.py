from datetime import datetime
import pandas as pd

baseUrl = "https://query1.finance.yahoo.com/v7/finance/download/"
startDateKeyword = "period1="
endDateKeyword = "&period2="
intervalKeyword = "&frequency="
trailingKeywords = "&includeAdjustedClose=false"


# Only retrieves TW stocks at the moment.
def GetSecurityInfo(stockNo, interval = "1d", startDate = "20180310", endDate = "20210312"):
    startDateParsed = int(datetime(int(startDate[:4]),int(startDate[4:6]), int(startDate[6:8])).timestamp())
    endDateParsed = int(datetime(int(endDate[:4]),int(endDate[4:6]), int(endDate[6:8])).timestamp())
    
    if interval != "1d" and interval != "1wk" and interval != "1mo":
        raise ValueError("interval keyword not accepted: ", interval)

    completeQueryUrl = baseUrl + str(stockNo) + ".TW?" + startDateKeyword + str(startDateParsed) + endDateKeyword + str(endDateParsed) + intervalKeyword + interval + trailingKeywords
    print(completeQueryUrl)
    downloadedDf = pd.read_csv(completeQueryUrl)
    downloadedDf = downloadedDf.dropna()
    print(downloadedDf.isnull().sum().sum())
    return downloadedDf