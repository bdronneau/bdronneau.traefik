import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_files(host):
    files = ['/etc/traefik', '/etc/traefik/acme', '/etc/traefik/conf.toml']
    for file in files:
        f = host.file(file)

        assert f.exists
        assert f.user == 'traefik'
        assert f.group == 'traefik'


def test_btraefik_bin(host):
    files = ['/usr/bin/traefik', '/etc/systemd/system/traefik.service']
    for file in files:
        f = host.file(file)

        assert f.exists
        assert f.user == 'root'
        assert f.group == 'root'


def test_service(host):
    traefik = host.service("traefik")
    assert traefik.is_running
    assert traefik.is_enabled


def test_user(host):
    traefik = host.user("traefik")
    assert traefik.group == "traefik"
