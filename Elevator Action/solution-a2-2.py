import queue

"""Description:
You're an elevator.
People on each floor get on you in the order they are queued as long as you're
stopped on their floor.
Your doors are one-person wide. No one can board you when someone else: is
departing or vice versa.
You must stop at each floor you pass that you can drop off and/or pick up
passengers.
Conversely, you don't stop if you're not changing passengers.
You can't switch directios while holding passengers. People won't get on you
if you're not going in the directio they want to go. During a stop, all
passengers who can get off gets off BEFORE any new passengers could get on.
When you're empty (at any point), you must go TOWARD the next person in the
queue, taking anyone going in that directio along your path if you're capable.
When you're empty AND you're on the same floor as the next person in the queue,
you must now go in the directio they want to go.
You must stop to open your doors, even if you haven't moved a floor. You begin
each day with closed doors.
Up to 5 people can be on you at a time.
Given a starting_floor and a queue of people represented by from the floor
they're on to the floor they want to go, return the order of stops you will
take this day.
Example
Given this queue:

queue = [
  { "from": 3, "to": 2 }, # Al
  { "from": 5, "to": 2 }, # Betty
  { "from": 2, "to": 1 }, # Charles
  { "from": 2, "to": 5 }, # Dan
  { "from": 4, "to": 3 }, # Ed
]

then

starting_floor = 1
order(starting_floor, queue)

should return:

[2, 5, 4, 3, 2, 1]

Explanation
You start on floor 1. Al is the first to queue for the elevator so you make your
way toward him traveling UP.
Going up a floor, you notice Charles and Dan on floor 2, however only Dan wants
to go up so your first stop is 2 to pick up Dan.
Going up to floor 3, you have now reached Al, but unfortunately for him, he
wants to go down, and you can't switch directios until you drop off Dan. You
promise to get Al later, so you pass him for now.
With no one else going up on your path, your second stop is 5 to drop off Dan.
Now that you're empty, you move toward Al again who is now below you. Since you
begin traveling DOWN, Betty, who's also on floor 5, joins you.
You stop on 4 to pick up Ed who is also going down.
You stop on 3 to drop off Ed. Meanwhile, you finally pick up Al.
You stop on 2 to drop off Al and Betty. You finally pick up Charles.
You stop on 1 to drop off Charles, the last person to transport.
Final Note
The building you operate in may have ANY arbitrarily large number of stories
(or basements) that people will want to travel between. For a given day, you
should not expect more than 500 people to ride you.
"""


def get_max_floor_in_queue(queue):
    return max(
        max(queue, key=lambda p: p["from"])["from"],
        max(queue, key=lambda p: p["to"])["to"],
    )


def get_min_floor_in_queue(queue):
    return min(
        min(queue, key=lambda p: p["from"])["from"],
        min(queue, key=lambda p: p["to"])["to"],
    )


def get_elevator_direction(
    elevator_direction, current_floor, min_floor_in_queue, max_floor_in_queue
):
    if (
        current_floor == min_floor_in_queue
        and elevator_direction == -1
        or current_floor == max_floor_in_queue
        and elevator_direction == 1
    ):
        return -elevator_direction
    return elevator_direction


def get_current_passenger_direction(p):
    return 1 if p["from"] < p["to"] else -1


def _del_passenders(buf: list, passengers: list):
    for b in buf:
        if b in passengers:
            passengers.remove(b)
    return passengers


