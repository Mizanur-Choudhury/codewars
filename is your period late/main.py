from datetime import date, timedelta


def is_period_late(last: date, today: date, cycleLength: int) -> (date, date, int):
    cycle_delta = timedelta(days=cycleLength)
    expected_period_date = last + cycle_delta
    if today > expected_period_date:
        print("True")
        return True
    else:
        print("False")
        return False


"""The function first calculates the expected date of the next period by adding the cycle length to the last period 
date. It then checks whether today's date is later than the expected period date. If today's date is later, 
it means the period is late, and the function returns True. Otherwise, it returns False. 

Note that this function assumes that the cycle length is fixed and that periods are regular. It may not work 
accurately for irregular cycles or for cases where there are other factors affecting the timing of the period. """

if __name__ == "__main__":
    is_period_late(
        date(2023, 3, 24),
        date(2023, 4, 30),
        28
    )
    is_period_late(date(2016, 1, 1), date(2016, 2, 1), 30)
