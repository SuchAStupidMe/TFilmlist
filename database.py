# -*- coding: utf-8 -*-

import psycopg2
from config import host, user, password, dbname


def insert_into_table(title, link):
    try:
        connection = psycopg2.connect(
            host=host,
            user=user,
            password=password,
            database=dbname
        )
        connection.autocommit = True

        with connection.cursor() as cursor:
            cursor.execute(
                f"INSERT INTO filmlist (title, link) VALUES ('{title}', '{link}')"
            )

    except Exception as _ex:
        print('Error while working with POSTGRESQL', _ex)

    finally:
        # noinspection PyUnboundLocalVariable
        if connection:
            # noinspection PyUnboundLocalVariable
            connection.close()


def get_list():
    try:
        connection = psycopg2.connect(
            host=host,
            user=user,
            password=password,
            database=dbname
        )
        connection.autocommit = True

        with connection.cursor() as cursor:
            cursor.execute(
                "SELECT title FROM filmlist"
            )
            lst = cursor.fetchall()
        return lst

    except Exception as _ex:
        print('Error while working with POSTGRESQL', _ex)

    finally:
        # noinspection PyUnboundLocalVariable
        if connection:
            # noinspection PyUnboundLocalVariable
            connection.close()


def get_link(title_name):
    try:
        connection = psycopg2.connect(
            host=host,
            user=user,
            password=password,
            database=dbname
        )
        connection.autocommit = True

        with connection.cursor() as cursor:
            cursor.execute(
                f"SELECT link FROM filmlist WHERE title = '{title_name}'"
            )
            link = cursor.fetchone()
        return link

    except Exception as _ex:
        print('Error while working with POSTGRESQL', _ex)

    finally:
        # noinspection PyUnboundLocalVariable
        if connection:
            # noinspection PyUnboundLocalVariable
            connection.close()


def delete_row(title):
    try:
        connection = psycopg2.connect(
            host=host,
            user=user,
            password=password,
            database=dbname
        )
        connection.autocommit = True

        with connection.cursor() as cursor:
            cursor.execute(
                f"DELETE FROM filmlist WHERE title = '{title}'"
            )

    except Exception as _ex:
        print('Error while working with POSTGRESQL', _ex)

    finally:
        # noinspection PyUnboundLocalVariable
        if connection:
            # noinspection PyUnboundLocalVariable
            connection.close()
