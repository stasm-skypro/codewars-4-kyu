def format_duration(seconds):
    t = seconds
    if t == 0:
        return "now"

    s = ["seconds", "second"]
    m = ["minutes", "minute"]
    h = ["hours", "hour"]
    d = ["days", "day"]
    y = ["years", "year"]

    year, day, hour, min, sec = 0, 0, 0, 0, 0

    # Вычисляем секунды
    carry, remainder = divmod(t, 60)
    sec = f"{remainder} {s[1 if remainder == 1 else 0]}" if remainder > 0 else ""
    t = carry

    # Вычисляем минуты
    carry, remainder = divmod(t, 60)
    min = f"{remainder} {m[1 if remainder == 1 else 0]}" if remainder > 0 else ""
    t = carry

    # Вычисляем часы
    carry, remainder = divmod(t, 24)
    hour = f"{remainder} {h[1 if remainder == 1 else 0]}" if remainder > 0 else ""
    t = carry

    # Вычисляем дни
    carry, remainder = divmod(t, 365)
    day = f"{remainder} {d[1 if remainder == 1 else 0]}" if remainder > 0 else ""
    t = carry

    # Вычисляем годы
    carry, remainder = divmod(t, 10)
    year = f"{remainder} {y[1 if remainder == 1 else 0]}" if remainder > 0 else ""
    t = carry

    result = [item for item in (year, day, hour, min, sec) if item]
    if len(result) == 1:
        out = "".join(result)
        return out
    out = ", ".join(result[:-1]) + " and " + result[-1]
    return out


# test cases
print(format_duration(0) == "now")
print(format_duration(1) == "1 second")
print(format_duration(62) == "1 minute and 2 seconds")
print(format_duration(120) == "2 minutes")
print(format_duration(3600) == "1 hour")
print(format_duration(3662) == "1 hour, 1 minute and 2 seconds")
print(format_duration(15731080) == "182 days, 1 hour, 44 minutes and 40 seconds")
print(format_duration(132030240) == "4 years, 68 days, 3 hours and 4 minutes")
print(format_duration(205851834) == "6 years, 192 days, 13 hours, 3 minutes and 5econds")
print(
    format_duration(253374061) == "8 years, 12 days, 13 hours, 41 minutes and 1 second"
)
print(
    format_duration(242062374)
    == "7 years, 246 days, 15 hours, 32 minutes and 54 seconds"
)
print(
    format_duration(101956166) == "3 years, 85 days, 1 hour, 9 minutes and 26 seconds"
)
print(
    format_duration(33243586) == "1 year, 19 days, 18 hours, 19 minutes and 46 seconds"
)
