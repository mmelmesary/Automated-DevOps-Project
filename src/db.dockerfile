FROM mysql:9.6.0-oraclelinux9

ENV MYSQL_ROOT_PASSWORD=root

COPY ./init.sql /docker-entrypoint-initdb.d/

CMD ["--default-authentication-plugin=mysql_native_password", "--init-file", "/docker-entrypoint-initdb.d/init.sql"]
