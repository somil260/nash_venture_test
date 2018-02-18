import time


max_val = 20
min_val = 10

mid_val = min_val + max_val>>1
max_list, min_list = [], []


class RandomNumber():
    def random(self, min_val, max_val):
        cur_time = time.time() * 234 * 322	# Time Multiply by  random digit
        num = cur_time - int(cur_time)      # get only float value
        value = num * (max_val-min_val) + min_val
        return int(value)


while len(max_list) != 73:
    val = RandomNumber().random(mid_val, max_val)
    max_list.append(val)
    
while len(min_list) != 27:
    val = RandomNumber().random(min_val, mid_val)
    min_list.append(val)

print max_list, min_list
