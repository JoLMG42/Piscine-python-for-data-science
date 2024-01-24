from datetime import datetime

today = datetime.today()
old = datetime(1970, 1, 1)
all_sec = (today - old).total_seconds()

print("Seconds since January 1, 1970: ", end="")

split = str(all_sec).split('.')
print(split[0][0] + ',', end="")
for i in range(1, len(split[0])):
    print(split[0][i], end="")
    if (i % 3 == 0 and i + 1 < len(split[0])):
        print(',', end="")
print('.'+split[1] + " or ", end="")

scientific = "{:.2e}".format(all_sec)
print(scientific + " in scientific notation")
print(datetime.fromtimestamp(all_sec).strftime("%B %d %Y"))
