# morningstar-company-by-star-crawler (accessed on 2021/03/17)
Crawl company data and save in a csv format by star. 

[1-star-stocks](https://www.morningstar.com/1-star-stocks)

[2-star-stocks](https://www.morningstar.com/2-star-stocks)

[3-star-stocks](https://www.morningstar.com/3-star-stocks)

[4-star-stocks](https://www.morningstar.com/4-star-stocks)

[5-star-stocks](https://www.morningstar.com/5-star-stocks)


## Commands
```
pip install -r requirements.txt
python crawl_morningstar.py --id <userid> --password <password>
```

## Example (star5.csv)
```
,star,Name,Ticker,Price $,Market Return YTD %,Market Return 1Y %,Market Return 3Y %,"Premium Fair Value Uncertainty Rating","Premium Fair Value $","Premium Morningstar Rating for Stocks"
0,5,Energy Transfer LP,ET,8.09,33.37,56.61,−8.34,Medium,18.00,
1,5,Macerich Co,MAC,13.45,27.46,44.93,−30.27,Very High,32.50,
2,5,NiSource Inc,NI,23.45,3.18,16.05,3.39,Low,28.50,
3,5,Tenneco Inc Class A,TEN,12.13,14.43,246.57,−38.01,Very High,29.00,
```
