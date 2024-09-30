from flask import Flask, render_template, redirect, request, session, flash
from flask_mysqldb import MySQL





class Inventory_Management:
    def __init__(self, name):
        self.app = Flask(name)
        self.app.secret_key = "JACKV"
        
        
        
        
        self.app.config['MYSQL_HOST'] = "localhost"
        self.app.config['MYSQL_USER'] = "root"
        self.app.config['MYSQL_PASSWORD'] = ""
        self.app.config['MYSQL_DB'] = "inventory_db"
        self.mysql = MySQL(self.app)
        
        
        
        
        

        
        
        #all def is method for handling webpages
    def setup_route(self):
        #function
        @self.app.route('/')
        def login():
            return render_template('login.html')
        
        
        
        
        
        
        
        
        @self.app.route('/login_process', methods=["POST", "GET"])
        def login_process():
            if request.method == "POST":
                user_textbox = request.form["userfield"]
                pass_textbox = request.form["passfield"]
                cursor = self.mysql.connection.cursor()
                cursor.execute("SELECT * FROM accounts WHERE username=%s AND password=%s", (user_textbox, pass_textbox))
                account_found = cursor.fetchone()
                if account_found:
                    session["user"] = account_found[3]
                    return redirect("/inventory")
                
                
                else:
                    flash("username or password is incorrect. ")
                    return redirect("/")
        
        
        
        
        
        
        
        @self.app.route('/logout')
        def logout():
            session.pop("user", None)
            return redirect('/')
        
        
        
        
        
        @self.app.route('/signup', methods=["GET"])
        def signup():
            return render_template('signup.html')

        @self.app.route('/signup_process', methods=["POST"])
        def signup_process():
            if request.method == "POST":
                username = request.form["username"]
                password = request.form["password"]
                confirm_password = request.form["confirm_password"]
                if password == confirm_password:
                    cursor = self.mysql.connection.cursor()
                    cursor.execute("SELECT * FROM accounts WHERE username=%s", (username,))
                    account_found = cursor.fetchone()
                    if not account_found:
                        cursor.execute("INSERT INTO accounts (username, password) VALUES (%s, %s)", (username, password))
                        self.mysql.connection.commit()
                        flash("Account created successfully. Please log in.")
                        return redirect("/")
                    else:
                        flash("Username already exists. Please try again.")
                        return redirect("/signup")
                else:
                    flash("Passwords do not match. Please try again.")
                    return redirect("/signup")
        
        
        
        
        
        
        @self.app.route('/search', methods=['POST'])
        def search():
            try:
                if 'search_query' in request.form:
                    search_query = request.form["search_query"]
                    cursor = self.mysql.connection.cursor()
                    cursor.execute("SELECT * FROM inv WHERE product_name LIKE %s", ('%' + search_query + '%',))
                    search_results = cursor.fetchall()
                    return render_template('search_res.html', search_results=search_results)
                else:
                    return 'No search query provided', 400
            except Exception as e:
                    return 'An error occurred: {}'.format(e), 500
        
        
        
        
        @self.app.route('/inventory')
        def inventory():
            if "user" in session:
                cursor = self.mysql.connection.cursor()
                categories = ["Drinks", "Snacks", "Dairy Products", "Condiments and Sauces", "Household Items", "Personal Care Products"]
                products = {}
                for category in categories:
                    cursor.execute("SELECT * FROM inv WHERE category=%s", (category,))
                    products[category] = cursor.fetchall()

                cursor.execute("SELECT * FROM inv")
                inv_list = cursor.fetchall()
                return render_template('inventory.html', products=products)

            else:
                return redirect("/")
       
       
       
       
       
       
        @self.app.route('/update', methods=['GET', 'POST'])
        def update():
            if request.method == 'POST':
                productID = request.form["productID"]
                action = request.form["action"]
        
                if action == "updater":
                    product_name = request.form["product_name"]
                    productQuantity = request.form["Qty"]
                    product_price = request.form["price"]
                    return render_template("update.html", productID=productID, product_name=product_name, productQuantity=productQuantity, product_price=product_price )
                elif action == "deleter":
                    return render_template("delete.html", productID=productID)







        @self.app.route('/delete_product', methods=['POST'])
        def delete_product():
            productID = request.form["productID"]
            confirm = request.form["confirm"]

            if confirm == "yes":
                cursor = self.mysql.connection.cursor()
                cursor.execute("SELECT * FROM inv WHERE product_ID=%s", (productID,))
                product_found = cursor.fetchone()
                if product_found:
                    cursor.execute("DELETE FROM inv WHERE product_ID=%s", (productID,))
                    self.mysql.connection.commit()
                    flash("Product successfully deleted!")
                else:
                    flash("Product not found.")
            elif confirm == "no":
                flash("Deletion cancelled. Product not deleted.")

            return redirect("/inventory")
               
               
               
        @self.app.route('/update_process', methods=['GET', 'POST'])
        def update_process():
            if request.method == 'POST':
                productID = request.form["productID"]
                new_product_name = request.form["new_product_name"]
                new_productQuantity = request.form["new_productQuantity"]
                new_product_price = request.form["new_product_price"]
               
               
               
                cursor = self.mysql.connection.cursor()
                cursor.execute("UPDATE inv set product_name=%s, Qty=%s, price=%s WHERE product_ID=%s", (new_product_name, new_productQuantity, new_product_price, productID))
                self.mysql.connection.commit()
                flash("Product successfully updated!")
                return redirect("/inventory")
       
       
       
       
       
       
       
       
        
        
        @self.app.route('/addprd', methods=['GET', 'POST'])
        def addprd():
           
        
            if request.method == "POST":
                prd_name = request.form["productName"]
                prd_price = request.form["productPrice"]
                prd_quantity = request.form["productQuantity"]
                prd_category = request.form["productCategory"]
            
            
                cursor = self.mysql.connection.cursor()
                cursor.execute("INSERT INTO inventory_db.inv (product_name, Qty, price, category) VALUES (%s, %s, %s, %s)", (prd_name, prd_quantity, prd_price, prd_category))
                self.mysql.connection.commit()
                
                
                
                cursor.close()

                flash("YOU SUCCESFULLY ADDED AN NEW ITEM")
            
                return redirect("/addprd")
            else:
                return render_template("addprd.html")
            
            
        
        
        @self.app.route('/aboutus')
        def aboutus():
            if "user" in session:
                return render_template('aboutus.html')
            else:
                return redirect("/")
        
        
        
        
        @self.app.route('/dashboard')
        def dashboard():
            
            if "user" in session:
                cur = self.mysql.connection.cursor()
                getDrinksCount = "SELECT SUM(Qty) FROM inv WHERE category = %s"
                cur.execute(getDrinksCount, ("Drinks",))
                drinksCount = cur.fetchone()
                
                getSnacksCount = "SELECT SUM(Qty) FROM inv WHERE category = %s"
                cur.execute(getSnacksCount, ("Snacks", ))
                snackCount = cur.fetchone()
                
                getDairyProductCount = "SELECT SUM(Qty) FROM inv WHERE category = %s"
                cur.execute(getDairyProductCount, ("Dairy Products", ))
                dairyProductcount = cur.fetchone()
                
                getCondimentSaucesCount = "SELECT SUM(Qty) FROM inv WHERE category = %s"
                cur.execute(getCondimentSaucesCount, ("Condiments and Sauces", ))
                condimentSaucesCount = cur.fetchone()
                
                getHouseholdItemsCount = "SELECT SUM(Qty) FROM inv WHERE category = %s"
                cur.execute(getHouseholdItemsCount, ("Household Items", ))
                householdItemCount = cur.fetchone()
                
                getPersonalCareCount = "SELECT SUM(Qty) FROM inv WHERE category = %s"
                cur.execute(getPersonalCareCount, ("Personal Care Products", ))
                personalCareCount = cur.fetchone()
                
                
                
                
                return render_template('dash.html', drinksCount = drinksCount, snackCount = snackCount, dairyProductcount = dairyProductcount, condimentSaucesCount = condimentSaucesCount, householdItemCount = householdItemCount, personalCareCount = personalCareCount)
                
            else:
                return redirect("/")
            
            
        @self.app.route('/transaction')
        def transaction():
            if "user" in session:
                return render_template('trans.html')
                
            else:
                return redirect("/")
        
        
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    def run(self):
        self.app.run(debug=True)
        
        
        
#object/instance
x = Inventory_Management(__name__)
x.setup_route()
x.run()