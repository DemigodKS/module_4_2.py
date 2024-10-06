# вызов inner_function внутри функции
def test_function ():
    def  inner_function():
        a = 'Я в области видимости функции test_function'
        print(a)
    inner_function()
test_function()

# вызов inner_function вне функции
def test_function ():
    def  inner_function():
        a = 'Я в области видимости функции test_function'
        print(a)
inner_function() #NameError: name 'inner_function' is not defined. Did you mean: 'test_function'?
test_function()
