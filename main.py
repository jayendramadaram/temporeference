from bs4 import BeautifulSoup
import requests
from selenium import webdriver
import time
import csv
class scrap():
    def __init__(self):
        self.url = 'https://www.ebay.co.uk/sch/i.html?_dmd=2&_ssn=jewellerykingdom1965&store_cat=0&store_name=jewellerykingdom1965&_oac=1&_ipg=192&rt=nc&LH_All=1'
# "Accept-Encoding": "gzip, deflate, br",
    def start_scrap(self,url ):
        headers =  {
                 
                 
                "Accept-Language": "en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7", 
                
                "Sec-Ch-Ua": "\"Chromium\";v=\"94\", \"Google Chrome\";v=\"94\", \";Not A Brand\";v=\"99\"", 
                "Sec-Ch-Ua-Mobile": "?0", 
                "Sec-Ch-Ua-Platform": "\"Windows\"", 
                "Sec-Fetch-Dest": "document", 
                "Sec-Fetch-Mode": "navigate", 
                "Sec-Fetch-Site": "cross-site", 
                "Sec-Fetch-User": "?1", 
                "Upgrade-Insecure-Requests": "1", 
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36", 
                "X-Amzn-Trace-Id": "Root=1-61537c5a-78125ae70390eae269a1ee2f", 
                "X-Client-Data": "CI62yQEIorbJAQjEtskBCKmdygEI+I7LAQjr8ssBCO/yywEInvnLAQjrg8wBCNmEzAEI3ITMAQjmhMwBCLWFzAEI24XMARiOnssB"
            }
        html = requests.get(url , headers=headers ).text
        return html
    def start_links(self):
        with open("links.txt" , "w") as f:
            for i in range(1, 23):
                url = "https://www.ebay.co.uk/sch/i.html?_dmd=2&_ssn=jewellerykingdom1965&store_cat=0&store_name=jewellerykingdom1965&_oac=1&_ipg=192&rt=nc&LH_All=1&_pgn={}".format(i)
                html = self.start_scrap(url)
                soup = BeautifulSoup(html,"html.parser")
                tags = soup.find_all("div" , {"class" : "s-item__image"})
                for i in tags:
                    f.write(i.a.get("href"))
                    f.write("\n")




    def st(self):
        with open("jklinks.txt" , "r") as f:

            with open("newpro.csv" , "w" , newline='')  as g:

                writer = csv.writer(g)

                writer.writerow(["Handle", "Title", "Body (HTML)", "Vendor", "Tags", "Published", "Option1 Name", "Option1 Value", "Option2 Name", "Option2 Value", "Option3 Name", "Option3 Value", "Variant SKU", "Variant Grams", "Variant Inventory Tracker", "Variant Inventory Qty", "Variant Inventory Policy", "Variant Fulfillment Service", "Variant Price", "Variant Compare At Price", "Variant Requires Shipping", "Variant Taxable", "Variant Barcode", "Image Src", "Image Position", "Image Alt Text", "Gift Card", "SEO Title", "SEO Description", "Google Shopping / Google Product Category", "Google Shopping / Gender", "Google Shopping / Age Group", "Google Shopping / MPN", "Google Shopping / AdWords Grouping", "Google Shopping / AdWords Labels", "Google Shopping / Condition", "Google Shopping / Custom Product", "Google Shopping / Custom Label 0", "Google Shopping / Custom Label 1", "Google Shopping / Custom Label 2", "Google Shopping / Custom Label 3", "Google Shopping / Custom Label 4", "Variant Image", "Variant Weight Unit", "Variant Tax Code", "Cost per item", "Status", "Standard Product Type", "Custom Product Type"])
                
                with open("products.txt" , "w") as l:
                    
                    count = 1
                    fail = []
                    for i in f.readlines():
                            print(count)
                            url = i.strip()
                            html = self.start_scrap(url)
                            soup = BeautifulSoup(html,"html.parser")
                            TITLE = soup.find("div" , {"class" :"prodright double right"}).h1.text.strip()

                            imgs = ["https://www.jokeshop.co.uk{}".format(soup.find("img" , {"itemprop" : "image"}).get("src"))]
                              
                            PRICE = soup.find("div" , {"class" :"prodright double right"}).div.text.strip().replace(",","")

                            pr = PRICE.find("£")
                            PRICE = PRICE[pr+1:]

                            p = PRICE
                            PRICE = int(float(PRICE))

                            desc = soup.find("div" , {"itemprop" :"description"}).text
                            Vendor = "The Joke shop.co.uk"
                            StandardProductType = ""
                            CustomProductType = "Fancy Accessories" 
                            Published = "TRUE"
                            Status = "active"
                            VariantWeightUnit = ""
                            Costperitem=""
                            VariantGrams,VariantInventoryQty = 0,0
                            VariantInventoryTracker = "shopify"
                            VariantInventoryPolicy = "deny"
                            VariantFulfillmentService = "manual"
                            
                            

                            sizes = soup.find_all("div" , {"class" : "varianttitle txtleft"})
                            size = []
                            for i in sizes:
                              size.append(i.text)
                            if len(imgs) >= len(size):
                                rn = len(imgs)
                                size += [""]*(len(imgs) - len(size))
                            else:
                                rn = len(size)
                                imgs += [""]*(len(size) - len(imgs))
                            # print(size)
                            if PRICE < 10:
                                ptag = "Price_Below £10"
                            elif 10 < PRICE < 50:
                                ptag = "Price_£10-£50"
                            elif 50 < PRICE < 100:
                                ptag = "Price_£50-£100"
                            elif 100 < PRICE < 150:
                                ptag = "Price_£100-£150"
                            elif 150 < PRICE < 200:
                                ptag = "Price_£150-£200"
                            elif 200 < PRICE < 300:
                                ptag = "Price_£200-£300"
                            elif 300 < PRICE < 400:
                                ptag = "Price_£300-£400"
                            elif 400 < PRICE < 500:
                                ptag = "Price_£400-£500"
                            elif 500 < PRICE < 600:
                                ptag = "Price_£500-£600"
                            elif 600 < PRICE < 700:
                                ptag = "Price_£600-£700"
                            elif 700 < PRICE < 800:
                                ptag = "Price_£700-£800"
                            elif 800 < PRICE < 900:
                                ptag = "Price_£800-£900"
                            elif 1000 < PRICE < 2000:
                                ptag = "Price_£1000-£2000"
                            elif 2000 < PRICE < 3000:
                                ptag = "Price_£2000-£3000"
                            elif 3000 < PRICE < 4000:
                                ptag = "Price_£3000-£4000"
                            
                            tags = ""
                            for i in size:
                              if i!="":
                                tags += "SIZE_" + i + ","
                            if tags!=[]:
                              tags = tags[:-1] +"," + ptag + "," + "Coming Soon" "," + "Fancy Accessories"
                              tags = tags[:-1] +"," + ptag + "," + "Coming Soon" "," + "Fancy Accessories"
                            else:
                              tags =   ptag + "," + "Coming Soon" "," + "Cosplay Costumes"
                            # print()

                            for i in range(rn):
                                if i==0:
                                    if size[0] != "":opt1 = "SIZE"
                                    else:opt1=""
                                    writer.writerow([TITLE, TITLE, desc, Vendor, tags, Published, opt1, size[0], "", "", "", "", "", VariantGrams, VariantInventoryTracker, VariantInventoryQty, VariantInventoryPolicy, VariantFulfillmentService, p, "", "", "", "", imgs[0], i+1, desc, "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", imgs[0], VariantWeightUnit, "", "", Status, StandardProductType, CustomProductType])
                                else:
                                    if imgs[i]!="":
                                        yoi = i +1
                                        imd = desc
                                    else:
                                        yoi= ""
                                        imd = ""
                                    
                                    writer.writerow([TITLE, "", "", "", "", "", "", size[i], "", "", "", "", "", VariantGrams, VariantInventoryTracker, VariantInventoryQty, VariantInventoryPolicy, VariantFulfillmentService, p, "", "", "", "", imgs[i], yoi, imd, "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", imgs[i], VariantWeightUnit, "", "", Status, "", ""])
                            writer.writerow(["",	"",	"",	"",	"",	"",	"",	"",	"",	"",	"",	"",	"",	"",	"",	"",	"",	"",	"",	"",	"",	"",	"",	"",	"",	"",	"",	"",	"",	"",	"",	"",	"", "",	"",	""	]	)
                            count += 1

                            
                        # except:
                        #     count += 1
                        #     fail.append(str(count))
                        #     continue
                        # l.write(",".join( fail))


    def start(self):
      html = self.start_scrap("https://naturalskincareproductscreationsbyviva.com/collections/all")
      soup = BeautifulSoup(html , "lxml")
      tags= soup.find_all("div" , {"class" :"sectcontainer"})
      with open("jlinks.txt" , "w") as f:
        for i in tags:
          f.write(i.a.get("href"))
          f.write("\n")
    def ph2(self):
      with open("jlinks.txt" , "r") as f:
          with open("jklinks.txt" , "w") as l:
            # for i in :
            url = f.readlines()[0].strip()
            html = self.start_scrap(url)
            soup = BeautifulSoup(html , "lxml")
            tags = soup.find_all("a" , {"class" :"product-card"})
            # print(tags)
            for i in tags:
              l.write("https://naturalskincareproductscreationsbyviva.com{}".format(i.get("href")))
              l.write("\n")
    def test(self):
      with open("jklinks.txt" , "r") as f:
        for i in f.readlines():
          url = i.strip()
          html = self.start_scrap(url)
          soup = BeautifulSoup(html,"html.parser")



        

jay = scrap()
jay.ph2()




head = ["Handle", "Title", "Body (HTML)", "Vendor", "Tags", "Published", "Option1 Name", "Option1 Value", "Option2 Name", "Option2 Value", "Option3 Name", "Option3 Value", "Variant SKU", "Variant Grams", "Variant Inventory Tracker", "Variant Inventory Qty", "Variant Inventory Policy", "Variant Fulfillment Service", "Variant Price", "Variant Compare At Price", "Variant Requires Shipping", "Variant Taxable", "Variant Barcode", "Image Src", "Image Position", "Image Alt Text", "Gift Card", "SEO Title", "SEO Description", "Google Shopping / Google Product Category", "Google Shopping / Gender", "Google Shopping / Age Group", "Google Shopping / MPN", "Google Shopping / AdWords Grouping", "Google Shopping / AdWords Labels", "Google Shopping / Condition", "Google Shopping / Custom Product", "Google Shopping / Custom Label 0", "Google Shopping / Custom Label 1", "Google Shopping / Custom Label 2", "Google Shopping / Custom Label 3", "Google Shopping / Custom Label 4", "Variant Image", "Variant Weight Unit", "Variant Tax Code", "Cost per item", "Status", "Standard Product Type", "Custom Product Type"]	


