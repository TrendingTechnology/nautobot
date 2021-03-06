# GraphQL

Nautobot supports a Read-Only GraphQL interface that can be used to query most information present in the database. The GraphQL interface is available at the endpoint `graphql/` for a human to explore and GraphQL can be queried as an API via the endpoint `api/graphql/`. Currently the support for GraphQL is limited to `query`, other operation type like `mutations` and `subscriptions` are not supported. Additionally, GraphQL variables are supported.

The GraphQL implementation is leveraging the `graphene-django` library and supports the [standard GraphQL language](https://graphql.org/learn/queries/).

## How to use the GraphQL interface

The GraphQL interface can be used to query multiple tables at once in a single request. In GraphQL, only the information requested will be returned which can be contrasted to REST APIs. In the example below, this query will return the name of all `interfaces` attached to the device `nyc-sw01` along with all `ip_addresses` attached to those interfaces.

```graphql
query {
  devices(name: "nyc-sw01") {
    name
    interfaces {
      name
      ip_addresses {
        address
      }
    }
  }
}
```
Result
```json
{
  "data": {
    "devices": [
      {
        "name": "nyc-sw01",
        "interfaces": [
          {
            "name": "xe-0/0/0",
            "ip_addresses": [
              {
                "address": "10.52.0.1/30"
              }
            ]
          },
          {
            "name": "xe-0/0/1",
            "ip_addresses": []
          }
        ]
      }
    ]
  }
}
```

It is possible to explore the Graph and create some queries in a human friendly UI at the endpoint `graphql/`. This interface (called `graphqli`) provides a great playground to build new queries as it provides full autocompletion and type validation.

## Querying the GraphQL interface over the rest API

It is possible to query the GraphQL interface via the rest API as well, the endpoint is available at `api/graphql` and supports the same Token based authentication as all other Nautobot APIs.

A GraphQL Query must be encapsulated in a JSON payload with the `query` key and sent with a POST request. Optionally it is possible to provide a list of `variables` in the same payload as presented below.

```json
{
  "query": "query ($id: Int!) { device(id: $id) { name }}",
  "variables": { "id": 3}
}
```

## Working with Custom Fields

GraphQL custom fields data data is provided in two formats, a "greedy" and a "prefixed" format. The greedy format provides all custom field data associated with this record under a single "custom_field_data" key. This is helpful in situations where custom fields are likely to be added at a later date, the data will simply be added to the same root key and immediately accessible without the need to adjust the query.

```graphql
query {
  sites {
    name
    custom_field_data
  }
}
```

Result
```json
{
  "data": {
    "sites": [
      {
        "name": "nyc-site-01",
        "custom_field_data": {
          "site_type": "large"
        }
      },
      {
        "name": "nyc-site-02",
        "custom_field_data": {
          "site_type": "small"
        }
      }
    ]
  }
}
```

Additionally, by default, all custom fields in GraphQL will be prefixed with `cf`. A custom field name `site_type` will appear in GraphQL as `cf_site_type` as an example. The prefix can be changed or remove the prefix by setting the value of `GRAPHQL_CUSTOM_FIELD_PREFIX`.

```graphql
query {
  sites {
    name
    cf_site_type
  }
}
```

Result
```json
{
  "data": {
    "sites": [
      {
        "name": "nyc-site-01",
        "cf_site_type": "large"
      },
      {
        "name": "nyc-site-02",
        "cf_site_type": "small"
      }
    ]
  }
}
```


