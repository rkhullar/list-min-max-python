"""
@author  :  Rajan Khullar
@created :  02/07/16
@updated :  02/14/16
"""

dict = {}

row = None
sym = None
val = None


class Stat:
    def __init__(self, v):
        self.min = v
        self.max = v

with open('data.csv', 'r') as file:
    # skip header row
    next(file)
    for line in file:
        # get data
        row = line.split(';')
        sym = row[0].strip()
        val = int(row[1].strip())
        # test for new symbol
        if sym not in dict:
            dict[sym] = Stat(val)
        else:
            # test for new min
            if val < dict[sym].min:
                dict[sym].min = val
            # test for new max
            if val > dict[sym].max:
                dict[sym].max = val

for sym in dict:
    print("[{:1s}] [{:4d} : {:4d}]".format(sym, dict[sym].min, dict[sym].max))
