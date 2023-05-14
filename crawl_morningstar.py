import os
import time
import argparse

import numpy as np
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver


def run(args):

    driver = webdriver.Chrome('./chromedriver')

    # sign in
    driver.get("https://www.morningstar.com/sign-in")
    driver.find_element_by_name("userName").send_keys(args.id)
    driver.find_element_by_name("password").send_keys(args.password)
    driver.find_element_by_css_selector("button[type='submit']").click()
    time.sleep(15) # wait for login

    # access sites based on 'star' (value from 1 to 5)
    for star in range(1,6):
        driver.get("https://www.morningstar.com/{}-star-stocks".format(star))
        # get number of pages
        pagination_texts = [l.text for l in driver.find_elements_by_css_selector("li[class='mdc-pager-item mds-pagination__item']")]
        list_pages = []
        for pagination_text in pagination_texts:
            try:
                page = int(pagination_text)
                list_pages.append(page)
            except:
                continue
        if len(list_pages)==0:
            n_pages = 1
        else:
            assert len(list_pages)==np.max(list_pages)
            n_pages = len(list_pages)
        
        # retrieve column names (currently table header)
        list_column_names = []
        page_source = driver.page_source
        soup = BeautifulSoup(page_source, "html.parser")
        all_rows = soup.find_all("div", {"class": "mdc-table-row"})
        for row in all_rows: 
            tag_column_names = row.find_all("div", {"class":"mdc-table-header"})
            if len(tag_column_names)>0:
                for tag_column_name in tag_column_names:
                    list_column_names.append(tag_column_name.text.strip())
        dict_contents = {"star":star}
        dict_contents.update({k:[] for k in list_column_names})
            
        # retrieve contents
        for page in range(1, n_pages+1):
            driver.get("https://www.morningstar.com/{}-star-stocks?pages={}".format(star, page))
            page_source = driver.page_source
            soup = BeautifulSoup(page_source, "html.parser")
            all_rows = soup.find_all("div", {"class": "mdc-table-row"})
            for row in all_rows: 
                tag_contents = row.find_all("div", {"class":"mdc-table-cell"})
                if len(tag_contents)>0:
                    for index, tag_content in enumerate(tag_contents):
                        column_name = list_column_names[index]
                        dict_contents[column_name].append(tag_content.text.strip())
            
        # save results
        os.makedirs(args.home_outdir, exist_ok=True)
        df = pd.DataFrame(dict_contents)
        df.to_csv(os.path.join(args.home_outdir, "star{}.csv".format(star)))

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Example script using argparse')
    parser.add_argument('--home_outdir', type=str, default="crawled_data_morningstar")
    parser.add_argument('--id', type=str)
    parser.add_argument('--password', type=str)
    args = parser.parse_args()

    run(args)