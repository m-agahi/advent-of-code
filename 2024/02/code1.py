reports = []
safe_reports_count = 0
with open('input.txt', 'r', encoding='utf-8') as file:
    for line in file:
        report = line.strip().split(' ')
        reports.append([int(value) for value in report])

# Part 1

def continual_series(levels, mode="", print_errors=False):
    def error_message():
        return "Too much value" if abs(levels[0] - levels[1]) > 3 else "Sign"
    if len(levels) <= 1:
        return True
    elif mode == "":
        if levels[0] > levels[1] and 1 <= abs(levels[0] - levels[1]) <= 3:
            return continual_series(levels[1:], ">")
        elif levels[0] < levels[1] and 1 <= abs(levels[0] - levels[1]) <= 3:
            return continual_series(levels[1:], "<")
        else:
            if print_errors:
                print(levels[0], levels[1], abs(levels[0] - levels[1]), error_message())
            return False
    elif mode == ">":
        if levels[0] > levels[1] and 1 <= abs(levels[0] - levels[1]) <= 3:
            return continual_series(levels[1:], ">")
        else:
            if print_errors:
                print(levels[0], levels[1], abs(levels[0] - levels[1]), mode, error_message())
            return False
    elif mode == "<":
        if levels[0] < levels[1] and 1 <= abs(levels[0] - levels[1]) <= 3:
            return continual_series(levels[1:], "<")
        else:
            if print_errors:
                print(levels[0], levels[1], abs(levels[0] - levels[1]), mode, error_message())
            return False

for report in reports:
    if continual_series(report):
        safe_reports_count += 1

print(safe_reports_count)

# Part 2

safe_reports_count = 0

def continual_series_with_single_bad_level(levels, mode="", print_errors=False):
    def error_message():
        return "Too much value" if abs(levels[0] - levels[1]) > 3 else "Sign"
    if len(levels) <= 1:
        return True
    for index in range(len(levels)):
        modified_levels = levels.copy()
        modified_levels.pop(index)
        if continual_series(modified_levels):
            return True
    return False

for report in reports:
    if continual_series_with_single_bad_level(report):
        safe_reports_count += 1

print(safe_reports_count)