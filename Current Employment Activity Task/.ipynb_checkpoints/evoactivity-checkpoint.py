import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import calendar as c

payfile = './files/protected_payments.csv'
memfile = './files/protected_memberships.csv'
clifile = './files/protected_clients.csv'
__version__ = '1.0.2'
sns.set()


def generate(payments=pd.read_csv(payfile), memberships=pd.read_csv(memfile)):
    # manipulating payments
    payments = payments.drop(columns=['Payment Time'])
    payments['Payment Date'] = pd.to_datetime(payments['Payment Date'])

    # manipulating memberships
    memberships['Member Joining Date'] = pd.to_datetime(memberships['Member Joining Date'])
    memberships['Membership Start Date'] = pd.to_datetime(memberships['Membership Start Date'])
    memberships['Membership Completed On'] = pd.to_datetime(memberships['Membership Completed On'])
    memberships = memberships[memberships['Division Name'] == 'Gym Membership']
    return payments, memberships


def generate_clients(memberships=pd.read_csv(clifile)):
    # manipulating memberships
    memberships['Membership Start Date'] = pd.to_datetime(memberships['Membership Start Date'])
    memberships['Membership End Date'] = pd.to_datetime(memberships['Membership End Date'])
    return memberships


def members_by_month():
    payments, memberships = generate()
    mem_month = memberships.groupby(memberships['Membership Start Date'].dt.month).agg('count')[['Member Joining Date']]
    mem_month = mem_month.rename(columns={'Member Joining Date': 'New Members'})
    mem_month = mem_month.drop(12)
    mem_month.index = [c.month_abbr[x] for x in mem_month.index]
    return mem_month


def clients_by_month():
    clients = generate_clients()
    cli_month = clients.groupby(clients['Membership Start Date'].dt.month).agg('count')[['Membership Start Date']]
    cli_month = cli_month.rename(columns={'Membership Start Date': 'New Clients'})
    cli_month.index = [c.month_abbr[x] for x in cli_month.index]
    cli_month = cli_month.drop('Nov')
    return cli_month


def payments_by_month():
    payments, memberships = generate()
    pay_month = payments.groupby(payments['Payment Date'].dt.month).agg('sum')[['Payment Amount ($)']]
    pay_month.index = [c.month_abbr[x] for x in pay_month.index]
    return pay_month


def merge_frames():
    mem_month = members_by_month()
    pay_month = payments_by_month()
    merged = mem_month.merge(pay_month, on=mem_month.index)
    merged = merged.rename(columns={'key_0': 'Month'})
    merged = merged.set_index('Month')
    return merged
