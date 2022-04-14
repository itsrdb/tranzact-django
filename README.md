# tranzact-django

## API Endpoints 🌐

### Base URL

```https
    https://http://localhost:8000/
```
<!-- 
### User

| Parameter | Type     | Required | Description        | 
| :-------- | :------- | :------- | :----------        |
| `username` | `string`| ✔️       | Username to fetch.|
 -->
#### Get/Patch all employees details

```https
  GET /api/employees/
```
```https
  POST /api/employees/
```

#### Get/Patch an employee detail

```https
  GET /api/employees/{id}
```
```https
  POST /api/employees/{id}
```

#### Get/Patch all company details

```https
  GET /api/company/
```
```https
  POST /api/company/
```

#### Get/Patch a company detail

```https
  GET /api/company/{id}
```
```https
  POST /api/company/{id}
```

#### Get/Patch all invoices

```https
  GET /api/invoices/
```
```https
  POST /api/invoices/
```

#### Get/Patch an invoice

```https
    GET /api/invoices/{id}
```
```https
    POST /api/invoices/{id}
```

<!-- 
#### Get questions

```https
    GET /api/questions/{start}-{end}
```

| Parameter | Type     | Required | Description                   | 
| :-------- | :------- | :------- | :---------------------------- |
| `start`   | `number` | ❌       | Question to start at. |
| `end`     | `number` | ❌       | Question to stop at.  |

#### Get questions by difficulty

```https
    GET /api/questions/{difficulty}/{start}-{end}
```

| Parameter | Type     | Required | Description                   | 
| :-------- | :------- | :------- | :---------------------------- |
| `difficulty` | `string` | ✔️       | Question difficulty. |
| `start`   | `number` | ❌       | Question to start at. |
| `end`     | `number` | ❌       | Question to stop at.  | -->

<!-- ## Roadmap 🛣️

- Add ability to GET question by questionID.
- Caching/Storing data to make API calls quicker.
 -->
