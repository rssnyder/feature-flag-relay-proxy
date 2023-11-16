# feature-flag-relay-proxy

resources for deploying the relay proxy for harness feature flags

# what is included

`docker` resources for deploying the proxy with docker

`kubernetes` resources for deploying the proxy with kubernetes

`test` helpful scripts for testing the proxy

`.harness` a harness pipeline that tests all these configurations

# proxy image

[v2 proxy image in dockerhub](https://hub.docker.com/layers/harness/ff-proxy/v2.0.0-rc.3/images/sha256-cc1f39cfc29f6762ba1f06b2edea56553640128d5e94a7befd05c4d6eed82de0?context=explore)

# general guidance

the two things you will need to deploy the relay proxy:

- PROXY_KEY: a relay proxy key with some associated org(s), project(s), and environment(s)
- AUTH_SECRET: used to sign JWT tokens that the proxy generates during /auth requests

To create a proxy key:

```
curl "https://app.harness.io/gateway/cf/admin/proxy/keys?accountIdentifier=$HARNESS_ACCOUNT_ID" \
--header 'Content-Type: application/json' \
--header "x-api-key: $HARNESS_PLATFORM_API_KEY" \
--data '
{
  "name": "TestKey",
  "identifier": "TestKey",
  "description": "A description",
  "organizations": {
      "ThisOrg": { 
          "projects": { 
              "thisProject": { "scope": "selected", "environments": ["RealProd", "Test"] }
              "thatProject": { "scope": "all" }
          }
      },
       "ThatOrg": { 
          "projects": { 
              "thisProject": { "scope": "all" }
          }
      }
  }
}'
```

# further documentation

[Read more docs from the relay proxy source repository](https://github.com/harness/ff-proxy/blob/main/docs/configuration.md)
