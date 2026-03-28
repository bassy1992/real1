#!/bin/bash
# Direct fix for Railway admin user - Run this NOW

echo "=========================================="
echo "FIXING ADMIN USER ON RAILWAY"
echo "=========================================="
echo ""
echo "Run these commands in your terminal:"
echo ""
echo "1. Install Railway CLI (if not installed):"
echo "   npm install -g @railway/cli"
echo ""
echo "2. Login to Railway:"
echo "   railway login"
echo ""
echo "3. Link to your project:"
echo "   railway link"
echo ""
echo "4. Run this command to fix the admin user:"
echo "   railway run python manage.py shell"
echo ""
echo "5. Then paste this Python code:"
echo ""
cat << 'EOF'
from django.contrib.auth import get_user_model
User = get_user_model()
try:
    user = User.objects.get(username='admin')
    user.set_password('logan123@')
    user.is_superuser = True
    user.is_staff = True
    user.is_active = True
    user.save()
    print("✅ SUCCESS! Admin password reset to: logan123@")
except User.DoesNotExist:
    user = User.objects.create_superuser('admin', 'admin@bellrockholdings.org', 'logan123@')
    print("✅ SUCCESS! Admin user created with password: logan123@")
exit()
EOF
echo ""
echo "=========================================="
echo "After running the above, login with:"
echo "Username: admin"
echo "Password: logan123@"
echo "=========================================="
