import streamlit as st
import pandas as pd
from datetime import datetime, timedelta

def draw_calendar(year, month):
    month_start = datetime(year, month, 1)
    month_end = (month_start + timedelta(days=31)).replace(day=1) - timedelta(days=1)
    
    # Initialize a list for storing days and events
    calendar_days = []
    current_day = month_start
    
    # Fill the calendar_days list with days and corresponding events
    while current_day <= month_end:
        calendar_days.append({
            'day': current_day.day,
            'weekday': current_day.weekday(),
            'date': current_day
        })
        current_day += timedelta(days=1)
    
    return calendar_days

def render_calendar(calendar_days, events):
    # Create a DataFrame for easy manipulation
    df = pd.DataFrame(calendar_days)
    
    # Map weekdays to their names
    weekdays = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    
    # Add events to the DataFrame
    df['event'] = df['date'].apply(lambda x: ', '.join(events.get(x, [])))
    
    # Create the calendar view
    st.write(" | ".join(weekdays))
    week = [""] * 7
    
    for index, row in df.iterrows():
        week[row['weekday']] = f"{row['day']} ({row['event']})"
        if row['weekday'] == 6:  # End of the week
            st.write(" | ".join(week))
            week = [""] * 7
    
    if any(week):  # Print the remaining days
        st.write(" | ".join(week))

def calendar():
    st.title('가족 캘린더')

    # Login status check
    if 'logged_in' not in st.session_state or not st.session_state.logged_in:
        st.warning('로그인이 필요합니다. 로그인 해주세요.')
        st.stop()

    # Initialize events storage
    if 'events' not in st.session_state:
        st.session_state.events = {}

    # Input for adding events
    event = st.text_input('일정')
    date = st.date_input('날짜')

    if st.button('Add Event'):
        if event and date:
            if date in st.session_state.events:
                st.session_state.events[date].append(event)
            else:
                st.session_state.events[date] = [event]
            st.success(f'Event "{event}" added on {date}')
        else:
            st.warning('Please enter both event and date.')

    # Select month and year to display
    today = datetime.today()
    year = st.number_input('Year', min_value=1900, max_value=2100, value=today.year)
    month = st.number_input('Month', min_value=1, max_value=12, value=today.month)
    
    # Generate calendar
    calendar_days = draw_calendar(year, month)
    render_calendar(calendar_days, st.session_state.events)

if __name__ == "__main__":
    calendar()
