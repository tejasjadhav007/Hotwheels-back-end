# Script to create pre-defined admin user
from app import create_app, db
from app.models import User
import os


app = create_app()
with app.app_context():
db.create_all()
admin_email = os.environ.get('ADMIN_EMAIL', 'admin@hotwheels.com')
admin_pw = os.environ.get('ADMIN_PASSWORD', 'Admin@1234')
if not User.query.filter_by(email=admin_email).first():
u = User(email=admin_email, is_admin=True)
u.set_password(admin_pw)
db.session.add(u)
db.session.commit()
print('Admin user created')
else:
print('Admin already exists')