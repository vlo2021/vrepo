# file1.txt
"""2026-04-20T10:00:00Z auth-service ERROR Failed login for user123
2026-04-20T10:00:01Z payment-service INFO Payment processed
2026-04-20T10:00:02Z auth-service ERROR Failed login for user456
2026-04-20T10:00:03Z auth-service INFO User logged out
2026-04-20T10:00:04Z payment-service ERROR Card declined"""

#############################################################

def is_within_this_time(start_time, end_time, time_stamp):
    if time_stamp >= start_time and time_stamp <= end_time:
        return True
    else:
        return False


#############################################################
d={}
count = 0
s_time = '10:00:00'
e_time = '10:00:04'

with open("file1.txt") as f:

    for line in f:
        parts = line.rstrip().split(' ')

        date,t = parts[0].split('T',2)
        time_frame,t= t.split('Z')

        if is_within_this_time(s_time, e_time, time_frame):
            if parts[2] == "ERROR":
                count = d.get(parts[1])
                if count is None:
                    d[parts[1]] = 1
                else:
                    d[parts[1]] = count + 1
        else:
            break

print(d)

#############################################################
def get_error_num(service):
    return service[1]

error_services_list = list(d.items())

sorted_error_service = sorted(error_services_list , key=get_error_num, reverse=True)
print(sorted_error_service)


#############################################################
