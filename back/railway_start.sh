#!/bin/bash
# Railway startup script with PostgreSQL library path fix

# Find PostgreSQL library path in Nix store
PG_LIB_PATH=$(find /nix/store -type f -name "libpq.so.5" 2>/dev/null | head -1 | xargs dirname)

if [ -n "$PG_LIB_PATH" ]; then
    echo "Found PostgreSQL libraries at: $PG_LIB_PATH"
    export LD_LIBRARY_PATH="$PG_LIB_PATH:$LD_LIBRARY_PATH"
else
    echo "Warning: PostgreSQL libraries not found in /nix/store"
    # Try alternative paths
    export LD_LIBRARY_PATH="/nix/var/nix/profiles/default/lib:$LD_LIBRARY_PATH"
fi

echo "LD_LIBRARY_PATH: $LD_LIBRARY_PATH"

# Run migrations
python manage.py migrate

# Start gunicorn
gunicorn backend.wsgi:application --bind 0.0.0.0:$PORT
