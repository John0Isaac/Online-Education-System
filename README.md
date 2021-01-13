# Online-Education-System

```bash
dropdb online_education_system
createdb online_education_system
export FLASK_APP=app.py
export FLASK_ENV=development
flask run --reload
psql online_education_system < data.sql
```

## Endpoints

* Sample:
`curl http://127.0.0.1:5000/`

* Sample:
`curl http://127.0.0.1:5000/login -X POST -H "Content-Type:application/json" -d '{"logincode": "D0001"}'`

```JSON
{
  "id": 1, 
  "success": true
}
```

* Sample:
`curl http://127.0.0.1:5000/student/profile/1`

```JSON
{
  "address": "Beni Suef", 
  "date_of_birth": "2000-10-07", 
  "email": "johnisaac@gmail.com", 
  "gender": "Male", 
  "id": 1, 
  "name": "John Isaac", 
  "phone": "+20 120 531 0694", 
  "success": true
}
```

*Sample:
`curl http://127.0.0.1:5000/staff/profile/1`

```JSON
{
  "address": "Menia", 
  "date_of_birth": "1960-11-08", 
  "email": "kahledmorsy@gmail.com", 
  "gender": "Male", 
  "id": 1, 
  "job": "Doctor", 
  "name": "Khaled Morsy", 
  "phone": "+20 112 654 8495", 
  "success": true
}
```
