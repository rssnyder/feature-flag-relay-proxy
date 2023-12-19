# kubernetes deployment example

![image](https://github.com/harness-community/feature-flag-relay-proxy/assets/7338312/ba9898d9-175a-4ecc-85fb-23c145f66995)

## deployment.yaml

deploy the relay proxy to kubernetes using this manifest

resources included:
- namespace
- deployment: for the main relay proxy, which fetches values from harness and stores them in redis
- deployment: the the read replicas, which expose the information in redis to ff sdk connections
- service: for exposing the main relay proxy (only needed for testing)
- service: for exposing the read replicas, for the ff sdk to connect to

see the `values.yaml` file for the inputs needed to deploy this manifest

## redis

in production deployments, redis should be used as a shared cache

deploy redis based on your internal standards

## harness_service.yaml

an example harness service yaml for deploying the relay proxy

you will need to change the project/org, github, and docker connector ids to match your setup
