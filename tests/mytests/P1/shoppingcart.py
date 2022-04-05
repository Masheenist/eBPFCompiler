ItemType = -1
ItemAmt = -2
ItemID = -3
NoItems = -4 
ItemList = -5
Item1 = 0
Item2 = 1
Item3 = 2
Item4 = 3

ShoppingCart = {
  Item1 : {
    ItemType: 0,
    ItemAmt: 700,
    ItemID: 01,
      },
  Item2: {
    ItemType: 1,
    ItemAmt: 800,
    ItemID: 02
      },
  Item3: {
    ItemType: 3,
    ItemAmt: 1200,
    ItemID: 03
      },
  NoItems: 3,
  ItemList: [Item1, Item2, Item3],
}

print ShoppingCart

# Add to Cart
ShoppingCart[Item4] = {
  ItemType: 4,
  ItemAmt: 10000,
  ItemID: 04
        }
ShoppingCart[NoItems] = ShoppingCart[NoItems] + 1
ShoppingCart[ItemList] = ShoppingCart[ItemList] + [Item4]

print ShoppingCart
