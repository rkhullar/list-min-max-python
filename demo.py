"""
@author  :  Rajan Khullar
@created :  02/07/16
@updates :  02/07/16
"""

dict = {}

row = None
sym = None
val = None

with open('data.csv', 'r') as file:
    # skip header row
    next(file)
    for line in file:
        # get data
        row = line.split(';')
        sym = row[0].strip()
        val = int(row[1].strip())
        # test for new symbolo
        if sym not in dict:
            dict[sym] = [val, val]
        else:
            # test for new min
            if val < dict[sym][0]:
                dict[sym][0] = val
            # test for new max
            if val > dict[sym][1]:
                dict[sym][1] = val

for sym in dict:
    print("[{:1s}] [{:4d} : {:4d}]".format(sym, dict[sym][0], dict[sym][0]))
