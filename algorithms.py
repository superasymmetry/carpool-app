import sqlite3

def verify_match(user1, user2):
    conn = sqlite3.connect("database.db")
    c = conn.cursor()
    c.execute("SELECT * FROM database WHERE username=?", (user1))
    a = c.fetchone()
    c.execute("SELECT * FROM database WHERE username=?", (user2))
    b = c.fetchone()
    conn.close()
    return (a[7] & b[7])


def convert_to_bin(num):
    return bin(num).replace("0b", "")

def convert_to_dec(num):
    return int(num, 2)

def find_recommendations(user):
    conn = sqlite3.connect("database.db")
    c = conn.cursor()
    c.execute("SELECT * FROM database")
    records = c.fetchall()
    conn.close()

def maximize_coverage(users, current_user):
    carpool_pairs = []
    
    while users:
        current_user = users.pop(0)
        best_match = None
        max_coverage = -1
        
        for i, other_user in enumerate(users):
            # Calculate the coverage of available weekdays using bitwise OR
            coverage = current_user | other_user
            num_covered_days = bin(coverage).count('1')
            
            if num_covered_days > max_coverage:
                max_coverage = num_covered_days
                best_match = i
        
        if best_match is not None:
            # Append the pair of users to the carpool_pairs list
            carpool_pairs.append((current_user, users[best_match]))
            users.pop(best_match)
    
    return carpool_pairs

# Example usage
users = [0b11001, 0b10001, 0b01001, 0b00110]
carpool_pairs = maximize_coverage(users)
print(carpool_pairs)
