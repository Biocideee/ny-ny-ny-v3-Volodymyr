# Тестування працездатності системи

## Можливі запити
![image](https://github.com/user-attachments/assets/35fa0db4-c004-479c-bfd9-54f5cdf5835b)

## POST

### *Створення користувача*

```bash
{
  "email": "string",
  "password": "string",
  "name": "string",
  "surname": "string",
  "nickname": "string"
}
```
![image](https://github.com/user-attachments/assets/fbb3d8dd-e723-450e-aeac-5969cffb4896)


### *Створення опитування*
```bash
{
  "name": "string",
  "description": "string",
  "User_id": 1
}
```
![image](https://github.com/user-attachments/assets/71db58c1-ab1c-4668-91c2-76cdaff4cf0e)


## GET

### *Перевірка створеного користувача*

![image](https://github.com/user-attachments/assets/719c1554-e333-4a9c-bc25-5b9fd1b77c77)


### *Перевірка створеного опитування*
![image](https://github.com/user-attachments/assets/c7d2b0ca-f491-4bb6-bf65-3ff45b238217)


## PUT

### *Зміна прізвиська користувача*
```bash
{
  "email": "string",
  "password": "string",
  "name": "string",
  "surname": "string",
  "nickname": "Volodymyr"
}
```
![image](https://github.com/user-attachments/assets/0b876908-571a-44d6-9a83-b8b7ba176038)


### *Перевірка зміни прізвиська користувача через GET*
![image](https://github.com/user-attachments/assets/a7ae358a-f3a3-4f85-ae13-dd9a4a63f724)


### *Зміна імені користувача*
```bash
{
  "name": "Volodymyr",
  "description": "string",
  "User_id": 1
}
```
![image](https://github.com/user-attachments/assets/87d5e3b0-42a9-465f-aa91-ebf3bb6044fb)

### *Перевірка зміни імені користувача через GET*
![image](https://github.com/user-attachments/assets/9c049350-7c7c-464d-b65b-dc09095c8cf6)



## DELETE

### *Видалення користувача*
![image](https://github.com/user-attachments/assets/4579fab9-27d3-4fa0-8b7d-edeb3250a358)

### *Перевірка видалення користувача через GET*
![image](https://github.com/user-attachments/assets/b2a56b0d-d688-43a6-9df8-41a60775afc0)


### *Видалення опитування*
![image](https://github.com/user-attachments/assets/e9ab2c64-1a26-4c20-85e6-b3ffccb54a96)

### *Перевірка видалення опитування через GET*
![image](https://github.com/user-attachments/assets/691eb6a5-3d83-4a83-8eda-95f3f4c4b736)


