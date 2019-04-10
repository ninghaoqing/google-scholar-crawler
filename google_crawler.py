#!/usr/bin/env python2

import pickle

from Spider import Spider

def main():
    ### The start page's URL
    start_url = 'https://scholar.google.com.hk/scholar?hl=zh-CN&as_sdt=0%2C5&q=laser+ablation&btnG='

    ### p_key and n
    p_key = ['laser', 'ultrafast', 'spectroscopy', 'ablation', 'probing',
             'exciton', 'pump-probe', 'probe',
             'photon', 'organic']
    n_key = ['sound', 'mass', 'gravity',
             ]

    ### Google Scholar Crawler, Class Spider
    myCrawler = Spider(start_url, p_key, n_key, page=50)

    results = myCrawler.crawl()

    with open('result.pickle', 'wb') as f:
        pickle.dump(results, f, protocol=pickle.HIGHEST_PROTOCOL)


if __name__ == '__main__':
    main()
