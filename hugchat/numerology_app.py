import streamlit as st
import datetime
from hugging_chat import connect_to_hugging_face
from hugging_chat import generate_response

st.set_page_config(page_title='Numerology App', page_icon='🤠')
st.title('My Num')
st.header(body='Welcome to you numerology reading bot', divider='rainbow', anchor='center')



if 'life_path' not in st.session_state:
    st.session_state.life_path = 0
if 'destiny' not in st.session_state:
    st.session_state.destiny = 0

def calculate_destiny_number(name):
    list = []
    string = ''
    st.write(name)
    for i in name:
        if i == ' ':
            list.append(string.lower())
            string = ''
        else:
            string += i
    list.append(string.lower())
    num = ''
    for word in list:
        part = 0
        for i in word:
            if i == 'a' or 'j' or 's':
                part += 1
            elif i == 'b' or 't' or 'k':
                part += 2
            elif i == 'l' or 'c' or 'u':
                part += 3
            elif i == 'm' or 'd' or 'v':
                part += 4
            elif i == 'n' or 'e' or 'w':
                part += 5
            elif i == 'o' or 'x' or 'f':
                part += 6
            elif i == 'p' or 'g' or 'y':
                part += 7
            elif i == 'q' or 'h' or 'z':
                part += 8
            elif i == 'r' or 'i':
                part += 9
            else:
                break
        while len(str(part)) > 1:
            part += sum(int(digit) for digit in str(part))
        num += str(part)
    while len(str(num)) > 1:
        num = sum(int(i) for i in str(num))
    st.write(num)
def calculate_life_path_number(date):
    """
    Calculate the life path number from a datetime object.

    Parameters:
        date (datetime): The date of birth.

    Returns:
        int: The life path number.
    """

    def reduce_to_single_or_master(num):
        """Reduce a number to a single digit or master number (11, 22, 33)."""
        while num > 9 and num not in (11, 22, 33):
            num = sum(int(digit) for digit in str(num))
        return num

    # Extract year, month, and day from the datetime object
    year = date.year
    month = date.month
    day = date.day

    # Reduce each component
    year_sum = reduce_to_single_or_master(year)
    month_sum = reduce_to_single_or_master(month)
    day_sum = reduce_to_single_or_master(day)

    # Sum up all parts and reduce again
    total_sum = year_sum + month_sum + day_sum
    life_path_number = reduce_to_single_or_master(total_sum)

    return life_path_number

def activate_lifepath():
    st.session_state.destiny = 0
    st.session_state.life_path = 1


def activate_destiny():
    st.session_state.life_path = 0
    st.session_state.destiny = 1


with st.chat_message("user"):
    st.write('Hello Human! What would you like me to calculate?')

    c1, c2 = st.columns(2)
    with c1:
        life_path = st.button("Life path number", on_click=activate_lifepath)
    with c2:
        destiny = st.button('Destiny number', on_click=activate_destiny)

if st.session_state.life_path == 1:
    with st.chat_message('user'):
        dob = st.date_input('What is your date of birth?')
        life_path_number = calculate_life_path_number(dob)
        confirm = st.button('click to confirm')
    if confirm:
        question = f"Your life path number of {life_path_number} means"
        prompt = f"What does the life path number {life_path_number} mean?"
        if prompt:
            with st.chat_message("assistant"):
                with st.spinner("Thinking..."):
                    response = generate_response(prompt)
                    st.write(response)


if st.session_state.destiny == 1:
    with st.chat_message('user'):
        name = st.text_input('What is your full name')
        if name:
            calculate_destiny_number(name)
