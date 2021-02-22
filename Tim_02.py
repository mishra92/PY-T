from datetime import datetime

inputTi = '8:50:48 PM'

in_time = datetime.strptime(inputTi, "%I:%M:%S %p")

out_time = datetime.strftime(in_time, "%H:%M:%S")

print(out_time)