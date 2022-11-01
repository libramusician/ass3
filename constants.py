OWNER = "owner"

TYPE = "type"

TECHNICAL_SUPPORT = "Technical_Support"

FINANCIAL_PLANNER = "Financial_Planner"

INVESTMENT_ANALYST = "Investment_Analyst"

PREMIUM = "Premium"

COMPLIANCE_OFFICER = "Compliance_Officer"

FINANCIAL_ADVISOR = "Financial_Advisor"

TELLER = "teller"

CLIENT = "client"

ACCOUNT_BALANCE = "account_balance"
INFO = "information"
INVESTMENT_PORTFOLIO = "investment_portfolio"
FINANCIAL_ADVISOR_CONTACT = "Financial_Advisor_Contact"
INVESTMENT_ANALYST_CONTACT = "Investment_Analyst_Contact"
FINANCIAL_PLANNER_CONTACT = "Financial_Planner_Contact"
MONEY_MARKET_INSTRUMENT = "money market instruments"
PRIVATE_CONSUMER_INSTRUMENTS = "private consumer instruments"
DERIVATIVES_TRADING = "derivatives trading"
INTEREST_INSTRUMENTS = "interest instruments"

VFS = {
    # private information
    "Mischa Lowery's info": {
        TYPE: INFO,
        OWNER: "Mischa Lowery"
    },
    "Mischa Lowery's account balance": {
        TYPE: ACCOUNT_BALANCE,
        OWNER: "Mischa Lowery"
    },
    "Mischa Lowery's investment portfolio": {
        TYPE: INVESTMENT_PORTFOLIO,
        OWNER: "Mischa Lowery"
    },
    "Veronica Perez's info": {
        TYPE: INFO,
        OWNER: "Veronica Perez"
    },
    "Veronica Perez's account balance": {
        TYPE: ACCOUNT_BALANCE,
        OWNER: "Veronica Perez"
    },
    "Veronica Perez's investment portfolio": {
        TYPE: INVESTMENT_PORTFOLIO,
        OWNER: "Veronica Perez"
    },
    "Willow Garza's info": {
        TYPE: INFO,
        OWNER: "Willow Garza"
    },
    "Willow Garza's account balance": {
        TYPE: ACCOUNT_BALANCE,
        OWNER: "Willow Garza"
    },
    "Willow Garza's investment portfolio": {
        TYPE: INVESTMENT_PORTFOLIO,
        OWNER: "Willow Garza"
    },
    "Nala Preston's info": {
        TYPE: INFO,
        OWNER: "Nala Preston"
    },
    "Nala Preston 's account balance": {
        TYPE: ACCOUNT_BALANCE,
        OWNER: "Nala Preston"
    },
    "Nala Preston 's investment portfolio": {
        TYPE: INVESTMENT_PORTFOLIO,
        OWNER: "Nala Preston"
    },

    # protected information
    "Nelson Wilkins's contact": {
        TYPE: FINANCIAL_ADVISOR_CONTACT,
        OWNER: "public"
    },
    "Kelsie Chang's contact": {
        TYPE: FINANCIAL_ADVISOR_CONTACT,
        OWNER: "public"
    },
    "Stacy Kent's contact": {
        TYPE: INVESTMENT_ANALYST_CONTACT,
        OWNER: "public"
    },
    "Keikilana Kapahu's contact": {
        TYPE: INVESTMENT_ANALYST_CONTACT,
        OWNER: "public"
    },
    "Kodi Matthews's contact": {
        TYPE: FINANCIAL_PLANNER_CONTACT,
        OWNER: "public"
    },
    "Malikah Wu's contact": {
        TYPE: FINANCIAL_PLANNER_CONTACT,
        OWNER: "public"
    },
    "money market instruments": {
        TYPE: MONEY_MARKET_INSTRUMENT,
        OWNER: "public"
    },
    "private consumer instruments": {
        TYPE: PRIVATE_CONSUMER_INSTRUMENTS,
        OWNER: "public"
    },
    "derivatives trading": {
        TYPE: DERIVATIVES_TRADING,
        OWNER: "public"
    },
    "interest instruments": {
        TYPE: INTEREST_INSTRUMENTS,
        OWNER: "public"
    },
}

ROLE = {
    "Mischa Lowery": CLIENT,
    "Veronica Perez": CLIENT,
    "Winston Callahan": TELLER,
    "Kelan Gough": TELLER,
    "Nelson Wilkins": FINANCIAL_ADVISOR,
    "Kelsie Chang": FINANCIAL_ADVISOR,
    "Howard Linkler": COMPLIANCE_OFFICER,
    "Stefania Smart": COMPLIANCE_OFFICER,
    "Willow Garza": PREMIUM,
    "Nala Preston": PREMIUM,
    "Stacy Kent": INVESTMENT_ANALYST,
    "Keikilana Kapahu": INVESTMENT_ANALYST,
    "Kodi Matthews": FINANCIAL_PLANNER,
    "Malikah Wu": FINANCIAL_PLANNER,
    "Caroline Lopez": TECHNICAL_SUPPORT,
    "Pawel Barclay": TECHNICAL_SUPPORT,
    "public": "public"
}