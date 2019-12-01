from __future__ import unicode_literals, print_function
from prompt_toolkit import print_formatted_text, HTML
from prompt_toolkit.styles import Style
from abc import ABC, abstractmethod 
import random
style = Style.from_dict({
    'aaa': '#ff0066',
    'bbb': '#44ff00 italic',
})
class MainAbstractClass(ABC):

    @abstractmethod
    def credit(self):
        pass
    
    @abstractmethod
    def debit(self):
        pass

    @abstractmethod
    def transfer(self):
        pass

    @abstractmethod
    def history(self):
        pass

        
class ATM(MainAbstractClass):
    def __init__(self):
        
        self.__all_account = [
            {1234 : {'name:' : 'raja','card_number:' : '9988771122','balance:' : 10000, 'total_no_transactions:' : 0, 'credit_count:' : 0, 'debit_count:' : 0, 'transfer_history:' : []}},
            {8888 : {'name:' : 'amirtha','card_number:' : '9988772233','balance:' : 10001, 'total_no_transactions:' : 0, 'credit_count:' : 0, 'debit_count:' : 0, 'transfer_history:' : []}},
            {7777 : {'name:' : 'ammu','card_number:' : '9988773344','balance:' : 10002, 'total_no_transactions:' : 0, 'credit_count:' : 0, 'debit_count:' : 0, 'transfer_history:' : []}},
        ]
        self.flag = False
        self.account_number = 0
        self.new_history = []

    


    def __open_account(self):
        name = str(input('Enter new name: '))
        ac_number = str(input('Enter account number: '))
        ac_number = int(ac_number[-4:])
        card_number = random.randint(111111111111,999999999999)
        opnning_balance = int(input('Enter openning balance: '))
        new_account = {ac_number : {'name:' : name,'card_number:' : card_number,'balance:' : opnning_balance, 'total_no_transactions:' : 0, 'credit_count:' : 0, 'debit_count:' : 0, 'transfer_history:' : []}}
        self.__all_account.append(new_account)
        print('\nNow, You have to enter your Last 4 Digit of the account number for the confirmation\n')
        self._login()

    def _login(self):
        if self.flag == False:
            self.account_number = int(input('Enter last 4 digits (Account number) : XXXX XXXX '))
            for i in self.__all_account:
                if self.account_number in i:
                    self.flag = True
                    self.__bank_operation()
                
                choice = str(input('\nSorry, Account is not found. \nIf you dont have Account, \n\tCreate account\tPress 1 \n\tRe - Login\tPress 2 \n\tExit()\tPress Anyother key\n\t\t'))
                if choice == '1':
                    self.__open_account()
                if choice == '2':
                    self._login() 
                else:
                    print('Thank you, Come again')
                    return     

    def __bank_operation(self):
        choice = str(input('\nSelect any one of the following\n\t 1. Credit\n\t 2. Debit\n\t 3. Transfer\n\t 4. Transaction History\n\t\t'))
        if choice == '1':
            card.credit()
        elif choice == '2':
            card.debit()
        elif choice == '3':
            card.transfer()
        elif choice == '4':
            card.history()
        else:
            print('\tSorry, Invalid selection. Please try again\n')
            self.__bank_operation()
        
    
    def credit(self):
        if self.flag == True:
            credit_amount = int(input('Credit amount: '))
            if credit_amount > 0:
                for account in self.__all_account:
                    for data in account:
                        if data == self.account_number:
                            print(account[data]['balance:'])
                            account[data]['balance:'] += credit_amount
                            account[data]['total_no_transactions:'] += 1
                            account[data]['credit_count:'] += 1
                            self.new_history = ['ATM','My Account',credit_amount,account[data]['balance:']]
                            account[data]['transfer_history:'].append(self.new_history)
                            print('Rs ', credit_amount, 'has been successfully created to your account is end with XXXX XXXX XXXX',self.account_number,'\n')
                            print('Now your Net Available balance: ',account[data]['balance:'],'\n')
                            self.__bank_operation()
            else:
                print('Enter Valid amount')
                self.credit()
                    
        else:
            self.__bank_operation()

    def debit(self):
        if self.flag == True:
            debit_amount = int(input('Debit amount: '))
            if debit_amount > 0:
                for account in self.__all_account:
                    for data in account:
                        if data == self.account_number and account[data]['balance:'] >= debit_amount:
                            print(account[data]['balance:'])
                            account[data]['balance:'] -= debit_amount
                            account[data]['total_no_transactions:'] += 1
                            account[data]['debit_count:'] += 1
                            self.new_history = ['My Account','ATM',debit_amount,account[data]['balance:']]
                            account[data]['transfer_history:'].append(self.new_history)
                            print('Rs ', debit_amount, 'has been successfully debited from your account is end with XXXX XXXX XXXX',self.account_number)
                            print('Now your Net Available balance: ',account[data]['balance:'])
                            self.__bank_operation()
                    else:
                        print('Amount is not available')
                        self.__bank_operation()
            else:
                print('Enter valid amount')
                self.debit()
                    

    def transfer(self):
        if self.flag == True:
            to_account = int(input("Enter Reciver's Last 4 Digit account: "))
            for account in self.__all_account:
                if to_account in account:
                    temp1 = account
                    for from_account in self.__all_account:
                        if self.account_number in from_account:
                            temp2 = from_account
                            transfer_amount = int(input('Transfer Amount: '))
                            if temp2[self.account_number]['balance:'] >= transfer_amount:
                                temp1[to_account]['balance:'] += transfer_amount
                                temp1[to_account]['total_no_transactions:'] += 1
                                new_transfer = [self.account_number,'My Account',transfer_amount,temp1[to_account]['balance:']]
                                temp1[to_account]['transfer_history:'].append(new_transfer)
                                temp2[self.account_number]['balance:'] -= transfer_amount
                                temp2[self.account_number]['total_no_transactions:'] += 1
                                new_transfer = ['My Account',to_account,transfer_amount,temp2[self.account_number]['balance:']]
                                temp2[self.account_number]['transfer_history:'].append(new_transfer)
                                print('Success, Amount transfered')
            else:
                self.__bank_operation()

                
            
    def history(self):
        s_no = 1
        account_number = int(input('Enter last 4 digits (Account number) : XXXX XXXX '))
        for account in self.__all_account:
            for data in account:
                if data == account_number:
                    print('\nTotal Credit & Debit: ',account[data]['total_no_transactions:'])
                    print('\tTotal Credits: ',account[data]['credit_count:'])
                    print('\tTotal Debits: ',account[data]['debit_count:'])
                    print('\nTotal Transfers: ',len(account[data]['transfer_history:']))
                    temp = account[data]['transfer_history:']
                    for history in temp:
                        print('\nTransaction Number: ', s_no)
                        print('\tFrom: ',history[0])
                        print('\tTo: ',history[1])
                        print('\tAmount: ',history[2])
                        print('\tBalance: ',history[3])
                        s_no += 1
                    s_no = 1
        else:
            self.__bank_operation()
                          

card = ATM()
print_formatted_text(HTML('\n\t\t<aaa>Welcome</aaa> <bbb>User</bbb>!\n'), style=style)
card._login()
 
