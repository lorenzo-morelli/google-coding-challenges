### TIMETABLE MATCHING

# A: [[9:00, 11:30], [12:30, 15:00], [16:00, 18:00]]
# B: [[9:30, 11:00], [15:20, 16:30], [17:00, 18:30]]
# Minimum: 30

# output: [[11:30, 12:30]]

def compare(time1, time2):
    hour1, minute1 = time1.split(":")
    hour2, minute2 = time2.split(":")
    time1 = int(hour1) * 60 + int(minute1)
    time2 = int(hour2) * 60 + int(minute2)
    diff = time2 - time1
    return diff


def unavailable(sched1, sched2):
    booked = []
    p1 = 0
    p2 = 0
    while p1 < len(sched1) or p2 < len(sched2) - 1:
        if compare(sched1[p1][0], sched2[p2][0]) > 0:
            booked.append(sched1[p1])
            p1 += 1
        else:
            booked.append(sched2[p2])
            p2 += 1
    return booked


def remove_repetitions(booked):
    i = 0
    while i < len(booked) - 1:
        if compare(booked[i][1], booked[i + 1][1]) <= 0:
            booked.pop(i+1)
        elif compare(booked[i][1], booked[i + 1][0]) <= 0:
            booked[i][1] = booked[i + 1][1]
            booked.pop(i+1)
        else:
            i += 1
    return booked


def available(booked, min):
    avail = []
    i = 0
    while i < len(booked) - 1:
        if compare(booked[i][1], booked[i+1][0]) >= min:
            freespace = []
            freespace.append(booked[i][1])
            freespace.append(booked[i + 1][0])
            avail.append(freespace)
        i += 1
    return avail


# TEST
schedule1 = [["9:00", "11:30"], ["12:30", "15:00"], ["16:00", "18:00"]]
schedule2 = [["9:30", "11:00"], ["15:20", "16:30"], ["17:00", "18:30"]]
minimum = 30
full = unavailable(schedule1, schedule2)
full = remove_repetitions(full)
free = available(full, minimum)
print(free)
