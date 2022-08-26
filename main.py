from tkinter import *

window = Tk()
window.title("Loan Payment Calculator")
window.minsize(width=250, height=300)
window.config(padx=30, pady=30)

loan_amount_label = Label(text='Loan Amount')
loan_amount_label.grid(column=2, row=1)

loan_amount = Entry()
loan_amount.grid(column=2, row=2)
loan_amount.focus()

interest_rate_label = Label(text='Interest Rate')
interest_rate_label.grid(column=2, row=3)

interest_rate = Entry()
interest_rate.grid(column=2, row=4)


def get_terms():
    return radio_state.get()


radio_state = IntVar()
yearly_term_radio = Radiobutton(text="Loan Term in Years", value=1, variable=radio_state, command=get_terms)
monthly_term_radio = Radiobutton(text="Loan Term in Months", value=2, variable=radio_state, command=get_terms)
yearly_term_radio.grid(column=2, row=5)
monthly_term_radio.grid(column=2, row=6)

term = Entry()
term.grid(column=2, row=7)


def calculate_payment():
    amount = float(loan_amount.get())
    rate = (float(interest_rate.get()) / 100) / 12
    length_of_loan = int(term.get())
    if get_terms() == 1:
        length_of_loan *= 12
    d = pow(1 + rate, length_of_loan)
    payment = round(((rate * d) / (d - 1)) * amount, 2)
    monthly_payment.config(text=f'Payment: \n${payment}')


calc_button = Button(text='Calculate Payment', command=calculate_payment)
calc_button.grid(column=2, row=8)

monthly_payment = Label()
monthly_payment.grid(column=2, row=9)

window.mainloop()
