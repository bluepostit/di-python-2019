from db import Db


class Customer:
    def __init__(self, first_name, last_name, phone, email,
                 address1, address2, postal_code, city, country,
                 customer_id=None, added_by=None):
        self.first_name = first_name
        self.last_name = last_name
        self.phone = phone
        self.email = email
        self.address1 = address1
        self.address2 = address2
        self.postal_code = postal_code
        self.city = city
        self.country = country
        self.customer_id = customer_id
        self.added_by = added_by

    def save(self):
        if self.customer_id is not None:
            query = ("UPDATE customer SET first_name = ?, last_name = ?, "
                     "phone = ?, email = ?, address1 = ?, address2 = ?, "
                     "postal_code = ?, city = ?, country = ?, added_by = ? "
                     "WHERE customer_id = ?")
            data = (self.first_name, self.last_name, self.phone, self.email,
                    self.address1, self.address2, self.postal_code, self.city,
                    self.country, self.added_by, self.customer_id)
        else:
            query = ("INSERT INTO customer (first_name, last_name, phone, "
                     "email, address1, address2, postal_code, city, country, "
                     "added_by) "
                     "VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)")
            data = (self.first_name, self.last_name, self.phone, self.email,
                    self.address1, self.address2, self.postal_code, self.city,
                    self.country, self.added_by)
        # Execute in all cases
        db = Db()
        db.execute(query, data)
        db.commit()

    def build_from_row(row):
        if row is None:
            return None
        customer = Customer(row[0], row[1], row[2], row[3], row[4],
                            row[5], row[6], row[7], row[8], row[9])
        if len(row) >= 11:
            customer.customer_id = row[9]
            customer.added_by = row[10]
        return customer

    # Class function (no self!)
    def get(customer_id):
        query = ("SELECT first_name, last_name, phone, "
                 "email, address1, address2, postal_code, city, country, "
                 "customer_id, added_by "
                 "FROM customer WHERE customer_id = ?")
        data = (customer_id,)
        db = Db()
        db.execute(query, data)
        row = db.fetchone()
        return Customer.build_from_row(row)

    # Class function (no self!)
    def get_all():
        query = ("SELECT first_name, last_name, phone, "
                 "email, address1, address2, postal_code, city, country, "
                 "customer_id, added_by "
                 "FROM customer "
                 "ORDER BY last_name, first_name")
        db = Db()
        db.execute(query)
        rows = db.fetchall()

        customers = []
        for row in rows:
            customer = Customer.build_from_row(row)
            customers.append(customer)

        return customers
