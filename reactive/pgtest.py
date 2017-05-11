from charmhelpers.core import hookenv
from charms.reactive import when, when_not, set_state, remove_state, hook
from charmhelpers.core.hookenv import (
    log, config, relation_set, relation_get,
    local_unit, related_units, remote_unit, status_set)
    
@hook('install')
def install_handler():

    # Set the user defined "installing" state when this hook event occurs.
    log("----------- install (hook) ----------", "INFO")
    set_state('pgtest.installing')

@hook('start')
def start_handler():

    # Set the user defined "starting" state when this hook event occurs.
    log("----------- start (hook) ----------", "INFO")
    set_state('pgtest.starting')


@hook('stop')
def stop_handler():

    # Set the user defined "stopping" state when this hook event occurs.
    log("----------- stop (hook) ----------", "INFO")
    set_state('pgtest.stopping')
    

@hook('config-changed')
def config_changed_handler():
    log("----------- config-changed (hook) ----------", "INFO")
    pass


@hook('update-status')
def update_status_handler():

    # We could set the user defined "update-status" state and do this just like
    # the start, install, stop handlers. But we leave this up to a reader to complete.
    log("----------- update-status (hook) ----------", "INFO")
    pass


@hook('leader-elected')
def leader_elected_handler():
    
    # We could set the user defined "leader-elected" state and do this just like
    # the start, install, stop handlers. But we leave this up to a reader to co
    log("----------- leader-elected (hook) ----------", "INFO")
    pass



##################################################
@when('db.connected')
def request_db(pgsql):
    log("----------- db.connected ----------", "INFO")
    
@when('config.changed')
def config_changed_reactive():
    log("----------- config.changed (state) ----------", "INFO")


@when('db.master.available', 'admin-pass')
def render_config(pgsql):
    log("----------- db.master.available ----------", "INFO")

##################################################

@when('pgtest.installing')
def install_handler():
    log("----------- pgtest.installing (user state) ----------", "INFO")
    
    status_set('maintenance', 'Installing...')
    
    # Handle the startup of the application
    
    status_set('active', 'I am installing.')
    
    # Remove the state "installing" since we are done.
    
    remove_state('pgtest.installing')
    

@when('pgtest.starting')
def start_handler():
    log("----------- pgtest.starting (user state) ----------", "INFO")
    
    status_set('maintenance', 'Starting...')

    # Handle the start of the application
    
    cfg = config()

    # Get the value for the "message" key.

    m = "DEGBUG"
    
    status_set('active', ("Started with message: %s" % m))

    # Remove the "starting" state since we are done.

    remove_state('pgtest.starting')

    
@when('pgtest.stopping')
def stop_handler():
    log("----------- pgtest.stopping (user state) ----------", "INFO")
    
    status_set('maintenance', 'Stopping...')

    # Handle the stop sequence of the application
    
    status_set('active', 'I am stopping.')

    # Remove the "stopping" state since we are done.
        
    remove_state('pgtest.stopping')

