import pypyodbc
from Product import Product

class ProductSevice():

    def __init__(self, SQLDataBaseName='FitnessCalculator', SQLServerName='DESKTOP-44DU6U2\SQLEXPRESS'):
        self.mySQLDatabase = SQLDataBaseName
        self.mySQLServer = SQLServerName

    def getAllProduct(self):
        productList = list()
        results = self.doQuery("SELECT * FROM dbo.Product")
        for row in results:
            product = Product(row[1], row[2], row[3], row[4], row[5])

            productList.append(product)
        return productList

    def getProductByName(self, product_name):
        result = self.doQuery("SELECT * FROM dbo.Product WHERE product_name =" + "'" + product_name + "'")
        print(result)

    def doQuery(self, query):
        connection = pypyodbc.connect('Driver={SQL Server};''Server=' + self.mySQLServer + ';''Database=' + self.mySQLDatabase + ';')
        cursor = connection.cursor()
        mySQLQuery = ("""
                """ + query + """
        """)
        cursor.execute(mySQLQuery)
        results = cursor.fetchall()
        connection.close()
        return results