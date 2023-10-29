The below snippet requires using httpie https://httpie.io/

```sh
http POST http://localhost:3000/api/v1/charge idempotency-token:"wxskCX171OYTCLcIDvej4KZ055sHOqEbJaNyrMy1u3ihqX1/RlcK9GgOM3iSIjZxTe1S0vGpmjBEH4Om51UtLg==" \
--raw '{
    "amount": 123.00,
    "recipient": "John Doe"
}'
```
