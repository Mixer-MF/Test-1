import json
from datetime import datetime
from file_handler import FileHandler

class FinanceManager:
    def __init__(self):
        self.transactions = []
        self.file_handler = FileHandler("data/transactions.json")
        self.load_data()
    
    def load_data(self):
        """Загрузка данных из файла"""
        data = self.file_handler.load()
        if data:
            self.transactions = data
    
    def save_data(self):
        """Сохранение данных в файл"""
        self.file_handler.save(self.transactions)
    
    def add_transaction(self, amount, category, trans_type, description=""):
        """Добавление новой финансовой операции"""
        transaction = {
            "id": len(self.transactions) + 1,
            "date": datetime.now().strftime("%Y-%m-%d %H:%M"),
            "amount": amount,
            "category": category,
            "type": trans_type,
            "description": description
        }
        self.transactions.append(transaction)
        self.save_data()
    
    def show_all_transactions(self):
        """Вывод всех операций"""
        if not self.transactions:
            print("Нет записей.")
            return
        
        print("\n" + "-"*70)
        print(f"{'№':<3} {'Дата':<16} {'Тип':<8} {'Категория':<12} {'Сумма':<10} {'Описание'}")
        print("-"*70)
        
        for i, t in enumerate(self.transactions, 1):
            amount_str = f"+{t['amount']}" if t['type'] == 'доход' else f"-{t['amount']}"
            type_str = "Доход" if t['type'] == 'доход' else "Расход"
            print(f"{i:<3} {t['date']:<16} {type_str:<8} {t['category']:<12} {amount_str:<10} {t['description']}")
    
    def edit_transaction(self, index):
        """Редактирование операции по индексу"""
        if 0 <= index < len(self.transactions):
            print("Введите новые данные (оставьте пустым, чтобы не менять):")
            
            try:
                amount = input(f"Сумма [{self.transactions[index]['amount']}]: ").strip()
                if amount:
                    self.transactions[index]['amount'] = float(amount)
                
                category = input(f"Категория [{self.transactions[index]['category']}]: ").strip()
                if category:
                    self.transactions[index]['category'] = category
                
                trans_type = input(f"Тип [{self.transactions[index]['type']}]: ").strip()
                if trans_type:
                    self.transactions[index]['type'] = trans_type
                
                description = input(f"Описание [{self.transactions[index]['description']}]: ").strip()
                if description:
                    self.transactions[index]['description'] = description
                
                self.transactions[index]['date'] = datetime.now().strftime("%Y-%m-%d %H:%M")
                self.save_data()
                return True
            except ValueError:
                print("Ошибка формата суммы")
                return False
        return False
    
    def delete_transaction(self, index):
        """Удаление операции по индексу"""
        if 0 <= index < len(self.transactions):
            self.transactions.pop(index)
            # Обновляем ID
            for i, t in enumerate(self.transactions, 1):
                t['id'] = i
            self.save_data()
            return True
        return False
    
    def get_balance(self):
        """Расчет текущего баланса"""
        balance = 0
        for t in self.transactions:
            if t['type'] == 'доход':
                balance += t['amount']
            else:
                balance -= t['amount']
        return balance
    
    def show_analysis(self):
        """Анализ расходов и доходов по категориям"""
        if not self.transactions:
            print("Нет данных для анализа")
            return
        
        income_by_category = {}
        expense_by_category = {}
        
        for t in self.transactions:
            if t['type'] == 'доход':
                income_by_category[t['category']] = income_by_category.get(t['category'], 0) + t['amount']
            else:
                expense_by_category[t['category']] = expense_by_category.get(t['category'], 0) + t['amount']
        
        print("\n" + "="*40)
        print("АНАЛИЗ ПО КАТЕГОРИЯМ")
        print("="*40)
        
        if income_by_category:
            print("\nДоходы:")
            for category, amount in income_by_category.items():
                print(f"  {category}: +{amount:.2f} руб.")
        
        if expense_by_category:
            print("\nРасходы:")
            for category, amount in expense_by_category.items():
                print(f"  {category}: -{amount:.2f} руб.")
        
        total_income = sum(income_by_category.values())
        total_expense = sum(expense_by_category.values())
        
        print("\n" + "-"*40)
        print(f"Всего доходов:  +{total_income:.2f} руб.")
        print(f"Всего расходов: -{total_expense:.2f} руб.")
        print(f"Итоговый баланс: {total_income - total_expense:.2f} руб.")