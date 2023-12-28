class Category:
    cate = []
    def __init__(self):
        self.ledger = []
        self.amount = 0
        self.name = input("Enter category name: ")
        Category.cate.append(self)


    def deposit(self):
        a = input("Enter category name: ")
        for item in Category.cate:
            if item.name == a:
                j = item
                j.ledger = []
                j.dict = {}
                j.amount = float(input("Enter amount:"))
                j.dict['Amount'] = j.amount
                j.dict['Description'] = 'initial deposit'
                j.ledger.append(j.dict)
                j = None

    def __repr__(self):
        return self.name
    def withdraw(self):
        b = input("Enter category name: ")
        for object in Category.cate:
            if object.name == b:
                j = object
                a = float(input("Enter amount: "))
                b = j.check_funds(a)
                if b is True:
                    k = {}
                    j.ledger.append(k)
                    k['Amount'] = -a
                    k['Description'] = input("Enter Description: ")
                else:
                    print(b)



    def get_balance(self):
        cate = input("Enter Category name:")
        for object in Category.cate:
            if object.name == cate:
                j = object
                k = 0
                total = 0
                for item in j.ledger:
                    if k == 0:
                        k += 1
                        continue
                    else:
                        total += (item['Amount']*-1)
                Total = j.ledger[0]['Amount'] - total
                print('Balance:',Total)

    def transfer(self,Cash = None,category = None):
        Cash = float(input('Transfer amount: '))
        category = input( "Transfer from: ")
        category2 = input( 'Transfer to: ')
        for object in Category.cate:
            if object.name == category:
                j = object
                a = j.check_funds(Cash)
                print(a)
                if a is True:
                    m = {}
                    m['Amount'] = -Cash
                    m['Description'] = f'Transfer to {category2}'
                    j.ledger.append(m)
                    for object in Category.cate:
                        if object.name == category2:
                            m = object
                            l = {}
                            l['Amount'] = Cash
                            l['Description'] = f'Transfer from {category}'
                            m.ledger.append(l)
                else:
                    return a
    def check_funds(self,amount):
        print(len(self.ledger))
        if len(self.ledger) == 1:
            if amount <= self.ledger[0]['Amount']:
                print('Transaction in progress')
                return True
            else:
                print('Transaction failure ')
                return False
        else:
            h = 0
            total6 = 0
            for item in self.ledger:
                if h == 0:
                    h += 1
                    continue
                else:
                    total6 += (item['Amount']*-1)
            print(total6)
            if amount <= (self.ledger[0]['Amount'] - total6):
                print('Transaction in progress')
                return True
            else:
                print('Transaction failure ')
                return False

    def display_category(self):
        inp = input('Enter category:')
        for object in Category.cate:
            if object.name == inp:
                assertcount = (30 - len(object.name)) // 2
                l = []
                n = 0
                Total = 0
                for item in object.ledger:
                    b = item['Amount']
                    c = item['Description']
                    p = (c,b)
                    l.append(p)
                a = ('*' * assertcount) + object.name + ('*' * assertcount)
                if len(a) != 30:
                    a = a + '*'
                print(a)
                for (v,k) in l:
                    v = v[:23]
                    print('{:23}{:>7.2f}'.format(v,k))
                for item in object.ledger:
                    if n == 0:
                        n += 1
                        continue
                    else:
                        Total += (item['Amount']*-1)
                zx = object.ledger[0]['Amount'] - Total
                print('Total:'+'{:.2f}'.format(zx))


def dispay_menu():
    print('''
1.CREATE CATEGORY
2.DEPOSIT
3.WITHDRAW
4.GET BALANCE
5.TRANSFER
6.DISPLAY CATEGORY
7.BAR GRAPHY
    ''')

def display_bar(a):
    k = []
    total = 0
    c = {}
    category = []
    percentage = []
    for object in a:
        s = {}
        for item in object.ledger:
            if item['Amount'] > 0 or item['Description'].startswith('Transfer'):
                continue
            else:
                total += (item['Amount']*-1)
        s[object.name] = total
        k.append(s)
        total = 0
    for i in k:
        for v,n in i.items():
                total += n
    for i in k:
        for v,n in i.items():
            c[v] = int((round(float(n/total),1))*100)
    print("Percentage of Category")
    for n,m in c.items():
        category.append(n)
        percentage.append(m)
    categories = [{'name':label,'withdrawals': withdrawal} for label ,withdrawal in zip(category,percentage)]
    bars = []
    for i in range(100,-10,-10):
        bar = ' '.join(['o' if per >= i else ' ' for per in percentage])
        bars.append(f'{i:3d}| {bar}')
    print(bars)

    line = '    '+'-'*(len(categories)*3+3)

    labels = []
    max_label_length = max(len(i) for i in category)
    for i in range(max_label_length):
        label1 = ' '.join([label['name'][i] if i < len(label['name'])else ' ' for label in categories])
        labels.append(f'     {label1}')
    chart = '\n'.join(bars + [line] + labels)
    return chart




a = dispay_menu()


while True:
    inp = input('Enter choice:')
    print('')
    if inp == '1':
        c = Category()
    if inp == '2':
        c.deposit()
    if inp == '3':
        c.withdraw()
    if inp == '4':
        c.get_balance()
    if inp == '5':
        c.transfer()
    if inp == '6':
        c.display_category()
    if inp == '7':
        print(display_bar(Category.cate))
