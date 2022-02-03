# Check password

- Read [the guideline](https://github.com/mate-academy/py-task-guideline/blob/main/README.md) before start

Write tests for the function `check_password`, 
which takes the string password and returns 
`True` for the valid password, and `False` for invalid.

Rules for the valid password:

- accepts only letters of the Latin alphabet Aa-Zz, digits 0-9
or special character from `$@#&!-_`;
- at least 8 characters;
- maximum 16 characters inclusive;
- contains at least 1 digit, 1 special character, 1 uppercase letter.

Examples:
```python
check_password('Pass@word1') == True
check_password('qwerty') == False
check_password('Str@ng') == False
```