# *******************************
def order(starting_floor: int, queue: list):
    stops = []
    passengers_on_elevator = []
    passengers_on_current_floor = []
    max_floor_in_queue = get_max_floor_in_queue(queue)
    min_floor_in_queue = get_min_floor_in_queue(queue)
    current_floor = starting_floor
    elevator_direction = 1 if queue[0]["from"] > current_floor else -1

    while queue or passengers_on_elevator:
        # Проверяем есть ли пассажиры в лифте. Если да, то высаживаем тех,
        # кому нужно выйти на текущем этаже.

        if passengers_on_elevator:
            buf = []
            for p in passengers_on_elevator:
                if p["to"] == current_floor:
                    if stops == [] or stops[-1] != current_floor:
                        stops.append(current_floor)
                    buf.append(p)
            # Удалить записанного пассажира из списка...
            passengers_on_elevator = _del_passenders(buf, passengers_on_elevator)
            buf.clear()

        # Проверяем пассажиров на теущем этаже. Если есть попутные пассажиры, то
        # берём их в лифт.
        if queue:
            p0 = queue[0]
        passengers_on_current_floor = [p for p in queue if p["from"] == current_floor]
        if passengers_on_current_floor:
            if not passengers_on_elevator and current_floor == p0["from"]:
                if p0["from"] > p0["to"]:
                    elevator_direction = -1
                if p0["from"] < p0["to"]:
                    elevator_direction = 1

            buf = []
            for p in passengers_on_current_floor:
                if get_current_passenger_direction(p) == elevator_direction:
                    if not stops or stops[-1] != current_floor:
                        stops.append(current_floor)
                    if len(passengers_on_elevator) <= 5:
                        passengers_on_elevator.append(p)
                    queue.remove(p)
                    buf.append(p)
            # Удалить записанного пассажира из списка...
            passengers_on_current_floor = _del_passenders(
                buf, passengers_on_current_floor
            )
            buf.clear()

        current_floor = current_floor + elevator_direction

        if current_floor == max_floor_in_queue:
            elevator_direction = -1
        if current_floor == min_floor_in_queue:
            elevator_direction = 1

    return stops


# # test case 1
puzzle = [
    {"from": 3, "to": 2},  # Al
    {"from": 5, "to": 2},  # Betty
    {"from": 2, "to": 1},  # Charles
    {"from": 2, "to": 5},  # Dan
    {"from": 4, "to": 3},  # Ed
]
solution = [2, 5, 4, 3, 2, 1]
result = order(1, puzzle)
print(f"False {result}" if result != solution else True)

# # test case 2
# puzzle = [{"from": 5, "to": 3}, {"from": 4, "to": 2}]
# solution = [5, 4, 3, 2]
# result = order(1, puzzle)
# print(f"False {result}" if result != solution else True)

# # test case 3
# puzzle = [{"from": 5, "to": 3}, {"from": 2, "to": 4}, {"from": 2, "to": 3}]
# solution = [2, 3, 4, 5, 3]
# result = order(1, puzzle)
# print(f"False {result}" if result != solution else True)

# # test case 4
# puzzle = [{"from": 5, "to": 3}, {"from": 4, "to": 2}]
# solution = [5, 4, 3, 2]
# result = order(4, puzzle)
# print(f"False {result}" if result != solution else True)

# # test case 5
# puzzle = [{"from": 4, "to": 2}, {"from": 5, "to": 3}]
# solution = [4, 2, 5, 3]
# result = order(4, puzzle)
# print(f"False {result}" if result != solution else True)

# # test case 6
# puzzle = [{"from": 5, "to": 1}, {"from": 4, "to": 3}, {"from": 2, "to": 1}]
# solution = [5, 4, 3, 2, 1]
# result = order(1, puzzle)
# print(f"False {result}" if result != solution else True)

# # test case 7
# puzzle = [
#     {"from": 5, "to": 1},
#     {"from": 4, "to": 3},
#     {"from": 2, "to": 1},
#     {"from": 2, "to": 4},
#     {"from": 5, "to": 2},
# ]
# solution = [2, 4, 5, 4, 3, 2, 1]
# result = order(1, puzzle)
# print(f"False {result}" if result != solution else True)

# # test case 8
# puzzle = [
#     {"from": 4, "to": 3},
#     {"from": 4, "to": 3},
#     {"from": 4, "to": 3},
#     {"from": 4, "to": 3},
#     {"from": 5, "to": 1},
#     {"from": 2, "to": 3},
#     {"from": 2, "to": 4},
#     {"from": 5, "to": 2},
# ]
# solution = [2, 3, 4, 3, 5, 2, 1]
# result = order(1, puzzle)
# print(f"False {result}" if result != solution else True)

# test case 9
# # print(order(starting_floor, []) == [])

