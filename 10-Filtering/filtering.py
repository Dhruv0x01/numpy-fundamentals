# Filtering = Refers to the process of selecting elements from an array that match a given condition
#variablename[condition] = whatever you want those satisfying condition to be turned into

import numpy as np

ages = np.array([[21, 17, 16, 20, 25, 66, 89, 14], 
                 [39, 22, 44, 99, 18, 19, 26, 28]])

teenagers = ages[ages < 18 ] #shape of array isn't preserved, it got flattened into 1d
print(teenagers)

#original array ages is preserved 

#To add multiple conditions, cover the condition with brackets() 
# AND (&), OR (|), NOT(!), NumPy use C style operators

adults = ages[(ages >= 18) & (ages < 45)] #AND operator is used, &
print(adults)

not_eligible = ages[(ages<18) | (ages>50)] 
print(not_eligible)

seniors = ages[ages >= 65]
print(seniors)

evens = ages[ ages % 2 == 0]
print(evens)

odds = ages[ ages % 2 != 0]
print(odds)


# To preserve the original shape
# np.where(condition, array, fillvalue) 
# fill-value = basically what you want to fill in those elements who does'nt satisfy condition, eg: 0, -1, np.nan
# np.where() is alot slower than using boolean indexing

shaped_adults = np.where(ages >= 18, ages, -1) 
print(shaped_adults)

#Boolean indexing: Just print out with condition it will give true/false 
shaped_adults_2 = ages>=18
print(shaped_adults_2)

