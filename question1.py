from constants import *


def role(user):
    with open("role.txt", "r") as f:
        lines = f.readlines()
        for line in lines:
            words = line.split(":")
            username = words[0]
            if username == user:
                return words[1]

def id(user):
    with open("role.txt", "r") as f:
        lines = f.readlines()
        for line in lines:
            words = line.split(":")
            username = words[0]
            if username == user:
                return words[2]


def f_type(file):
    return VFS[file][TYPE]


def owner(file):
    return VFS[file][OWNER]


def in_office_hour(time):
    if 9 <= time < 17:
        return True
    else:
        return False


def can_view(user, file, time):
    # all clients can view all Financial Advisor contact
    if role(user) in [CLIENT, PREMIUM] and f_type(file) == FINANCIAL_ADVISOR_CONTACT:
        return True
    # all premium clients can view all Investment Analyst contact, Financial Planner contact
    elif role(user) == PREMIUM and f_type(file) in [INVESTMENT_ANALYST_CONTACT, FINANCIAL_PLANNER_CONTACT]:
        return True
    # all clients can view their own account balance and investment portfolio
    elif role(user) in [CLIENT, PREMIUM] and owner(file) == user and \
            f_type(file) in [ACCOUNT_BALANCE, INVESTMENT_PORTFOLIO]:
        return True
    # all employees (except IT, teller must in business hour) can view client’s account balance and investment portfolio
    elif (role(user) in [FINANCIAL_ADVISOR, INVESTMENT_ANALYST, FINANCIAL_PLANNER] or
          (role(user) == TELLER and in_office_hour(time))) and role(owner(file)) in [CLIENT, PREMIUM] and \
            f_type(file) in [ACCOUNT_BALANCE, INVESTMENT_PORTFOLIO]:
        return True
    # Financial Planner can view money market instruments
    elif role(user) == FINANCIAL_PLANNER and f_type(file) == MONEY_MARKET_INSTRUMENT:
        return True
    # Financial Advisors and Financial Planners can view private consumer instruments
    elif role(user) in [FINANCIAL_ADVISOR, FINANCIAL_PLANNER] and f_type(file) == PRIVATE_CONSUMER_INSTRUMENTS:
        return True
    # Investment Analysts can view money market instruments,
    # derivatives trading, interest instruments, and private consumer instruments.
    elif role(user) == INVESTMENT_ANALYST and f_type(file) in \
            [MONEY_MARKET_INSTRUMENT, DERIVATIVES_TRADING, INTEREST_INSTRUMENTS, PRIVATE_CONSUMER_INSTRUMENTS]:
        return True
    # Technical Support can view a client’s information
    elif role(user) == TECHNICAL_SUPPORT and f_type(file) == INFO:
        return True
    # Compliance Officers can view  investment portfolios.
    elif role(user) == COMPLIANCE_OFFICER and f_type(file) == INVESTMENT_PORTFOLIO:
        return True
    else:
        return False


def can_modify(user, file):
    # premium client can modify his own investment portfolio
    if role(user) == PREMIUM and owner(file) == user and f_type(file) == INVESTMENT_PORTFOLIO:
        return True
    # Financial Advisors, Financial Planners, and Investment Analysts can modify a client’s investment portfolio
    elif role(user) in [FINANCIAL_ADVISOR, FINANCIAL_PLANNER, INVESTMENT_ANALYST] and role(owner(file)) in \
            [CLIENT, PREMIUM] and f_type(file) == INVESTMENT_PORTFOLIO:
        return True
    else:
        return False


def can_access(user, file, approved):
    if role(user) == TECHNICAL_SUPPORT and role(owner(file)) in [CLIENT, PREMIUM] and approved:
        return True
    else:
        return False
