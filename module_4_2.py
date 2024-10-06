
# вызов inner_function внутри функции
def test_function ():
    def  inner_function():
        a = 'Я в области видимости функции test_function'
        print(a)
    inner_function()
test_function()

# вызов inner_function вне функции
def test_function():
    def inner_function():
        global a
        a = 'Я в области видимости функции test_function'
    inner_function()
test_function()
print(a)


