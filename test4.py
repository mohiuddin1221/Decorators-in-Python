def admin_required(function):
    def wrapper(*args,**kwargs):
        user = kwargs.get('user')
        if user == 'admin':
            return function(*args,**kwargs)
        
        print('Forbidden to call this api')
    return wrapper
        

@admin_required
def add_product(product_title,user):
    print(f"{product_title} added by {user}")
   
    
add_product(product_title='Mango', user = 'xyz')

