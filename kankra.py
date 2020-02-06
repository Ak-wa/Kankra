import requests
from parsel import Selector
import tldextract
import argparse

class Kankra:
    def __init__(self,arguments):
        self.target_url = args.target
        self.found_items = []
        self.crawler_depth = args.depth


    def crawler_extract_one_site(self, url_to_extract):
        r = requests.get(url_to_extract)
        response = r.text
        selector = Selector(response)

         # HREF COLLECTING
        for link in selector.xpath('//a/@href').getall():
            if link not in self.found_items:
                if link.startswith("http"):
                    if self.check_scope(link):
                        self.found_items.append(link)
                else:
                    if link.startswith("/"):
                        self.found_items.append(link)
                    else:
                        link = "/"+str(link)

        # JS COLLECTING
        for link in selector.xpath('//script/@src').getall():
            if link not in self.found_items:
                if link.startswith("http"):
                    if self.check_scope(link):
                        self.found_items.append(link)
                else:
                    if link.startswith("/"):
                        self.found_items.append(link)
                    else:
                        link = "/"+str(link)

        # IMG COLLECTING

        for link in selector.xpath('//img/@src').getall():
            if link not in self.found_items:
                if link.startswith("http"):
                    if self.check_scope(link):
                        self.found_items.append(link)
                else:
                    if link.startswith("/"):
                        self.found_items.append(link)
                    else:
                        link = "/"+str(link)

        if not args.silent:
            print("Current List:", len(self.found_items))

    def check_scope(self, link_url):
        target_domain = tldextract.extract(self.target_url).registered_domain
        url_domain = tldextract.extract(link_url).registered_domain

        if str(target_domain) == str(url_domain):
            return True
        else:
            return False

    def run(self):
        self.crawler_extract_one_site(self.target_url)
        crawler_depth_counter = 0
        for link in self.found_items:
            if crawler_depth_counter <= self.crawler_depth:
                crawler_depth_counter += 1
                # CONDITION: Some hrefs are full links, some are not
                if link.startswith("http"):
                    if self.check_scope(link):
                        if not args.silent:
                            print("[+] Extracting links from:", link)
                        self.crawler_extract_one_site(link)
                    else:
                        print("Link: %s is out of Scope" % link)
                else:
                    if not args.silent:
                        print("[+] Extracting links from:", link)
                    self.crawler_extract_one_site(self.target_url+"/"+link)
            else:
                break

        for link in self.found_items:
            if args.full:
                print("| %s%s" % (self.target_url,link))
            else:
                print("|",link)
        print("[+] Crawling finished with depth %d" % self.crawler_depth)
        if args.output:
            with open(str(args.output), "w+") as output_file:
                for link in self.found_items:
                    output_file.write("%s%s\n" % (self.target_url,link))
            print("[+] Saved output to %s" % args.output)



if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--target", help="Target URL to start crawling from", required=True)
    parser.add_argument("--depth", help="Crawling depth, 0 means only Target URL", type=int, required=True)
    parser.add_argument("--full", help="Show output with full website links", action="store_true")
    parser.add_argument("--silent", help="Do not show progress, only results", action="store_true")
    parser.add_argument("--output", help="Send raw links to text file", type=str, required=False)
    args = parser.parse_args()

    crawler = Kankra(args)
    crawler.run()