# test case 10
puzzle = [
    {"from": 3, "to": 2},  # 3rd passenger
    {"from": 5, "to": 6},  # 4th passenger
    {"from": 2, "to": 1},  # 5th passenger
    {"from": 2, "to": 5},  # 1st passenger
    {"from": 4, "to": 3},  # 2nd passenger
]
solution = [2, 5, 4, 3, 2, 5, 6, 2, 1]
result = order(1, puzzle)
print(f"False {result}" if result != solution else True)

# # test case 11
# puzzle = [
#     {"from": 3, "to": 6},  # 16th passenger
#     {"from": 2, "to": 6},  # 1st  passenger
#     {"from": 2, "to": 6},  # 2nd  passenger
#     {"from": 2, "to": 6},  # 3rd  passenger
#     {"from": 2, "to": 6},  # 4th  passenger
#     {"from": 2, "to": 6},  # 5th  passenger
#     {"from": 2, "to": 6},  # 10th passenger
#     {"from": 2, "to": 6},  # 11th passenger
#     {"from": 2, "to": 6},  # 12th passenger
#     {"from": 2, "to": 6},  # 13th passenger
#     {"from": 3, "to": 2},  # 8th  passenger
#     {"from": 5, "to": 6},  # 15th passenger
#     {"from": 2, "to": 1},  # 9th  passenger
#     {"from": 2, "to": 5},  # 14th passenger
#     {"from": 4, "to": 3},  # 7th  passenger
#     {"from": 6, "to": 1},  # 6th  passenger
# ]
# solution = [2, 6, 4, 3, 2, 1, 2, 5, 6, 3, 6]
# result = order(1, puzzle)
# print(f"False {result}" if result != solution else True)

# # test case 12
# puzzle = [
#     {"from": 3, "to": 2},  # Al
#     {"from": 5, "to": 2},  # Betty
#     {"from": 2, "to": 1},  # Charles
#     {"from": 2, "to": 5},  # Dan
#     {"from": 4, "to": 3},  # Ed
# ]
# solution = [2, 5, 4, 3, 2, 1]
# result = order(1, puzzle)
# print(f"False {result}" if result != solution else True)

# # test case 13
# puzzle = [
#     {"from": 3900, "to": 500},
#     {"from": 450000, "to": 50000000},
#     {"from": 1800, "to": -400},
#     {"from": 4300, "to": 500},
# ]
# solution = [3900, 1800, 500, -400, 450000, 50000000, 4300, 500]
# result = order(1, puzzle)
# print(f"False {result}" if result != solution else True)

# # test case 14
# puzzle = [
#     {"from": 5, "to": 4},  # 1st
#     {"from": 5, "to": 3},  # 2nd
#     {"from": 3, "to": 4},  # 3rd
#     {"from": 0, "to": 2},  # 5th
#     {"from": 3, "to": -4},  # 4th
#     {"from": 1, "to": 2},
# ]  # 6th
# solution = [5, 4, 3, 4, 3, -4, 0, 1, 2]
# result = order(1, puzzle)
# print(f"False {result}" if result != solution else True)

# test case 15
# puzzle = [
#     {"from": 39, "to": 14},
#     {"from": 6, "to": 0},
#     {"from": 10, "to": 6},
#     {"from": 8, "to": 43},
#     {"from": 20, "to": 2},
#     {"from": 7, "to": 32},
#     {"from": 41, "to": 37},
#     {"from": 37, "to": 21},
#     {"from": 19, "to": -1},
#     {"from": 21, "to": 4},
#     {"from": 1, "to": 23},
#     {"from": 34, "to": -3},
#     {"from": 19, "to": -3},
#     {"from": 9, "to": 39},
#     {"from": 0, "to": 26},
#     {"from": 26, "to": 18},
#     {"from": 36, "to": 18},
#     {"from": 6, "to": 33},
# ]
# solution = [
#     39,
#     37,
#     36,
#     34,
#     26,
#     21,
#     18,
#     14,
#     10,
#     6,
#     4,
#     0,
#     -3,
#     0,
#     1,
#     6,
#     7,
#     8,
#     23,
#     26,
#     32,
#     33,
#     43,
#     41,
#     37,
#     20,
#     19,
#     2,
#     -1,
#     -3,
#     9,
#     39,
# ]
# result = order(1, puzzle)
# print(f"False {result}" if result != solution else True)
