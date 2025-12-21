

import datetime

for month_index in range(1, 13):
    month_name = datetime.date(2000, month_index, 1).strftime('%B')
    print(month_name)
