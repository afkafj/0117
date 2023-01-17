year_lists = [1999, 2000, 2001, 2002, 2003]
print(year_lists)

print(year_lists[2])

print(year_lists[4])

things = ['mozzarella', 'cinderella', 'salmonella']
print(things)

things[1] = things[1].title()
print(things)

things[0] = things[0].upper()
print(things)

del things[-1]
print(things)

surprise = ['Groucho', 'Chico', 'Harpo']
surprise[-1] = surprise[-1].lower()[::-1].title()
print(surprise)

number_list = [i for i in range(1, 11) if i % 2 ==0]
print(number_list)

start1 = ["fee", "fie", "foe"]
rhymes = [
    ("flop", "get a mop"),
    ("fope", "turn the rope"),
    ("fa", "get your ma"),
    ("fudge", "call the judge"),
    ("fat", "pet the cat"),
    ("fog", "walk the dog"),
    ("fun", "say we're done")
         ]
start2 = "Someone better"
start1 = f'{start1[0].title()}! {start1[1].title()}! {start1[2].title()}! '
print(start1)
rhymes_ = f'{rhymes[0][0].title()}'
print(rhymes)
print(f'{start1}{rhymes}')
print(f'{start2}{rhymes[0][1]}. ')