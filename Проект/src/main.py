from finance_manager import FinanceManager

def print_menu():
    """Вывод главного меню"""
    print("\n" + "="*30)
    print("   УЧЕТ ЛИЧНЫХ ФИНАНСОВ")
    print("="*30)
    print("1. Показать все операции")
    print("2. Добавить операцию (доход/расход)")
    print("3. Редактировать операцию")
    print("4. Удалить операцию")
    print("5. Показать баланс")
    print("6. Анализ по категориям")
    print("0. Выход")
    print("="*30)

def main():
    manager = FinanceManager()
    
    while True:
        print_menu()
        choice = input("Выберите действие: ").strip()
        
        if choice == "1":
            manager.show_all_transactions()
        
        elif choice == "2":
            try:
                amount = float(input("Сумма: "))
                category = input("Категория (еда, транспорт, зарплата, др.): ").strip()
                trans_type = input("Тип (доход/расход): ").strip().lower()
                description = input("Описание: ").strip()
                
                if trans_type not in ["доход", "расход"]:
                    print("Ошибка: тип должен быть 'доход' или 'расход'")
                    continue
                    
                manager.add_transaction(amount, category, trans_type, description)
                print("✓ Операция добавлена!")
            except ValueError:
                print("Ошибка: неверный формат суммы")
        
        elif choice == "3":
            manager.show_all_transactions()
            try:
                idx = int(input("Номер операции для редактирования: ")) - 1
                if manager.edit_transaction(idx):
                    print("✓ Операция изменена!")
                else:
                    print("Ошибка: неверный номер операции")
            except ValueError:
                print("Ошибка: введите число")
        
        elif choice == "4":
            manager.show_all_transactions()
            try:
                idx = int(input("Номер операции для удаления: ")) - 1
                if manager.delete_transaction(idx):
                    print("✓ Операция удалена!")
                else:
                    print("Ошибка: неверный номер операции")
            except ValueError:
                print("Ошибка: введите число")
        
        elif choice == "5":
            balance = manager.get_balance()
            print(f"\nТекущий баланс: {balance:.2f} руб.")
        
        elif choice == "6":
            manager.show_analysis()
        
        elif choice == "0":
            print("Сохранение данных...")
            manager.save_data()
            print("До свидания!")
            break
        
        else:
            print("Неверный выбор. Попробуйте снова.")

if __name__ == "__main__":
    main()