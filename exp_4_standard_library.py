# %% Open the datetime library
import datetime

#%% get the current date
current_date = datetime.date.today()
print(current_date)

# %% get the current date and time
current_date_time = datetime.datetime.now()
print(current_date_time)

# %% define a date
christmas_day = datetime.date(2023, 12, 25)
print(christmas_day)

# %% subtracting the two dates --> returns a "timedelta" object
days_before_christmas = christmas_day - current_date
print(days_before_christmas)

# %% add 50 days
future_date = current_date + datetime.timedelta(days=50)
print(future_date)

# %% subtract 10 weeks
past_date = current_date - datetime.timedelta(weeks=10)
print(past_date)

# %% How many days to you live currently
birthday_date = datetime.date(1990, 4, 10)
total_days = current_date - birthday_date
print(total_days)

# %%
birthday_date_time = datetime.datetime(1990, 4, 10, 1, 10, 0)
total_time = current_date_time - birthday_date_time
print(total_time)

# %%
