# Kankra
A Website Spider/Crawler, Python 3.x

![python](https://img.shields.io/pypi/pyversions/Django.svg)
![size](https://img.shields.io/github/size/ak-wa/Kankra/kankra.py.svg)
![lastcommit](https://img.shields.io/github/last-commit/ak-wa/Kankra.svg)
![follow](https://img.shields.io/github/followers/ak-wa.svg?label=Follow&style=social)


* Crawls a website for hrefs, js & img files
* Automatic out of Scope checking
* Configurable:   
--target      | Target to scan   
--depth <int> | Depth to crawl through   
--output      | Output file
--full        | Show output with full website links      
--silent      | Do not show progress, only results

## Usage & examples

1. Basic Crawling with depth 10

`
python3 kankra.py --target https://example.com --depth 10
`

2. Basic Crawling with depth 15, output file, silent mode & full URL output

`
python3 kankra.py --target https://example.com --depth 15 --silent --full --output output.txt
`



