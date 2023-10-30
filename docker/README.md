# docker deployment example

![image](https://github.com/harness-community/feature-flag-relay-proxy/assets/7338312/acb315bb-3a0f-413e-b0be-acbe869e4d12)

## docker-compose.yml

deploy the relay proxy and two replicas using docker

redis is included and should be used in production deployment

## environment

`PROXY_KEY` (required):
`AUTH_SECRET` (required): used to sign JWT tokens that the proxy generates during /auth requests
`PRIMARY_PORT` (7000): port for accessing primary instance
`REPLICA0_PORT` (7001): port for accessing replica instance
`REPLICA1_PORT` (7002): port for accessing replica instance
