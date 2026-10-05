import datetime
timestamp = datetime.datetime.now().strftime("%a %b %d %H:%M:%S IST %Y")
with open('store/index.html', 'a') as f:
    f.write(f"\n<!-- Cache Bust 24: {timestamp} -->")
print("Busted")
