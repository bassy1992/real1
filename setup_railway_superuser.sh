#!/bin/bash
# Quick setup script for creating Railway superuser

echo "╔══════════════════════════════════════════════════════════════════════╗"
echo "║                                                                      ║"
echo "║           🚀 Railway Superuser Setup                                 ║"
echo "║                                                                      ║"
echo "╚══════════════════════════════════════════════════════════════════════╝"
echo ""

# Check if Railway CLI is installed
if ! command -v railway &> /dev/null; then
    echo "❌ Railway CLI not found."
    echo ""
    echo "Install it with:"
    echo "  npm install -g @railway/cli"
    echo ""
    echo "Or visit: https://docs.railway.app/develop/cli"
    exit 1
fi

echo "✅ Railway CLI found"
echo ""

# Check if logged in
echo "📝 Checking Railway login status..."
if ! railway whoami &> /dev/null; then
    echo "❌ Not logged in to Railway"
    echo ""
    echo "Logging in..."
    railway login
    echo ""
fi

echo "✅ Logged in to Railway"
echo ""

# Link to project
echo "🔗 Linking to Railway project..."
railway link
echo ""

# Show options
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "Choose a method to create superuser:"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""
echo "1) Interactive (you'll be prompted for username, email, password)"
echo "2) Automatic (using environment variables)"
echo "3) Exit"
echo ""
read -p "Enter your choice (1-3): " choice

case $choice in
    1)
        echo ""
        echo "🔐 Creating superuser interactively..."
        echo ""
        railway run python manage.py createsuperuser
        ;;
    2)
        echo ""
        echo "⚙️  Using environment variables method..."
        echo ""
        echo "Make sure you have set these in Railway Dashboard:"
        echo "  - DJANGO_SUPERUSER_USERNAME"
        echo "  - DJANGO_SUPERUSER_EMAIL"
        echo "  - DJANGO_SUPERUSER_PASSWORD"
        echo ""
        read -p "Have you set these variables? (y/n): " confirm
        if [ "$confirm" = "y" ] || [ "$confirm" = "Y" ]; then
            railway run python manage.py create_superuser
        else
            echo ""
            echo "Please set the environment variables first:"
            echo "1. Go to Railway Dashboard"
            echo "2. Select your project"
            echo "3. Go to Variables tab"
            echo "4. Add the required variables"
            echo "5. Run this script again"
        fi
        ;;
    3)
        echo ""
        echo "👋 Exiting..."
        exit 0
        ;;
    *)
        echo ""
        echo "❌ Invalid choice"
        exit 1
        ;;
esac

echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "✅ Done!"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""
echo "You can now login at:"
echo "  https://real-production-4319.up.railway.app/admin/"
echo ""
echo "For more information, see: back/CREATE_SUPERUSER_RAILWAY.md"
echo ""
