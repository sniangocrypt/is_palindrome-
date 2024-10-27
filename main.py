#Задание: Палиндром

#Создайте функцию is_palindrome(), которая будет проверять, является ли строка палиндромом (то есть читается одинаково слева направо и справа налево).
#
#Требования:
#
#	1.	Функция должна принимать на вход строку.
#	2.	Если строка является палиндромом, функция должна вернуть True, иначе — False.
##
##	3.	Игнорируйте регистр и пробелы при проверке.
#word1 = "madam"
#word2 = "hello"

#print(is_palindrome(word1)) # Вывод: True
#print(is_palindrome(word2)) # Вывод: False



def is_palindrome():
	print(f"Введите ваше предложение")
	a = str(input().lower().replace(",", "").replace(".", "").replace(":", "").replace("!", "").replace("?", "").replace(" ", "").replace("—", ""))

	if a == a[::-1]:
		print("True")
	else:print("Folse")


is_palindrome()



