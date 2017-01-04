from flask_bcrypt import Bcrypt
bcrypt= Bcrypt()
pw_hash = bcrypt.generate_password_hash('hunter2')
print pw_hash
print bcrypt.check_password_hash(pw_hash, 'hunter2') # returns True
