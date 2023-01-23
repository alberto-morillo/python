import argparse
import math


parser = argparse.ArgumentParser(description="This program is a credit \
calculator.")
parser.add_argument("--type")          # positional argument
parser.add_argument("--principal")
parser.add_argument("--periods")
parser.add_argument("--interest")
parser.add_argument("--payment")

args = parser.parse_args()             # reading arguments from CMD
option_user_has_chosen = args.type

def calc_differentiated_payments():
    loan_principal = float(args.principal)
    number_monthly_payments = int(args.periods)
    user_input_loan_interest = args.interest
    user_input_loan_interest = float(user_input_loan_interest)
    loan_interest = user_input_loan_interest / (12 * 100)
    sum_all_payments = 0
    for month_number in range(1,number_monthly_payments+1):
        calc_1_month_payment  =  (loan_principal / number_monthly_payments) + \
                                 (loan_interest * \
                                  (loan_principal - ((loan_principal * (month_number -1))/number_monthly_payments)) \
                                  )
        calc_1_month_payment = math.ceil(calc_1_month_payment)
        print(f"Month {month_number}: payment is {calc_1_month_payment}")
        sum_all_payments += calc_1_month_payment
    overpayment = int(sum_all_payments - loan_principal)
    print(f"Overpayment = {overpayment}")

def calc_annuity():
    user_input_loan_interest = args.interest
    user_input_loan_interest = float(user_input_loan_interest)
    loan_interest = user_input_loan_interest / (12 * 100)
    loan_principal = float(args.principal)
    number_monthly_payments = int(args.periods)

    calculated_monthly_payment = loan_principal * \
    (loan_interest * math.pow((loan_interest+1),number_monthly_payments)) / \
    (math.pow((loan_interest+1),number_monthly_payments) - 1)
    print(f"Your annuity payment = {math.ceil(calculated_monthly_payment)}!")
    overpayment = int((math.ceil(calculated_monthly_payment) * \
                   number_monthly_payments) - loan_principal)
    print(f"Overpayment = {overpayment}")

def calc_loan_principal():
    monthly_payment = float(args.payment)
    number_monthly_payments = int(args.periods)
    user_input_loan_interest = args.interest
    user_input_loan_interest = float(user_input_loan_interest)
    loan_interest = user_input_loan_interest / (12 * 100)

    calculated_loan_principal = monthly_payment / \
    ((loan_interest * math.pow((loan_interest+1),number_monthly_payments)) / \
    (math.pow((loan_interest+1),number_monthly_payments) - 1))
    print(f"Your loan principal = {math.floor(calculated_loan_principal)}!")
    overpayment = int((math.ceil(monthly_payment) * \
                   number_monthly_payments) - math.floor(calculated_loan_principal))
    print(f"Overpayment = {overpayment}")

def calc_mumber_monthly_payments():
    loan_principal = float(args.principal)
    monthly_payment = float(args.payment)
    user_input_loan_interest = args.interest
    user_input_loan_interest = float(user_input_loan_interest)
    loan_interest = user_input_loan_interest / (12 * 100)

    pow = (monthly_payment / (monthly_payment - loan_interest * loan_principal))
    log_base = 1 + loan_interest
    calc_number_monthly_payments = math.ceil(math.log(pow, log_base))
    if calc_number_monthly_payments == 1:
        print(f"It will take 1 month to repay this loan!")
    elif calc_number_monthly_payments < 12:
        print(f"It will take {calc_number_monthly_payments // 12} months to repay this loan!")
    elif calc_number_monthly_payments == 12:
        print(f"It will take 1 year to repay this loan!")
    elif calc_number_monthly_payments % 12 == 0:
        print(f"It will take {calc_number_monthly_payments // 12} years to repay this loan!")
    else:
        print(f"It will take {math.floor(calc_number_monthly_payments / 12)} years and {calc_number_monthly_payments % 12} months to repay this loan!")
    overpayment = int((monthly_payment * \
                   calc_number_monthly_payments) - loan_principal)
    print(f"Overpayment = {overpayment}")

v = vars(args)
n_args = sum([ 1 for a in v.values( ) if a])

if n_args < 4:
    print("Incorrect parameters")
    exit()
if str(args.interest) == "None" and option_user_has_chosen == "diff":
    print("Incorrect parameters")
    exit()
if str(args.payment) != "None" and float(args.payment) < 0:
    print("Incorrect parameters")
    exit()
if str(args.periods) != "None" and float(args.periods) < 0:
    print("Incorrect parameters")
    exit()
if str(args.interest) != "None" and float(args.interest) < 0:
    print("Incorrect parameters")
    exit()
if str(args.principal) != "None" and float(args.principal) < 0:
    print("Incorrect parameters")
    exit()

if option_user_has_chosen == "annuity" and str(args.principal) != "None" \
    and str(args.periods) != "None":
    calc_annuity()
elif option_user_has_chosen == "annuity" and str(args.principal) == "None":
    calc_loan_principal()
elif option_user_has_chosen == "annuity" and str(args.periods) == "None":
    calc_mumber_monthly_payments()
elif option_user_has_chosen == "diff":
    calc_differentiated_payments()
else:
    print("Incorrect parameters")