FROM mysql

ENV MYSQL_ROOT_PASSWORD=urubu100
ENV MYSQL_DATABASE=poupay

COPY ./valores.sql ./docker-entrypoint-initdb.d

EXPOSE 3306
