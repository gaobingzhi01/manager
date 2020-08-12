from myApp.exts import db


class DBHelp():
    def save(self):
        try:
            # insert a data
            db.session.add(self)
            db.session.commit()
        except Exception as e:
            return str(e)

    @classmethod
    def save_all(cls, arr):
        try:
            # insert multiple data
            db.session.add_all(arr)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            return str(e)

    def delete(self):
        try:
            db.session.delete(self)
            db.session.commit()
        except Exception as e:
            return str(e)