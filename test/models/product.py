
from gspread_models.base import BaseModel
from pprint import pprint


class Product(BaseModel):

    SHEET_NAME = "products"

    COLUMNS = ["name", "description", "price", "url"]

    SEEDS = [
        {
            'name': 'Strawberries',
            'description': 'Juicy organic strawberries.',
            'price': 4.99,
            'url': 'https://picsum.photos/id/1080/360/200'
        },
        {
            'name': 'Cup of Tea',
            'description': 'An individually-prepared tea or coffee of choice.',
            'price': 3.49,
            'url': 'https://picsum.photos/id/225/360/200'
        },
        {
            'name': 'Textbook',
            'description': 'It has all the answers.',
            'price': 129.99,
            'url': 'https://picsum.photos/id/24/360/200'
        }
    ]



if __name__ == "__main__":

    products = Product.all()

    if any(products):
        for product in products:
            #breakpoint()
            pprint(dict(product))
    else:
        will_seed = input("Seed products? (y/n)? ").upper()
        if will_seed == "Y":
            Product.seed()

    #breakpoint()

    results = Product.where(name="Strawberries")
    print(len(results))

    results = Product.where(name="Strawberries", price=1000)
    print(len(results))

    #product = Product(dict(name="Blueberries", price=3.99, description="organic blues", url="https://images.unsplash.com/photo-1498557850523-fd3d118b962e?q=80&w=2938&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"))
    #product.save()

    Product.create(dict(name="Blueberries", price=3.99, description="organic blues", url="https://images.unsplash.com/photo-1498557850523-fd3d118b962e?q=80&w=2938&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"))
