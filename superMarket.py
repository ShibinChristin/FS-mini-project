"""
This is the backend of the application
updates the file system as well as retrieves the content from the file system
"""
import csv


class Cart:
    def __init__(self):
        self.cart = []
        self.total_cost = 0

    def newProduct(self, product_code, units):
        pass

    def purchase(self):
        pass


class Inventory:
    def __init__(self):
        self.brandIds = ['25', '36']
        self.categoryIds = ['36', '45']
        self.productIds = ['65', '36']

    def getAllBrandNames(self):
        """:returns a list containing all brand names"""
        brands = []
        with open('dataFiles/brands.txt', 'r') as file:
            reader = csv.reader(file, delimiter='|')
            for row in reader:
                brands.append(row[1])
        return brands

    def getAllCategoryNames(self):
        """:returns a list containing all category names"""
        categories = []
        with open('dataFiles/categories.txt', 'r') as file:
            reader = csv.reader(file, delimiter='|')
            for row in reader:
                categories.append(row[1])
        return categories

    def getAllProductNames(self, brand=None, category=None):
        """
        :returns a list containing all brand names based on the brand and category set
        :type category: str
        :type brand: str
        """
        products = []
        brandId = self.getBrandId(brand)
        categoryId = self.getCategoryId(category)
        with open('dataFiles/products.txt', 'r') as file:
            reader = csv.reader(file, delimiter='|')
            for row in reader:
                if brandId is not None and brandId != row[2]:
                    continue
                if categoryId is not None and categoryId != row[3]:
                    continue
                products.append(row[1])
        return products

    def getBrandId(self, brand):
        """
        :returns brand id of specified brand
        :type brand: str
        """
        if brand is None:
            return None
        else:
            with open('dataFiles/brands.txt', 'r') as file:
                reader = csv.reader(file, delimiter='|')
                for row in reader:
                    if row[1] == brand:
                        return row[0]

    def getCategoryId(self, category):
        """
        :returns category id of specified category
        :type category: str
        """
        if category is None:
            return None
        else:
            with open('dataFiles/categories.txt', 'r') as file:
                reader = csv.reader(file, delimiter='|')
                for row in reader:
                    if row[1] == category:
                        return row[0]

    def getProductId(self, product):
        """
        :returns product id of specified brand
        :type product: str
        """
        if product is None:
            return None
        else:
            with open('dataFiles/products.txt', 'r') as file:
                reader = csv.reader(file, delimiter='|')
                for row in reader:
                    if row[1] == product:
                        return row[0]

    def getBrandName(self, brandId):
        """
        :returns brand name of specified brand
        :type brandId: str
        """
        if brandId is None:
            return None
        else:
            with open('dataFiles/brands.txt', 'r') as file:
                reader = csv.reader(file, delimiter='|')
                for row in reader:
                    if row[0] == brandId:
                        return row[1]

    def getCategoryName(self, catId):
        if catId is None:
            return None
        else:
            with open('dataFiles/categories.txt', 'r') as file:
                reader = csv.reader(file, delimiter='|')
                for row in reader:
                    if row[0] == catId:
                        return row[1]

    def getProductDetails(self, code):
        """
        :type code: str
        """
        details = []
        with open('dataFiles/products.txt', 'r') as file:
            reader = csv.reader(file, delimiter='|')
            for row in reader:
                if code == row[0]:
                    details.append(row[0])
                    details.append(row[1])
                    details.append(self.getBrandName(row[2]))
                    details.append(self.getCategoryName(row[3]))
                    return details

    def addProduct(self, name, brand, category, stock, prize):
        pass

    def addBrand(self, brand):
        pass

    def addCategory(self, category):
        pass
