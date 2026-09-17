# FD AI 0.1 API contract

Base URL: `http://HOST:8080`

## Health
`GET /health`

Response:
```json
{"ok": true, "version": "0.1.0"}
```

## Info
`GET /api/v1/info`

Returns version and registered tools.

## Command
`POST /api/v1/command`

Request:
```json
{"command":"tính 2+2"}
```

Response:
```json
{"ok":true,"tool":"calculator","data":{"expression":"2+2","result":4}}
```

## Memory
`GET /api/v1/memory`

`POST /api/v1/memory`
```json
{"key":"project","value":"FD AI"}
```

For production/mobile release, put the server behind HTTPS and authentication. Do not expose the development server directly to the public Internet.
