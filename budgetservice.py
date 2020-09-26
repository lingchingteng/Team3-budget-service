class Period(object):
    def __init__(self, start, end) -> None:
        self.start = start
        self.end = end

    def overlapping_days(self, budget):
        if self.start > self.end:
            return 0
        if self.end < budget.first_day() or self.start > budget.last_day():
            return 0

        overlapping_end = self.end if self.end < budget.last_day() else budget.last_day()
        overlapping_start = self.start if self.start > budget.first_day() else budget.first_day()
        return (overlapping_end - overlapping_start).days + 1


class BudgetService(object):
    def query(self, start, end):
        period = Period(start, end)
        total_amount = 0
        for budget in self.get_budgets():
            total_amount += round(budget.daily_amount() * period.overlapping_days(budget), 2)

        return total_amount

    def get_budgets(self):
        pass
