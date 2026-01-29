``` docker build -t carzone .```

```docker run -e PROXY_URL=http://user:pass@host:port -v $(pwd)/carzone:/app/carzone carzone```
