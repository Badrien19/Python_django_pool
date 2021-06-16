
def run():
    d = [
        ('Hendrix' , '1942'),
        ('Allman' , '1946'),
        ('King' , '1925'),
        ('Clapton' , '1945'),
        ('Johnson' , '1911'),
        ('Berry' , '1926'),
        ('Vaughan' , '1954'),
        ('Cooder' , '1947'),
        ('Page' , '1944'),
        ('Richards' , '1943'),
        ('Hammett' , '1962'),
        ('Cobain' , '1967'),
        ('Garcia' , '1942'),
        ('Beck' , '1944'),
        ('Santana' , '1947'),
        ('Ramone' , '1948'),
        ('White' , '1975'),
        ('Frusciante', '1970'),
        ('Thompson' , '1949'),
        ('Burton' , '1939')
]

    my_dict = {}
    for i in d:
        if(i[1] in my_dict):
            my_dict[i[1]] = my_dict[i[1]] + " " + i[0]
        else:
            my_dict[i[1]] = i[0]

    for key, value in my_dict.items():
        print("%s : %s" % (key, value))

if __name__ == '__main__':
    run()