import os

print("Hello! I'm bot which show you best sellers book of the most popular websites")
print("First: Tell me which website you want to see? (Amazon, eBay, Empik)")
acc = input()
if acc == str('Amazon') or acc == str('AMAZON') or acc == str('amazon'):
    print("Okay, you choose amazon" )
    print("Second: Do you want to save the books? Y/N")
    yn = input()
    if yn == 'Y' or yn == 'y':
        print("Sure. Where do you want to save it? (json, xml, csv)")
        save = input()
        if save == str('json'):
            print("Okay! I'll save it in json file")
            os.system("start /B start cmd.exe @cmd /k scrapy crawl amazon -o amazon.json")
        elif save == str('xml'):
            print("Okay! I'll save it in xml file")
            os.system("start /B start cmd.exe @cmd /k scrapy crawl amazon -o amazon.xml")
        elif save == str('csv'):
            print("Okay! I'll save it in csv file")
            os.system("start /B start cmd.exe @cmd /k scrapy crawl amazon -o amazon.csv")
        else:
            print("Something went wrong. Make sure you write one of three extenson")
            exit()
    else:
        print("Okay, I'll just show you books right there")
        os.system("start /B start cmd.exe @cmd /k scrapy crawl amazon")

elif acc == str('EBay') or acc == str('EBAY') or acc == str('ebay') or acc == ('eBay') or acc == ('Ebay'):
    print("Okay, you choose eBay")
    print("Second: Do you want to save the books? Y/N")
    yn = input()
    if yn == 'Y' or yn == 'y':
        print("Sure. Where do you want to save it? (json, xml, csv)")
        save = input()
        if save == str('json'):
            print("Okay! I'll save it in json file")
            os.system("start /B start cmd.exe @cmd /k scrapy crawl ebay -o ebay.json")
        elif save == str('xml'):
            print("Okay! I'll save it in xml file")
            os.system("start /B start cmd.exe @cmd /k scrapy crawl ebay -o ebay.xml")
        elif save == str('csv'):
            print("Okay! I'll save it in csv file")
            os.system("start /B start cmd.exe @cmd /k scrapy crawl ebay -o ebay.csv")
        else:
            print("Something went wrong. Make sure you write one of three extenson")
            exit()
    else:
        print("Okay, I'll just show you books right there")
        os.system("start /B start cmd.exe @cmd /k scrapy crawl ebay")
elif acc == str('Empik') or acc == str('EMPIK') or acc == str('empik'):
    print("Okay, you choose empik")
    print("Second: Do you want to save the books? Y/N")
    yn = input()
    if yn == 'Y' or yn == 'y':
        print("Sure. Where do you want to save it? (json, xml, csv)")
        save = input()
        if save == str('json'):
            print("Okay! I'll save it in json file")
            os.system("start /B start cmd.exe @cmd /k scrapy crawl empik -o empik.json")
        elif save == str('xml'):
            print("Okay! I'll save it in xml file")
            os.system("start /B start cmd.exe @cmd /k scrapy crawl empik -o empik.xml")
        elif save == str('csv'):
            print("Okay! I'll save it in csv file")
            os.system("start /B start cmd.exe @cmd /k scrapy crawl empik -o empik.csv")
        else:
            print("Something went wrong. Make sure you write one of three extenson")
            exit()
    else:
        print("Okay, I'll just show you books right there")
        os.system("start /B start cmd.exe @cmd /k scrapy crawl amazon")

else:
    print("Oops! Something went wrong. Make sure u write one of three websites")
    exit()