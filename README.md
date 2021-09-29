# bd-bank-branch-list
All of the bank in bangladesh and their branches with bank code and routing number will be there in different format.
* formatted json - [Formatted Json](https://github.com/shourav9884/bd-bank-branch-list/blob/main/bank_data.json)
* minified json - [Minified json](https://github.com/shourav9884/bd-bank-branch-list/blob/main/bank_data_minified.json)
## Structure of the json
```json
[
    {
        "slug": "AB_BANK_LIMITED",
        "bank_code": "020",
        "name": "AB BANK LIMITED",
        "districts": [
            {
                "district_name": "BARISAL",
                "branches": [
                    {
                        "routing_number": "020060288",
                        "branch_name": "BARISAL BRANCH",
                        "branch_slug": "BARISAL_BRANCH",
                        "branch_code": "4321 / 028",
                        "swift_code": "ABBLBDDH",
                        "address": "MONSUR MANSION, 101 SADAR ROAD, BARISAL",
                        "telephone": "0431 2173186",
                        "email": "brslmg@abbl.com",
                        "fax": "0431 63562"
                    }
                ]
            }
            ...
        ]
    }
    ...
]
```

## Note
* I scraped the data from [http://thecodes.us/](http://thecodes.us/) using scrapy, requests and python3

* Here is my script - [Script](https://github.com/shourav9884/bd-bank-branch-list/blob/main/bank_scrape.py)

