def sort_func(li):
    result = sorted(li, key= lambda x: x['color'])
    print(result)


models = [{'make':'Nokia', 'model':216, 'color':'Black'}, {'make':'Mi Max', 'model':'2', 'color':'Gold'}, {'make':'Samsung', 'model': 7, 'color':'Blue'}]
sort_func(models)
