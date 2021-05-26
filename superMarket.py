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


# noinspection PyMethodMayBeStatic
class Inventory:
    def getBrandsData(self, b_id=False, name=False):
        """:returns a list containing all brand data based on parameters"""
        data = []
        with open('dataFiles/brands.txt', 'r') as file:
            reader = csv.reader(file, delimiter='|')
            for row in reader:
                subData = []
                if b_id:
                    subData.append(row[0])
                if name:
                    subData.append(row[1])
                data.append(subData)
        if [b_id, name].count(True) == 1:
            data = [item for sublist in data for item in sublist]
        return data

    def getCategoriesData(self, c_id=False, name=False):
        """:returns a list containing all brand data based on parameters"""
        data = []
        with open('dataFiles/categories.txt', 'r') as file:
            reader = csv.reader(file, delimiter='|')
            for row in reader:
                subData = []
                if c_id:
                    subData.append(row[0])
                if name:
                    subData.append(row[1])
                data.append(subData)
        if [c_id, name].count(True) == 1:
            data = [item for sublist in data for item in sublist]
        return data

    def getProductsData(self, p_id=False, name=False, brand=False, category=False, stock=False, prize=False,
                        filterBrand=None, filterCategory=None):
        """:returns a list containing all brand data based on parameters"""
        data = []
        brandId = self.getBrandId(filterBrand)
        categoryId = self.getCategoryId(filterCategory)
        with open('dataFiles/products.txt', 'r') as file:
            reader = csv.reader(file, delimiter='|')
            for row in reader:
                if brandId is not None and brandId != row[2]:
                    continue
                if categoryId is not None and categoryId != row[3]:
                    continue
                subData = []
                if p_id:
                    subData.append(row[0])
                if name:
                    subData.append(row[1])
                if brand:
                    subData.append(self.getBrandName(row[2]))
                if category:
                    subData.append(self.getCategoryName(row[3]))
                if stock:
                    subData.append(row[4])
                if prize:
                    subData.append(row[5])
                data.append(subData)
        if [p_id, name, brand, category, stock, prize].count(True) == 1:
            data = [item for sublist in data for item in sublist]
        return data

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
        with open('dataFiles/products.txt', 'r') as file:
            try:
                code = int(file.readlines()[-1].split('|')[0])
            except IndexError:
                code = 0
        with open('dataFiles/products.txt', 'a', newline='') as file:
            writer = csv.writer(file, delimiter='|')
            writer.writerow([code + 1, name, brand, category, stock, prize])

    def addBrand(self, brand):
        with open('dataFiles/brands.txt', 'r') as file:
            try:
                code = int(file.readlines()[-1].split('|')[0])
            except IndexError:
                code = 0
        with open('dataFiles/brands.txt', 'a', newline='') as file:
            writer = csv.writer(file, delimiter='|')
            writer.writerow([code + 1, brand])

    def addCategory(self, category):
        with open('dataFiles/categories.txt', 'r') as file:
            try:
                code = int(file.readlines()[-1].split('|')[0])
            except IndexError:
                code = 0
        with open('dataFiles/categories.txt', 'a', newline='') as file:
            writer = csv.writer(file, delimiter='|')
            writer.writerow([code + 1, category])
