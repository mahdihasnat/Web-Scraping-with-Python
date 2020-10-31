In = open('countries.txt' , 'r')
out = open('populate_country.sql' , 'w')
for c in In.read().splitlines():
    command = f"insert into oj.country(oj.country.country_id , oj.country.country_name )\
        values(oj.country_id_seq.nextval , '{c}');\n"
    print(command)
    out.write(command)
out.close()

