#!/usr/bin/env sh
PGDATA=${PGDATA:-\/var\/lib\/postgresql\/data}
POSTGRES_DB=${POSTGRES_DB:-postgres}
POSTGRES_USER=${POSTGRES_USER:-postgres}
POSTGRES_PASSWORD=${POSTGRES_PASSWORD:-postgres}

echo "Installing postgresql"
apk update && apk add --no-cache postgresql

echo -e "\nInitialize postgres folder"
mkdir /run/postgresql && \
    chown postgres:postgres /run/postgresql
su postgres -c "mkdir ${PGDATA} && chmod 700 ${PGDATA}"

echo -e "\nModify postgres settings"
su postgres -c "initdb -D ${PGDATA}"
echo "host all all 0.0.0.0/0 md5" >> ${PGDATA}/pg_hba.conf

echo -e "\nRunning postgresql"
su postgres -c "pg_ctl start -D ${PGDATA}"

echo -e "\nCreating user ${POSTGRES_USER}"
su postgres -c "createuser ${POSTGRES_USER}"

echo -e "\nCreating database ${POSTGRES_DB}"
su postgres -c "createdb ${POSTGRES_DB}"

echo -e "\nChanging password for ${POSTGRES_USER}"
su postgres -c "psql -c \"ALTER USER ${POSTGRES_USER} WITH ENCRYPTED PASSWORD '${POSTGRES_PASSWORD}';\""

echo -e "\nGrant database ${POSTGRES_DB} access to ${POSTGRES_USER}"
su postgres -c "psql -c \"GRANT ALL PRIVILEGES ON DATABASE ${POSTGRES_DB} TO ${POSTGRES_USER};\""

echo -e "\nStopping postgresql"
su postgres -c "pg_ctl stop -D ${PGDATA}"
