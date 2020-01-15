from tkinter import *
import requests
from bs4 import BeautifulSoup
from tkinter import ttk

page = requests.get("https://www.livecoinwatch.com/")
soup = BeautifulSoup(page.content, 'html.parser')

prices = soup.find_all("span", {"class": "data"})
mcap = soup.find_all("span", {"class": "price"})
rank = soup.find_all("p")

# BTC
'''btc = {'btcr': rank[0].get_text(),
       'btcp': prices[0].get_text(),
       'btcm': mcap[0].get_text()}

eth = {'ethr': rank[1].get_text(),
       'ethp': prices[1].get_text(),
       'ethm': mcap[1].get_text()}

xrp = {'xrpr': rank[2].get_text(),
       'xrpp': prices[2].get_text(),
       'xrpm': mcap[2].get_text()}

bch = {'bchr': rank[4].get_text(),
       'bchp': prices[4].get_text(),
       'bchm': mcap[4].get_text()}

ltc = {'ltcr': rank[5].get_text(),
       'ltcp': prices[5].get_text(),
       'ltcm': mcap[5].get_text()}'''

# The Palette
root = Tk()
root.geometry("750x800")
root.title("LiveCoinWatch Widget")
root.configure(background='Black')
root.iconbitmap('Cones/favicon.ico')

# The Head
titlelabl = Label(root, text="Crypto Oracle", font="Arial 40 bold",
                  fg="Blue", bg="Black", pady=20)
titlelabl.grid(row=0, column=1, columnspan=2, sticky=E + W)

displaylabl = Text(root, width=65, height=10, bg="Grey",
                   relief=SUNKEN, bd='8', wrap=WORD)
displaylabl.grid(row=1, column=1, padx=10, pady=10, columnspan=2, sticky=E + W)


# BTC
# function
def btc_func():
    displaylabl.delete(0.0, 'end')
    btcs = """
    BTC otherwise known as BITCOIN
    is the first major cryptocurrency 
    to hit the market.  It was founded 
    by an anonymous cryptographer by the
    name of Satoshi Nakamoto.  
    
    BTC currently trades at: """ + (btc['btcp']) + """
    and has a market cap of """ + (btc['btcm'])
    displaylabl.insert(INSERT, btcs)


# label
btclbl = Label(root, text="Bitcoin:", bg='Black', fg='White',
               font="none 15")
btclbl.grid(row=2, column=0, pady=20)

# button
btcbtn = ttk.Button(root, command=btc_func)
btcbtn.grid(row=2, column=1, sticky=W, pady=20)

# picture
btcpic = PhotoImage(file='cones/BTC3.png')
btcbtn.config(image=btcpic)
resizbtc = btcpic.subsample(8, 8)
btcbtn.config(image=resizbtc)


# ETH
# function
def eth_func():
    displaylabl.delete(0.0, 'end')
    eths = """
    ETH otherwise known as ETHEREUM
    was founded by Russian Canadian developer
    Vitalik Buterin
    
    ETH currently trades for """ + (eth['ethp']) + """ per coin
    and has a market cap of """ + (eth['ethm'])
    displaylabl.insert(INSERT, eths)


# label
ethlbl = Label(root, text="Ethereum:", bg='Black', fg='White',
               font="none 15")
ethlbl.grid(row=3, column=0)

# button
ethbtn = ttk.Button(root, command=eth_func)
ethbtn.grid(row=3, column=1, sticky=W, pady=20)

# picture
ethpic = PhotoImage(file='cones/ETH.png')
ethbtn.config(image=ethpic)
resizeth = ethpic.subsample(31, 30)
ethbtn.config(image=resizeth)


# XRP
# function
def xrp_func():
    displaylabl.delete(0.0, 'end')
    xrps = """
    XRP aka 'Unknown Ripples' was founded by 
    Ryan Fugger in 2004  It is also closely 
    associated with the company RIPPLE
    
    The coin will be a major catalyst in how 
    money is transferred around the world

    XRP currently trades for """ + (xrp['xrpp']) + """ per coin
    and has a market cap of """ + (xrp['xrpm'])
    displaylabl.insert(INSERT, xrps)


# label
xrplbl = Label(root, text="XRP:", bg='Black', fg='White',
               font="none 15")
xrplbl.grid(row=4, column=0, pady=20)

# button
xrpbtn = ttk.Button(root, command=xrp_func)
xrpbtn.grid(row=4, column=1, sticky=W, pady=20)

# picture
xrppic = PhotoImage(file='cones/XRP.png')
xrpbtn.config(image=xrppic)
resizexrp = xrppic.subsample(22, 19)
xrpbtn.config(image=resizexrp)


# BCH
# function
def bch_func():
    displaylabl.delete(0.0, 'end')
    bchs = """
    BCH aka BITCOIN CASH was founded by Roger Ver
    in 2017 as a hard fork to BITCOIN due to its 
    larger block size and fees involved in use
    
    BCH or BCASH was created as a better 
    TRANSACTION instrument
    
    BCH currently trades at """ + (bch['bchp']) + """ per coin
    and has a market cap of """ + (bch['bchm'])
    displaylabl.insert(INSERT, bchs)


# label
bchlbl = Label(root, text="Bitcoin Cash:", bg='Black', fg='White',
               font="none 15")
bchlbl.grid(row=5, column=0, sticky=W, pady=20)

# button
bchbtn = ttk.Button(root, command=bch_func)
bchbtn.grid(row=5, column=1, sticky=W, pady=20)

# picture
bchpic = PhotoImage(file='cones/BCH.png')
bchbtn.config(image=bchpic)
resizebch = bchpic.subsample(19, 19)
bchbtn.config(image=resizebch)


# LTC
# function
def ltc_func():
    displaylabl.delete(0.0, 'end')
    ltcs = """
    LTC aka LiteCoin was founded by Charlie Lee 
    a computer scientist and ex employee at Google 
    
    Like BCASH, LTCs intention was to serve as a 
    cheaper more efficient method of crypto transactions 
    
    LTC currently trades for """ + (ltc['ltcp']) + """ per coin
    and has a market cap of """ + (ltc['ltcm'])
    displaylabl.insert(INSERT, ltcs)


# label
ltclbl = Label(root, text="Litecoin:", bg='Black', fg='White',
               font="none 15")
ltclbl.grid(row=6, column=0, sticky=W, pady=20)

# button
ltcbtn = ttk.Button(root, command=ltc_func)
ltcbtn.grid(row=6, column=1, sticky=W, pady=20)

# picture
ltcpic = PhotoImage(file='cones/LTC2.png')
ltcbtn.config(image=ltcpic)
resizeltc = ltcpic.subsample(5, 5)
ltcbtn.config(image=resizeltc)

root.mainloop()
