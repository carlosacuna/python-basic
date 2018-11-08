# -- coding: utf-8 -*-

def say_hello(age):
	if age > 18:
		print("Hola senor")
	else:
		print("Hola nino")


def main():
	age = int(raw_input('Ingresa tu edad : '))
	say_hello(age)

if __name__ == '__main__':
    main()