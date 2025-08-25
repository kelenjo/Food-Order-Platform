echo "Waiting for Postgres to be ready..."
while ! pg_isready -h "$DB_HOST" -p "$DB_PORT" -U "$DB_USER"; do
  sleep 1
done
echo "Postgres is ready."

# Check if 'products' table exists
TABLE_EXISTS=$(psql "postgresql://$DB_USER:$DB_PASSWORD@$DB_HOST:$DB_PORT/$DB_DATABASE" -tAc "SELECT to_regclass('public.products');")

if [ "$TABLE_EXISTS" = "" ]; then
  echo "Database not initialized. Running migrations and populating data..."
  flask init_db
  flask populate_db
else
  echo "Database already initialized. Skipping init."
fi

# Start Flask app with uwsgi
exec uwsgi uwsgi.ini