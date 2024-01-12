import psycopg2

DATA_BASE_CONNECT_STRING = "user=postgres password=this_is_a_strong_password host=db.espmlrforfrdunawqkqg.supabase.co port=5432 dbname=postgres"

class DataBase:
    def __init__(self) -> None:
        self.connection = psycopg2.connect(DATA_BASE_CONNECT_STRING)

    def select_query(self, str_query:str) -> list:
        try:
            result = None
            header = None
            with self.connection.cursor() as cursor:
                cursor.execute(str_query)
                result = cursor.fetchall()
                header = [description[0] for description in cursor.description]
                self.connection.commit()
            return header, result
        except psycopg2.Error as e:
            self.connection.rollback()
            return False, str(e)
        
    def insert_query(self, table, records):
        keys_str = "(" + ", ".join(map(str, records.keys())) + ")"
        value_str = "(" + ", ".join(map(lambda key: f"'{key}'", records.values())) + ")"
        str_query = f"""INSERT INTO {table}{keys_str}\nVALUES\n{value_str} RETURNING {table}_id;"""
        last_inserted_id = None
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(str_query)
                last_inserted_id = cursor.fetchone()[0]
                self.connection.commit()
        except psycopg2.Error as e:
            self.connection.rollback()
            return False, str(e)
        else:
            return True, f'Inserted -{last_inserted_id}- into {table}'
    
    def delete_query(self, table:str, **condition):
        conditions = (f"{key} = {value}" for key, value in condition.items())
        condition_str = ", ".join(conditions)
        query = f"""
            DELETE FROM {table}
            WHERE {condition_str}
        """
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(query)
                self.connection.commit()
        except psycopg2.Error as e:
            self.connection.rollback()
            return False, str(e)
        else:
            return True, 'Delete successful!'

    def update_query(self, table, id, changed_column:dict):
        update_colums = [f'{key} = \'{val}\'' for key, val in changed_column.items()]
        update_colums = ', '.join(update_colums)
        query = f'''UPDATE {table} SET {update_colums} where {table}_id = {id}'''
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(query)
                self.connection.commit()
        except psycopg2.Error as e:
            self.connection.rollback()
            return False, str(e)
        else:
            return True, 'Update successful!'

    def query(self, query:str):
        if 'select' in query.lower():
            return self.select_query(query)
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(query)
                self.connection.commit()
                return True, 'Done'
        except psycopg2.Error as e:
            self.connection.rollback()
            return False, str(e)
           
    def log_out(self):
        print('Going to close database connection')
        try:
            self.connection.close()
            print(f"Closed connection to database. Code {self.connection.closed}")
        except Exception:
            pass
        finally:
            if self.connection and self.connection.closed == 0:
                self.connection.close()
                print(f"Closed connection to database. Code {self.connection.closed}")
