## Roadmap

Issues for future implementation.

#### Updating

Enable row updating.

Add `updated_at` column that gets the current timestamp whenever a previously persisted record has been saved again.

#### Initializing and Saving Records

After initializing a new record (whether it has previously been persisted or not), invoking `.save()` persists that record to the sheet:

```py
product = Product(name="Blueberries", price=3.99, description="organic blues", url=None)
product.save()
```

```py
product = Product.find(3)
product.price = 9999.99
product.save()
```
