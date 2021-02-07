def remove_fails(d):
    passed = {}
    for key in d:
        if int(d[key]) >= 60:
            passed[key] = d[key]
    return passed

students = {'Henry': 42, 'Ani': 60, 'Anna': 34, 'Artur': 70, 'Max': 90}
print(remove_fails(students))
