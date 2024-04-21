def get_depo_profit(money, time, percentage):
    profit = money * (1 + percentage / 100) ** time
    return profit

