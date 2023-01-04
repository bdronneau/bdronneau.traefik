[![CI](https://github.com/bdronneau/bdronneau.traefik/actions/workflows/base.yml/badge.svg?branch=main)](https://github.com/bdronneau/bdronneau.traefik/actions/workflows/base.yml)

# bdronneau.traefik

Ansible role to deploy and manage [traefik](https://traefik.io/).

## Dev

### Tests

Using vagrant for testing because in docker we do not have systemd (natively)

```shell script
molecule test
```

__Note__: Uncomment staging let's encrypt url in traefik configuration when testing
