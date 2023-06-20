import mysql.connector
import hashlib


my_db = mysql.connector.connect(
    host='localhost',
    user='root',
    password='mysql',
    database='bankclients'
)

my_cursor = my_db.cursor()

# my_cursor.execute("CREATE DATABASE bankclients")

# my_cursor.execute("CREATE TABLE IF NOT EXISTS client_list (name Varchar(35), surname Varchar(65), age Integer(3), "
#                  "email Varchar(150), phone_number Varchar(25), card_number DECIMAL(16, 0), account_number DECIMAL(14, 0), "
#                  "password Varchar(255), money_amount Integer(15), loan_amount Integer(7))")

# people_to_fill_db = [
#     ('Alice', 'Johnson', 31, 'alice.johnson@example.com', '+15551234567', 1234567892401234, 98765432101234, hashlib.sha224(b'alicepassword').hexdigest(), 2500, 2000),
#     ('Robert', 'Davis', 29, 'robert.davis@example.com', '+15559876543', 2345678349012345, 87654321098765, hashlib.sha224(b'robertpassword').hexdigest(), 50000, 0),
#     ('Emily', 'Taylor', 27, 'emily.taylor@example.com', '+33789012345', 3456789012123456, 76543210987654, hashlib.sha224(b'emilypassword').hexdigest(), 150000, 25000),
#     ('Daniel', 'Anderson', 33, 'daniel.anderson@example.com', '+61234567890', 4567896401234567, 65432109876543, hashlib.sha224(b'danielpassword').hexdigest(), 1000000, 0),
#     ('Olivia', 'Wilson', 26, 'olivia.wilson@example.com', '+15558765432', 5678901224345678, 54321098765432, hashlib.sha224(b'oliviapassword').hexdigest(), 5000, 500),
#     ('Sophia', 'Martinez', 35, 'sophia.martinez@example.com', '+15554567890', 6789750123456789, 43210987654321, hashlib.sha224(b'sophiapassword').hexdigest(), 30000, 0),
#     ('David', 'Thompson', 28, 'david.thompson@example.com', '+15559876543', 7890123424567890, 32109876543210, hashlib.sha224(b'davidpassword').hexdigest(), 250000, 0),
#     ('Emma', 'Harris', 30, 'emma.harris@example.com', '+15552345678', 8901234553678901, 21098765432109, hashlib.sha224(b'emmapassword').hexdigest(), 500000, 30000),
#     ('Jackson', 'Walker', 32, 'jackson.walker@example.com', '+49123456789', 9012345536789012, 10987654321098, hashlib.sha224(b'jacksonpassword').hexdigest(), 100000, 0),
#     ('Ava', 'Garcia', 29, 'ava.garcia@example.com', '+33345678901', 1234567890471234, 98765432101234, hashlib.sha224(b'avapassword').hexdigest(), 75000, 15000),
#     ('Ethan', 'Smith', 35, 'ethan.smith@example.com', '+445678901234', 2373456789012345, 87654321098765, hashlib.sha224(b'ethanpassword').hexdigest(), 200000, 0),
#     ('Elon', 'Musk', 26, 'elon.musk@example.com', '+37412345678', 3456789042123456, 76543210987654, hashlib.sha224(b'elonpassword').hexdigest(), 1500000, 0),
#     ('Aram', 'Aramyan', 33, 'aram.aramyan@example.com', '+37423456789', 4567238901234567, 65432109876543, hashlib.sha224(b'arampassword').hexdigest(), 400000, 0),
#     ('Sophia', 'Lee', 28, 'sophia.lee@example.com', '+49567890123', 5678901234745678, 54321098765432, hashlib.sha224(b'sophiapassword').hexdigest(), 80000, 10000),
#     ('Alex', 'Amirkhanyan', 30, 'alex.amirkhanyan@example.com', '+37434567890', 6789011223456789, 43210987654321, hashlib.sha224(b'alexpassword').hexdigest(), 300000, 0),
#     ('Ararat', 'Avetisyan', 37, 'ararat.avetisyan@example.com', '+37445678901', 7897401234567890, 32109876543210, hashlib.sha224(b'araratpassword').hexdigest(), 5000000, 0),
#     ('Lily', 'Scott', 32, 'lily.scott@example.com', '+37456789012', 8901234537678901, 21098765432109, hashlib.sha224(b'lilypassword').hexdigest(), 120000, 0),
#     ('Noah', 'Gonzalez', 33, 'noah.gonzalez@example.com', '+446789012345', 9012743456789012, 10987654321098, hashlib.sha224(b'noahpassword').hexdigest(), 80000, 5000)
# ]
#
# sql_command = "INSERT INTO client_list (name, surname, age, email, phone_number, card_number, account_number, password, " \
#              "money_amount, loan_amount) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s) "
#
# my_cursor.executemany(sql_command, people_to_fill_db)
# my_db.commit()
