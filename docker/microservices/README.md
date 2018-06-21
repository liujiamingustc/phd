# microservices

# Node.js

```
$ docker pull node:8-alpine

$ docker run -it --rm --name myNodeApp node:8-alpine
>
> .help
```

## Best Practice Docker and Node.js

### Docker Run

Here is an example of how you would run a default Node.JS Docker Containerized application:

```
$ docker run \
  -e "NODE_ENV=production" \
  -u "node" \
  -m "300M" --memory-swap "1G" \
  -w "/home/node/app" \
  --name "my-nodejs-app" \
  node [script]
```

## Best Practice Links

* [nodejs-docker-webapp](https://nodejs.org/en/docs/guides/nodejs-docker-webapp/)
