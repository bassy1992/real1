#!/bin/bash

# Verification script for Railway-Vercel connection
# This script tests the backend API endpoints

echo "🔍 Verifying Railway Backend Connection..."
echo "=========================================="
echo ""

BACKEND_URL="https://real-production-4319.up.railway.app"
API_URL="${BACKEND_URL}/api"

# Test 1: Backend Health Check
echo "1️⃣  Testing backend health..."
HTTP_CODE=$(curl -s -o /dev/null -w "%{http_code}" "${BACKEND_URL}/admin/")
if [ "$HTTP_CODE" -eq 200 ] || [ "$HTTP_CODE" -eq 302 ]; then
    echo "✅ Backend is running (HTTP $HTTP_CODE)"
else
    echo "❌ Backend health check failed (HTTP $HTTP_CODE)"
fi
echo ""

# Test 2: Properties API
echo "2️⃣  Testing Properties API..."
HTTP_CODE=$(curl -s -o /dev/null -w "%{http_code}" "${API_URL}/properties/")
if [ "$HTTP_CODE" -eq 200 ]; then
    echo "✅ Properties API is accessible (HTTP $HTTP_CODE)"
    PROPERTIES_COUNT=$(curl -s "${API_URL}/properties/" | grep -o '"id"' | wc -l)
    echo "   Found $PROPERTIES_COUNT properties"
else
    echo "❌ Properties API failed (HTTP $HTTP_CODE)"
fi
echo ""

# Test 3: Investments API
echo "3️⃣  Testing Investments API..."
HTTP_CODE=$(curl -s -o /dev/null -w "%{http_code}" "${API_URL}/investments/opportunities/")
if [ "$HTTP_CODE" -eq 200 ]; then
    echo "✅ Investments API is accessible (HTTP $HTTP_CODE)"
    INVESTMENTS_COUNT=$(curl -s "${API_URL}/investments/opportunities/" | grep -o '"id"' | wc -l)
    echo "   Found $INVESTMENTS_COUNT investment opportunities"
else
    echo "❌ Investments API failed (HTTP $HTTP_CODE)"
fi
echo ""

# Test 4: CORS Headers
echo "4️⃣  Testing CORS headers..."
CORS_HEADER=$(curl -s -I -H "Origin: https://bellrockholdings.org" "${API_URL}/properties/" | grep -i "access-control-allow-origin")
if [ -n "$CORS_HEADER" ]; then
    echo "✅ CORS headers are configured"
    echo "   $CORS_HEADER"
else
    echo "⚠️  CORS headers not found (may need to check OPTIONS request)"
fi
echo ""

# Test 5: Frontend URL
echo "5️⃣  Testing frontend..."
FRONTEND_URL="https://bellrockholdings.org"
HTTP_CODE=$(curl -s -o /dev/null -w "%{http_code}" "${FRONTEND_URL}")
if [ "$HTTP_CODE" -eq 200 ]; then
    echo "✅ Frontend is accessible (HTTP $HTTP_CODE)"
else
    echo "❌ Frontend check failed (HTTP $HTTP_CODE)"
fi
echo ""

echo "=========================================="
echo "✨ Verification complete!"
echo ""
echo "Next steps:"
echo "1. Update Railway environment variables with CORS settings"
echo "2. Update Vercel environment variables with VITE_API_BASE_URL"
echo "3. Deploy both backend and frontend"
echo "4. Test in browser at https://bellrockholdings.org"
