from charmhelpers.core import hookenv
from charms.reactive import when, when_not, set_state, remove_state, hook
from charmhelpers.core.hookenv import (
    log, config, relation_set, relation_get,
    local_unit, related_units, remote_unit, status_set)
from time import sleep

@when_not('pgtest.installed')
def install_pgtest():
    log("----------- pgtest.install_pgtest ----------", "INFO")
    status_set('maintenance', 'Installing...')
    # Do what needs to be done to bring your software in adding a sleep here
    sleep(5)
    # Done with installing!
    set_state('pgtest.installed')


@when('pgtest.installed')
@when_not('db.connected')
def waiting_for_db():
    log("----------- pgtest.waiting_for_db ----------", "INFO")
    status_set('blocked', 'Please add a relation to DB.')


@when('db.connected')
@when_not('pgtest.started')
def request_db(pgsql):
    log("----------- pgtest.request_db ----------", "INFO")
    status_set('waiting', 'Waiting for DB to become available.')
    # TODO (The followign will work only once)!!
    pgsql.set_database('mydb')


@when('db.master.available')
def start(pgsql):
    status_set('maintenance', 'Starting...')
    conn_str = pgsql.master
    log("Got connection string {}".format(conn_str))
    # Setup your application to use the connection string (See documentation of interface)
    sleep(5)
    # Done with configuring and starting your service!
    set_state('pgtest.started')
    status_set('active', 'Ready.')
