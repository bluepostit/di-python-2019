from db import Db

from auth import Auth

class Call:
    def __init__(self, customer_id, user_id, call_time, notes, call_id=None):
        self.customer_id = customer_id
        self.user_id = user_id
        self.call_time = call_time
        self.notes = notes
        self.call_id = call_id

    def save(self):
        if self.call_id is not None:
            query = ("UPDATE phone_call SET customer_id = ?, user_id = ?, "
                     "call_time = ?, notes = ? "
                     "WHERE call_id = ?")
            data = (self.customer_id, self.user_id, self.call_time, self.notes,
                    self.call_id)
        else:
            query = ("INSERT INTO phone_call (customer_id, user_id, call_time, notes) "
                     "VALUES (?, ?, ?, ?)")
            data = (self.customer_id, self.user_id, self.call_time, self.notes)
        # Execute in all cases
        db = Db()
        db.execute(query, data)
        db.commit()

    def build_from_row(row):
        if row is None:
            return None
        call = Call(row[0], row[1], row[2], row[3], row[4])
        return call

    # Class function (no self!)
    def get_for_customer(customer_id, include_user=False):
        query = ("SELECT customer_id, user_id, call_time, notes, call_id "
                 "FROM phone_call WHERE customer_id = ? "
                 "ORDER BY call_time DESC")
        data = (customer_id,)
        db = Db()
        db.execute(query, data)
        calls = []
        rows = db.fetchall()
        for row in rows:
            call = Call.build_from_row(row)
            if include_user:
                user = Auth().get_by_user_id(call.user_id)
                call.user = user
            calls.append(call)
        return calls

    def get(call_id):
        query = ("SELECT customer_id, user_id, call_time, notes, call_id "
                 "FROM phone_call WHERE call_id = ?")
        data = (call_id,)
        db = Db()
        db.execute(query, data)
        row = db.fetchone()
        return Call.build_from_row(row)

    # Class function (no self!)
    def get_all():
        query = ("SELECT customer_id, user_id, call_time, notes, call_id "
                 "FROM phone_call "
                 "ORDER BY last_name, first_name")
        db = Db()
        db.execute(query)
        rows = db.fetchall()

        calls = []
        for call in calls:
            call = Call.build_from_row(row)
            calls.append(call)

        return calls
