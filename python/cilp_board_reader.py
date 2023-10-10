import pyperclip



repeated = 0

while True:
    text = pyperclip.paste()

    if repeated > 0:
        if text != prevtext:     
            print(text)

    prevtext = text

    repeated += 1

    